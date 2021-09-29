#Random Walk(Project 1)
#Import requirements
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.pylab as pl
import statistics as stats
import math
#Creating the Intial Array of random points

point=np.array([0,0])                                # Intial origin point
step_plot_points=[point]
total_plot_no=np.random.randint(50,100)             # Random total number
for k in range(total_plot_no):
    step= 2*np.random.rand(2)-1                     # Random step size  
    point=point+step                                # Adding step size to cordinates
    step_plot_points.append(point)                  # Cordinates List created
    
array_step=np.array(step_plot_points)                 #list plot point is turned into an array

#Calculating origin from distance for each point
def origin_distance():
    length_list=[]
    for k in range(total_plot_no):
        x=math.sqrt(array_step[k][0]**2+array_step[k][1]**2) #math cordinate distance equation
        length_list.append(x)
    return length_list


#Calculating the distance between each step
def step_distance():
    step_list=[]
    for k in range(1,total_plot_no+1):
        x=math.sqrt((array_step[k-1][0]-array_step[k][0])**2+(array_step[k-1][1]-array_step[k][1])**2) #math cordinate distance equation
        step_list.append(x)
    return step_list
    

#Creating the plot point for the first graph
x=[] #list of x cordinates
y=[] #list of y cordinates
for k in range(total_plot_no):
    x.append(array_step[k,0])
    y.append(array_step[k,1])
#Creating Plot points for the second graph and third graph
o_d=origin_distance() #list of all origin distance
s_d=step_distance()   #list of all step distance
step_number=[]        #list of step numbers
for k in range(total_plot_no):
    step_number.append(k)   
s_n=step_number

#Creating the Subplots
#Create gridspace for the plots
gs = gridspec.GridSpec(22,20)
fig=pl.figure()
fig.suptitle('Random Walk',fontsize=16)
#Random Walk Project
#The random walk cordinate subplot
ax = pl.subplot(gs[2:12,0:8]) 
pl.plot(x,y)   #Initial plotting lines(but scatter looks better)
plt.title('Step Cordinates')
plt.grid(True)
#plt.scatter(x,y,s=50,c='red')
plt.xlabel("Random x Cordinate")
plt.ylabel("Random y cordinate")

#Distance from origin subplot
ax = pl.subplot(gs[2:12,12:20]) 
pl.plot(s_n,o_d,c="green")
plt.title('Distance from Origin for Each Step')
plt.grid(True)
plt.xlabel("Steps")
plt.ylabel("Distance from Origin")

#Distance between each step histogram subplot
ax = pl.subplot(gs[17:,:]) 
pl.hist(s_d,bins=7)
plt.title('Distace between Each Step')
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.show()
"""
Citation
gridpspace source: https://stackoverflow.com/questions/37360568/python-organisation-of-3-subplots-with-matplotlib/37363441
"""