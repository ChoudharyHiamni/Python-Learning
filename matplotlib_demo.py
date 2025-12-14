import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# print(matplotlib.__version__)
 
           #BASIC LINE PLOT
# x=[1,2,3,4]
# y=[10,15,20,25]
# # plt.plot(x,y)   
# # plt.show()
# plt.plot(x,y,color="Gold",marker='o',linestyle='dashed',linewidth = '20.5',markeredgecolor='blue',markersize=20,mfc='red')
# plt.title("Sales growth")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()


# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()


# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()




                   #MATPLOT GRID

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()




# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title('Heading',fontdict={'fontsize':40})
# plt.plot(x,y)
# plt.show()
# plt.savefig('firstgraph',dpi=200)


                                               #HISTOGRAM:USED FOR DISTRIBUTION OF DATA
# data = [10, 20, 20, 30, 40, 40, 40]


# plt.hist(data, bins=5)
# plt.title("Frequency Distribution")
# plt.show()


                                 #BAR CHART:USED FOR CATEGORY COMPARISON
# x=np.array([1,2,3,4,5,6])
# y=np.array([5,10,15,20,25,30])
# plt.bar(x,y,color="red",width=0.9)
# plt.show()

                            #SCATTER PLOT:USED TO SHOW RELATIONSHIP BETWEEN TWO VARIABLE
# x=np.array([1,2,3,4])
# y=np.array([5,6,7,8])
# plt.scatter(x,y,color="brown")
# plt.show()



# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()



                             #PIE CHART:FOR PERCENTAGE REPRESENTATION
# y=np.array([10,20,30,40])
# mylabels=["Apple","Mango","Orange","Grapes"]
# plt.pie(y,labels=mylabels)
# plt.show()
 
        #EXPLODE

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode,shadow=True)
plt.legend(title="Four Fruite:")
plt.show() 







# Matplotlib is used for data visualization in Python

# Line plot shows trends

# Bar chart compares categories

# Histogram shows distribution

# Scatter plot shows relationships