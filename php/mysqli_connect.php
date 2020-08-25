<?php

    $php_connect = [
        'host'      =>      'localhost',
        'username'  =>      'root',
        'passwd'    =>      '123456',
        'db_name'   =>      'ctf'
    ];  

    $mysqli_connect = mysqli_connect($php_connect['host'],$php_connect['username'],$php_connect['passwd']);

    $mysqli_connect->set_charset('utf-8');
    $mysqli_connect->select_db($php_connect['db_name']);

?>