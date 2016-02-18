<?php
  if(!isset($main)) exit;
?>
<div id="chart_name">Posledních 24 hodin</div>
<div style="width:100%;">
  <canvas id="canvas" style="width:100%;height:100%"></canvas>
</div>
<br>
<br>
<button id="last24hoursLight">Posledních 24 hodin</button>
<button id="thisMonthLight">Tento měsíc</button>
<button id="thisYearLight">Tento rok</button>
<button id="yearlyAveragesLight">Roční průměry</button>
<br />
<br />
<?php 
  //label
  $data_labels="";
  for($j=23;$j>=0;$j--)
  {
    $cas = date("H")-$j;
    if($cas<0) $cas = 24 + $cas;
    $data_labels.= '"'.$cas.':00"'.($j>0?', ':'');
  }
  //data
  $result = query("select date,ROUND(light,2) as light from #hour where date > DATE_SUB(NOW() , INTERVAL 1 DAY) order by date",$check);
  $data_light = "";
  $light_min = null;
  $light_max = null;
  for($j=23;$j>=0;$j--)
  {
    $den = date("Y-m-d H", time() - 60 * 60 * $j);
    $search = searchForDate($den,$result);
    $data_light.= (!is_null($search)?'"'.$result[$search]['light'].'"':'').($j>0?', ':'');
    if(!is_null($search))
    {
      if(is_null($light_min)) $light_min = $result[$search]['light'];
      if(is_null($light_max)) $light_max = $result[$search]['light'];
      if($result[$search]['light']<$light_min) $light_min = $result[$search]['light'];
      if($result[$search]['light']>$light_max) $light_max = $result[$search]['light'];      
    }
  }
  $data_dates="";
  for($j=23;$j>=0;$j--)
  {
    $cas = date("H")-$j;
    $den = date("d.m.Y");
    if($cas<0)
    {
      $cas = 24 + $cas;
      $den = date("d.m.Y", time() - 60 * 60 * 24);
    }
    $data_dates.= '"'.den_nazev(date("w",strtotime($den))).' '.$den.' '.$cas.':00"'.($j>0?', ':'');
  }
  //min, max
  if(!is_null($light_min)) echo 'Minimální světlost: <span id="min1">',$light_min,'</span> lx<br />';
  if(!is_null($light_max)) echo 'Maximální světlost: <span id="max1">',$light_max,'</span> lx<br />';
?>
  <script>
      var dataset24hourLabels = [<?php echo $data_labels; ?>];
      var dataset24hourDates = [<?php echo $data_dates; ?>];
      var dataset24hourLight = [<?php echo $data_light; ?>];
      var dataset24LightMin = "<?php echo $light_min; ?>";
      var dataset24LightMax = "<?php echo $light_max; ?>";
      var data_dates = dataset24hourDates;
      var datasetMonthLoaded = false;
      var datasetYearLoaded = false;
      var datasetAllYearLoaded = false;
      var yAxexDefaultMin = 0;
      var yAxexDefaultMax = 100;
      var chart_name_24hour = $('#chart_name').text();
      var chart_name_month = "Měsíční přehled";
      var chart_name_year = "Roční přehled";
      var chart_name_all_year = "Roční průměry";
      var config = {
          type: 'line',
          data: {
              labels: dataset24hourLabels,
              datasets: [{
                  label: "Světlost",
                  data: dataset24hourLight
              }]
          },
          options: {
              responsive: true,
              tooltips: {
                  mode: 'label',
                  callbacks: {
                      title: function(tooltipItem, data) {
                            //console.log(tooltipItem);
                            //console.log(data);
                            return data_dates[tooltipItem[0].index];                             
                       },
                      label: function(tooltipItem, data) {
                           if(tooltipItem.yLabel=="undefined" || isNaN(tooltipItem.yLabel))
                            return "žádná hodnota";
                           return tooltipItem.yLabel+' lx';                             
                       } 
                  }
              },
              hover: {
                  mode: 'dataset'
              },
              scales: {
                  xAxes: [{
                      display: true,
                      scaleLabel: {
                          show: true,
                          labelString: 'Čas'
                      }
                  }],
                  yAxes: [{
                      display: true,
                      scaleLabel: {
                          show: true,
                          labelString: 'Hodnota'
                      },
                      ticks: {
                          suggestedMin: yAxexDefaultMin,
                          suggestedMax: yAxexDefaultMax,
                      }
                  }]
              },
          }
      };
  </script>
  <script type='text/javascript' src='includes/chart_script.js'></script>
