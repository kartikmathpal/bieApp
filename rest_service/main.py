from bottle   import Bottle, request, template
from services import search_service
import json

app = Bottle()

@app.get('/survey')
def survey():
	key = request.query["key"]
	collection = request.query["collection"]
	print key
	print collection
	response  = search_service.searchByKey(key, collection)
	print response
	return json.dumps(response)
	
@app.get('/survey/ABINITIO')
def survey1():
	return     

@app.get('/')
def restServiceHome():
	return template('rest_service_home')


if __name__ == "__main__" :
	app.run(host='localhost', port=8080, debug="True")


# def handleExcept(e):
# 	errorObject = ErrorObject()
# 	response = HttpResponse()
# 	if e instance of NotFound:
# 		response.setStatusCode = "404"
# 	else:
# 		response.setStatusCode = "500"

# 	errorObject.setMessage(e.getMessage())
# 	response.setBody(errorObject)

