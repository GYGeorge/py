import pandas as pd
data = pd.read_excel('C:/Users/El/Desktop/desktopFile/CS.xlsx')#读数据
value = data.values.tolist()#数据转为列表
res = []
for i in range(len(value)):
    res.append(value[i][2])
res = set(res)
df = pd.DataFrame(res,columns=['College Names'])#转换成pandas的格式
df.to_excel("C:/Users/El/Desktop/desktopFile/college.xlsx")#往excel写数据



