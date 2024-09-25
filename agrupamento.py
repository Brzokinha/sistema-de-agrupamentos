import numpy as np
from sklearn.cluster import KMeans


filmes_assistidos = np.array([
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1]
])

num_clusters = 2

kmeans = KMeans (n_clusters=num_clusters,
                 random_state=0,n_init=10)

kmeans.fit(filmes_assistidos)

grupos_indice = kmeans.predict(filmes_assistidos)

print("Usuario pertence ao seguinte grupo:")
for i, cluster in enumerate(grupos_indice):
  print(f"Usuario {i+1} pertence ao grupo {cluster+1}")

  print("\nfilmes assistido:")
  for i in range (len(filmes_assistidos)):
    assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
    print(f"Usuario {i+1} assistiu aos filmes: {assistidos}")

def recomendar_filmes(filmes, filmes_assistidos, grupos_indice):
  filmes = np.array(filmes)

  usuario_id = len(filmes_assistidos)
  grupo_usuario = kmeans.predict([filmes])[0]

  usuario_no_mesmo_grupo = [i for i in range(len(grupos_indice))
  if grupos_indice[i] == grupo_usuario]

  filmes_recomendados = set()
  for usuario in usuario_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

  filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

  filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

  return sorted(filmes_recomendados)


filmes_assistidos_usuario = [0, 1, 1, 1]

filmes_recomendados = recomendar_filmes(filmes_assistidos_usuario, filmes_assistidos, grupos_indice)

print(f"\nfilmes recomendados: {filmes_recomendados}")