V tomto �kolu byl pou�it LCD displej.
N�vod na zprovozn�n� I2C (I2C Installation for Raspberry Pi � Step by Step Guide):
http://skpang.co.uk/blog/archives/575

N�vod na zapojen� a zprovozn�n� LCD displeje:
http://malinowo.net.pl/raspberry-pi-ekran-lcd-4x20-hd44780-konwerter-i2c/

D�le je t�eba zkontrolovat I2C adresu v souboru lcddriver.py
pomoc� p��kazu sudo i2cdetect -y 0 p��padn� sudo i2cdetect -y 1 detekujte I2C za��zen� 
a porovnejte zda je ji�t�n� adresa 0x27. Pokud ne tak ji zm�nte v souboru lcdriver.py.

Program spus�te souborem 05_run_me.py. Pokud nechcete pou��vat LCD displej spus�te 
jen soubor 05_morse.py.

Program pou��v� lok�ln� zvukov� v�stup (RCA jack):
http://rpishop.cz/raspberry-pi-prislusenstvi/69-kabel-35mm3x-cinch-15m.html

