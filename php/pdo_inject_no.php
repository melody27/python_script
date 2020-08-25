<?php

# php的PDO组件进行查询(ps.预编译的方式，不可被sql注入)
    show_source(__FILE__);
    $pdo = new PDO('mysql:host=localhost;dbname=ctf','root','123456');
    
    if($_GET[id]){
        $sql = 'select * from user where id=?';
        

        $exec = $pdo->prepare($sql);
        $exec->bindParam(1,$_GET[id]);
        
        # 也能够这样写：
        // $sql = 'select * from user where id=:id';
        // $pdo->bindParam(':id',$_GET[id]);

        $exec->execute();
        $result = $exec->fetchAll();

        var_dump($result);

    }
?>