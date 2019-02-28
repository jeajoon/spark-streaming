# spark-streaming
模拟流数据，实现实时统计功能

Spark Streaming 是Spark核心API的一个扩展，可以实现实时流数据的处理。这里基于spark streaming实现实时统计功能
数据：Kaggle_Chicago Crime https://www.kaggle.com/chicago/chicago-crime
功能：实时犯罪率变化；不同犯罪类型频率分布；犯罪地点的分布以及动态图展示。


1、数据处理
chunk.py：数据分块
2、模拟流数据
writeHDFS.sh：将分块后的文件上传至HDFS，然后移动到目标目录
3、spark streaming程序
收集流数据，进行统计;
做图展示结果

