<?php
  if(!isset($main)) exit;
  
  if ( !function_exists('json_decode') ){
    function json_decode($json) 
    {  
        // Author: walidator.info 2009 
        $comment = false; 
        $out = '$x='; 
    
        for ($i=0; $i<strlen($json); $i++) 
        { 
            if (!$comment) 
            { 
                if ($json[$i] == '{' || $json[$i] == '[')        $out .= ' array('; 
                else if ($json[$i] == '}' || $json[$i] == ']')    $out .= ')'; 
                else if ($json[$i] == ':')    $out .= '=>'; 
                else                         $out .= $json[$i];            
            } 
            else $out .= $json[$i]; 
            if ($json[$i] == '"')    $comment = !$comment; 
        } 
        eval($out . ';'); 
        return $x; 
    }  
  }
  
  //Sunrise and sunset
  $sun_rise = "";
  $sun_set = "";
  $owm_url = 'http://api.openweathermap.org/data/2.5/weather?id='.$cfg['owm_location_id'].'&appid='.$cfg['owm_appid'].'&units=metric';
  try
  {
    $json = file_get_contents($owm_url);
    $obj = json_decode($json);
    if(intval($obj['sys']['sunrise']>0)) $sun_rise = date('H:m', intval($obj['sys']['sunrise']));
    if(intval($obj['sys']['sunset']>0)) $sun_set = date('H:m', intval($obj['sys']['sunset']));
  }
  catch (Exception $e) {}
    
  //load data from database
  $temperature = '';
  $humidity = '';
  $light = '';
  $temperature = queryFirstCell("select value from #actual where name='temperature'");
  $humidity = queryFirstCell("select value from #actual where name='humidity'");
  $light = queryFirstCell("select value from #actual where name='light'");
  
?>
<div id="city_name">.:: <?php echo $cfg['location_name'];  ?> ::.</div>
<div class="Row">
    <div class="Column"><?php if(strlen($temperature)>0 and count(query("select value from #actual where name='temperature_date' and value > DATE_SUB(NOW() , INTERVAL 3 HOUR)"))>0) echo 'Teplota<br /><span>',$temperature,' °C</span>'; ?></div>
    <div class="Column"><?php if(strlen($humidity)>0 and count(query("select value from #actual where name='humidity_date' and value > DATE_SUB(NOW() , INTERVAL 3 HOUR)"))>0) echo 'Vlhkost<br /><span>',$humidity,' %</span>'; ?></div>
    <div class="Column"><?php if(strlen($light)>0 and count(query("select value from #actual where name='light_date' and value > DATE_SUB(NOW() , INTERVAL 3 HOUR)"))>0) echo 'Světlost<br /><span>',$light,' lx</span>'; ?></div>
</div>
<br />
<div class="Row">
    <div class="Column2">
      Den v týdnu: <?php echo den_nazev(date("w")); ?><br />
      Den v roce: <?php echo date("z")+1; ?><br />
    </div>
    <div class="Column2">
      Měsíc: <?php echo mesic_nazev(date("n")); ?><br />
      Týden v roce: <?php echo date("W")+0, (date("W")%2==0?' (sudý)':' (lichý)'); ?><br />
    </div>
    <div class="Column2">
      <?php if(strlen($sun_rise)>0) echo 'Slunce vychází: ', $sun_rise; ?><br />
      <?php if(strlen($sun_set)>0) echo 'Slunce zapadá: ', $sun_set; ?><br />
    </div>
</div>
<br />
<?php $date = queryFirstCell("select value from #actual where name='date'"); if(strlen($date)>0) echo 'Údaje senzorů aktualizovány: ',date('d.m.Y H:i',strtotime($date)); ?><br />
