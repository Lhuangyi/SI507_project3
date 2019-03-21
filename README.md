# SI507_project3
## Introduction: 
    In my project, I have done the following things:
    - Refer to and revise the database diagram in Project 2.
    - Write code to integrate some data with a Flask application
    - Integrate models with the Flask framework to build a Flask app that uses databases for the first time.
   
   
## Simple Flask APP
   -Defined three model classes: Movies,Director and Genre
   -Created four routes:
    * `/index` -> `index.html` - shows the home page
    
   ![Image text](https://github.com/Lhuangyi/SI507_project3/blob/master/Project_3/images/homepage.png)  
      
      
   * `/all_movies` -> `all_movies.html`  - shows all movies
    
        ![Image text](https://github.com/Lhuangyi/SI507_project3/blob/master/Project_3/images/all_movies.png)  
         
         
   * `/all_directors` -> `all_directors.html`  - shows all directors
    
        ![Image text](https://github.com/Lhuangyi/SI507_project3/blob/master/Project_3/images/all_directors.png)  
         
         
   * `/movie/new/<title>/<director>/<genre>` - create a new movie
    
        ![Image text](https://github.com/Lhuangyi/SI507_project3/blob/master/Project_3/images/save.png)
        ![Image text](https://github.com/Lhuangyi/SI507_project3/blob/master/Project_3/images/saved.png)
     

    
    
## How to run the flask app?
    - First we need to run the terminal in mac.
    - Second we need to type "mkdir SI507_poject3" and then type "cd SI507_poject3", and then type "virtualenv lSI507_poject3" to set up virtual environment, and then type "cd SI507_poject3", and then type "source bin/activate" to activate the virtual environment, and then type "pip install flask" to install web framework, and last we need to type "python SI507_project3.py runserver" to run the server.
    - Last, we can type specified urls(showed above) to reach the websites we want.
  
  
## Dependencies
    Click==7.0
    Flask==1.0.2
    Flask-SQLAlchemy==2.3.2
    itsdangerous==1.1.0
    Jinja2==2.10
    MarkupSafe==1.1.1
    SQLAlchemy==1.3.1
    Werkzeug==0.15.0

