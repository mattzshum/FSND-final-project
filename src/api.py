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
                })
            except:
                abort(422)
        except:
            abort(500)

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

    
    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)