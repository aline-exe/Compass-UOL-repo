### operadores de matemática
+
-
*
/
^
%
|| -> não é um operador aritmético  
ele vai fazer soma de strings/textos, podendo criar uma coluna nova, como por exemplo primeiro e segundo nome



### calcular idade e criar coluna calculada com um alias

select 
     email, 
     birth_date, 
     (current_date - birth_date) / 365 as customer_age 
from sales.customers

obs: o 'as' vai ser um comando pra criar a coluna nova

### operadores de comparação
=
>
<
>=
<=
<>

usados pra retornar um valor true ou false
por exemplo,

select
      customer_id,
      first_name,
      professional_status,
      (professional_status = 'clt') as cliente_clt
from sales.customers

o output vai nos retornar com uma nova coluna dizendo se o cliente é clt (true) ou não (false)


### operadores lógicos
AND
OR
NOT (pode ser usado em conjunto com outros, ex IN ou NULL)
BETWEEN
IN (dentro de uma lista, exemplo ('HONDA', 'TOYOTA'))
LIKE (funciona com o %)
ILIKE (ignora letras maiúsculas e minúsculas)
IS NULL


