from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello Cloud!'
  
@app.route('/host')
def host_info():
  return 'Hello Form ECS Fargate'


app.run(host='0.0.0.0')
