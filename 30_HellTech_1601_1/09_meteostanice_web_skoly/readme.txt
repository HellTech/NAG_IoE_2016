1. Importujte do MySQL databáze strukturu mysql/import.sql
2. Upravte nastaveni v souboru includes/config.inc.php.
- nastavení pøipojení k MySQL databázi (dbhost, dbuser, dbpass, dbname)
- na webu openweather.org vyhledejte ID vaší lokace. Pøednastavené ID odpovídá mìstu Velešín.
- na webu openweather.org registrací získáte appid, které je nutné pro získávání aktuální pøedpovìïi
3. Vkládat aktuální údaje do databáze lze následujícím zpùsobem:
Teplota: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0
Vlhkost: http://example.cz/com/meteo.php?id=aaa111bbb222&h=90
Osvìtlenost: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0&h=90&l=1500
Vkládat lze souèasnì jeden, dva nebo všechny tøi údaje souèasnì: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0&h=90&l=1500

