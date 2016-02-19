#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import gtk
from gi.repository import Gtk as gtk
from gi.repository.GdkPixbuf import Pixbuf 
from gi.repository import Gio 
from gi.repository import GObject 
from gi.repository import GLib
import urllib2, json, datetime, time, os, sys, threading
import meteo_function
from meteo_function import *
import meteo_config
from meteo_config import *
import meteo_gpio
from meteo_gpio import *

time_to_next_read_data = read_data_after_seconds
time_to_next_report = report_after_seconds

#owm_url = 'http://api.openweathermap.org/data/2.5/weather?id='+default_owm_location_id+'&appid='+default_owm_appid+'&units=metric&mode=json'

class Meteostation:
	def onDeleteWindow(self, object, data=None):
		gtk.main_quit()

	def on_gtk_quit_activate(self, menuitem, data=None):
		gtk.main_quit()

	def clock_time(self):
		global time_to_next_read_data, time_to_next_report, time_to_next_owm
		try:
			now = datetime.datetime.now()
			#datum
			self.builder.get_object("label39").set_text(now.strftime('%d.%m.%Y'))
			#cas
			self.builder.get_object("label40").set_text(now.strftime('%H:%M:%S'))
			#cast dne
			cast_dne = ""
			hodina = int(now.strftime('%H'))
			if 6 <= hodina < 10:
				cast_dne = "ráno"
			elif 10 <= hodina < 12:
				cast_dne = "dopoledne"
			elif hodina == 12:
				cast_dne = "poledne"
			elif 13 <= hodina < 18:
				cast_dne = "odpoledne"
			elif 18 <= hodina < 22:
				cast_dne = "večer"
			else:
				cast_dne = "noc"
			self.builder.get_object("label14").set_text(cast_dne)
			#den v tydnu
			self.builder.get_object("label13").set_text(denTydne(int(now.strftime('%d')),int(now.strftime('%m')),int(now.strftime('%Y'))))
			#mesic
			self.builder.get_object("label20").set_text(mesicNazev(int(now.strftime('%m'))))
			#svatek
			self.builder.get_object("label32").set_text(dnes_svatek(int(now.strftime('%m')),int(now.strftime('%d'))))
			#den v roce
			self.builder.get_object("label18").set_text(str(now.timetuple().tm_yday))
			#cislo tydne
			#self.builder.get_object("label20").set_text(now.strftime('%U'))
			cislo_tydne = str(now.isocalendar()[1])
			if int(cislo_tydne) % 2 == 0:
				cislo_tydne += " (sudý)"
			else:
				cislo_tydne += " (lichý)"
			self.builder.get_object("label33").set_text(cislo_tydne)
			#cas do dalsi aktualizace
			if time_to_next_read_data>0:
				time_to_next_read_data -= 1
			if time_to_next_report>0:
				time_to_next_report -= 1
			if time_to_next_owm>0:
				time_to_next_owm -= 1
			#self.builder.get_object("time_remaining_label").set_text(str(time_to_next_read_data)+" s"+" / "+str(time_to_next_report)+" s" +" / "+str(time_to_next_owm)+" s")
			self.builder.get_object("time_remaining_label").set_text(str(datetime.datetime.now().strftime("%H:%M")))
		finally:
			return True
			#report/update clock countdown
			'''
			if report_last_second != int(now.strftime('%S')):
				time_to_next_update -= 1
				time_to_next_report -= 1
			report_last_second = int(now.strftime('%S'))
				time.sleep(0.5)
			'''
			#auto update
			#GObject.timeout_add_seconds(1, self.update_clock)

	def clock_read_data(self):
		#print "clock_read_data "+str(datetime.datetime.now().strftime("%H:%S"))
		try:
			#temperature
			meteo_gpio.readTemperature()
			self.builder.get_object("label9").set_text(str(meteo_gpio.temperature)+ " °C")
			#humidity
			meteo_gpio.readHumidity()
			self.builder.get_object("label8").set_text(str(meteo_gpio.humidity)+ " %")
			#light
			meteo_gpio.readLight()
			self.builder.get_object("label42").set_text(str(meteo_gpio.light)+ " lx")
			self.builder.get_object("levelbar1").set_value(float(meteo_gpio.light)/1000)
			#info
			self.builder.get_object("label10").set_text(str(datetime.datetime.now().strftime("%H:%M:%S")))
		finally:
			return True

	def clock_owm(self):
		try:
			#print "clock_owm "+str(datetime.datetime.now().strftime("%H:%S"))
			response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?id='+meteo_config.owm_location_id+'&appid='+meteo_config.owm_appid+'&units=metric&mode=json')
			data = json.loads(response.read())
			response.close()
			temperature = float(data['main']['temp'])
			humidity = float(data['main']['humidity']) 
			self.builder.get_object("label25").set_text(str(temperature)+ " °C")
			self.builder.get_object("label26").set_text(str(humidity)+ " %")
			#print "OWM teplota "+str(temperature) + " °C"
			#print "OWM vlhkost "+str(humidity) + " %"
			#print "OWM aktualizováno -> "+datetime.datetime.fromtimestamp(int(data['dt'])).strftime('%d.%m.%Y %H:%M')
			#url = 'https://resources.cloud.genuitec.com/wp-content/uploads/2015/11/PRO-CODER-badge.png' 
			#self.builder.get_object("image3").set_from_file("pokus.jpg")
			#self.builder.get_object("image3").show()
			#response = urllib2.urlopen(url) 
			#input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None) 
			#pixbuf = Pixbuf.new_from_stream(input_stream, None) 
			#self.builder.get_object("image4").set_from_pixbuf(pixbuf)
			
			filename = data['weather'][0]['icon']
			if len(filename)>0:
				filename = filename + ".png"
				if not os.path.exists(filename):
					os.popen("wget http://openweathermap.org/img/w/"+filename)
				self.builder.get_object("image4").set_from_file(filename)
				self.builder.get_object("image4").show()
		finally:
			return True
	
	def clock_report(self):
		try:
			#print "clock_report "+str(datetime.datetime.now().strftime("%H:%S"))
			#self.builder.get_object("spinner1").set_visible(True)
			#self.builder.get_object("status_label").set_text("<<<>>>")
			self.pending_all()
			report_error = False
			
			textbuffer =  self.builder.get_object("textview1").get_buffer() 
			startiter, enditer = textbuffer.get_bounds() 
			urls_list = textbuffer.get_text(startiter, enditer,1).split('\n')
			for url in urls_list:
			  try:
				f = urllib2.urlopen(url.replace("{t}",str(meteo_gpio.temperature)).replace("{h}",str(meteo_gpio.humidity)).replace("{l}",str(meteo_gpio.light)))
				result_data = f.read().rstrip()
				f.close()
			  except:
				self.addRecord("Chyba odesilani dat na "+url)
				report_error = True
			#self.builder.get_object("spinner1").set_visible(False)
			#if report_error:
				#self.builder.get_object("status_label").set_text("ERROR")
			#else:
				#self.builder.get_object("status_label").set_text(str(datetime.datetime.now().strftime('%H:%M:%S')))
		finally:
			return True

	def update_openweather(self=None):
		try:
			response = urllib2.urlopen(meteo_config.owm_url)
			data = json.loads(response.read())
			response.close()
			#teplota
			self.builder.get_object("label25").set_text(str(data['main']['temp']) + " °C")
			#vlhkost
			self.builder.get_object("label26").set_text(str(data['main']['humidity']) + " %")
			#aktualizovano
			self.builder.get_object("label23").set_text(datetime.datetime.fromtimestamp(int(data['dt'])).strftime('%d.%m.%Y %H:%M'))
			#slunce vychazi
			self.builder.get_object("label35").set_text(datetime.datetime.fromtimestamp(int(data['sys']['sunrise'])).strftime('%H:%M'))
			#slunce zapada
			self.builder.get_object("label37").set_text(datetime.datetime.fromtimestamp(int(data['sys']['sunset'])).strftime('%H:%M'))
		finally:
			return True
	
	def pending_all(self=None):
		try:
			while gtk.events_pending():
				gtk.main_iteration_do(True)
		finally:
			return True
	
	def addRecord(self,text):
		self.builder.get_object("labellog").set_text(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S - ')+text+"\n"+self.builder.get_object("labellog").get_text())

	def report_clock(self):
		global repeat_update_after_seconds, repeat_report_after_seconds, time_to_next_update, time_to_next_report, report_last_second 
		try:
			#if True:
				#korekce start v celou minutu
				#time_to_next_update = 60 - int(datetime.datetime.now().strftime('%S'))
				#time_to_next_report = time_to_next_update
			#while meteo_config.wait_to_minute == 1:
			self.builder.get_object("time_remaining_label").set_text(str(time_to_next_update)+" s"+" / "+str(time_to_next_report)+" s")
			#self.pending_all()
			if time_to_next_update <= 0:
				#print("read data")
				readSenzorData(self)
				time_to_next_update = repeat_update_after_seconds
			if time_to_next_report <= 0:
				#print("send data")
				self.update_openweather()
				self.send_data_zcu()
				time_to_next_report = repeat_report_after_seconds
				if meteo_config.correct_time == 1:
					#korekce casu
					time_to_next_update = repeat_update_after_seconds
				#self.pending_all()
				#time.sleep(0.5)
		finally:
			return True

	def menu_quit_onclick(self, button):
		gtk.main_quit()
	
	def menu_about_onclick(self, button):
		return
	
	def default_config_onclick(self, button):
		meteo_config.default_config(self)
		
	def save_config_onclick(self, button):
		meteo_config.save_config(self)

	def my_timer(*args):
		print time.strftime("%H:%S")
		return True

	def __init__(self):
		global time_to_next_read_data, time_to_next_report, time_to_next_owm, repeat_read_data_after_seconds, repeat_report_after_seconds, repeat_owm_after_seconds

		self.gladefile = "meteo.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window1")
		self.window.show()

		#load config to GUI
		meteo_config.load_config_to_GUI(self)
		
		#spinnbutton fix
		adj = gtk.Adjustment(meteo_config.read_data_after_seconds, 1, 1000000, 1, 1, 1)
		spinBtn = self.builder.get_object("spinbutton1")
		spinBtn.configure(adj, 1, 0)
		adj2 = gtk.Adjustment(meteo_config.report_after_seconds, 1, 1000000, 1, 1, 1)
		spinBtn2 = self.builder.get_object("spinbutton2")
		spinBtn2.configure(adj2, 1, 0)
		
		
		
		#time
		GLib.timeout_add_seconds(1, self.clock_time)
		#owm
		self.clock_owm()
		GLib.timeout_add_seconds(meteo_config.report_after_seconds, self.clock_owm)
		#read sensors
		self.clock_read_data()
		print meteo_config.read_data_after_seconds
		GLib.timeout_add_seconds(meteo_config.read_data_after_seconds, self.clock_read_data)
		#report data
		self.clock_report()
		GLib.timeout_add_seconds(meteo_config.report_after_seconds, self.clock_report)
		
		#GLib.treads_init()
		#GLib.timeout_add_seconds(read_data_after_seconds, self.clock_read_data)
		
		
		#sleep_time = 1
		#if meteo_config.wait_to_minute == 1:
		#	sleep_time = 61 - time.time() % 60 - report_after_seconds
		#	time_to_next_report = int(sleep_time) + report_after_seconds
		#GLib.timeout_add_seconds(sleep_time, self.clock_run_clocs)
		self.window.fullscreen()
		self.addRecord("start Meteostanice")

if __name__ == "__main__":
	try:
		main = Meteostation()
		gtk.main()
	except KeyboardInterrupt:
		#gtk.main_quit()
		#sys.exit(0)
		print
		pass
	finally:
		#GPIO.setwarnings(False)
		#GPIO.cleanup()
		#sys.exit(0)
		print
