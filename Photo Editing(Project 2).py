#Photo Editing (Project 02)
#imports
import numpy as np
from skimage import data, io
import matplotlib.pyplot as plt
import matplotlib
from skimage.transform import rescale, resize

#numpy random integer function used to change the picture position everytime
#Warhol Image boradcast into (1200,1200) big image
#first of the four images
def first_image(pic):
    new_pic = np.array(pic)
    c = abs(len(new_pic[0,:]))    #calling in rows and columns
    r = abs(len(new_pic[:,0]))    #callin in rown adn columns
    for i in range(r):
        for j in range(c):
            new_pic[i,c-j-1] = new_pic[i,j]  #making the picture into the two sides of a mirror image
    
    for i in range(r):
        for j in range(c):
            r = new_pic[i,j,0]
            g = new_pic[i,j,1]
            b = new_pic[i,j,2]
            gray = r//3+g//3+b//3
            new_pic[i,j] = np.uint8([gray,gray,gray]) #creating an gray image
   
    new_pic=(255-new_pic)
    return new_pic

#second image
def second_image(pic):
    new_pic = np.array(pic)
    new_pic[0:300,0:300,0:2]=np.random.randint(0,255)//np.random.randint(1,5) # quarter of the image being designed with a unique color
    new_pic[300:600,0:300,0:2]=np.random.randint(0,255)//np.random.randint(1,5) # quarter of the image being designed with a unique color
    new_pic[0:300,300:600,1:3]=np.random.randint(0,255)//np.random.randint(1,5) # quarter of the image being designed with a unique color
    new_pic[300:600,300:600,1:3]=np.random.randint(0,255)//np.random.randint(1,5) # quarter of the image being designed with a unique color
    return new_pic

#third image
def third_image(pic):
    new_pic = np.array(pic)
    c = abs(len(new_pic[0,:]))    #calling in rows and columns
    r = abs(len(new_pic[:,0]))    #calling in rows and columns
    for i in range(r):
        for j in range(c):
            if np.random.randint(0,2)==1:
                 new_pic[r-i-1,c-j-1]=pic[i,j] #turning parts of the picture upside down based on the if statement above
            else:
                pass
    if np.random.randint(0,2)==1:
        for i in range(r):           #creating a negative filter version of the picture
            for j in range(c):
                r = new_pic[i,j,0]
                g = new_pic[i,j,1]
                b = new_pic[i,j,2]
                r=255-np.random.randint(1,3)*r
                g=255-np.random.randint(1,3)*g
                b=255-np.random.randint(1,3)*b
                new_pic[i,j] = [r,g,b]
    else:
        pass          
      
    return new_pic

#fourth image

def fourth_image(pic):
    new_pic = np.array(pic)
    c = abs(len(new_pic[0,:]))       #calling in rows and columns
    r = abs(len(new_pic[:,0]))       #calling in rows and columns
    if np.random.randint(0,2)==1:    #flip or not to flip that is the question
        for i in range(r):
            for j in range(c):
                new_pic[r-i-1,c-j-1]=pic[i,j]
    else:
        pass
                
    for i in range(r):
        for j in range(c):
            r = new_pic[i,j,0]
            g = new_pic[i,j,1]
            b = new_pic[i,j,2]
            gray = r/3+g/3+b/3
            if gray>50:
                val = np.uint8([np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,120)])
            elif gray>100:
                val = np.uint8([np.random.randint(0,255),np.random.randint(0,255),np.random.randint(50,200)])                
            elif gray>160:
                val = np.uint8([np.random.randint(0,100),np.random.randint(0,255),np.random.randint(0,200)])   
            elif gray>225:
                val = np.uint8([np.random.randint(0,255),np.random.randint(0,255),np.random.randint(50,200)])     
            else:
                val = np.uint8([30,10,80])
            new_pic[i,j] = val
            
    return new_pic
            
#combined image
my_image=io.imread('Wabash Photo.jpeg')

#calling functions
first_image=first_image(my_image)
second_image=second_image(my_image)
third_image=third_image(my_image)
fourth_image=fourth_image(my_image)

#creating big image
big_image=np.ndarray((1200,1200,3),dtype=np.uint8)
big_image[0:600,0:600]=first_image
big_image[0:600,600:1200]=second_image
big_image[600:1200,0:600]=third_image
big_image[600:1200,600:1200]=fourth_image

#plotting image
plt.imshow(big_image)

#Original Image shown for comparison
plt.imshow(my_image)
"""
Homework Documentation Introduction: I created a Warhol Image from an initial image of myself that I took last year. Each image was edited to make it look cool or weird depending on your tastes. I used four different functions to edit the four images before combining them into one. The use of the NumPy random function adds a sense of mystery to every running of the image.

First Image: The image went through two separate edits. Firstly, the image was edited to make it look like two mirror images were combining into one. This was followed by making the image grayscale. Both of them combined to make the image quite frightening, almost like a ghost.

Second Image: The Second Image was separated into four quadrants; each quadrant was given a unique color value and divided by a number to make it either a light or dark version of that color. However, the more interesting aspect is that all the aforementioned editing was done using random integers, which means the image changes color and darkness every time it is being run.

Third Image: In this image, the negative filter code was combined with turning the image upside down. However, for every pixel, there is a truth value that decided to either to turn that pixel upside down or not, which adds to the craziness. Finally, almost all the functions have random truth value-added so the picture could turn out between completely normal to something truly weird.

Fourth Image: It is also an image that goes upside down. Furthermore, it changes the underlying color values of each pixel based on the gray value of each pixel.

The four images are combined above as shown.
"""
