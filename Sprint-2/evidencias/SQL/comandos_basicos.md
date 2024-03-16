### SELECT
seleciona valores específicos de uma coluna dentro de uma tabela  
exemplo, pra selecionar o email e o nome de um cliente, colocaríamos:

**select** email, first_name, last_name
from sales.customers  

sendo email, first_name e last_name valores de uma coluna numa tabela.  

pra selecionar **todas** as colunas, escrevemos 
select *   



### DISTINCT
seleciona e faz com que valores não se repitam
exemplo, pra que selecionemos marcas dos carros dos clientes sem que elas sem repitam, colocamos:

select **distinct** brand 
from sales.product

sendo brand o valor da marca e sales.product a tabela
o resultado, ao invés de aparecer as marcas de todos os carros de todos os clientes, vai mostrar apenas quais marcas estão presentes na tabela

se selecionar mais de uma coluna, o comando vai retornar combinações diferentes, **nunca duplicado**

### WHERE
seleciona valores específicos, como por exemplo localização ou idade
por exemplo, pra selecionar email de clientes que moram em SC e MS que tenham mais de 30 anos:  

select email 
from sales.customers
**where** (state = 'SC' or state = 'MS') and birth_date < '1991-12-28'

obs: colocamos aspas simples pra strings/textos
obs 2: a idade é calculada com o birth_date do cliente pra evitar colocar info redundante nas tabelas
obs 3: datas são escritas no formato 'YYYY-MM-DD' ou 'YYYYMMDD'

### ORDER BY
vai organizar os valores selecionados em ordem crescente ou decrescente (desc)   
por exemplo, pra ordenar carros por seus valores:  

select *
from sales.product
**order by** price **desc** (decrescente)

o resultado vai ser a tabela dos carros mais caros até os mais baratos.

obs: se tratando de texto, a ordem crescente é a ordem alfabética


### LIMIT
vai limitar a quantidade de resultados que aparecem na query
por exemplo, pra selecionar os 10 produtos mais caros

select *
from sales.products
order by price desc
**limit 10** 

 