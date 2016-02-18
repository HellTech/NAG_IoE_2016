<?php
  if(!isset($main)) exit;
?>
<div id="chart_name">Posledních 24 hodin</div>
<div style="width:100%;">
  <canvas id="canvas" style="width:100%;height:100%"></canvas>
</div>
<br>
<br>
<button id="hideTemperature">Skrýt teplotu</button>
<button id="hideHumidity">Skrýt vlhkost</button>
<button id="showAll">Zobrazit vše</button>
<button id="last24hours">Posledních 24 hodin</button>
<button id="thisMonth">Tento měsíc</button>
<button id="thisYear">Tento rok</button>
<button id="yearlyAverages">Roční průměry</button>
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
  $result = query("select date,ROUND(temperature,2) as temperature,ROUND(humidity,2) as humidity from #hour where date > DATE_SUB(NOW() , INTERVAL 1 DAY) order by date",$check);
  $data_temperature="";
  $data_humidity = "";
  $temperature_min = null;
  $temperature_max = null;
  $humidity_min = null;
  $humidity_max = null;
  for($j=23;$j>=0;$j--)
  {
    $den = date("Y-m-d H", time() - 60 * 60 * $j);
    $search = searchForDate($den,$result);
    $data_temperature.= (!is_null($search)?'"'.$result[$search]['temperature'].'"':'').($j>0?', ':'');
    $data_humidity.= (!is_null($search)?'"'.$result[$search]['humidity'].'"':'').($j>0?', ':'');
    if(!is_null($search))
    {
      if(is_null($temperature_min)) $temperature_min = $result[$search]['temperature'];
      if(is_null($temperature_max)) $temperature_max = $result[$search]['temperature'];
      if(is_null($humidity_min)) $humidity_min = $result[$search]['humidity'];
      if(is_null($humidity_max)) $humidity_max = $result[$search]['humidity'];
      if($result[$search]['temperature']<$temperature_min) $temperature_min = $result[$search]['temperature'];
      if($result[$search]['temperature']>$temperature_max) $temperature_max = $result[$search]['temperature'];      
      if($result[$search]['humidity']<$humidity_min) $humidity_min = $result[$search]['humidity'];
      if($result[$search]['humidity']>$humidity_max) $humidity_max = $result[$search]['humidity'];      
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
  if(!is_null($temperature_min)) echo 'Minimální teplota: <span id="min1">',$temperature_min,'</span> °C<br />';
  if(!is_null($temperature_max)) echo 'Maximální teplota: <span id="max1">',$temperature_max,'</span> °C<br />';
  if(!is_null($humidity_min)) echo 'Minimální vlhkost: <span id="min2">',$humidity_min,'</span> %<br />';
  if(!is_null($humidity_max)) echo 'Maximální vlhkost: <span id="max2">',$humidity_max,'</span> %';
?>
  <script>
      var dataset24hourLabels = [<?php echo $data_labels; ?>];
      var dataset24hourDates = [<?php echo $data_dates; ?>];
      var dataset24hourHumidity = [<?php echo $data_humidity; ?>];
      var dataset24hourTemperature = [<?php echo $data_temperature; ?>];
      var dataset24TemperatureMin = "<?php echo $temperature_min; ?>";
      var dataset24TemperatureMax = "<?php echo $temperature_max; ?>";
      var dataset24HumidityMin = "<?php echo $humidity_min; ?>";
      var dataset24HumidityMax = "<?php echo $humidity_max; ?>";
      var data_dates = dataset24hourDates;
      var datasetMonthLoaded = false;
      var datasetYearLoaded = false;
      var datasetAllYearLoaded = false;
      var yAxexDefaultMin = -20;
      var yAxexDefaultMax = 100;
      var yAxexTemperatureMin = <?php echo floatval($temperature_min); ?>;
      var yAxexTemperatureMax = <?php echo floatval($temperature_max); ?>;
      var chart_name_24hour = $('#chart_name').text();
      var chart_name_month = "Měsíční přehled";
      var chart_name_year = "Roční přehled";
      var chart_name_all_year = "Roční průměry";
      var config = {
          type: 'line',
          data: {
              labels: dataset24hourLabels,
              datasets: [{
                  label: "Vlhkost",
                  data: dataset24hourHumidity
              }, {
                  label: "Teplota",
                  data: dataset24hourTemperature
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
                           if(tooltipItem.datasetIndex==0)
                            return tooltipItem.yLabel+' %';                             
                           else
                            return tooltipItem.yLabel+' °C';
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
