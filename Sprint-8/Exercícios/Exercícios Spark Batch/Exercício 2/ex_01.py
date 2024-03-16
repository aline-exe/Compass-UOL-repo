from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv(
    "Sprint-8\\Exercícios\\Exercícios Spark Batch\\Exercício 2\\nomes_aleatorios.txt"
)

df_nomes.show(5)
