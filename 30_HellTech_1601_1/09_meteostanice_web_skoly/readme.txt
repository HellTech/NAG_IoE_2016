1. Importujte do MySQL datab�ze strukturu mysql/import.sql
2. Upravte nastaveni v souboru includes/config.inc.php.
- nastaven� p�ipojen� k MySQL datab�zi (dbhost, dbuser, dbpass, dbname)
- na webu openweather.org vyhledejte ID va�� lokace. P�ednastaven� ID odpov�d� m�stu Vele��n.
- na webu openweather.org registrac� z�sk�te appid, kter� je nutn� pro z�sk�v�n� aktu�ln� p�edpov��i
3. Vkl�dat aktu�ln� �daje do datab�ze lze n�sleduj�c�m zp�sobem:
Teplota: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0
Vlhkost: http://example.cz/com/meteo.php?id=aaa111bbb222&h=90
Osv�tlenost: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0&h=90&l=1500
Vkl�dat lze sou�asn� jeden, dva nebo v�echny t�i �daje sou�asn�: http://example.cz/com/meteo.php?id=aaa111bbb222&t=22.0&h=90&l=1500

