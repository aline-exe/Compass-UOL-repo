select
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media

from tbvendas

where status = 'Concluído'

group by 
    estado, 
    nmpro
order by estado