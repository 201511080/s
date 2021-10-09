#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pyspark
def doIt():
    print "---------RESULT-----------"
    print "------mongodb write-------"
    myRdd = spark.sparkContext.parallelize([
        ("js", 150),
        ("Gandalf", 1000),
        ("Thorin", 195),
        ("Balin", 178),
        ("Kili", 77),
        ("Dwalin", 169),
        ("Oin", 167),
        ("Gloin", 158),
        ("Fili", 82),
        ("Bombur", None)
    ])
    myDf = spark.createDataFrame(myRdd, ["name", "age"])
    print myDf
    myDf.write.format("com.mongodb.spark.sql.DefaultSource").mode("overwrite").save()
    print "---------read-----------"
    df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
    print df.printSchema()
    df.registerTempTable("myTable")
    myTab = spark.sql("SELECT name, age FROM myTable WHERE age >= 100")
    myTab.show()

if __name__ == "__main__":
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/myDB.ds_spark_df_mongo") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/myDB.ds_spark_df_mongo") \
        .getOrCreate()
    doIt()
    spark.stop()
