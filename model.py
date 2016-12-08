import datetime
import sqlite3 as sql


def user_login(email,passcode):
    
   
    con = sql.connect("MainT.db")
    cur = con.cursor()
    cur.execute('SELECT * from USERS where email="%s"' %(email))
    row = cur.fetchone()
    if row:
        if (row[4] == (passcode)):
        	return row
    else:
      	return False
   

def create_user(email,first_name,last_name,passcode,is_admin):
	con = sql.connect("MainT.db")
	try:
		
		cur = con.cursor()
		cur.execute("INSERT INTO users (email,first_name,last_name,password,is_admin) VALUES (?,?,?,?,?)", (email, first_name,last_name,passcode,is_admin) )
		con.commit()
		return True
	except Exception as e:
		print(e)
		con.rollback()
		return False

def hash_password(password):
    return generate_password_hash(password) 

def verify_password(password_hash,password):
    return check_password_hash(password_hash,password)

def add_fundi(first_name,last_name,speciality,contact):
    try:
    	con = sql.connect("MainT.db")
    	cur = con.cursor()
    	cur.execute("INSERT INTO fundi (first_name,last_name,speciality,contact) values (?,?,?,?) " , (first_name,last_name,speciality,contact) )
    	con.commit()
        return "Record successfully added"
    except:
        con.rollback()
        return"error in insert operation"

def view_fundis():
	con = sql.connect("MainT.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM FUNDI")
	row = cur.fetchall()
	return row

def update_fundi_contact(fundi_id,contact):
	try:
		con = sql.connect("MainT.db")
		cur = con.cursor()
		cur.execute("UPDATE fundi SET contact = ? where id = ?", (fundi_id,contact))
	except:
	    con.rollback()
	    return "error in update operation"

def add_repair(user_id,email,description,desc_type,request_date,status,progress,fundi_id,fundi_name,req_type):
    try:
    	con = sql.connect("MainT.db")
    	cur = con.cursor()
    	cur.execute("INSERT INTO repairs (user_id,email,description,repair_type,status,progress,fundi_id,fundi_name,request_date,request_type) values (?,?,?,?,?,?,?,?,?,?) " ,(user_id,email,description,desc_type,request_date,status,progress,fundi_id,fundi_name,req_type))
    	con.commit()
        msg = "Record successfully added"
    except:
    	con.rollback()
    	return "error in update opertaion"

def view_repairs():
    con = sql.connect("MainT.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM repairs")
    row = cur.fetchall()
    return row

def view_repairs_user(user_id):
	con = sql.connect("MainT.db")
	cur = con.cursor()
	cur.execute('SELECT * from repairs where user_id = ? ', ( user_id ) )
	row = cur.fetchall()
	if row: 
		return row
	else:
		return False

def view_progress(progress):
	con = sql.connect("MainT.db")
	cur = con.cursor()
	cur.execute('SELECT * from repairs where progress="%s"' %(progress))
	if cur.fetchone() is not None:
		return row.user_id
	else:
		return False

def update_status(status,progress,fundi_id,fundi,rep_id ):
	try:
		con = sql.connect("MainT.db")
		cur = con.cursor()
		cur.execute("UPDATE repairs SET progress = ?,status = ?,fundi_id = ?,fundi_name = ? where id = ?" ,(progress,status,fundi_id,fundi,rep_id))
		con.commit()
		return True
	except Exception as e:
		print(e)
		con.rollback()
		return "error in update operation"

def view_repairs_fundi(fundi_id):
	con = sql.connect("MainT.db")
	cur = con.cursor()
	cur.execute('SELECT * from repairs where fundi_id="%d"'%(fundi_id))
	if cur.fetchone() is not None:
		return row
	else:
		return False
