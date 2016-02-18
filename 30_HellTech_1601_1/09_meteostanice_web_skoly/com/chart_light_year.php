<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $result = query("select DATE_FORMAT(date, '%Y-%m') as date,ROUND(AVG(light),2) as light from #day where YEAR(date) = YEAR(NOW()) group by MONTH(date) order by date",$check);
  $data_light = "";
  $light_min = null;
  $light_max = null;
  for($j=1;$j<=12;$j++)
  {
    //label
    $data_labels.= '"'.mesic_nazev($j).'"'.($j<12?', ':'');
    //Data dates
    $data_dates.= '"'.mesic_nazev($j).date(" Y").'"'.($j<12?', ':'');
    //Data
    $search = searchForDate(date("Y-").($j<10?'0':'').$j,$result);
    $data_light.= (!is_null($search)?'"'.$result[$search]['light'].'"':'').($j>0?', ':'');
    if(!is_null($search))
    {
      if(is_null($light_min)) $light_min = $result[$search]['light'];
      if(is_null($light_max)) $light_max = $result[$search]['light'];
      if($result[$search]['light']<$light_min) $light_min = $result[$search]['light'];
      if($result[$search]['light']>$light_max) $light_max = $result[$search]['light'];
    }
  }
?>
var datasetYearLabels = [<?php echo $data_labels; ?>];
var datasetYearDates = [<?php echo $data_dates; ?>];
var datasetYearLight = [<?php echo $data_light; ?>];
var datasetYearLightMin = "<?php echo $light_min; ?>";
var datasetYearLightMax = "<?php echo $light_max; ?>";
