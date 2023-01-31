from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparkdfdemo').getOrCreate()
# Create empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)

#alternatively create empty RDD in PySpark using parallelize() from SparkContext 
rdd2 = spark.sparkContext.parallelize([])
print(rdd2)

# Create an empty Dataframe with schema 
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([
    StructField('firstname', StringType(), True),
    StructField('middlename', StringType(), True),
    StructField('lastname', StringType(), True)])


# Create an empty Dataframe from an empty RDD 

df = spark.createDataFrame(emptyRDD, schema)
df.printSchema() 

