import machine, ssd1306
import urequests, json, time
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))

while True:
	oled = ssd1306.SSD1306_I2C(128, 64, i2c)
	oled.fill(0) 
	response = urequests.get('http://192.168.22.16:8080/last')
	j = json.loads(response.text)
	oled.text(str('temp'),0,0)
	oled.text(str(j[0]['temp']),0,10)
	oled.show()
	time.sleep(30)
