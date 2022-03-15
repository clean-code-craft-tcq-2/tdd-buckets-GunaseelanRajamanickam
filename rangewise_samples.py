def infers_readings(readings):
  validReadings = isSequenceOk(readings)
  if validReadings == True:
    readings.sort()
    sortedReadings = []
    sortedReadings.append(sortReadings(readings))
    groups = detectRange(readings)
    for list in groups:
      formattedString = convertCSVFormat(list)
      printOnConsole(formattedString)
    return formattedString
  return False

def isSequenceOk(readings):
  if len(readings) <= 0:
    return False
  return True

def sortReadings(readings):
  return readings.sort()

def detectRange(readings):
  diff = [j-i for i, j in zip(readings[:-1], readings[1:])]
  diff.insert(0, 0)

  ind = [i for i,v in enumerate(diff) if v >= 2]
  ind.insert(0, 0)

  groups = [readings[i:j] for i,j in zip(ind, ind[1:]+[None])]
  return groups

def convertCSVFormat(list):
  return f'{list[0]}-{list[-1]}, {len(list)}'

def printOnConsole(string):
  print(string)