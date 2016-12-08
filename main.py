from flask import Flask, request, session,redirect, url_for, abort,render_template,flash
import datetime
import model

app = Flask(__name__)
app.config['SECRET_KEY'] = "TIA"

logged_in = False
admin = False

@app.route('/')
def index():    
    if session.get("active"):
        if session.get("admin") == True:
            return render_template("Admin_Repairs.html" ,repairs = model.view_repairs())
        else:
            user_id = str(session.get("user_id")) 
            return render_template("user_repairs.html",repairs = model.view_repairs_user(user_id))
    else:
        return render_template("sign_in.html")
    
@app.route('/login', methods=['GET','POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        if request.form.get('email') != "" and request.form.get('password') != "":
            email = request.form.get('email')
            passcode =request.form.get('password')
            session['active'] = False            

            if not model.user_login(email,passcode):
                
                error = "Enter the right credentials"                
                return render_template('sign_in.html',error = error)
            else:

                row = model.user_login(email,passcode)
                session['active'] = True
                session['user_id'] = row[0]
                session['email'] = email
                session['user_name'] = row[2]
                if row[5] == 1:
                    admin = True
                    logged_in = True
                    session['admin'] = True                   
                else:
                    logged_on,session['admin'] = True,False
                return redirect(url_for('index'))
                                    
        else:
            error = "Enter the Details"            
            return render_template("sign_in.html",error=error)
    else:
        return render_template("sign_in.html")

@app.route("/logout")
def logout():    
    session.clear()
    return render_template("sign_in.html")

@app.route("/sign_up",methods=["GET","POST"])
def sign_up():
    error = None
    
    if request.method == 'POST':
        if request.form.get("password") == request.form.get("confirm_password"):
            email = request.form.get("email")
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            password = request.form.get("password")
            role = request.form.get("role")
            try:
                model.create_user(email,first_name,last_name,password,"0")
            
                return redirect(url_for('view_all'))

            except:

                error = "Did not send message"
                return redirect(url_for('index'))
        else:
            error = "Passwords not a match"
            return  render_template("create_user.html" ,error = error)
    return render_template("create_user.html")
    

@app.route("/view_user_repairs")
def view_repairs():
    try:
        repairs = model.view_repairs_user(session["user_id"])
        return render_template("user_repairs.html",repairs = repairs)
    except:
        return render_template("user_repairs.html",repairs = repairs)

@app.route("/view_all_repairs")
def view_all():
    if session.get("admin") == True :
        if model.view_repairs():
            repairs = model.view_repairs()            
            return render_template("Admin_Repairs.html", repairs = repairs)
    
        

@app.route("/repair_request", methods =["GET","POST"] )
def repair_request():
    error =None
    message = None
    if session.get("active") == True:
        return render_template("repair_request.html")
        if request.method == "POST":
            desc = request.form.get("description")
            desc_type = request.form.get("desc_type")
            req_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user_id = session.get("user_id")
            email = session.get("email")
            repair_type = request.form.get("request_type")
            import pdb;pdb.pm()
            model.add_repair(user_id,email,desc,desc_type," "," "," "," ",req_date,repair_type)                
            return render_template("user_repairs.html",repairs = model.view_repairs_user(session["user_id"]))

@app.route("/add_repair")
def add_repair():
    if session.get("active"):        
        return render_template("repair_request.html")

@app.route("/approval" , methods=['GET','POST'])
def admin_approval():
    if session.get("admin"):
        if request.method == 'POST':
            repair_id = request.form.get("repair_id")
            status = request.form.get("status")
            progress = request.form.get("progress")            
            fundi = request.form.get("fundi")
            if int(fundi) == 1:
                fundi_name = "Kevin"
            elif int(fundi) == 2:
                fundi_name = "brian"
            else:
                fundi_name = "perez" 
            
            if model.update_status(int(status),progress,int(fundi),fundi_name,int(repair_id)):
                return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
                
              
              


