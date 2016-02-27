require('ds18b20')
gpio0 = 3
gpio2 = 4
ds18b20.setup(gpio0)



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
        buf = buf.."<meta charset=\"UTF-8\"><h1>Zapnutí a vypnutí diody</h1><form src=\"/\">";
	buf = buf.."Dioda LED GPIO 0 <button name=\"pin\" value=\"ON1\" onclick=\"form.submit()\">Zapnout</button><button name=\"pin\" value=\"OFF1\" onclick=\"form.submit()\">Vypnout</button><br>";	
	t1=ds18b20.read()
	t1=ds18b20.read()
	--print("Temp:"..t1.." C\n")
	buf = buf.."Teplota: "..t1.." °C";	
        --local _on,_off = "",""
        if(_GET.pin == "ON1")then
              gpio.write(gpio2, gpio.HIGH);
	end
        if(_GET.pin == "OFF1")then
              gpio.write(gpio2, gpio.LOW);
	end
	buf = buf.."</form>";
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
