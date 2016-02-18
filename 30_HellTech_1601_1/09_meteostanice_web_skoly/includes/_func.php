<?php

function query($query, &$check)
{
    global $conn;
    $check = true;
    $result = mysql_query(replaceTableAlias($query), $conn) or $check = false;
    if (!$check)
        return null;
    for ($i = 0; $i < @mysql_num_rows($result); $i++)
    {
        $returnVar[$i] = mysql_fetch_array($result, MYSQL_ASSOC);
    }
    @mysql_free_result($result);
    return ($returnVar);
}

function queryFirst($query,&$check)
{
    $result = query($query,$check);
	if($check and count($result)>0)
	{
		return $result[0];
	}else
	{
		return $result;
	}
}

function queryFirstCell($query,&$check)
{
    $result = query($query,$check);
	if($check and count($result)>0)
	{
		return reset($result[0]);
	}else
	{
		return $result;
	}
}

function queryLastInsertID()
{
    return mysql_insert_id();
}

function replaceTblArray()
{
    global $cfg;
    $tblTranslated = array();
    foreach($cfg as $key => $value)
    {
        $tblTranslated['#'.$key] = $cfg[$key];
    }
    return $tblTranslated;
}

function replaceTableAlias($query)
{
    global $tblTranslated;
    foreach ($tblTranslated as $key => $value)
    {
    	$query = str_replace($key, $value, $query);
    }
    return $query;
}

function searchForDate($id, $array) {
 foreach ($array as $key => $val) {
     if ($val['date'] === $id) {
         return $key;
     }
 }
 return null;
}

function mesic_nazev($mesic) {
  $nazvy = array('leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září', 'říjen', 'listopad', 'prosinec');
  return $nazvy[$mesic-1];
}

function den_nazev($den) {
   $nazvy = array('neděle', 'pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota');
   return $nazvy[$den];
}

function foo($data)
{
    echo '<pre>';
    print_r($data);
    echo '</pre>';
}

function firstLetterUpper($text)
{
    return mb_convert_case($text, MB_CASE_TITLE, "UTF-8");
}

// A function to return the Roman Numeral, given an integer
function numberToRoman($num)
{
		// Make sure that we only use the integer portion of the value
		$n = intval($num);
		$result = '';
		// Declare a lookup array that we will use to traverse the number:
		$lookup = array('M' => 1000, 'CM' => 900, 'D' => 500, 'CD' => 400,
		'C' => 100, 'XC' => 90, 'L' => 50, 'XL' => 40,
		'X' => 10, 'IX' => 9, 'V' => 5, 'IV' => 4, 'I' => 1);
		foreach ($lookup as $roman => $value)
		{
			// Determine the number of matches
			$matches = intval($n / $value);
			// Store that many characters
			$result .= str_repeat($roman, $matches);
			// Substract that from the number
			$n = $n % $value;
		}
		// The Roman numeral should be built, return it
		return $result;
}

?>