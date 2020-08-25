<?php

$ss = fsockopen('www.melodyspace.cn',80);
// stream_set_blocking($ss,false);
if (!$ss){
    echo "报错楼d";
}
$out = "GET / HTTP/1.1\r\n";
$out .= "Host: www.baidu.com\r\n";
$out .= "Connection: Close\r\n\r\n";
fwrite($ss,$out);
while (!feof($ss)){                 # 检测文件读取是否结束
    echo fgets($ss,10);             # 从文件句柄中获取数据
}
fclose($ss)                         # 关闭文件句柄
?>