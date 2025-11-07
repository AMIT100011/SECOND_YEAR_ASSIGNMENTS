import random

def sensor_data_stream():
  while True:
    value = random.uniform(20,30)
    value = int(value * 100 + 0.5) / 100.0
    #value = round(value)
    yield value

s = sensor_data_stream()
for i in range(10):
    print("Reading", i + 1, ":", next(s), "°C")