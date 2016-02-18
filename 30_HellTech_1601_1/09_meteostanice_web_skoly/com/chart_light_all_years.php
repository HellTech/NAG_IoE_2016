<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $result = query("select DATE_FORMAT(date, '%Y') as date,ROUND(AVG(light),2) as light from #day where YEAR(date) = YEAR(NOW()) group by YEAR(date) order by date",$check);
  $data_light = "";
  $light_min = null;
  $light_max = null;
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
    $data_light.= (!is_null($search)?'"'.$result[$search]['light'].'"':'').($j<$lastYear?', ':'');
    if(!is_null($search))
    {
      if(is_null($light_min)) $light_min = $result[$search]['light'];
      if(is_null($light_max)) $light_max = $result[$search]['light'];
      if($result[$search]['light']<$light_min) $light_min = $result[$search]['light'];
      if($result[$search]['light']>$light_max) $light_max = $result[$search]['light'];
    }
  }
?>
var datasetAllYearLabels = [<?php echo $data_labels; ?>];
var datasetAllYearDates = [<?php echo $data_dates; ?>];
var datasetAllYearLight = [<?php echo $data_light; ?>];
var datasetAllYearLightMin = "<?php echo $light_min; ?>";
var datasetAllYearLightMax = "<?php echo $light_max; ?>";
