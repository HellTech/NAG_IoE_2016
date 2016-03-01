# NAG IoE 2016, 4. kolo, únor 2015
Když jsme do modulu nahráli tento fimware tak abychom kod nemuseli psát přímo do picocomu zvolili jsme program který se jmenuje luatool a pomocí tohoto jsme nahrávali soubor s příslušným kodem pomocí říkazu: ./luatool.py --port /dev/AMA0 --src “název souboru“.lua --dest “název souboru“.lua –verbose
Poté jsme daný soubor spustily příkazem: dofile(název souboru)


