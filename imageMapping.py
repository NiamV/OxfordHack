import math

# Returns the n-tuple containing the image ids (ints)

def imageId(n, imageCount, sampleSize, index):
  num = n % (math.factorial(imageCount + 1 - index) / math.factorial(imageCount - sampleSize) )
  den = math.factorial(8 - index) / math.factorial(8 - sampleSize)
  return math.ceil(num / den)

def images(n, imageCount, sampleSize):
  numbers = [i for i in range(1, imageCount+1)]
  indexes = []
  for i in range(1,sampleSize + 1):
    index = imageId(n, imageCount, sampleSize, i)
    location = numbers[index-1]
    indexes.append(location)
    numbers.remove(location)
  return indexes

