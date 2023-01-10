## Technology 
python3
Flask
SQLAlchemy


## Routes
|Method	     |Path	            |Purpose|
|------------|------------------|-----------------------------------------------------------|
|GET	     |/	                |The Main page|
|GET	     |/user:name	    |The Main page(logged in)|
|POST	     |/signup	        |sign up page(form)|
|GET	     |/log in	        |log in page(form)|
|POST	     |/upload	        |Upload a new meme|
|GET	     |/meme/:id	        |Show one meme in details|
|PUT	     |/meme/:id/edit	|Edit one meme's attributes|
|PUT	     |/meme/:id	        |Comment on a meme|
|DELETE	     |/meme/:id	        |Delete a meme|


# laugh_factory_app