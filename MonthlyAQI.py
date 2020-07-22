import pandas as pd
import numpy as np
from pyecharts import Line

df = pd.read_csv('air_tianjin_2020.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])
dom = df[['Date', 'AQI']]
list1 = []
for j in dom['Date']:
    time = j.split('-')[1]
    list1.append(time)
df['month'] = list1

month_message = df.groupby(['month'])
month_com = month_message['AQI'].agg(['mean'])
month_com.reset_index(inplace=True)
month_com_last = month_com.sort_index()

attr = ["{}".format(str(i) + 'month') for i in range(1, 7)]
v1 = np.array(month_com_last['mean'])
v1 = ["{}".format(int(i)) for i in v1]
print(len(attr))
print(len(v1))

line = Line("2020 Monthly AQI", title_pos='center', title_top='18', width=800, height=400)
line.add("", attr, v1, mark_point=["max", "min"])
line.render("2020 Monthly AQI.html")