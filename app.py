from flask import Flask
app = Flask(__name__) 

@app.route('/he')
def hello():
    return 'Hello'

@app.route('/hello')
def hello_name():
    return 'Hello Kipyegon'

if __name__=='__main__':
    app.run(debug=True)
