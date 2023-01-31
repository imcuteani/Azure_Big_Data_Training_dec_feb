from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparkdfdemo').getOrCreate()
# Create empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)

#alternatively create empty RDD in PySpark using parallelize() from SparkContext 
rdd2 = spark.sparkContext.parallelize([])
print(rdd2)