import pandas as pd
from pyecharts import Line

df = pd.read_csv('/Users/RachelZhang/Desktop/air_tianjin_2020.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])
attr = df['Date']
v1 = df['AQI']
line = Line("2020_AQI_trend", title_pos='center', title_top='18', width=800, height=400)
# line = Line("2020_AQI_trend")
line.add("",attr, v1, mark_line=['average'], is_fill=True, area_color="#000", area_opacity=0.3, mark_point=["max", "min"], mark_point_symbol="circle", mark_point_symbolsize=25)
# line.add_xaxis("",attr,v1,markline_opts=['average'], is_stack = True, color="#000",  markpoint_opts=["max", "min"],is_symbol_show=True, symbol="circle", symbol_size = 25)
line.render("2020_AQI_trend.html")