<?
  header('Content-Type: application/javascript');
  require '../includes/_func.php';
  require '../includes/config.inc.php'; 
  $data_labels="";
  $data_dates="";
  $num_days = date("t");
  $result = query("select DATE_FORMAT(date, '%Y-%m-%d') as date,ROUND(light,2) as light from #day where YEAR(date) = YEAR(NOW()) AND MONTH(date) = MONTH(NOW()) group by DAY(date) order by date",$check);
  $data_light = "";
  $light_min = null;
  $light_max = null;
  for($j=1;$j<=$num_days;$j++)
  {
    //label
    $data_labels.= '"'.$j.'"'.($j<$num_days?', ':'');
    //Data dates
    $data_dates.= '"'.den_nazev(date("w",strtotime($j.date(".m.Y")))).' '.($j<10?'0':'').$j.date(".m.Y").'"'.($j<$num_days?', ':'');
    //Data
    $search = searchForDate(date("Y-m-").($j<10?'0':'').$j,$result);
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
var datasetMonthLabels = [<?php echo $data_labels; ?>];
var datasetMonthDates = [<?php echo $data_dates; ?>];
var datasetMonthLight = [<?php echo $data_light; ?>];
var datasetMonthLightMin = "<?php echo $light_min; ?>";
var datasetMonthLightMax = "<?php echo $light_max; ?>";
