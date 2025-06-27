from . import dht
import time
import datetime

# initialize GPIO
PIN2 = 16

# read data using pin
instance = dht.DHT(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: {0:0.1f} C".format(result.temperature))
        print("Humidity: {0:0.1f} %%".format(result.humidity))

    time.sleep(1)
