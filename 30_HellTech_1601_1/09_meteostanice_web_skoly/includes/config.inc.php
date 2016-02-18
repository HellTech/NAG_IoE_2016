<?php
//Konfigurace připojení k DB 
static $cfg_db=array(
	"dbhost" => "localhost",
	"dbuser" => "user_name",
	"dbpass" => "password",
	"dbname" => "nag_meteo"
);  

//Konfigurace
static $cfg=array(
  "input_id" => "aaa111bbb222", 
  "actual" => "meteo_actual",
  "hour" => "meteo_hour",
  "day" => "meteo_day",
  "location_name" => "VELEŠÍN",
  "owm_location_id" => "3067696",
  "owm_appid" => "aaa111bbb222"  
);

//Spojeni s databazi
$conn = false;
$conn = @MySQL_Connect($cfg_db['dbhost'],$cfg_db['dbuser'],$cfg_db['dbpass']) or $conn=true;
@MySQL_Select_DB($cfg_db['dbname']) or $conn=true;
if(!$conn)mysql_query("SET NAMES utf8;",$conn);
$tblTranslated = replaceTblArray();


?>