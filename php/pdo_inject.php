<?php


function check_image($file_name){
    $types = '.gif|.png|.jpeg';

    $info = getimagesize($file_name);
    $ext = image_type_to_extension($info[2]);
    if (stripos($types,$ext)){
        echo "<br>文件头检测成功<br>";
        pass;
    }else{
        echo "<br>文件上传失败<br>";
        exit();
    }

}


if (($_FILES["file"]["type"]=="image/gif")&&(substr($_FILES["file"]["name"], strrpos($_FILES["file"]["name"], '.')+1))== 'gif') {
    echo "Upload: " . $_FILES["file"]["name"];
    echo "Type: " . $_FILES["file"]["type"];
    echo "Temp file: " . $_FILES["file"]["tmp_name"];
    check_image($_FILE['file']['tmp_name']);



    if (file_exists("upload_file/" . $_FILES["file"]["name"]))
      {
      echo $_FILES["file"]["name"] . " already exists. ";
      }
    else
      {
      move_uploaded_file($_FILES["file"]["tmp_name"],
      "upload_file/" .$_FILES["file"]["name"]);
      echo "Stored in: " . "upload_file/" . $_FILES["file"]["name"];
      }
    }
else
  {
  echo "Invalid file,you can only upload gif";
  }


