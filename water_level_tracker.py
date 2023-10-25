import RPi.GPIO as gpio
import time as time
import Adafruit_CharLCD as LCD
trigger=26
echo=27
buzzer=12
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
gpio.setup(trigger,output)
gpio.setup(echo,input)
gpio.setup(buzzer,output)
def distance_func():
    gpio.output(trigger,True)
    time.delay(0.0001)
    gpio.output(trigger,False)
    while(gpio.input(echo)==0):
        start=time.time();
    while(gpio.input(echo)==1):
        end=time.time()
    time_taken=end-start
    distance=(timetaken*34300)/2
    return distance
lcd.message("Water Level:")
#consider 1000ltr water tank height is 60cm 
while(1):
    distance=distance_func()
    percentage=distance*100/60
    lcd.setCursur(0,12)
    lcd.message(perentage,"%")
    lcd.setCursur(1,0)
    if(percentage<50):
        gpio.output(buzzer,False)
        lcd.message("Itz Not Enough")
    elif(percentage<75):
        gpio.output(buzzer,False)
        lcd.message("wait a minute")
    elif(percentage<85):
        gpio.output(buzzer,False)
        lcd.message("Itz Enough")
    elif(percentage>95):
        gpio.output(buzzer,True)
        lcd.message("Alert")
    time.delay(5)    
