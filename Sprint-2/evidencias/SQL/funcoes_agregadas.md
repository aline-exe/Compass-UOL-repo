### COUNT
vai fazer a contagem de linhas ou de valores de uma coluna

ex
select count (product_id)
from sales.funnel
where visit_page_date between '2021-01-01' and '2021-01-31'

ex2
select min(price), max (price), avg(price)
from sales.product

ex3
select *
from sales.products
where price = (select max (price) from sales.products)

obs.: pode funcionar com o distinct

### GROUP BY
serve pra agrupar registros semelhantes de uma coluna

ex 1, calcular nº de clientes por estado
select state, count (*) as contagem
from sales.customers
group by state
order by contagem desc

### HAVING
é igual o WHERE mas pode ser usado em funções agragadas, onde o não se pode utulizar o where
