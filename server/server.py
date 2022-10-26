from flask import Flask, request

app = Flask(__name__)

@app.post('/update')
def update():
    print(request.data)
    print(request.json)
    return str(request.json)
