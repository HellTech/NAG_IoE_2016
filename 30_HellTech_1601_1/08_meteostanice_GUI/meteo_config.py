import ConfigParser

secret_id = "aaa111bbb222"

default_server_enable = 1
default_server_url = "http://ioe.zcu.cz/th.php?id="+secret_id+"&temperature={t}&humidity={h}"
default_owm_enable = 1
default_owm_location_id = "3063307"
default_owm_appid = "aaa111bbb222"
default_wait_to_minute = 1
default_correct_time = 1
default_read_data_after_seconds = 30
default_report_after_seconds = 60

server_enable = default_server_enable
server_url = default_server_url
owm_enable = default_owm_enable
owm_location_id = default_owm_location_id
owm_appid = default_owm_appid
wait_to_minute = default_wait_to_minute
correct_time = default_correct_time
read_data_after_seconds = default_read_data_after_seconds
report_after_seconds = default_report_after_seconds

config = ConfigParser.SafeConfigParser()
config.read('meteo.ini')
server_enable = int(config.get('main', 'server_enable'))
server_url = config.get('main', 'server_url')
owm_enable = int(config.get('main', 'owm_enable'))
owm_location_id = config.get('main', 'owm_location_id')
owm_appid = config.get('main', 'owm_appid')
wait_to_minute = int(config.get('main', 'wait_to_minute'))
correct_time = int(config.get('main', 'correct_time'))
read_data_after_seconds = int(config.get('main', 'read_data_time'))
report_after_seconds = int(config.get('main', 'report_time'))

def load_config_to_GUI(self):
	self.builder.get_object("switch1").set_active(server_enable)
	self.builder.get_object("textview1").get_buffer().set_text(server_url)
	self.builder.get_object("switch3").set_active(owm_enable)
	self.builder.get_object("entry3").set_text(owm_location_id)
	self.builder.get_object("entry1").set_text(owm_appid)
	self.builder.get_object("switch4").set_active(wait_to_minute)
	self.builder.get_object("switch5").set_active(correct_time)
	self.builder.get_object("spinbutton1").set_value(read_data_after_seconds)
	self.builder.get_object("spinbutton2").set_value(report_after_seconds)

def save_config(self):
	config = ConfigParser.SafeConfigParser()
	#config.read('meteo.ini')
	config.add_section('main')
	config.set('main', 'server_enable', str(int(self.builder.get_object("switch1").get_active())))
	textbuffer =  self.builder.get_object("textview1").get_buffer() 
	startiter, enditer = textbuffer.get_bounds() 
	config.set('main', 'server_url', textbuffer.get_text(startiter, enditer,1))
	config.set('main', 'owm_enable', str(int(self.builder.get_object("switch3").get_active())))
	config.set('main', 'owm_location_id', str(self.builder.get_object("entry3").get_text()))
	config.set('main', 'owm_appid', str(self.builder.get_object("entry1").get_text()))
	config.set('main', 'wait_to_minute', str(int(self.builder.get_object("switch4").get_active())))
	config.set('main', 'correct_time', str(int(self.builder.get_object("switch5").get_active())))
	config.set('main', 'read_data_time', str(int(self.builder.get_object("spinbutton1").get_value())))
	config.set('main', 'report_time', str(int(self.builder.get_object("spinbutton2").get_value())))
	with open('meteo.ini', 'w') as f:
		config.write(f)
	
def default_config(self):
	server_enable = default_server_enable
	server_url = default_server_url
	owm_enable = default_owm_enable
	owm_location_id = default_owm_location_id
	owm_appid = default_owm_appid
	wait_to_minute = default_wait_to_minute
	correct_time = default_correct_time
	read_data_after_seconds = default_read_data_after_seconds
	report_after_seconds = default_report_after_seconds
	load_config_to_GUI(self)





