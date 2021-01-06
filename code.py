import imageio
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook

pic1 = []
n = int(input("How many images do you have? ")) # input the number of images
print("\n") # create a new line

print('Where did you take these pictures? ')
location = str(input()) # input of the location the photos were taken

xlsxformat = location + '.xlsx' # name the excel file

shutter = [
'1/400','1/3200','1/2500', '1/2000', '1/1600', '1/1250', 
'1/1000', '1/800', '1/640', '1/500', '1/400', '1/320', 
'1/250', '1/200', '1/160', '1/125', '1/100', '1/80', 
'1/60', '1/50', '1/40', '1/30', '1/25', '1/20', 
'1/15', '1/13', '1/10', '1/10', '1/6', '1/5', 
'1/4', '0.3', '0.4', '0.5', '0.6', '0.8', 
'1', '1.3', '1.6', '2', '2.5', '3.2', 
'4', '5', '6', '8', '10', '13', 
'15', '20', '25', '30' ] # shutter speeds
row = [
'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 
'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 
'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 
'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 
'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 
'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 
'A49', 'A50', 'A51', 'A52', 'A53', 'A54' ] # Excel sheet row for each shutter speed

book = Workbook()
sheet = book.active

sheet.column_dimensions['A'].width = 25

x = 0
for i in range(0, n): # loop the question for the number of images
    print("Enter the image with this shutter speed: ", shutter[i], ":")
    item = str(input())
    pic1.append(item)

for i in pic1: # change the images into grey scaled images
  pic1 = imageio.imread(i)
  gray = lambda rgb : np.dot(rgb[... , :3] , [0.21 , 0.72, 0.07]) 
  gray = gray(pic1)

  plt.figure( figsize = (1,1))
  plt.imshow(gray, cmap = plt.get_cmap(name = 'gray')) 
  plt.show() # output the images

  mean = format(gray.mean()) # get the average pexil value of the gray scaled images
  print(mean) # output the average pexil value
  sheet[row[x]] = mean #assign the row to the mean throught the rows
  x = x + 1 # add 1 to x so it could go to the next row
book.save(xlsxformat) # save the file
