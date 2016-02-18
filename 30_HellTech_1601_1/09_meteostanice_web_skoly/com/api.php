<?
  require '../includes/_func.php';
  require '../includes/config.inc.php';
  
  //type set
  if(!(isset($_GET['type']) && ($_GET['type']=='xml' || $_GET['type']=='csv')))
  {
    echo 'no type';
    exit;
  }

  //array to xml
  function array_to_xml( $data, &$xml_data ) {
      foreach( $data as $key => $value ) {
          if( is_array($value) ) {
              if( is_numeric($key) ){
                  $key = 'item'.$key;
              }
              $subnode = $xml_data->addChild($key);
              array_to_xml($value, $subnode);
          } else {
              $xml_data->addChild("$key",htmlspecialchars("$value"));
          }
       }
  }

  //array to csv 
  function array_2_csv($array) {
    $csv = array();
    foreach ($array as $item) {
        if (is_array($item)) {
            $csv[] = array_2_csv($item);
        } else {
            $csv[] = $item;
        }
    }
    return implode(',', $csv);
  }

  //load data
  $data = array();
  if(isset($_GET['date']))
  {
    switch($_GET['date'])
    {
      case 'today': 
        $date = queryFirstCell("select value from #actual where name='date'",$check);
        $temperature = queryFirstCell("select value from #actual where name='temperature'",$check);
        $humidity = queryFirstCell("select value from #actual where name='humidity'",$check);
        $light = queryFirstCell("select value from #actual where name='light'",$check);
        if($_GET['type']=='xml')
          $data = array("date" => $date, "temperature" => $temperature, "humidity" => $humidity, "light" => $light);
        else
          $data[1] = array("date" => $date, "temperature" => $temperature, "humidity" => $humidity, "light" => $light);                    
        break;
      case 'month': 
        $data = query("select date, temperature, humidity, light from #day where YEAR(date) = YEAR(NOW()) AND MONTH(date) = MONTH(NOW()) group by DAY(date) order by date",$check);
        break;
      default: echo 'bad date'; exit;          
    }
  }else $data = query("select * from #day order by date",$check);
 
  //creating SimpleXML    
  if($_GET['type']=='xml')
  {
    header('Content-Type: text/xml');
    if(isset($_GET['download']))
      header("Content-Disposition: attachment; filename=data.xml");
    header("Pragma: no-cache");
    header("Expires: 0");
    $xml_data = new SimpleXMLElement('<?xml version="1.0"?><data></data>');
    array_to_xml($data,$xml_data);
    echo $xml_data->asXML('/file/path/name.xml');
  }

  //creating CSV
  if($_GET['type']=='csv')
  {
    if(isset($_GET['download'])) {
      header('Content-Type: text/csv');
      header("Content-Disposition: attachment; filename=data.csv");
      header("Pragma: no-cache");
      header("Expires: 0");
    }
    $resp = array();
    $resp[0] = "date,temperature,humidity,light";
    foreach ($data as $entry) {
        $row = array();          
        foreach ($entry as $key => $value) {
            array_push($row, $value);
        }                        
        array_push($resp, implode(',', $row));
    }                            
    $csv_data = implode(PHP_EOL, $resp);
    if(!isset($_GET['download'])) echo '<pre>';
    print_r($csv_data);
    if(!isset($_GET['download'])) echo '</pre>'; 
  }

?>