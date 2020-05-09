# FSND Casting Agency Capstone Project

## final project for the Udacity 'Full Stack Nanodegree Program'

Heroku Link: (https://fsnd-cap-movie-actor.herokuapp.com/)

### Getting Started
#### Installing Dependencies
- must have Python 3 installed

###### PIP Dependencies
All of the required dependenceis can be installed via locating the 'requirements.txt' file in the program directory and executing the command:
``` pip install -r requriements.txt```

###### Vital Software
- Flask -> micro web framework written in Python
- SQLAlchemy -> open-source SQL toolkit and object-relational mapping for Python
- Flask-CORS -> extension for handling Cross Origin Resource sharing
  
### Running the Server
To establish the correct environemnt variables, navigate to ```\src``` and execute the following:
```
export FLASK_APP=api.py
export FLASK_ENV=debug
flask run --reload
```

### About the Project
The Casting Agency models is a company that tracks Movies as well as Actors. Directors have the abiltity to add actors to their movies while actors can make changes to their own profile.

### Models
Movies:
```
title
year
month
day
genre
```
Actors:
```
self.name
self.age
self.gender
```

### Environment
In the ```\src\.env``` file the following can be found:
```
DATABASE_URL -> postgres database
Director -> JWT Token
Actor -> JWT Token
```

##### Actor Permissions
- delete:actors
- patch:actors
- post:actors


##### Director Permissions
- ALL permissions

### Endpoints
```
GET '/actors'

reponse = {
success: True,
actors: [
          {
            name: "KEEANU REEVES",
            age: 50,
            gender: "male",
          },
          {
            name: "CAvv",
            age: 22,
            gender: "male",
          }
        ]
  }


POST '/actors'

payload = {
        name: "KEEANU REEVES",
        age: 50,
        gender: "male",
      },
response = {
  success: True,
  actor:{  
    name: "KEEANU REEVES",
    age: 50,
    gender: "male"
   }
}

PATCH '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
  success: True,
  actor:{  
    name: "KEEANU REEVES",
    age: 800,
    gender: "male"
   }
}

DELETE '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
  success: True,
  delete: actor_id
}

GET '/movies'

response = {
success: True,
movies: [
          {
            title: "telltale",
            year: 2020,
            month: 5,
            day:25,
            genre: "fiction"
          }
        ]
  }


POST '/movies'

payload = {
        title: "telltale",
        year: 2020,
        month: 5,
        day:25,
        genre: "fiction"
      }
response = {
  success: True,
  movie: {
        title: "telltale",
        year: 2020,
        month: 5,
        day:25,
        genre: "fiction"
      }
}

PATCH '/movies/<int:movie_id>'

params = <int:movie_id>

response = {
success: True,
movies:{
            title: "telltale",
            year: 2020,
            month: 5,
            day:25,
            genre: "fiction"
          }
        
  }


DELETE '/movies/<int:movie_id>'


params = <int:movie_id>

response = {
  success: True,
  delete: movie_id
} 
```

### Testing
run the command
```
python test.py
```