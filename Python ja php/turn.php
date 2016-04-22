<?php
error_reporting(E_ALL);
ini_set('display_errors',1);
$file = fopen("turn", "w") or die("Unable to open file!");

$kulma = $_GET["kulma"];

if ($kulma > 0 && $kulma < 0.0026) {
	$txt = $kulma;
} else {
	$txt = "";
}
fwrite($file, $txt);
fclose($file);
?>
