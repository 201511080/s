import os
import pyspark

def doIt():
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .getOrCreate()

    bigdataWikiRdd=spark.sparkContext\
        .textFile(os.path.join("data","ds_bigdata_wiki.txt"))


    wordCount = bigdataWikiRdd\
        .flatMap(lambda x: x.split())\
        .map(lambda x: (x, 1))\
        .reduceByKey(lambda x, y: x+y)\
        .map(lambda x:(x[1],x[0]))\
        .sortByKey(False)\
        .take(15)
    
    for i in wordCount:
        print (i[0],i[1])

if __name__ == "__main__":
    os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"
    os.environ["PYSPARK_DRIVER_PYTHON"]="/usr/bin/python3"
    doIt()
    spark.stop()
