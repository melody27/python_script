<?php


# php的mysql组件进行查询(ps.可被注入的情况)
# 简单的话，可以通过addslashes和mysql_real_escape_string函数来进行防止sql注入


show_source(__FILE__);
$dbuser ='root';
$dbpass ='';
$dbname ="security";

@$con = mysql_connect($host,$dbuser,$dbpass);
@mysql_select_db('security');

if(isset($_GET['id']))
{
$id=$_GET['id'];
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
$result=mysql_query($sql);
$row = mysql_fetch_array($result);
    if($row)
    {
      echo 'Your name:'. $row['username'];
      echo "<br>";
      echo 'Your password:' .$row['password'];
      }
    }
    
?>