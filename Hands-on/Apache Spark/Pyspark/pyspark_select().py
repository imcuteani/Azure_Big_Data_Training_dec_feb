import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparklabs').getOrCreate()

data = [("James","Smith","US","CA"),
... ("Michael","Rose","US","NY"),
... ("Robert","William","UK","London"),
... ("Maria","Brown","US","FL")]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data=data,schema=columns)
df.show(truncate=False)
+---------+--------+-------+------+
|firstname|lastname|country|state |
+---------+--------+-------+------+
|James    |Smith   |US     |CA    |
|Michael  |Rose    |US     |NY    |
|Robert   |William |UK     |London|
|Maria    |Brown   |US     |FL    |
+---------+--------+-------+------+

df.select("firstname","lastname").show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

df.select(df.firstname,df.lastname).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

df.select(df["firstname"],df["lastname"]).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

