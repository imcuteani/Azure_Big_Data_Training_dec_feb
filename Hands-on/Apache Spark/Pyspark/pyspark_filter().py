from pyspark.sql.types import StructType,StructField
from pyspark.sql.types import StringType,IntegerType,ArrayType
data = [(("James","","Smith"),["Java","Scala","C++"],"OH","M"),
... (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
... (("Maria","A","Jones"),["C++","VB","Python"],"NY","F")]
schema = StructType([
... StructField('name', StructType([
... StructField('firstname',StringType(),True),
... StructFiekd('middlename',StringType(),True),
... StructField('lastname',StringType(),True)])),
...


schema = StructType([
... StructField('name', StructType([
... StructField('firstname', StringType(), True),
... StructField('middlename',StringType(),True),
... StructField('lastname', StringType(), True)])),
... StructField('languages', ArrayType(StringType()), True),
... StructField('state', StringType(), True),
... StructField('gender', StringType(), True)])
df = spark.createDataFrame(data = data, schema = schema)
df.printSchema()
root
 |-- name: struct (nullable = true)
 |    |-- firstname: string (nullable = true)
 |    |-- middlename: string (nullable = true)
 |    |-- lastname: string (nullable = true)
 |-- languages: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- state: string (nullable = true)
 |-- gender: string (nullable = true)

df.show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{James, , Smith} |[Java, Scala, C++]|OH   |M     |
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+

df.filter(df.state == "NY").show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+

df.filter(df.state != "NY").show(truncate=False)
+----------------+------------------+-----+------+
|name            |languages         |state|gender|
+----------------+------------------+-----+------+
|{James, , Smith}|[Java, Scala, C++]|OH   |M     |
+----------------+------------------+-----+------+

df.filter(~(df.state == "OH")).show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+
