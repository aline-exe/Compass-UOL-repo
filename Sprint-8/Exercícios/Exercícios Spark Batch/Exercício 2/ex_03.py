from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv(
    "Sprint-8\\Exercícios\\Exercícios Spark Batch\\Exercício 2\\nomes_aleatorios.txt"
)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").otherwise(
        when(rand() < 0.66, "Medio").otherwise("Superior")
    ),
)
df_nomes.printSchema()
df_nomes.show(10)
