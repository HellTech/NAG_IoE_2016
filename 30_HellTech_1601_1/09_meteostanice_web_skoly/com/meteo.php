<?php
  //http://meteo.sosvel.cz/com/meteo.php?id=40e2c63769d3425a63f7e09c06312401&t=6&h=79&l=189
  require '../includes/_func.php';
  require '../includes/config.inc.php';

  //kontrola input id
  if(!isset($_GET['id']) || strlen($_GET['id'])==0 || $_GET['id']!=$cfg['input_id'])
  {
    echo "bad id";
    exit;
  }
  
  //uložení aktuálních dat ze senzorů do db
  function input_value($type, $value, $noapostrof = false)
  {
    global $check_all_ok; 
    if(count(query("select * from #actual where name='".$type."'",$check))>0 && $check)
      if($noapostrof) $query = "update #actual set value=".$value." where name='".$type."' limit 1;";
        else $query = "update #actual set value='".$value."' where name='".$type."' limit 1;";
    else
      if($noapostrof) $query = "insert into #actual (name,value) values('".$type."',".$value.");";
        else $query = "insert into #actual (name,value) values('".$type."','".$value."');";
    query($query,$check);
    if(!$check) $check_all_ok=false;      
  }
  
  //aktualizace prumeru hodiny
  function update_statistics_hour($table, $date, $name, $value)
  {
    global $check_all_ok, $first_value;
    //zaznam neexistuje
    if(count(query("select * from ".$table." where date='".$date."'",$check))==0 && $check)
    {
      $query = "insert into ".$table." (date,temperature,humidity,light) values('".$date."','0','0','0');";
      query($query,$check);
      $first_value = true;
    }  
    //aktualizace prumeru    
    if($check) $query = "update ".$table." set ".$name."=".($first_value?"'".$value."'":"(".$name."_sum+".$value.")/(".$name."_count+1)").", ".$name."_sum=".$name."_sum+".$value.", ".$name."_count=".$name."_count+1 where date='".$date."' limit 1;";  
    query($query,$check);
    //smazani starych zaznamu
    if($table == '#hour') query("delete from ".$table." where date < DATE_SUB(NOW() , INTERVAL 3 DAY)",$check);
    //kontrola vse ok
    if(!$check) $check_all_ok=false;      
  }

  //aktualizace prumeru dny
  function update_statistics_day($table, $date, $name, $value)
  {
    global $check_all_ok, $first_value;
    //zaznam neexistuje
    if(count(query("select * from #day where date='".$date."'",$check))==0 && $check)
    {
      $query = "insert into ".$table." (date,temperature,humidity,light) values('".$date."','0','0','0');";
      query($query,$check);
      $first_value = true;
    }
    //aktualizace prumeru    
    if($check) $query = "update ".$table." set ".$name."=(select avg(".$name.") from meteo_hour where date like '".$date."%') where date='".$date."' limit 1;";
    //echo $query;
    query($query,$check);
    //kontrola vse ok
    if(!$check) $check_all_ok=false;
  }

  $check_all_ok = true;
  $temperature = null;
  $humidity = null;
  $light = null;  
  
  //aktuální data ze senzorů 
  if(isset($_GET['t'])) {input_value('temperature',floatval($_GET['t'])); $temperature = floatval($_GET['t']); }
  if(isset($_GET['h'])) {input_value('humidity',intval($_GET['h'])); $humidity = intval($_GET['h']); }
  if(isset($_GET['l'])) {input_value('light',intval($_GET['l'])); $light = intval($_GET['l']); }
  
  //aktualuizace času poslední aktualizace dat
  if(!is_null($temperature)) input_value('temperature_date','NOW()',true);
  if(!is_null($humidity)) input_value('humidity_date','NOW()',true);
  if(!is_null($light)) input_value('light_date','NOW()',true); 
  if(!is_null($temperature) || !is_null($humidity) || !is_null($light))
  {
    input_value('date','NOW()',true);
  }
  
  //aktualizace průměrů naměřených hodnot, hodiny
  $date = date('Y-m-d H');
  $first_value = false;
  if(!is_null($temperature)) update_statistics_hour('#hour',$date,'temperature', $temperature);
  if(!is_null($humidity)) update_statistics_hour('#hour',$date,'humidity', $humidity);
  if(!is_null($light)) update_statistics_hour('#hour',$date,'light', $light);  
  
  //aktualizace průměrů naměřených hodnot, dny
  $date = date('Y-m-d');
  $first_value = false;
  if(!is_null($temperature)) update_statistics_day('#day',$date,'temperature', $temperature);
  if(!is_null($humidity)) update_statistics_day('#day',$date,'humidity', $humidity);
  if(!is_null($light)) update_statistics_day('#day',$date,'light', $light); 
  
  //vypíše ok, pokud všechny operace byli úspěšné 
  if($check_all_ok) echo 'ok';
?>