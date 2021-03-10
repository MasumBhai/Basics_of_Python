# topics covered pandas,numpy arrays,matplotlib,mplfinance,csv to plot graph
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

file = 'AMZN.csv'
data = pd.read_csv(file)

# print(data.info())
# print(data.columns)
# as our date is object in csv file,i need to modify it as dateTime
data.Date = pd.to_datetime(data.Date)
# print(data.info())
# now i want to make index column as Date column not 0,1,2,3
data = data.set_index('Date')
# print(data)

mpf.plot(data, title="Big Bull Masum's Income (just data represantation)")
mpf.plot(data, volume=True, type='line', title="Big Bull Masum's Income (line chart)")
# from 2020 march to 2020 may candlestick chart
mpf.plot(data['2020-03':'2020-05'], type='candle', volume=True, title="Big Bull Masum's Income (candlestick chart)")

info1 = """The velocity of 2 moving objects according to same time
    TIME  : 0    5    10    15     20      25     30
    Obj1  : 10   15   20    20     30      15     00
    Obj2  : 10   12   15    12     20      10     00
"""
print(info1)

x = [0, 5, 10, 15, 20, 25, 30]
x1 = [10, 15, 20, 20, 30, 15, 0]
y1 = [10, 12, 15, 12, 20, 10, 0]

plt.plot(x, x1, linewidth=2, color="Green", label="Line-1", marker="o")
plt.plot(x, y1, label="Line-2", marker="D")
plt.title("Velocity vs Time Graph")
plt.xlabel("Time (second)-->")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.show()

info2 = """Draw a graph where y=2x+1 & y=2x^2 + 2 """
print(info2)
xx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xx1 = []
xx2 = []


def yy1(x):
    val = 1 + 2 * x;
    return val


def yy2(x):
    val = 2 + 2 * x * x;
    return val;


for i in xx:
    xx1.append(yy1(i))
    xx2.append(yy2(i))

# print(xx1)
# print(xx2)

plt.plot(xx, xx1, marker="o", label="y= 2*x + 1")
plt.plot(xx, xx2, marker="o", label="y = 2x^2 + 2")
plt.title("Graph Plotting of some funtions")
plt.xlabel("value of x")
plt.ylabel("value of y")
plt.legend()
plt.show()
