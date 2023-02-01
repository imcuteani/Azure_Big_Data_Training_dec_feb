#PySpark we have StructType which defines the structure of the dataframe. 

# pyspark.sql.types module from where we can import StructType class to define the structure of the dataframe 

# StructField defines the metadata of the dataframe column. 

# pyspark provides pyspark.sql.types module from where we can import StructField class to define the columns which include the column name(string), column type(datatype), nullable column(boolean), and metadata(metadata).
# 
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder.master("local[1]").appName('cgpysparklabs').getOrCreate()
data = [("James","A","Smith", "36676","M", 4000),
... ("Michael","S","Rose","45523","M", 6000),
... ("Robert","K","Williams","42133","M",7000),
... ("Jen","A", "Brown","34423","F",4000)]
schema = StructType([ \
... StructField("firstname",StringType(),True), \
... StructField("middlename",StringType(),True), \
... StructField("lastname",StringType(),True), \
... StructField("id",StringType(),True), \
... StructField("gender",StringType(),True), \
... StructField("salary",IntegerType(),True)])
df = spark.createDataFrame(data=data, schema=schema)
df.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- id: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: integer (nullable = true)

df.show(truncate=False)
 