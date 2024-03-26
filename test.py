import requests

# Obtener todas las películas
response = requests.get('http://localhost:5000/peliculas')
peliculas = response.json()
print("Películas existentes:")
for pelicula in peliculas:
    print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
print()

# Agregar una nueva película
nueva_pelicula = {
    'titulo': 'Pelicula de prueba',
    'genero': 'Acción'
}
response = requests.post('http://localhost:5000/peliculas', json=nueva_pelicula)
if response.status_code == 201:
    pelicula_agregada = response.json()
    print("Película agregada:")
    print(f"ID: {pelicula_agregada['id']}, Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
else:
    print("Error al agregar la película.")
print()

# Obtener detalles de una película específica
id_pelicula = 1  # ID de la película a obtener
response = requests.get(f'http://localhost:5000/peliculas/{id_pelicula}')
if response.status_code == 200:
    pelicula = response.json()
    print("Detalles de la película:")
    print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
else:
    print("Error al obtener los detalles de la película.")
print()

# Actualizar los detalles de una película
id_pelicula = 1  # ID de la película a actualizar
datos_actualizados = {
    'titulo': 'Nuevo título',
    'genero': 'Comedia'
}
response = requests.put(f'http://localhost:5000/peliculas/{id_pelicula}', json=datos_actualizados)
if response.status_code == 200:
    pelicula_actualizada = response.json()
    print("Película actualizada:")
    print(f"ID: {pelicula_actualizada['id']}, Título: {pelicula_actualizada['titulo']}, Género: {pelicula_actualizada['genero']}")
else:
    print("Error al actualizar la película.")
print()

# Eliminar una película
id_pelicula = 1  # ID de la película a eliminar
response = requests.delete(f'http://localhost:5000/peliculas/{id_pelicula}')
if response.status_code == 200:
    print("Película eliminada correctamente.")
else:
    print("Error al eliminar la película.")

# Obtener películas por género
response = requests.get('http://localhost:5000/peliculas/genero/Fantasía')
if response.status_code == 200:
    peliculas_fantasia = response.json()
    print("Películas de Fantasía:")
    for pelicula in peliculas_fantasia:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    print()
else:
    print("Error al obtener las películas de Fantasía.")

# Buscar películas por título
subcadena_busqueda = "Inception"
response = requests.get(f'http://localhost:5000/peliculas/buscar/{subcadena_busqueda}')
if response.status_code == 200:
    peliculas_encontradas = response.json()
    print(f"Películas que contienen '{subcadena_busqueda}' en el título:")
    for pelicula in peliculas_encontradas:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    print()
else:
    print("Error al buscar películas por título.")

# Obtener una película aleatoria
response = requests.get('http://localhost:5000/peliculas/aleatoria/')
if response.status_code == 200:
    pelicula_aleatoria = response.json()
    print("Película aleatoria:")
    print(f"ID: {pelicula_aleatoria['id']}, Título: {pelicula_aleatoria['titulo']}, Género: {pelicula_aleatoria['genero']}")
    print()
else:
    print("Error al obtener una película aleatoria.")

# Obtener una película aleatoria según un género específico
genero_aleatorio = "Aventura"
response = requests.get(f'http://localhost:5000/peliculas/aleatoria/genero/{genero_aleatorio}')
if response.status_code == 200:
    pelicula_aleatoria_genero = response.json()
    print(f"Película aleatoria de género '{genero_aleatorio}':")
    print(f"ID: {pelicula_aleatoria_genero['id']}, Título: {pelicula_aleatoria_genero['titulo']}, Género: {pelicula_aleatoria_genero['genero']}")
    print()
else:
    print(f"No hay películas de género '{genero_aleatorio}'.")

# Obtener una película sugerida para el próximo feriado de un género específico
genero_sugerido = "Drama"
response = requests.get(f'http://localhost:5000/peliculas/sugerida/genero/{genero_sugerido}')
if response.status_code == 200:
    pelicula_sugerida = response.json()
    print(f"Película sugerida de género '{genero_sugerido}' para el próximo feriado:")
    print(f"Próximo feriado: {pelicula_sugerida['El próximo feriado']}")
    print(f"Película sugerida: ID: {pelicula_sugerida['pelicula']['id']}, Título: {pelicula_sugerida['pelicula']['titulo']}, Género: {pelicula_sugerida['pelicula']['genero']}")
    print()
else:
    print(f"No hay películas de género '{genero_sugerido}' para el próximo feriado.")    
