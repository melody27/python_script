<?php

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
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    set_time_limit(0);                      # 让php页面脱离执行时间的限制
    $headers = apache_request_headers();
    $action = $headers['X-CMD'];
    // echo "\$action is".$action;
    // var_dump($headers);
    switch ($action){
        case "CONNECT":
            echo "this is connect";
        break;
        
        case "READ":
            echo "this is read";
        break;

        case "FORWARD":
            echo "this is forward";

        case "DISCONNECT":
            echo "this is disconnect";
    }





}




?>