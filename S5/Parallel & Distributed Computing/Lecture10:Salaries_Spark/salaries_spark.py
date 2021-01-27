
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import expr
from pyspark.sql.types import *
from pyspark.sql.functions import *
from functools import reduce

# SAMPLE LINE:
#"Aaron,Keontae E",AIDE BLUE CHIP,W02200,Youth Summer  ,06/10/2013,$11310.00,$873.63

spark = SparkSession.builder.appName("Top Salaries").getOrCreate()

mySchema = StructType([
    StructField("a", StringType(), False),
    StructField("b", StringType(), False),
    StructField("c", StringType(), False),
    StructField("d", StringType(), False),
    StructField("e", StringType(), False),
    StructField("salary", StringType(), False),
    StructField("f", StringType(), False)
    ])

df = spark.read.format("csv").option("header","true").schema(mySchema).load("salaries.csv")
excluColumns = "a,b,c,d,e,f".split(",")
df = reduce(DataFrame.drop, excluColumns, df).withColumn('d_salary', regexp_replace('salary', '[$,]', '').cast('double'))
excluColumns= ["salary"]
df2 = reduce(DataFrame.drop, excluColumns, df)
df2.show()
result = df2.sort(desc("d_salary")).limit(10)
result.write.format("csv").option("path", "output3").save()

