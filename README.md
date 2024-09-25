# sistema-de-agrupamentos
# EXPLICAÇAO CODIGO
 #####  Esse código serve para agrupar usuários com base nos filmes que assistiram e, a partir desses grupos, recomendar novos filmes. Ele utiliza o algoritmo K-Means para identificar padrões nos hábitos de visualização dos usuários, formando grupos semelhantes. Com base nesses grupos, o sistema sugere filmes que outros usuários, com gostos parecidos, assistiram, mas que o usuário em questão ainda não viu. Assim, o objetivo é proporcionar recomendações mais personalizadas e relevantes.
# KMeans
##### A função do K-Means é agrupar dados em clusters, ou seja, em grupos de forma que os dados dentro de cada grupo sejam mais semelhantes entre si do que em relação a dados de outros grupos. Aqui estão os principais pontos sobre como o K-Means funciona:
 Inicialização: O algoritmo começa escolhendo aleatoriamente um número pré-definido de centroids (centros de grupos). Cada centroid representa a média dos pontos que pertencem a um cluster.

Atribuição de Grupos: Para cada ponto de dados, o algoritmo calcula a distância entre o ponto e cada centroid e atribui o ponto ao grupo cujo centroid está mais próximo.

Atualização dos Centroids: Depois que todos os pontos foram atribuídos a grupos, os centroids são recalculados como a média dos pontos de cada grupo.

Iteração: Os passos de atribuição de grupos e atualização dos centroids são repetidos até que os centroids não mudem significativamente (ou até atingir um número máximo de iterações). Isso significa que os grupos se estabilizaram.

Resultado: O resultado final é uma divisão dos dados em clusters, onde cada cluster representa um grupo de dados semelhantes.