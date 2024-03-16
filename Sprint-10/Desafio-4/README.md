
1. criação de um data lake no amazon s3
2. script python (csv) executado através de um conteiner docker
3. script python lambda (dados da API TMBD)
4. aws glue pra limpar e modificar os dados e levar pro bucket no s3 (camada trusted e refined) e modelagem dos dados
5. athena para importar dados ao quicksight

[text](Folha_1_2024-03-03T09_52_15.pdf)


- minha análise é sobre a variação de classificação dos filmes do gênero de guerra na API do TMBD.
eu percebi que tanto a classificação dos filmes quanto a quantidade de votos variam bastante entre os 5,299 filmes analisados.

- meu primeiro gráfico mostra a popularidade dos filmes de guerra por ano, e pode-se observar que em 2022 e 2023 ela é bem maior, pode ser devido aos filmes nada de novo ao front e o pacto.
- nessa análise da quantidade de filmes de guerra produzidos por ano, é possível notar picos em 1943 e o segundo maior em 2014. o aumento dos filmes desse gênero nessa época foi possívelmente por conta da segunda guerra mundial, onde os filmes eram usados tanto em formas de entretenimento quanto propaganda. mesmo assim, dá pra notar que a popularidade e a quantidade de avaliações desses filmes não aumentam na mesma proporção na banco de dados.
-isso pode ser devido a grande quantidade de filmes ou pela falta de dados na api, pois foi possível notar que a grande maioria dos filmes dese gênero não possuem muitos votos [grafico de rodela], o que inflinge no resultado da avaliação e popularidade do filme, sendo o resultado muito alto ou muito baixo por falta de classificiação. é possível ver que apenas 125 filmes analisados possuem mais de 1000 avaliações.

-por exemplo, alguns filmes possuem pouquíssimos votos e a sua classificação pode ficar alta demais ou baixa demais. os filmes com maiores quantidades de votos, nesse caso os mais recentes, têm notas mais balanceadas.

então resumidamente, mesmo com picos de produção e até da popularidade em alguns anos, a quantidade de avaliações pode ser insuficiente pra fazer uma análise da classificação dos filmes. a api pode apresentar uma quantidade insuficiente de dados, especialmente aos filmes menos recentes e fazer uma análise voltada a classificações com a api pode não ser muito interessante.


