from flask import Flask, request, session,redirect, url_for, abort,render_template,flash
import model

app = Flask(__name__)
app.config['SECRET_KEY'] = "fdjnmsldfnmksfnjsnsdfnd"

@app.route('/')
def main():
    return render_template("sign_in.html")
    
@app.route('/login', methods=['POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        if request.form.get('email') != "" and request.form.get('password') != "":
            email,passcode = request.form.get('email'),request.form.get('password')

            if not user_login(email,passcode):
                sesssion["active"] = False
                error = "Enter the right credentials"
                flash("Error","Invalid Credentials")
                return render_template("sign_in.html",error = error)
            else:
                row = user_login(email,passcode)
                session["active"] = True
                session["user_id"] = row[0]
                session["email"] = email
                session["user_name"] = row[2]
                if row[5] == 1:
                    session["admin"]= True
                else:
                    session["admin"]= False
                    flash("SuccessFul Login")
                    print "Hello Flask"
        else:
            error = "Please Enter Your Details "
            return render_template("sign_in.html",error=error)
    redirect(url_for("sign_in"))

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("user_entries"))

@app.route("/signup",methods=["POST"])
def sign_up():
    if session["admin"] == True:
        if request.method == 'POST':
            if request.form["password"] == request["confirm_password"]:
                email = request.form["email"]
                first_name = request.form["first_name"]
                last_name = request.form["last_name"]
                password = request.form["password"]
                role = request.form["role"]

                if create_user(email,first_name,last_name,password,role):
                    print "yes"
                else:
                    print "no"

if __name__ == "__main__":
    app.run(debug=True)
                
              
              


