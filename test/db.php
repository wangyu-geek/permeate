<?php
$host = '127.0.0.1';
$user = 'root';
$pwd = 'wy7452525.';
$db = 'bbs';

$con = mysqli_connect($host, $user, $pwd, $db);

if(! $con ) {
	echo "链接错误".mysqli_connect_error();
}
