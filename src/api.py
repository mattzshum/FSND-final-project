import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .models import setup_db, Actor, Movie
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Headers', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    #--------------------------------------------------------------------------------------------------------------
    # | ACTORS |

    @app.route('/actors')
    def get_actors():
        try:
            actors=Actor.query.order_by(Actor.id).all()
            
            if len(actors) == 0:
                abort(404)
            
            try:
                return_actors = [actor.format() for actor in actors]

                return jsonify({
                    'success':True,
                    'actors':return_actors
                }), 200
            except:
                abort(422)
        except:
            abort(500)
    
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(self):
        body = request.get_json()
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        if new_name is None:
            abort(400)
        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()
            new_actor = actor.format()

            return jsonify({
                'success':True,
                'actor':new_actor
            }), 200
        except:
            abort(422)
    
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(self, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_more()

        if actor is None:
            abort(404)
        
        body = request.get_json()
        if body is None:
            abort(400)
        
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        try:
            if new_name is not None:
                actor.name = new_name
            if new_gender is not None:
                actor.gender = new_gender
            if new_age is not None:
                actor.age = new_age
            
            actor.update()

            new_actor = [actor.format()]
            return jsonify({
                'success':True,
                'actor':new_actor
            }), 200
        except:
            abort(422)
    
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_more()

        if actor is None:
            abort(404)
        
        actor.delete()

        return jsonify({
            'success':True,
            'delete':actor_id
        }), 200

    #--------------------------------------------------------------------------------------------------------------
    # | MOVIES |
    @app.route('/movies')
    def get_movies():
        try:
            movies = Movie.query.order_by(Movie.id).all()

            if len(movies) == 0:
                abort(404)
            
            try:
                return_movies = [movie.format() for movie in movies]
            
                return jsonify({
                    'success':True,
                    'movies':return_movies
                })
            except:
                abort(422)
        except:
            abort(500)
    
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie():
        body = request.get_json()
        new_title = body.get('title')
        new_year = body.get('year')
        new_month = body.get('month')
        new_day = body.get('day')
        new_genre = body.get('genre')

        if new_title is None or new_genre is None:
            abort(400)
        
        try:
            movie = Movie(title=new_title, year=new_year, month=new_month, day=new_day, genre=new_genre)
            movie.insert()
            new_movie = movie.format()

            return jsonify({
                'success':True,
                'movie':new_movie
            }), 200
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['{PATCH'])
    @requires_auth('patch:movies')
    def update_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)
        
        body = request.get_json()
        new_title = body.get('title')
        new_year = body.get('year')
        new_month = body.get('month')
        new_day = body.get('day')
        new_genre = body.get('genre')

        try:
            if new_title is not None:
                movie.title = new_title
            if new_year is not None:
                movie.year = new_year
            
            movie.update()

            new_movie = [movie.format()]

            return jsonify({
                'success':True,
                'movie':new_movie
            }), 200
        except:
            abort(422)
        
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_more()

        if movie is None:
            abort(404)
        
        movie.delete()

        return jsonify({
            'success':True,
            'delete':movie_id
        }), 200
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success':False,
            'error':400,
            'message':'bad_request'
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success':False,
            'error':404,
            'message':'not_found'
        })
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':422,
            'message':'unprocessable'
        })
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success':False,
            'error':500,
            'message':'internal_server_error'
        })
    
    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000, debug=True)
