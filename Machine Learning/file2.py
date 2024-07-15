import matplotlib.pyplot as plt
 
# x axis values
x = ["Mitte", "Ecke", "Rand"]
# corresponding y axis values
y = [55504, 59704, 63904]

x2 = ["Mitte", "Ecke", "Rand"]
# corresponding y axis values
y2 = [6138, 4949, 6061]
# plotting the points 
plt.plot(x, y)
plt.plot(x2, y2)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()