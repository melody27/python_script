<?php

# php 的mysqli组件实现并且参数的预编译方式查询

$mysqli = new mysqli("localhost", "root", "123456", "ctf");

$id = $_GET['id'];
/* 检查连接 */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}


/* 创建一个预编译 SQL 语句 */
if (mysqli_connect_errno()){
    echo mysqli_connect_errno()."<br>";
}else{
    echo "连接正确，mysql_connect_error未抛出错误<br>";
}

if ($stmt = $mysqli->prepare('select username,password from user where id=?')) {

    /* 对于参数占位符进行参数值绑定 */
    $stmt->bind_param("s", $id);

    /* 执行查询 */
    $stmt->execute();

    /* 将查询结果绑定到变量 */
    $stmt->bind_result($usernmae,$password);        # 绑定的时候需要一一对应，尤其是结果集实际上是由多个列的情况。
                                                        # 必须绑定多个变量才能正确的实现绑定结果集

    /* 获取查询结果值 */
    $stmt->fetch();

    // printf("其结果为 %s\n",$district);
    printf("用户名:%s <br>密码:%s",$usernmae,$password);

    /* 关于语句对象 */
    $stmt->close();
}else{
    echo "连接错误<br>";
    
}

/* 关闭连接 */
$mysqli->close();
?>
