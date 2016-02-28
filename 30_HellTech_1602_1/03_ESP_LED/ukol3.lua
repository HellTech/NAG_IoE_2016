gpio.mode(3, gpio.OUTPUT)
gpio.mode(4, gpio.OUTPUT)
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
	buf = buf.."Dioda LED GPIO 2 <button name=\"pin\" value=\"ON2\" onclick=\"form.submit()\">Zapnout</button><button name=\"pin\" value=\"OFF2\" onclick=\"form.submit()\">Vypnout</button><br>";
	buf = buf.."Dioda LED GPIO 0, 2 <button name=\"pin\" value=\"BLINK1\" onclick=\"form.submit()\">Zablikat</button><br>";
        --local _on,_off = "",""
        if(_GET.pin == "ON1")then
              gpio.write(3, gpio.HIGH);
	end
        if(_GET.pin == "OFF1")then
              gpio.write(3, gpio.LOW);
	end
        if(_GET.pin == "ON2")then
              gpio.write(4, gpio.HIGH);
	end
        if(_GET.pin == "OFF2")then
              gpio.write(4, gpio.LOW);
        end
	if(_GET.pin == "BLINK1")then
              for i=1, 10, 1 do
		gpio.write(3, gpio.HIGH);
		gpio.write(4, gpio.HIGH);
		tmr.delay(1000000)
		gpio.write(3, gpio.LOW);
		gpio.write(4, gpio.LOW);
		i = i + 1
		tmr.delay(1000000)
              end
        end
	buf = buf.."</form>";
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
