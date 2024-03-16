## Scripts Job

### Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes).  
### Imprima o schema do dataframe gerado no passo anterior.

```Import sys
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

######################
#imprimir o schema
print("SCHEMA")
df.printSchema()

######################
data_frame = df.toDF()
DataFrameWriter(data_frame).mode('append').json(target_path)



job.commit()
```             
#### <a href="JSON\schema-dataframe.json"> Resultado </a>

#

### Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO.       

``` import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql.functions import upper
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

######################

#imprimir o schema
print("SCHEMA")
df.printSchema()

######################
data_frame = df.toDF()
data_frame = data_frame.withColumn('nome',upper(data_frame['nome'])) #maiusculo

#escrever em json
DataFrameWriter(data_frame).mode('append').json(target_path)



job.commit()

```

#### <a href="JSON\nomes-upper.json"> Resultado </a>

#

### Imprimir a contagem de linhas presentes no dataframe.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql.functions import upper
from pyspark.sql import Row #n de linhas
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)


data_frame = df.toDF()


#imprimir n de linhhas
num_linhas = df.count()
row = Row("Nº DE LINHAS")
df_linhas = spark.createDataFrame([row(num_linhas)])

#escrever em json
df_linhas.write.mode('append').json(target_path)



job.commit()

```

#### <a href="JSON\n_linhas.json"> Resultado </a>

#

### Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo. Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.

``` import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql import functions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

data_frame = df.toDF()

#agrupamento
df_group = data_frame.groupBy('ano', 'sexo').agg(functions.count('nome').alias('contagem'))
#ano decresc
df_ano_ordem = df_group.orderBy(functions.desc('ano'))

#imprimir
print('SCHEMA')
df_ano_ordem.coalesce(1).write.mode('append').json(target_path) #escrever em uma só partição ao invés de 5

job.commit()
```
#### <a href="JSON\nomes_ano_decrescente.json"> Resultado </a>

#

### Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql import functions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

data_frame = df.toDF()

df_n_feminino = data_frame.filter(data_frame.sexo == 'F')
df_n_feminino = df_n_feminino.withColumn('total', df_n_feminino['total'].cast('integer'))
df_maior = df_n_feminino.orderBy(functions.desc('total')).first()

df_maior_total = spark.createDataFrame([df_maior])



df_maior_total.write.mode('append').json(target_path)

job.commit()

```
#### <a href="JSON\nome-feminino-popular.json"> Resultado </a>

#

### Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql import functions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

data_frame = df.toDF()

df_n_masculino = data_frame.filter(data_frame.sexo == 'M')
df_n_masculino = df_n_masculino.withColumn('total', df_n_masculino['total'].cast('integer'))
df_maior = df_n_masculino.orderBy(functions.desc('total')).first()

df_maior_total = spark.createDataFrame([df_maior])


df_maior_total.write.mode('append').json(target_path)

job.commit()

```

#### <a href="JSON\nome-masculino-popular.json"> Resultado </a>

#

### Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe. Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions
from pyspark.sql import DataFrameWriter
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)


data_frame = df.toDF()
data_frame = data_frame.withColumn('total', data_frame['total'].cast('integer'))

#agrupar + somar
df_group = data_frame.groupBy('ano').agg(functions.sum('total').alias('total'))
df_ordenado = df_group.orderBy('ano')

df_10 = df_ordenado.limit(10)
df_10.show()

df_10.write.mode('append').json(target_path)

job.commit()

```

#### <a href="JSON\total-registros-10"> Resultado </a>

#

### Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.
- A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path 's3://BUCKET/lab-glue/'
- O formato deve ser JSON  
- O particionamento deverá ser realizado pelas colunas sexo e ano   (nesta ordem)   

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql.functions import upper
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
#PARAMETROS
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminho do csv e target
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo + df
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

######################

#imprimir o schema
print("SCHEMA")
df.printSchema()

######################
data_frame = df.toDF()
data_frame = data_frame.withColumn('nome',upper(data_frame['nome'])) #maiusculo

#partition sexo e ano e escrever em json
data_frame.write.partitionBy('sexo', 'ano').mode('append').json(target_path)



job.commit()

```
não consegui baixar os resultados por estarem em <a href="Prints do Lab\partição"> pastas. </a>


#