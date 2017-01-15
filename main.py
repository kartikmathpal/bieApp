#imports
from bottle import Bottle, template
from rest_service import main as rest_service_app
from web_app import main as web_app

#initializes app
app = Bottle()

#mounts sub apps
app.mount('/rest_service', rest_service_app.app)
app.mount('/web_app'     , web_app.app)

@app.get('/')
def appHome():
	return template('index')

if __name__ == "__main__":
	app.run(host='localhost', port=8080, debug="True", reloader="True")
