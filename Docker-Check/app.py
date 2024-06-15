from flask import Flask
app=Flask(__name__)
#decorators

@app.route('/')

def Hello_page():
    return "Hello Welcome to my page"

if __name__ == "__main__":
    app.run(debug=True,port=8001,host="0.0.0.0")
