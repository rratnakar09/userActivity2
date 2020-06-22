# userActivity2
A Django API application with User and ActivityPeriod

Problem Statement:</br>
Design and implement a Django application with User and ActivityPeriod models, write a custom management command to 
populate the database with some dummy data, and design an API to serve that data in the json format given in 
this link(https://drive.google.com/open?id=1xZa3UoXZ3uj2j0Q7653iBp1NrT0gKj0Y).

Instructions:
* Please complete this assignment using Python & Django. Feel free to use any Python packages as you see fit.
* The code and API endpoint should be production ready and hosted somewhere in a publicly accessible location like on AWS, Heroku, PythonAnywhere, etc.
* Please include a README file.

Solution Approach:</br>
Create a new django application</br>
Create a new app inside this application</br>
Create two model with name User and Activity. User will store the user data like id(as primary key), first name, last name and time zone. Activity will store the user's activity.</br>
The User will have a one to many relation with activity. One user can have multiple activities.</bt>
I have used a class View which has extended generic view. I have defined a get function in this I have reformated the data 
from User and Activity to make it look like the given format.</br> 
For this I have used dictionary and list data structure. I have used jsonresponse to serialize the data and send it to use</br>

I have deployed this on pythonanywhere "http://rratnakar09.pythonanywhere.com/"</br>
end point: 'api/get/' <br>

import requests<br>
BASE_URLS = "http://rratnakar09.pythonanywhere.com/"<br>
ENDPOINT = "api/get"<br>
resp = requests.get(BASE_URLS + ENDPOINT)<br>
print(resp.json())


It was a great learning experience to learn and deploy a web api app on pythonanywhere.

### Future Work:<br>
Working on to use Django Rest Framework to make an API which will serve <br>
* get users
* get user by user_id
* post by user_id
* delete by user_id
* get activities
* get activity by user_id and activity_id
* post activity by user_id and activity_id
* delete activity by user_id and activity_id 

