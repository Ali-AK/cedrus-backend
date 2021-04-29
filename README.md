#Cedrus Backend

##Installing Requirements 
To install the requirements, run the following command:
    `pip install -r requirements.txt`

##Connecting to the database
In file  `database.py`, you will find this variable: `SQLALCHEMY_DATABASE_URI`
You should insert your connection string as follows: 
    `SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@<host>:<port>/<database name>'`
    
##Populating the tables
Once you connect to your database and run the application, the tables will be crated automatically
To populate the tables:
* genres table: send a post request to this url: `http://127.0.0.1:5000/api/v1/genres/populate` with a json body that you can find in data/genres.json
* movies table: send a post request to this url: `http://127.0.0.1:5000/api/v1/movies/populate` with a json body that you can find in data/movies.json


##Run the app
Run the following command: `python app.py`