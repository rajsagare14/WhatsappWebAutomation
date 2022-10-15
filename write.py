##Schedule A message Here
import pandas as pd
import numpy as np

df = pd.DataFrame(
	{
		'Name':['Raj','Aarya','Snowbo','PK'],
		'Message':['you are awesome','Forgive me','Are you okay?','apply for this'],
		'hh':[0,6,23,10],
		'mm':[0,30,0,26],
		'date':['14:04:2000','05:04:2000','02:02:2000','10:11:1999']
	}
)
print(df)
df.to_excel('test.xlsx',index=False)
df1 = pd.DataFrame(
	{
		'Name':['Raj1','Aarya2','Snowbo0.5','PK0',np.nan],
		'Message':['you are awesome','Forgive me','Are you okay?','apply for this',np.nan],
		'hh':[0,6,23,10,7],
		'mm':[0,30,0,26,30],
		'date':['14:04:2000','05:04:2000','02:02:2000','10:11:1999','25:01:2022']
	}
)
print(df1)
# df1.to_excel('test.xlsx',sheet_name='Sheet1',index=False)
with pd.ExcelWriter('test.xlsx') as writer:
	df1.to_excel(writer,index=False)
df3 = pd.read_excel('test.xlsx','Sheet1',)
print('df3\n',df3)
df3 = dict(df3)
print('Dict df3\n',df3)
upd = {
	'Name':['Rajwardhan','Aarya2','Snowbo0.5','PK0',np.nan],
	'Message':['you are awesome','Forgive me','Are you okay?','apply for this',np.nan],
	'hh':[10,6,23,10,7],
	'mm':[10,30,0,26,30],
	'date':['14:04:2000','05:04:2000','02:02:2000','10:11:1999','25:01:2022']
}
df3.update(upd)
print('updated df3 in dict format\n',df3)
# with pd.ExcelWriter('test.xlsx',mode='a') as writer:
# 	df3.to_excel(writer,index=False)
df3 = pd.DataFrame(df3)
print('updated df3 in dataframe format format\n',df3)
df3.to_excel('test.xlsx',sheet_name='Sheet1',index_label='S.ID')
