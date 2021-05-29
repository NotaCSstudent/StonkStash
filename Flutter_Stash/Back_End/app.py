from flask import Flask,jsonify

hello = "{}".format(3)
bye = "{}".format(2)


app = Flask(__name__)
#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET'])
def index():
    return jsonify({'greetings' : 'Hi! this is python'}) #returning key-value pair in json format


if __name__ == "__main__":
    app.run(debug = True) #debug will allow changes without shutting down the server 


