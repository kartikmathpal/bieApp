from bottle   import Bottle, request, template
from services import search_service
import json

app = Bottle()

@app.get('/survey')
def survey():
    key = request.query["key"]
    print key
    response  = search_service.searchByKey(key)
    print response
    return json.dumps(response)

@app.get('/')
def restServiceHome():
	return template('rest_service_home')


if __name__ == "__main__" :
	app.run(host='localhost', port=8080, debug="True")
