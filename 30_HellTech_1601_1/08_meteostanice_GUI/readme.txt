1. zapojte obvod dle schématu

2. aplikace používá GTK, aktualizujte jej na nejnovìjší verzi
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install glade

3. po spuštìní programu (sudo python meteo.py) zkontrolujte nastavení na kartì NASTAVENÍ
- zkontrolujte odkaz pro odesílání údajù na web ZCU a vyplòte vaše soutìžní ID
- na webu openweather.org vyhledejte ID vaší lokace. Pøednastavené ID odpovídá mìstu Velešín.
- na webu openweather.org registrací získáte appid, které je nutné pro získávání aktuální pøedpovìïi
