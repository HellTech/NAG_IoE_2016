<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $result = query("select DATE_FORMAT(date, '%Y-%m') as date,ROUND(AVG(temperature),2) as temperature,ROUND(AVG(humidity),2) as humidity from #day where YEAR(date) = YEAR(NOW()) group by MONTH(date) order by date",$check);
  $data_temperature="";
  $data_humidity = "";
  $temperature_min = null;
  $temperature_max = null;
  $humidity_min = null;
  $humidity_max = null;
  for($j=1;$j<=12;$j++)
  {
    //label
    $data_labels.= '"'.mesic_nazev($j).'"'.($j<12?', ':'');
    //Data dates
    $data_dates.= '"'.mesic_nazev($j).date(" Y").'"'.($j<12?', ':'');
    //Data
    $search = searchForDate(date("Y-").($j<10?'0':'').$j,$result);
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
var datasetYearLabels = [<?php echo $data_labels; ?>];
var datasetYearDates = [<?php echo $data_dates; ?>];
var datasetYearHumidity = [<?php echo $data_humidity; ?>];
var datasetYearTemperature = [<?php echo $data_temperature; ?>];
var datasetYearTemperatureMin = "<?php echo $temperature_min; ?>";
var datasetYearTemperatureMax = "<?php echo $temperature_max; ?>";
var datasetYearHumidityMin = "<?php echo $humidity_min; ?>";
var datasetYearHumidityMax = "<?php echo $humidity_max; ?>";
