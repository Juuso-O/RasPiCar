<?php
error_reporting(E_ALL);
ini_set('display_errors',1);
$file = fopen("./move", "w") or die("Unable to open file!");

if (isset($_GET["move"])){
	$move = $_GET["move"];
	switch($move) {
		case "true":
			$txt = "true";
			break;
		case "back":
			$txt = "back";
			break;
		default:
			$txt = "false";
			break;
	}
} else {
	$txt = "false";
}
fwrite($file, $txt);
fclose($file);
?>
