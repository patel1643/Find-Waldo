#Name: Parth Patel 
#StudentNumber: 500893723

waldo = makePicture(r"F:\University\Computer Science 1 CPS 109\Assignments\Assignment 2\waldo.jpg")
scene = makePicture(r"F:\University\Computer Science 1 CPS 109\Assignments\Assignment 2\scene.jpg")
tinywaldo = makePicture(r"F:\University\Computer Science 1 CPS 109\Assignments\Assignment 2\tinywaldo.jpg")
tinyscene = makePicture(r"F:\University\Computer Science 1 CPS 109\Assignments\Assignment 2\tinyscene.jpg")

def compareOne(template, srcImg,x1,y1):#This function compares the first x1,y1 pixels with the main scene and returns the array and returns the sum of them
  srcL = 0
  templateL = 0
  SAD = 0
  for x in range(getWidth(template)):
    for y in range(getHeight(template)):
      templatePx = getPixel(template, x, y)
      searchPx = getPixel(srcImg, x+x1,y+y1)
      srcL = srcL + getRed(searchPx)
      templateL = templateL + getRed(templatePx)
      SAD = SAD + abs(srcL - templateL) #This would return the absolute sum of the differences on the given pixels 
  return SAD

def compareAll(template, srcImg):#This function compares all the groups of pixels with the background pic and returns a big array of Sum of Absolute differences of all the pixels
  srcH = getHeight(srcImg)
  srcW = getWidth(srcImg)
  tempH = getHeight(template)
  tempW = getWidth(template)
  matrix = [[500000 for i in range(srcW)] for j in range(srcH)]
  for x in range(srcW - tempW):
    for y in range(srcH - tempH):
      matchScore = compareOne(template, srcImg, x,y)
      matrix[x][y] = matchScore
  return matrix

def find2Dmin(matrix): #This function would fins the smallest/least value in the matrix and will assign it to x and y respectively
  minRow = 0 
  minCol = 0
  minValue = 500000
  for x in range(len(matrix)):
    for y in range(len(matrix[0])):
      if minValue > matrix[x][y]:
        minValue = matrix[x][y]
        minRow = x
        minCol = y
  return(minRow, minCol)
  
def displayMatch(srcImg, x1,y1,w1,h1,color): #This function will add a rectangle to the main picture taking x and y from the previous function as the starting point
  addRect(srcImg, x1,y1,w1,h1,red)
  explore(srcImg)
  
def grayscale(picture): #this is the normal greyscale function which would return the grey picture
  for x in range(getWidth(picture)):
    for y in range(getHeight(picture)):
      p = getPixel(picture, x, y)
      avg = (getRed(p) + getGreen(p) + getBlue(p))/3
      setColor(p, makeColor(avg,avg,avg))
  
def findWaldo(targetJPG, searchJPG): #This function would combine all the above functions and would return the main scene with a rectangle where the rectangle is the image we tried to find in the big scene by using all the functions above 
  w = getWidth(targetJPG)
  h = getHeight(targetJPG)
  grayscale(targetJPG)
  grayscale(searchJPG)
  matrix = compareAll(targetJPG, searchJPG)
  row,col = find2Dmin(matrix)
  displayMatch(searchJPG, row,col,w,h,red)
  writePictureTo(searchJPG, "F:\University\Computer Science 1 CPS 109\Assignments\Assignment 2\FinalImage.jpg")
  