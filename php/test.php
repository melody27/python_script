<?php
$key="e45e329feb5d925b";
function jisuan($post){
	$key="e45e329feb5d925b";
	$t="base64_"."decode";
	$post=$t($post."");
	
	for($i=0;$i<strlen($post);$i++) {
				$post[$i] = $post[$i]^$key[$i+1&15]; 
			}
	echo $post;
}

function jisuan2($post){
	$key="e45e329feb5d925b";
	// echo 'aaa';
	$post=openssl_decrypt($post, "AES128", $key);
	echo $post;
}

function test_encrypt($post){
	$post = openssl_encrypt($post,'AES128', $key);
	echo $post;
}

// jisuan('3Mn1yNMtoZViV5wotQHPJtwwj0F4b2lyToNK7LfdUnN7zmyQFfx/zaiGwUHg+8SlXZemCLBkDIvxiBIGd6bgOEiZtNpn6YmnWiiaCBNbXkC5JWFTARrD8lCOCQ4ZVFjsJFDaAOwzinbqne/oYuNwWjQvKM9ii2RE/b+Gc+ya2f4+OIDU2Wk/QSIL7GOAoyaUYZSq4bL2wmX5RnP1Lbf7S+TAy3K7JPruBiZeZGC/ay14vUj4+IgmNHwEAzWl3DNIsL1yhH4Do5FI8HwZpG5XnrZwpKdFIEgN4GKmcDODTdO2pj8DVXCwes3m+v/wRykVd++xsex2EkGn9p0SgL+GpXlGg6OlQscedjdgBXv15UyPfJude5BJv+j7cEF7zpdtyAnFYCSqiRX+XD7DNsIUVbU+oamjVwZCgr4L+bbRvs1NfjV6iKKs65VTnlSIbCArJv/w+axR9Gc7Jt9v/GBKckbRjefZGqx7UTKDMahYEBgrwpXrii28q/UerEq/VKFKKeHQuovmpvlx8CblMBkG+rHmhQrP7QVJuzSOUbwdWZpbhys2bufqT6hyOjsu/0sSmHdrzvlZgkRsnsNK0Kv56sesEx9AiwuvgxMh5gAi86uAfhQISoEU5jZNs/T0LiJksv6xddHsDoKSwx+2s74jiNNFh9p0AmUdDloXXvRrfJvCdfaTHnkDEOH6BcSyZj9r53ZKiQUHPh7Sd13x/bk7zcKrUubSplf5cFLc+7m2nSWkXM1Ei7GVkZKBvKorowWkuS0katSgEt3WN00g95HyDfGdxZyUIthJ9hIETiP81O67weGqjFraZfXQUuOHNibydSrZTj/1La6OqSSHoAVnghH9TbYzM4lDdppSZJ1j5eWx8CVn+E8LeCyeROLhKix+P9yJh72FbLOoMFvCurzarkbYZrmQ7Qb0R1oOt2rKNFxY8/itqOSZdk/d2lFkZeT8sbzLmdMQBdSvP/WlvhRdgtbvt3SwcoBU5R45sI75m');

jisuan2('XsvIMFQSHbCkgK2YVOoMIA==');
// test_encrypt('id');

?>