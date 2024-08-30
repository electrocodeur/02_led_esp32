from machine import Pin
import time

pin_led = Pin(15, mode=Pin.OUT)

while True:
    pin_led.on()
    time.sleep(2)
    pin_led.value(0)
    time.sleep_ms(1500)
    
    
"""
time.sleep(duree_en_secondes)
time.sleep_ms(duree_en_millisecondes)
time.sleep_us(duree_en_microsecondes)

Pin.on() et Pin.off()
Pin.value(valeur)
"""
