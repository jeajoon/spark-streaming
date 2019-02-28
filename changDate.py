import pandas as pd

#将日期转换为“mm/yyyy”的格式
data = pd.read_csv('/Users/macbookpro/Documents/commit/Egroupware/Haditest.csv',encoding='utf-8')
data[u'DATE'] = data[u'DATE'].astype(str)
data[u'DATE'] = data[u'DATE'].apply(lambda x :x[0:10])
data.to_csv('/Users/macbookpro/Documents/commit/Egroupware/Haditestnew.csv',index=False, encoding='utf-8')

