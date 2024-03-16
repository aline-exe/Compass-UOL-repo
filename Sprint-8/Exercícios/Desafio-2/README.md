## Desafio 2
comparação da avalição e classificação dos filmes: o quão o TMBD é confiável para esse tipo de análise?
notei que alguns filmes possuem uma classificação muito grande ou pequena porque haviam pouquíssimas avaliações.

endpoints:
nome do filme, ano do filme, classificação, avaliações

https://api.themoviedb.org/3/movie/{movie_id}  
https://api.themoviedb.org/3/movie/{movie_id}/release_dates  
https://api.themoviedb.org/3/movie/{movie_id}/reviews  

## Prints
Criação da função no AWS Lambda  
![Função Lambda](Evid%C3%AAncias/funcao-lambda.png)

Criação das camadas do Lambda com as imports "Boto3" e "Requests"  
![Camadas Lambda](Evid%C3%AAncias/camadas.png)  

Código Python na interface do Lambda   
![Código Python](Evid%C3%AAncias/lambda.png)   

Resultado do código  
![Saída](Evid%C3%AAncias/resultado-lambda.png)  

Buckets no S3
![Buckets](Evid%C3%AAncias/objetos-bucket.png)  

Objetos JSON no bucket  
![Alt text](Evid%C3%AAncias/json-objetos.png)