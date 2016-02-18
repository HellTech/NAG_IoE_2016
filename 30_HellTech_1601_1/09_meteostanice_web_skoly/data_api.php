<?php
  if(!isset($main)) exit;
?>
<div class="apidata">
  <span>Aktuální hodnoty</span><br />
  <div>
    XML <a href="com/api.php?type=xml&date=today">[zobrazit]</a>, <a href="com/api.php?type=xml&date=today&download">[stáhnout]</a><br />
    CSV <a href="com/api.php?type=csv&date=today">[zobrazit]</a>, <a href="com/api.php?type=csv&date=today&download">[stáhnout]</a><br />
  </div>
  <br />
  <span>Tento měsíc</span><br />
  <div>
    XML <a href="com/api.php?type=xml&date=month">[zobrazit]</a>, <a href="com/api.php?type=xml&date=month&download">[stáhnout]</a><br />
    CSV <a href="com/api.php?type=csv&date=month">[zobrazit]</a>, <a href="com/api.php?type=csv&date=month&download">[stáhnout]</a><br />
  </div>
  <br />
  <span>Kompletní sada dat</span><br />
  <div>
    XML <a href="com/api.php?type=xml">[zobrazit]</a>, <a href="com/api.php?type=xml&download">[stáhnout]</a><br />
    CSV <a href="com/api.php?type=csv">[zobrazit]</a>, <a href="com/api.php?type=csv&download">[stáhnout]</a><br />
  </div>
  <br />
</div>