var randomScalingFactor = function() {
    return Math.round(Math.random() * 10);
    //return 0;
};
var randomColorFactor = function() {
    return Math.round(Math.random() * 255);
};
var randomColor = function(opacity) {
    return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
};

/*$.each(config.data.datasets, function(i, dataset) {
    //dataset.borderColor = randomColor(0.4);
    //dataset.backgroundColor = randomColor(0.5);
    //dataset.pointBorderColor = randomColor(0.7);
    //dataset.pointBackgroundColor = randomColor(0.5);

    dataset.pointBorderWidth = 1;
});*/

//console.log(config.data);

function loadScript(url, callback) {

    var script = document.createElement("script")
    script.type = "text/javascript";

    if (script.readyState){  //IE
        script.onreadystatechange = function(){
            if (script.readyState == "loaded" ||
                    script.readyState == "complete"){
                script.onreadystatechange = null;
                callback();
            }
        };
    } else {  //Others
        script.onload = function(){
            callback();
        };
    }

    script.src = url;
    document.getElementsByTagName("head")[0].appendChild(script);
}

function setNewDatasets(chart_name,labels,dates,datasets,min1,max1,min2,max2) {
  config.data.datasets.splice(0, 1);
  config.data.datasets.splice(0, 1);
  config.options.scales.yAxes[0].ticks.suggestedMin = yAxexDefaultMin;
  config.options.scales.yAxes[0].ticks.suggestedMax = yAxexDefaultMax;
  config.data.labels = [];
  //set new labels
  config.data.labels = labels;
  //set new dates
  data_dates = dates;
  //set new datasets
  if(datasets.length==2)
  {
    config.data.datasets.push({
        label: "Vlhkost",
        data: datasets[0]
      }, {
        label: "Teplota",
        data: datasets[1]
      });
  }else
  {
    config.data.datasets.push({
        label: "Světlost",
        data: datasets[0]
      });
  }
  //update chart name  
  $('#chart_name').text(chart_name);
  updateMinMax(min1,max1,min2,max2);
  //update chart
  setDatasetColors();
  window.myLine.update();
  updateLegend();
}

function setDatasetColors() {
  //vlhkost
  config.data.datasets[0].borderColor = "rgba(0,0,255,0.4)";
  config.data.datasets[0].backgroundColor = "rgba(64,64,255,0.5)";
  config.data.datasets[0].pointBorderColor = "rgba(64,0,255,0.7)";
  config.data.datasets[0].pointBackgroundColor = "rgba(0,0,255,0.5)";
  config.data.datasets[0].pointBorderWidth = 1;
  config.data.datasets[0].fill = false;
  config.data.datasets[0].borderDash = [5, 5];
  if(config.data.datasets.length==2)
  {
    //teplota
    config.data.datasets[1].borderColor = "rgba(255,0,22,0.4)";
    config.data.datasets[1].backgroundColor = "rgba(255,0,22,0.5)";
    config.data.datasets[1].pointBorderColor = "rgba(255,0,0,22.7)";
    config.data.datasets[1].pointBackgroundColor = "rgba(255,0,0,0.5)";
    config.data.datasets[1].pointBorderWidth = 1;
  }
}

function updateMinMax(min1,max1,min2,max2)
{
  if(min1.length>0) $('#min1').text(min1);
  if(max1.length>0) $('#max1').text(max1);
  if(min2.length>0) $('#min2').text(min2);
  if(max2.length>0) $('#max2').text(max2);
}

function updateLegend() {
    $legendContainer = $('#legendContainer');
    $legendContainer.empty();
    $legendContainer.append(window.myLine.generateLegend());
}

window.onload = function() {
    var ctx = document.getElementById("canvas").getContext("2d");
    setDatasetColors();
    window.myLine = new Chart(ctx, config);
};

$('#hideTemperature').click(function() {
    config.data.datasets[0].hidden = false;
    config.data.datasets[1].hidden = true;
    config.options.scales.yAxes[0].ticks.suggestedMin = 0;
    config.options.scales.yAxes[0].ticks.suggestedMax = yAxexDefaultMax;
    window.myLine.update();
    updateLegend();
});

$('#hideHumidity').click(function() {
    config.data.datasets[0].hidden = true;
    config.data.datasets[1].hidden = false;
    config.options.scales.yAxes[0].ticks.suggestedMin = yAxexTemperatureMin;
    config.options.scales.yAxes[0].ticks.suggestedMax = yAxexTemperatureMax;
    window.myLine.update();
    updateLegend();
});

$('#showAll').click(function() {
    config.data.datasets[0].hidden = false;
    config.data.datasets[1].hidden = false;
    config.options.scales.yAxes[0].ticks.suggestedMin = yAxexDefaultMin;
    config.options.scales.yAxes[0].ticks.suggestedMax = yAxexDefaultMax;
    window.myLine.update();
    updateLegend();
});

$('#last24hours').click(function() {
  //local data
  setNewDatasets(chart_name_24hour,dataset24hourLabels,dataset24hourDates,[dataset24hourHumidity,dataset24hourTemperature],dataset24TemperatureMin,dataset24TemperatureMax,dataset24HumidityMin,dataset24HumidityMax);
});

$('#thisMonth').click(function() {
  if(!datasetMonthLoaded) {
    //load data from server
    loadScript("com/chart_th_month.php", function(){
      setNewDatasets(chart_name_month,datasetMonthLabels,datasetMonthDates,[datasetMonthHumidity,datasetMonthTemperature],datasetMonthTemperatureMin,datasetMonthTemperatureMax,datasetMonthHumidityMin,datasetMonthHumidityMax);
      datasetMonthLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_month,datasetMonthLabels,datasetMonthDates,[datasetMonthHumidity,datasetMonthTemperature],datasetMonthTemperatureMin,datasetMonthTemperatureMax,datasetMonthHumidityMin,datasetMonthHumidityMax);
  }      
});

$('#thisYear').click(function() {
  if(!datasetYearLoaded) {
    //load data from server
    loadScript("com/chart_th_year.php", function(){
      setNewDatasets(chart_name_year,datasetYearLabels,datasetYearDates,[datasetYearHumidity,datasetYearTemperature],datasetYearTemperatureMin,datasetYearTemperatureMax,datasetYearHumidityMin,datasetYearHumidityMax);
      datasetYearLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_year,datasetYearLabels,datasetYearDates,[datasetYearHumidity,datasetYearTemperature],datasetYearTemperatureMin,datasetYearTemperatureMax,datasetYearHumidityMin,datasetYearHumidityMax);
  }      
});

$('#yearlyAverages').click(function() {
  if(!datasetAllYearLoaded) {
    //load data from server
    loadScript("com/chart_th_all_years.php", function(){
      setNewDatasets(chart_name_all_year,datasetAllYearLabels,datasetAllYearDates,[datasetAllYearHumidity,datasetAllYearTemperature],datasetAllYearTemperatureMin,datasetAllYearTemperatureMax,datasetAllYearHumidityMin,datasetAllYearHumidityMax);
      datasetAllYearLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_all_year,datasetAllYearLabels,datasetAllYearDates,[datasetAllYearHumidity,datasetAllYearTemperature],datasetAllYearTemperatureMin,datasetAllYearTemperatureMax,datasetAllYearHumidityMin,datasetAllYearHumidityMax);
  }      
});

$('#last24hoursLight').click(function() {
  //local data
  setNewDatasets(chart_name_24hour,dataset24hourLabels,dataset24hourDates,[dataset24hourLight],dataset24LightMin,dataset24LightMax,'','');
});

$('#thisMonthLight').click(function() {
  if(!datasetMonthLoaded) {
    //load data from server
    loadScript("com/chart_light_month.php", function(){
      setNewDatasets(chart_name_month,datasetMonthLabels,datasetMonthDates,[datasetMonthLight],datasetMonthLightMin,datasetMonthLightMax,'','');
      datasetMonthLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_month,datasetMonthLabels,datasetMonthDates,[datasetMonthLight],datasetMonthLightMin,datasetMonthLightMax,'','');
  }      
});

$('#thisYearLight').click(function() {
  if(!datasetYearLoaded) {
    //load data from server
    loadScript("com/chart_light_year.php", function(){
      setNewDatasets(chart_name_year,datasetYearLabels,datasetYearDates,[datasetYearLight],datasetYearLightMin,datasetYearLightMax,'','');
      datasetYearLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_year,datasetYearLabels,datasetYearDates,[datasetYearLight],datasetYearLightMin,datasetYearLightMax,'','');
  }      
});

$('#yearlyAveragesLight').click(function() {
  if(!datasetAllYearLoaded) {
    //load data from server
    loadScript("com/chart_light_all_years.php", function(){
      setNewDatasets(chart_name_all_year,datasetAllYearLabels,datasetAllYearDates,[datasetAllYearLight],datasetAllYearLightMin,datasetAllYearLightMax,'','');
      datasetAllYearLoaded = true;
    });
  }else {
    //local data
    setNewDatasets(chart_name_all_year,datasetAllYearLabels,datasetAllYearDates,[datasetAllYearLight],datasetAllYearLightMin,datasetAllYearLightMax,'','');
  }      
});





$('#randomizeData').click(function() {
    $.each(config.data.datasets, function(i, dataset) {
        dataset.data = dataset.data.map(function() {
            return randomScalingFactor();
        });

    });

    window.myLine.update();
    updateLegend();
});

$('#changeDataObject').click(function() {
    config.data = {
        labels: ["0", "1", "2", "3", "4", "5"],
        datasets: [{
            label: "My First dataset",
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()],
            fill: false,
        }, {
            label: "My Second dataset",
            fill: false,
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()],
        }]
    };

    $.each(config.data.datasets, function(i, dataset) {
        dataset.borderColor = randomColor(0.4);
        dataset.backgroundColor = randomColor(0.5);
        dataset.pointBorderColor = randomColor(0.7);
        dataset.pointBackgroundColor = randomColor(0.5);
        dataset.pointBorderWidth = 1;
    });

    // Update the chart
    window.myLine.update();
});

$('#addDataset').click(function() {
    var newDataset = {
        label: 'Dataset ' + config.data.datasets.length,
        borderColor: randomColor(0.4),
        backgroundColor: randomColor(0.5),
        pointBorderColor: randomColor(0.7),
        pointBackgroundColor: randomColor(0.5),
        pointBorderWidth: 1,
        data: [],
    };

    for (var index = 0; index < config.data.labels.length; ++index) {
        newDataset.data.push(randomScalingFactor());
    }

    config.data.datasets.push(newDataset);
    window.myLine.update();
    updateLegend();
});

$('#addData').click(function() {
    if (config.data.datasets.length > 0) {
        config.data.labels.push('dataset #' + config.data.labels.length);

        $.each(config.data.datasets, function(i, dataset) {
            dataset.data.push(randomScalingFactor());
        });

        window.myLine.update();
        updateLegend();
    }
});

$('#removeDataset').click(function() {
    config.data.datasets.splice(0, 1);
    window.myLine.update();
    updateLegend();
});

$('#removeData').click(function() {
    config.data.labels.splice(-1, 1); // remove the label first

    config.data.datasets.forEach(function(dataset, datasetIndex) {
        dataset.data.pop();
    });

    window.myLine.update();
    updateLegend();
});        
