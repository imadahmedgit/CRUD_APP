For Running this prototype:


Recommended Requirements:
------------------------------
OS: Ubuntu 18.04 or latest

Python 3+

Flask Framework

To install flask framework - from terminal please enter the following command:

pip3 install flask



Instruction:
---------------------------------

To run the prototype go inside the downloaded CRUD_APP directory from terminal

Inside that directory just type the following command: 

python3 app.py

then go to the browser and type localhost:5000

Done!


Prototype Features:
---------------------

Create/Insert, Read, Update, Delete features are implemented for Users, Orders and Scenes.

On every page, table is placed below the forms to verify insertions, updates, changes.

SQLite3 database is used to support portability. crud.db is the database file. This file can also be viewed by SQLite3 Browser.

One single user can place multiple orders. Orders can have multiple scenes. 

Once a user is deleted, no orders can be placed for that particular user to ensure data consistency. Same goes for the orders, once deleted it can't be found
for new scenes.

After doing insert data for orders and scenes make sure page is refreshed to load data 
from database into dropdowns. Changes are reflected on Data Tables.


Files
----------------
app.py
queries.py
Templates Dir-- all html view files 
crud.db - sqlite3 database file




