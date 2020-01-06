from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route("/")
@app.route("/home")
@app.route("/users")
def users():
	from queries import sql_query
	results = sql_query(''' SELECT * FROM users''')
	return render_template('users.html', title='User', Users = results)


@app.route("/orders")
def orders():
    from queries import sql_query
    exusers = sql_query(''' SELECT user_id FROM users''')
    results = sql_query(''' SELECT * FROM orders''')
    return render_template('orders.html', exusers=exusers, Orders=results)

@app.route("/scenes")
def scenes():
    from queries import sql_query
    exorders = sql_query(''' SELECT order_id FROM orders''')
    results = sql_query(''' SELECT * FROM scenes''')
    return render_template('scenes.html', exorders=exorders, Scenes=results)

@app.route('/insert',methods = ['POST', 'GET']) # CREATE / INSERT USER INFO
def sql_datainsert():
    from queries import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        email = request.form['email']
        date_created = request.form['date_created']
        active = request.form['active']
        sql_edit_insert(''' INSERT INTO users (first_name,last_name,email,date_created,active) VALUES (?,?,?,?,?) ''', (first_name,last_name,email,date_created,active) )
    results = sql_query(''' SELECT * FROM users''')
    msg = 'INSERT INTO data_table (first_name,last_name,email,date_created,active) VALUES ('+first_name+','+last_name+','+email+','+date_created+','+active+')'
    return render_template('users.html', Users = results)


@app.route('/query_edit',methods = ['POST', 'GET']) # Edit USER INFO
def sql_editlink():
    from queries import sql_query, sql_query2
    if request.method == 'GET':
        user_id = request.args.get('euser_id')
        eresults = sql_query2(''' SELECT * FROM users where user_id = ?''', (user_id))
    results = sql_query(''' SELECT * FROM users''')
    return render_template('users.html', eresults=eresults, results=results)



@app.route('/edit',methods = ['POST', 'GET']) # Update USER INFO
def sql_dataedit():
    from queries import sql_edit_insert, sql_query
    if request.method == 'POST':
        user_id = request.form['user_id']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        email = request.form['email']
        date_created = request.form['date_created']
        active = request.form['active']
        sql_edit_insert(''' UPDATE users set first_name=?,last_name=?,email=?,date_created=?,active=? WHERE user_id=?''', (first_name,last_name,email,date_created,active,user_id) )
    results = sql_query(''' SELECT * FROM users''')
    return render_template('users.html', Users=results)


@app.route('/delete',methods = ['POST', 'GET']) # Delete USER INFO
def sql_datadelete():
    from queries import sql_delete, sql_query
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        sql_delete(''' DELETE FROM users where user_id = ?''', (user_id) )
    results = sql_query(''' SELECT * FROM users''')
    return render_template('users.html', Users=results)


@app.route('/insert_orders',methods = ['POST', 'GET']) # CREATE / INSERT ORDERS INFO
def sql_datainsert_orders():
    from queries import sql_edit_insert, sql_query
    exusers = sql_query(''' SELECT user_id FROM users''')
    print(exusers)
    if request.method == 'POST':
        order_date = request.form['order_date']
        status = request.form['status']
        user_id = request.form['user_id']
        sql_edit_insert(''' INSERT INTO orders (order_date,status,user_id) VALUES (?,?,?) ''', (order_date,status,user_id) )
    results = sql_query(''' SELECT * FROM orders''')
    return render_template('orders.html', Orders = results)

@app.route('/query_edit_orders',methods = ['POST', 'GET']) # Edit Orders INFO
def sql_editlink_orders():
    from queries import sql_query, sql_query2
    if request.method == 'GET':
        order_id = request.args.get('eorder_id')
        eresults = sql_query2(''' SELECT * FROM orders where order_id = ?''', order_id)
    results = sql_query(''' SELECT * FROM orders''')
    return render_template('orders.html', eresults=eresults, Orders=results)


@app.route('/edit_orders',methods = ['POST', 'GET']) # Update Orders INFO
def sql_dataedit_orders():
    from queries import sql_edit_insert, sql_query
    if request.method == 'POST':
        order_id = request.form['order_id']
        order_date = request.form['order_date']
        status = request.form['status']
        sql_edit_insert(''' UPDATE orders set order_date=?,status=? WHERE order_id=?''', (order_date,status,order_id) )
    results = sql_query(''' SELECT * FROM orders''')
    return render_template('orders.html', Orders=results)

@app.route('/delete_orders',methods = ['POST', 'GET']) # Delete Order INFO
def sql_datadelete_orders():
    from queries import sql_delete, sql_query
    if request.method == 'GET':
        order_id = request.args.get('order_id')
        sql_delete(''' DELETE FROM orders where order_id = ?''', (order_id) )
    results = sql_query(''' SELECT * FROM orders''')
    return render_template('orders.html', Orders=results)

@app.route('/insert_scenes',methods = ['POST', 'GET']) # CREATE / INSERT Scenes INFO
def sql_datainsert_scenes():
    from queries import sql_edit_insert, sql_query
    exorders = sql_query(''' SELECT order_id FROM orders''')
    if request.method == 'POST':
        name = request.form['name']
        s_status = request.form['s_status']
        sensor = request.form['sensor']
        order_id = request.form['order_id']
        sql_edit_insert(''' INSERT INTO scenes (name,s_status,sensor,order_id) VALUES (?,?,?,?) ''', (name,s_status,sensor,order_id) )
    results = sql_query(''' SELECT * FROM scenes''')
    return render_template('scenes.html', Scenes = results)

@app.route('/query_edit_scenes',methods = ['POST', 'GET']) # Edit Scenes INFO
def sql_editlink_scenes():
    from queries import sql_query, sql_query2
    if request.method == 'GET':
        scene_id = request.args.get('scene_id')
        eresults = sql_query2(''' SELECT * FROM scenes where scene_id = ?''', scene_id)
    results = sql_query(''' SELECT * FROM scenes''')
    return render_template('scenes.html', eresults=eresults, Scenes=results)


@app.route('/edit_scenes',methods = ['POST', 'GET']) # Update scenes INFO
def sql_dataedit_scenes():
    from queries import sql_edit_insert, sql_query
    if request.method == 'POST':
        name = request.form['name']
        s_status = request.form['s_status']
        sensor = request.form['sensor']
        scene_id = request.form['scene_id']
        sql_edit_insert(''' UPDATE scenes set name=?,s_status=?,sensor=? WHERE scene_id=?''', (name,s_status,sensor,scene_id) )
    results = sql_query(''' SELECT * FROM scenes''')
    return render_template('scenes.html', Scenes=results)

@app.route('/delete_scenes',methods = ['POST', 'GET']) # Delete Scenes INFO
def sql_datadelete_scenes():
    from queries import sql_delete, sql_query
    if request.method == 'GET':
        scene_id = request.args.get('scene_id')
        sql_delete(''' DELETE FROM scenes where scene_id = ?''', (scene_id) )
    results = sql_query(''' SELECT * FROM scenes''')
    return render_template('scenes.html', Scenes=results)

if __name__ == '__main__':
    app.run(debug=True)
    