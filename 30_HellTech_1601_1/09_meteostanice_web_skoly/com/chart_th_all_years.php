<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $result = query("select DATE_FORMAT(date, '%Y') as date,ROUND(AVG(temperature),2) as temperature,ROUND(AVG(humidity),2) as humidity from #day where YEAR(date) = YEAR(NOW()) group by YEAR(date) order by date",$check);
  $data_temperature="";
  $data_humidity = "";
  $temperature_min = null;
  $temperature_max = null;
  $humidity_min = null;
  $humidity_max = null;
  $firstYear = date("Y",strtotime($result[0]['date']));
  $lastYear = date("Y",strtotime($result[count($result)-1]['date'])); 
  for($j=$firstYear;$j<=$lastYear;$j++)
  {
    //label
    $data_labels.= '"'.$j.'"'.($j<$lastYear?', ':'');
    //Data dates
    $data_dates.= '"rok '.$j.'"'.($j<$lastYear?', ':'');
    //Data
    $search = searchForDate($j,$result);
    $data_temperature.= (!is_null($search)?'"'.$result[$search]['temperature'].'"':'').($j<$lastYear?', ':'');
    $data_humidity.= (!is_null($search)?'"'.$result[$search]['humidity'].'"':'').($j<$lastYear?', ':'');
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
var datasetAllYearLabels = [<?php echo $data_labels; ?>];
var datasetAllYearDates = [<?php echo $data_dates; ?>];
var datasetAllYearHumidity = [<?php echo $data_humidity; ?>];
var datasetAllYearTemperature = [<?php echo $data_temperature; ?>];
var datasetAllYearTemperatureMin = "<?php echo $temperature_min; ?>";
var datasetAllYearTemperatureMax = "<?php echo $temperature_max; ?>";
var datasetAllYearHumidityMin = "<?php echo $humidity_min; ?>";
var datasetAllYearHumidityMax = "<?php echo $humidity_max; ?>";
