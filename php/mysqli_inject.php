<?php
show_source(__FILE__);
# php 的mysqli组件普通的查询方式。(ps.可以被sql注入的情况)
?>

<?php
        # 创建链接对象
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

<?php
if(!empty($_GET['id'])){

        $yuju = "select * from user where id = $_GET[id]";
        echo "sql语句为：".$yuju."<br>";
        $result = $mysqli_connect->query($yuju);
        if ($result){
                var_dump($result->fetch_array());
                # var_dump($result->free_result());
        }else{
                echo "查询错误";
                echo $mysqli_connect->error;
        }
        $mysqli_connect->close();
}

# 备注：堆叠注入的函数mysqli_multi_query()是mysqli独有的函数
?>

