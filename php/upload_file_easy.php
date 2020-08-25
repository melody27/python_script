<?php

defined("UPLOAD_DIR",__DIR__);
if ($_FILES['file1']['name']){}
        $file_name = $_FILES['file1']['name'];
        echo "你上传的图片文件的mimetype类型为：".$_FILES['file1']['type']."<br>";

        if(stripos($file_name,'.php')){
                die('检测到非法后缀');
        } 


        move_uploaded_file($_FILES['file1']['tmp_name'],"uploads/".$_FILES['file1']['name']);


?>

<html>
<head>
</head>
<body>
<form action="" method="post" enctype="multipart/form-data">
<input type="file" name="file1">
<input type="submit" value="提交">
</form>

</body>
</html>