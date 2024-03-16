-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers

WITH num_of_visits AS (
    SELECT customer_id, COUNT(*) AS visits_n
    FROM sales.funnel
    GROUP BY customer_id
)

SELECT cust.*, nv.visits_n
FROM sales.customers AS cust
LEFT JOIN num_of_visits AS nv ON cust.customer_id = nv.customer_id
WHERE nv.visits_n IS NOT NULL;
