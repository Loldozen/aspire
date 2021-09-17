# aspire
<div>
<h1>Aspire Challenge</h1>
  This is the repository for the aspire challenge
</div>
<div>
<h1>Setup</h1>
  After installing python, creating a virtual environment and installing all dependencies, run the following commands<br>
  python manage.py makemigrations<br>
  python manage.py migrate<br>
  python manage.py createquotes<br>
  python manage.py createcharacters<br>
  python manage.py createmovies<br>
  python manage.py runserver<br>
  </div>
<div>
<h1>Testing</h1>
Below are the list of endpoints available<br>
  POST http://127.0.0.1:8000/user/login/<br>
  POST http://127.0.0.1:8000/user/signup/  #request data of username, email, password<br>
  GET http://127.0.0.1:8000/user/favorites/{id}/ # returns the favorite quote and character of a user<br>
  GET http://127.0.0.1:8000/movie/character #returns all the characters <br>
  GET http://127.0.0.1:8000/movie/character/{id}/quote/ #returns all the quotes of a specific character<br>
  POST http://127.0.0.1:8000/movie/character/favorites/ #request body contains the user and character id. adds the character to the users favorites<br>
  POST http://127.0.0.1:8000/movie/character/quote/favorites/ #request body contains the user and quote id. adds the quote to the users favorites<br>
</div>
