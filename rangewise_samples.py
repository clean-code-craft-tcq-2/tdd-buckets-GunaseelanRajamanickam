def infers_readings(readings):
  readings.sort()
  return f'{readings[0]}-{readings[-1]},{len(readings)}'
