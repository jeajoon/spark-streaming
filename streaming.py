from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
import matplotlib.pyplot as plt

conf = SparkConf()
conf.setAppName('TestDStream')
conf.setMaster('local[1]')
sc = SparkContext(conf = conf)
ssc = StreamingContext(sc, 2)
lines = ssc.textFileStream('hdfs://localhost:9000//test')

plt.ion()
x=[]
y=[]
def func(record):
    plt.figure(num=1,dpi=128, figsize=(10,5))
    for i in record.collect():
        x.append(i[0])
        y.append(int(i[1]))
        plt.xlabel("The crime year")
        plt.ylabel("The amount of crime")
        plt.title("Chicago Crime Record")
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.plot(x, y)
        plt.show()
        plt.pause(0.001)


def func2(record):
    plt.figure(num=1, figsize=(12, 12))
    plt.clf()
    record.collect()
    plt.xlabel("The Primary Type ")
    plt.ylabel("The amount of crime")
    plt.title("Chicago Crime Record")
    for i in record.collect():
        x.append(i[0])
        y.append(int(i[1]))
        plt.text(i[0], int(i[1]), '%d' % int(i[1]), ha='center', va='bottom')
        plt.bar(x, y, facecolor="red", edgecolor='white')
        plt.pause(0.1)

def func3(record):
    plt.figure(num=1, figsize=(20, 10))
    list=record.collect()
    for i in list:
        x.append(i[0])
        y.append(int(i[1]))
        plt.clf()
        plt.pie(y, labels=x,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
        plt.pause(0.001)


newRows = lines.map(lambda r: r.split(','))
newRows.pprint()


#计算时间变化
dates = newRows.map(lambda r: (r[4], 1))
dates_crime = dates.reduceByKey(lambda x, y: x+y)
dates_crime.pprint() # 输出时间变化

#计算每种犯罪的人数
types = newRows.map(lambda r: (r[7], 1))
types_crime = types.reduceByKey(lambda x, y: x+y)
types_crime.pprint() # 输出每种犯罪的人数

#计算犯罪地点的频率
locations = newRows.map(lambda r: (r[9], 1))
locations_crime = locations.reduceByKey(lambda x, y: x+y)
locations_crime.pprint() # 输出犯罪地点的频率


ssc.start()
ssc.awaitTermination()