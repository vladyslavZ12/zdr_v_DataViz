import matplotlib.pyplot as plt

hours = [4,8,2]

activities = ['sleep', 'work', 'play']
colors = ['gold', 'silver', 'blue']

plt.pie(hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')

plt.show()