-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Identifique quais as marcas de veículo mais visitada na tabela sales.funnel

select 
     products.brand,
     count(*) as visits

from sales.funnel as funnel
left join sales.products as products
     on funnel.product_id = products.product_id
	
group by products.brand
order by visits desc

-- (Exercício 2) Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel

select 
  store.store_name,
  count(*) as visits

from sales.funnel as funnel
left join sales.stores as store
   on funnel.store_id = store.store_id
	
group by store.store_name
order by visits desc


-- (Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
-- consta na coluna "size" da tabela temp_tables.regions)

select
 region.size,
  count(*) as quant
  from sales.customers as customer

left join temp_tables.regions as region
  on lower(customer.city) = lower(region.city)
  and lower(customer.state) = lower(region.state)
	
group by region.size
order by quant desc
