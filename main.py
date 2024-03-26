import random
from flask import Flask, jsonify, request
from proximo_feriado  import *
app = Flask(__name__)
peliculas = [
    {'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'},
    {'id': 2, 'titulo': 'Star Wars', 'genero': 'Acción'},
    {'id': 3, 'titulo': 'Interstellar', 'genero': 'Ciencia ficción'},
    {'id': 4, 'titulo': 'Jurassic Park', 'genero': 'Aventura'},
    {'id': 5, 'titulo': 'The Avengers', 'genero': 'Acción'},
    {'id': 6, 'titulo': 'Back to the Future', 'genero': 'Ciencia ficción'},
    {'id': 7, 'titulo': 'The Lord of the Rings', 'genero': 'Fantasía'},
    {'id': 8, 'titulo': 'The Dark Knight', 'genero': 'Acción'},
    {'id': 9, 'titulo': 'Inception', 'genero': 'Ciencia ficción'},
    {'id': 10, 'titulo': 'The Shawshank Redemption', 'genero': 'Drama'},
    {'id': 11, 'titulo': 'Pulp Fiction', 'genero': 'Crimen'},
    {'id': 12, 'titulo': 'Fight Club', 'genero': 'Drama'}
]


def obtener_peliculas():
    return jsonify(peliculas)


def obtener_pelicula(id):
    pelicula_encontrada = [pelicula for pelicula in peliculas if pelicula['id'] == id]
    if pelicula_encontrada:
        return jsonify(pelicula_encontrada[0])
    else:
        return jsonify({'mensaje': 'Película no encontrada'}), 404
    


def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)
    return jsonify(nueva_pelicula), 201


def actualizar_pelicula(id):
    pelicula = next((p for p in peliculas if p['id'] == id), None)
    if pelicula:
        pelicula['titulo'] = request.json.get('titulo', pelicula['titulo'])
        pelicula['genero'] = request.json.get('genero', pelicula['genero'])
        return jsonify(pelicula)
    else:
        return jsonify({'mensaje': 'Película no encontrada'}), 404


def eliminar_pelicula(id):
    pelicula = next((p for p in peliculas if p['id'] == id), None)
    if pelicula:
        peliculas.remove(pelicula)
        return jsonify({'mensaje': 'Película eliminada correctamente', 'pelicula': pelicula})
    else:
        return jsonify({'mensaje': 'Película no encontrada'}), 404
    
# Obtener películas por género
def obtener_peliculas_por_genero(genero):
    peliculas_por_genero = [pelicula for pelicula in peliculas if pelicula['genero'].lower() == genero.lower()]
    return jsonify(peliculas_por_genero)    

# Buscar películas por título
def buscar_peliculas_por_titulo(subcadena):
    peliculas_encontradas = [pelicula for pelicula in peliculas if subcadena.lower() in pelicula['titulo'].lower()]
    return jsonify(peliculas_encontradas)

# Obtener una película aleatoria
def obtener_pelicula_aleatoria():
    pelicula_aleatoria = random.choice(peliculas)
    return jsonify(pelicula_aleatoria)

# Obtener una película aleatoria según un género específico
def obtener_pelicula_aleatoria_por_genero(genero):
    peliculas_por_genero = [pelicula for pelicula in peliculas if pelicula['genero'].lower() == genero.lower()]
    if peliculas_por_genero:
        pelicula_aleatoria = random.choice(peliculas_por_genero)
        return jsonify(pelicula_aleatoria)
    else:
        return jsonify({'mensaje': 'No hay películas en el género especificado'}), 404


def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1

def pelicula_por_fecha(genero):
    next_holiday = NextHoliday()
    response = requests.get(get_url(date.today().year))
    holidays = response.json()
    next_holiday.set_next(holidays)
    peliculas_por_genero = [pelicula for pelicula in peliculas if pelicula['genero'].lower() == genero.lower()]
    if peliculas_por_genero:
        pelicula_aleatoria = random.choice(peliculas_por_genero)
    else:
         pelicula_aleatoria = "no hay para esta fecha"

    return jsonify({'El próximo feriado': next_holiday.holiday,'pelicula':pelicula_aleatoria})



app.add_url_rule('/peliculas/genero/<string:genero>', 'obtener_peliculas_por_genero', obtener_peliculas_por_genero, methods=['GET'])
app.add_url_rule('/peliculas/buscar/<string:subcadena>', 'buscar_peliculas_por_titulo', buscar_peliculas_por_titulo, methods=['GET'])
app.add_url_rule('/peliculas/aleatoria/', 'obtener_pelicula_aleatoria', obtener_pelicula_aleatoria, methods=['GET'])
app.add_url_rule('/peliculas/aleatoria/genero/<string:genero>', 'obtener_pelicula_aleatoria_por_genero', obtener_pelicula_aleatoria_por_genero, methods=['GET'])
app.add_url_rule('/peliculas/sugerida/genero/<string:genero>', 'pelicula_por_fecha', pelicula_por_fecha, methods=['GET'])
app.add_url_rule('/peliculas', 'obtener_todas_las_peliculas', obtener_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/<int:id>', 'obtener_pelicula_por_id', obtener_pelicula, methods=['GET'])
app.add_url_rule('/peliculas', 'agregar_nueva_pelicula', agregar_pelicula, methods=['POST'])
app.add_url_rule('/peliculas/<int:id>', 'actualizar_pelicula_por_id', actualizar_pelicula, methods=['PUT'])
app.add_url_rule('/peliculas/<int:id>', 'eliminar_pelicula_por_id', eliminar_pelicula, methods=['DELETE'])

if __name__ == '__main__':
    app.run()
