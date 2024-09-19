# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.plot(x,y)
# plt.show()

#different (no same dimensions so give error)
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10,12]
# plt.plot(x,y)
# plt.show()

#with title of graph
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.title("Graph ")
# plt.plot(x,y)
# plt.show()

#to give name on x and y axis 
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.title("Graph for students ")
# plt.plot(x,y)
# plt.xlabel("student performance")
# plt.ylabel("student semester")
# plt.show()


# """Assignment"""
# import matplotlib.pyplot as plt
# percentage=[88.2,74.8,78]
# year=[2018,2020,2023]
# plt.title("Mine growth graph")
# plt.xlabel("percentage")
# plt.ylabel("year")
# plt.plot(percentage,year)
# plt.show()
"""Another for pie graph"""
import matplotlib.pyplot as plt
percentage=[88.2,74.8,78]
year=[2018,2020,2023]
plt.pie(percentage)
plt.title("Mine growth graph")
plt.xlabel("percentage")
plt.ylabel("year")
plt.plot()
plt.show()
