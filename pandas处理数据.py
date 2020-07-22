import pandas as pd
data = pd.read_excel('C:/Users/El/Desktop/desktopFile/CS.xlsx')#读数据
value = data.values.tolist()#数据转为列表
res = []
for i in range(len(value)):
    res.append(value[i][:3])
school = []
for i in res:
    if i not in school:
        school.append(i)
# res = set(res)
df = pd.DataFrame(school)#转换成pandas的格式
df.to_excel("C:/Users/El/Desktop/desktopFile/college.xlsx")#往excel写数据



