<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $num_days = date("t");
  $result = query("select DATE_FORMAT(date, '%Y-%m-%d') as date,ROUND(temperature,2) as temperature,ROUND(humidity,2) as humidity from #day where YEAR(date) = YEAR(NOW()) AND MONTH(date) = MONTH(NOW()) group by DAY(date) order by date",$check);
  $data_temperature="";
  $data_humidity = "";
  $temperature_min = null;
  $temperature_max = null;
  $humidity_min = null;
  $humidity_max = null;
  for($j=1;$j<=$num_days;$j++)
  {
    //label
    $data_labels.= '"'.$j.'"'.($j<$num_days?', ':'');
    //Data dates
    $data_dates.= '"'.den_nazev(date("w",strtotime($j.date(".m.Y")))).' '.($j<10?'0':'').$j.date(".m.Y").'"'.($j<$num_days?', ':'');
    //Data
    $search = searchForDate(date("Y-m-").($j<10?'0':'').$j,$result);
    $data_temperature.= (!is_null($search)?'"'.$result[$search]['temperature'].'"':'').($j>0?', ':'');
    $data_humidity.= (!is_null($search)?'"'.$result[$search]['humidity'].'"':'').($j>0?', ':'');
    if(!is_null($search))
    {
      if(is_null($humidity_min)) $humidity_min = $result[$search]['humidity'];
      if(is_null($humidity_max)) $humidity_max = $result[$search]['humidity'];
      if(is_null($temperature_min)) $temperature_min = $result[$search]['temperature'];
      if(is_null($temperature_max)) $temperature_max = $result[$search]['temperature'];
      if($result[$search]['humidity']<$humidity_min) $humidity_min = $result[$search]['humidity'];
      if($result[$search]['humidity']>$humidity_max) $humidity_max = $result[$search]['humidity'];
      if($result[$search]['temperature']<$temperature_min) $temperature_min = $result[$search]['temperature'];
      if($result[$search]['temperature']>$temperature_max) $temperature_max = $result[$search]['temperature'];      
    }
  }
?>
var datasetMonthLabels = [<?php echo $data_labels; ?>];
var datasetMonthDates = [<?php echo $data_dates; ?>];
var datasetMonthHumidity = [<?php echo $data_humidity; ?>];
var datasetMonthTemperature = [<?php echo $data_temperature; ?>];
var datasetMonthTemperatureMin = "<?php echo $temperature_min; ?>";
var datasetMonthTemperatureMax = "<?php echo $temperature_max; ?>";
var datasetMonthHumidityMin = "<?php echo $humidity_min; ?>";
var datasetMonthHumidityMax = "<?php echo $humidity_max; ?>";
