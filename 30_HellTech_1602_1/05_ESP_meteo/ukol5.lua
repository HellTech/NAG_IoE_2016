secretid = "111AAA222BBB"

require('ds18b20')
gpio0 = 3
gpio2 = 4
ds18b20.setup(gpio0)
require('dht11')


--- Get temp and send data
function sendData()
dht11.getTemp()
-- conection
-- print("Sending data")
conn=net.createConnection(net.TCP, 0) 
conn:on("receive", function(conn, payload) print(payload) end)
-- ioe.zcu.cz 147.228.53.14
conn:connect(80,'147.228.53.14') 
conn:send("GET /esp.php?id="..secretid.."&temperature="..dht11.Temperature.."."..dht11.TemperatureDec.." HTTP/1.1\r\n") 
conn:send("Host: ioe.zcu.cz\r\n") 
conn:send("Accept: */*\r\n") 
conn:send("User-Agent: Mozilla/4.0 (compatible; esp8266 Lua; Windows NT 5.1)\r\n")
conn:send("\r\n")
conn:on("sent",function(conn)
                      -- print("Closing connection")
                      conn:close()
                  end)
conn:on("disconnection", function(conn)
                      -- print("Got disconnection...")
  end)
end


-- send data every X ms
tmr.alarm(2, 60000, 1, function() sendData() end )



gpio.mode(gpio2, gpio.OUTPUT)
srv=net.createServer(net.TCP) 
srv:listen(80,function(conn) 
    conn:on("receive", function(client,request)
        local buf = "";
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then 
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP"); 
        end
        local _GET = {}
        if (vars ~= nil)then 
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do 
                _GET[k] = v 
            end 
        end
        t1=ds18b20.read()
	      t1=ds18b20.read()
        buf = buf.."<meta charset=\"UTF-8\"><h1>Meteostanice 30-HELLTECH</h1><form src=\"/\">";
        buf = buf.."Teplota: "..t1.." °C<br>";
        buf = buf.."Vlhkost: "..dht11.Humidity.."."..dht11.HumidityDec.." %<br>";
        t1 = nil
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
