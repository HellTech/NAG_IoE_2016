1. zapojte obvod dle sch�matu

2. aplikace pou��v� GTK, aktualizujte jej na nejnov�j�� verzi
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install glade

3. po spu�t�n� programu (sudo python meteo.py) zkontrolujte nastaven� na kart� NASTAVEN�
- zkontrolujte odkaz pro odes�l�n� �daj� na web ZCU a vypl�te va�e sout�n� ID
- na webu openweather.org vyhledejte ID va�� lokace. P�ednastaven� ID odpov�d� m�stu Vele��n.
- na webu openweather.org registrac� z�sk�te appid, kter� je nutn� pro z�sk�v�n� aktu�ln� p�edpov��i
