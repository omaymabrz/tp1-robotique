from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
    print("hello nik ben omayma")
    print("ok ok")
    print("ok ojhhyugyuk")