
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

import re
import sys

spark = SparkSession.builder.appName("Stock Analysis").getOrCreate()

mySchema = StructType([
    StructField("date", DateType(), False),
    StructField("apple_value", DoubleType(), False),
    StructField("ibm_value", DoubleType(), False)])

df = spark.read.format('csv').option("sep", ",").schema(mySchema).load("AAPL_IBM_open.csv")

df.show()

apple_stock = df.groupBy("date").agg(max("apple_value"))
ibm_stock = df.groupBy("date").agg(max("ibm_value"))

apple_stock.write.format("csv").option("sep", "\t").option("path", "output").save()
ibm_stock.write.format("csv").option("sep", "\t").option("path", "output").save()
