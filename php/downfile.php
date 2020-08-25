<?php

    // show_source(__FILE__);
    function download($url, $filename) {
        // 获得文件大小, 防止超过2G的文件, 用sprintf来读
        $filesize = sprintf ( "%u", filesize ( $url ) );
        echo "你请求的url为：".$url."<br>"; 
        if (! $filesize) {
            return;
        }
        header ( "Content-type:application/octet-stream\n" ); //application/octet-stream
        header ( "Content-disposition: attachment; filename=\"" . $filename . "\"" );
        header ( 'Content-transfer-encoding: binary' );
        if ($range = getenv ( 'HTTP_RANGE' )) { // 当有偏移量的时候，采用206的断点续传头
            $range = explode ( '=', $range );
            $range = $range [1];
            header ( "HTTP/1.1 206 Partial Content" );
            header ( "Date: " . gmdate ( "D, d M Y H:i:s" ) . " GMT" );
            header ( "Last-Modified: " . gmdate ( "D, d M Y H:i:s", filemtime ( $url ) ) . " GMT" );
            header ( "Accept-Ranges: bytes" );
            header ( "Content-Length:" . ($filesize - $range) );
            header ( "Content-Range: bytes " . $range . ($filesize - 1) . "/" . $filesize );
            header ( "Connection: close" . "\n\n" );
            header('Content-Type:application/json; charset=utf-8');
            header('Content-type: image/webp');
        } else {
            header ( "Content-Length:" . $filesize . "\n\n" );
            $range = 0;
        }
        loadFile ($url);
    }
    
    function loadFile($filename, $retbytes = true) {
        $buffer = '';
        $cnt = 0;
        $handle = fopen ( $filename, 'rb' );
        if ($handle === false) {
            return false;
        }
        while ( ! feof ( $handle ) ) {
            $buffer = fread ( $handle, 1024 * 1024 );
            echo $buffer;
            ob_flush ();
            flush ();
            if ($retbytes) {
                $cnt += strlen ( $buffer );
            }
        }
        $status = fclose ( $handle );
        if ($retbytes && $status) {
            return $cnt; // 返回从文件中读入的字节数，像readfile()。
        }
        return $status;
    }
    if($_GET[path]){
        if(file_exists($_GET[path])){
            // echo "你请求的文件存在";
            download($_GET[path],$_GET[name]);
            
        }else{
            echo "你请求的文件不存在";
        }

        
    }

?>