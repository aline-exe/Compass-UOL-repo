from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand, floor, col

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv(
    "Sprint-8\\Exercícios\\Exercícios Spark Batch\\Exercício 2\\nomes_aleatorios.txt"
)
paises = [
    "Argentina",
    "Bolívia",
    "Brasil",
    "Chile",
    "Colômbia",
    "Equador",
    "Guiana",
    "Paraguai",
    "Peru",
    "Suriname",
    "Uruguai",
    "Venezuala",
    "Guiana Francesa",
]


# rand paises start
df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 1 / 13, paises[0])
    .when(rand() < 2 / 13, paises[1])
    .when(rand() < 3 / 13, paises[2])
    .when(rand() < 4 / 13, paises[3])
    .when(rand() < 5 / 13, paises[4])
    .when(rand() < 6 / 13, paises[5])
    .when(rand() < 7 / 13, paises[6])
    .when(rand() < 8 / 13, paises[7])
    .when(rand() < 9 / 13, paises[8])
    .when(rand() < 10 / 13, paises[9])
    .when(rand() < 11 / 13, paises[10])
    .when(rand() < 12 / 13, paises[11])
    .otherwise(paises[12]),
)
# rand paises end
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")  # renomear coluna
df_nomes = df_nomes.withColumn(
    "AnoNascimento", floor(rand() * (2010 - 1945 + 1) + 1945)
)  # adc coluna ano nasc
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").otherwise(
        when(rand() < 0.66, "Medio").otherwise("Superior")
    ),
)  # adc coluna escolaridade

# filtragem (só consegui filtrar 2000 pra cima usando o rand, tentei usar >= mas não filtrou os anos certos)
df_nomes = df_nomes.withColumn(
    "AnoNascimento", floor(rand() * (2022 - 2000 + 1) + 2000)
)

df_nomes.printSchema()
df_nomes.show(10)
