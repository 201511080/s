#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pyspark

def doIt():
    d = [{'name': 'Alice', 'age': 1}]
    print spark.createDataFrame(d).collect()

if __name__ == "__main__":
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .getOrCreate()
    doIt()
    spark.stop()
