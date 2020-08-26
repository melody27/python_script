<?php

$ss = fsockopen('192.168.2.82',80);
// stream_set_blocking($ss,false);
if (!$ss){
    echo "报错楼d";
}
$out = "GET / HTTP/1.1\r\n";
$out .= "Host: 192.168.2.82\r\n";
$out .= "Connection: Close\r\n\r\n";
fwrite($ss,$out);
while ($o = fgets($ss,10)){
    if($o == false){
        break;
    }
    echo $o;


}
fclose($ss)                         # 关闭文件句柄
?>