<?php
  require 'includes/_func.php';
  require 'includes/config.inc.php';
  $include_page = "home.php";
  $menu_item = 1;
  if(isset($_GET['page']))
  {
    switch($_GET['page'])
    {
      case 'home': $include_page = 'home.php'; $menu_item = 1; break;
      case 'temperature_humidity': $include_page = 'chart_temperature.php'; $menu_item = 2; break;
      case 'light': $include_page = 'chart_light.php'; $menu_item = 3; break;
      case 'api': $include_page = 'data_api.php'; $menu_item = 4; break;
      default: $include_page = 'home.php'; $menu_item = 1; 
    }  
  }
  $main = true;
?>
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='cs' lang='cs'>
<head>
<title>Meteostanice SOŠ strojní a elektrotechnická Velešín</title>
<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
<meta name='description' content='Meteostanice SOŠ strojní a elektrotechnická Velešín' />
<meta name='keywords' content='Meteostanice, SOŠ strojní a elektrotechnická, střední odborná škola, střední technická škola, Velešín, České Budějovice, Český Krumlov' />
<link rel='shortcut icon' href='http://sosvel.cz/images/favicon.ico' type='image/x-icon' />
<link rel='stylesheet' href='includes/styles.css' type='text/css' media='screen' />
<script type='text/javascript' src='includes/moment.js'></script>
<script type='text/javascript' src='includes/chartjs/Chart.js'></script>
<script src="http://sosvel.cz/includes/jquery.js"></script>
</head>
<body>
  <div class="container">
    <table id="maintable" border="0" cellpadding="0">
      <tr>
        <td class="header"></td>
      </tr>
      <tr>
        <td>
          <ul class="glossymenu">
          	<li<?php echo $menu_item==1?' class="current"':'';?>><a href="/"><b>Úvodní stránka</b></a></li>
          	<li<?php echo $menu_item==2?' class="current"':'';?>><a href="?page=temperature_humidity"><b>Graf teploty a vlhkosti</b></a></li>
          	<li<?php echo $menu_item==3?' class="current"':'';?>><a href="?page=light"><b>Světlost</b></a></li>	
          	<li<?php echo $menu_item==4?' class="current"':'';?>><a href="?page=api"><b>Strojově čitelná data</b></a></li>	
          	<li><a href="http://sosvel.cz/"><b>SOŠ Velešín</b></a></li>	
          </ul>
          <br />
          <br />
          <?php include($include_page); ?>
        </td>
      </tr>
      <tr id="table_footer">
        <td>&copy 2016 SOŠ strojní a elektrotechnická Velešín | <a href="http://sosvel.cz/">www.sosvel.cz</a></td>
      </tr>  
    </table>
  </div>  
</body>
</html>