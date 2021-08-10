import matplotlib.pyplot as plt
import re
import numpy as np


def get_sentiment_trend(data):
    trend_star = {}
    trend_num = {}
    for d in data:
        date = int(re.sub("-", "", d['date']))
        date = int(date / 100)
        if date not in trend_star.keys():
            trend_star[date] = int(d['star'])
            trend_num[date] = 1
        else:
            trend_star[date] += int(d['star'])
            trend_num[date] += 1
    row, column = [], []
    for date in sorted(trend_star):
        row.append(str(date))
        column.append(trend_star[date] / trend_num[date])
    row = np.array(row)
    print(row[0])
    print(row[-1])
    print(len(row))
    column = np.array(column)
    fig, ax = plt.subplots()
    ax.plot(row, column)
    plt.show()
