# HDFS命令
HDFS="hadoop fs"

# Streaming程序监听的目录，注意跟后面Streaming程序的配置要保持一致
streaming_dir="/test"

# 清空旧数据
#$HDFS -rm "${streaming_dir}"'/*' > /dev/null 2>&1

#文件分块
#python3 chunks.py

#move至test文件夹下
i=0
doc='/Users/macbookpro/Documents/crime/crime'
while [ $i -le 100 ]
do
    docs=$doc${i}'.csv'
    echo $docs
    $HDFS -put ${docs} ${streaming_dir}/tmp
    sleep 1
    $HDFS -mv ${streaming_dir}/tmp/crime${i}.csv ${streaming_dir}
    i=$(( i+1 ))
    sleep 1
done
