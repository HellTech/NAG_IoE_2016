V tomto úkolu byl pouit LCD displej.
Návod na zprovoznìní I2C (I2C Installation for Raspberry Pi – Step by Step Guide):
http://skpang.co.uk/blog/archives/575

Návod na zapojení a zprovoznìní LCD displeje:
http://malinowo.net.pl/raspberry-pi-ekran-lcd-4x20-hd44780-konwerter-i2c/

Dále je tøeba zkontrolovat I2C adresu v souboru lcddriver.py
pomocí pøíkazu sudo i2cdetect -y 0 pøípadnì sudo i2cdetect -y 1 detekujte I2C zaøízení 
a porovnejte zda je jištìná adresa 0x27. Pokud ne tak ji zmìnte v souboru lcdriver.py.

Program spuste souborem 05_run_me.py. Pokud nechcete pouívat LCD displej spuste 
jen soubor 05_morse.py.

Program pouívá lokální zvukovı vıstup (RCA jack):
http://rpishop.cz/raspberry-pi-prislusenstvi/69-kabel-35mm3x-cinch-15m.html

