import math

def images(n, imageCount):
  numbers = [i for i in range(1,imageCount+1)]
  img1 = math.ceil(n / ((imageCount-1)*(imageCount-2)))
  numbers.remove(img1)

  img2 = numbers[int(math.ceil((n % ((imageCount-1)*(imageCount-2))) / (imageCount-2))-1)]
  numbers.remove(img2)

  img3 = numbers[int(math.ceil( (n % (imageCount-2)))-1)]

  return img1, img2, img3

