import pandas as pd
import numpy as np

# 文件的名字
FILENAME1 = "air_tianjin_2020.csv"
# 禁用科学计数法
pd.set_option('float_format', lambda x: '%.3f' % x)
np.set_printoptions(threshold=np.inf)
# 读取数据
data = pd.read_csv(FILENAME1)
rows, clos = data.shape
# DataFrame转化为array
DataArray = data.values
Y=[]
y = DataArray[:, 1]
for i in y:
    if i=="良":
        Y.append(0)
    if i=="轻度污染":
        Y.append(1)
    if i=="优":
        Y.append(2)
    if i=="严重污染":
        Y.append(3)
    if i=="重度污染":
        Y.append(4)
print(Y)
print(len(y))
X = DataArray[:, 2:5]
print(X[1])

for i in range(len(Y)):
   f=open("data.txt","a+")
   for j in range(3):
        f.write(str(X[i][j])+",")
   f.write(str(Y[i])+"\n")
print("data.txt is done!")