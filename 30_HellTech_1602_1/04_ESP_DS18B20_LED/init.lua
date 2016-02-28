--init.lua
print("Pripojovani k WiFi...")
wifi.setmode(wifi.STATION)
--pristupe udaje k WiFi
wifi.sta.config("SSID","PASSWORD")
wifi.sta.connect()
tmr.alarm(1, 1000, 1, function() 
if wifi.sta.getip()== nil then 
print("Zjišťování IP adresy...") 
else 
tmr.stop(1)
print("Připojeno, IP adresa je "..wifi.sta.getip())
dofile("ukol4.lua")
end 
end)


