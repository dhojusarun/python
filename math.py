#matplotlib tutorial

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y)
plt.show()

#add title 
plt.title("Line Graph")

#add label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#bar graph
# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# plt.bar(x,y)
# plt.show()