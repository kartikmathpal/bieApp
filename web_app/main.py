from bottle import Bottle, template, static_file, request

app = Bottle()

@app.route('/')
def index():
  # return template('main', {})
  # print(request.query["domain"])
  return static_file('main.html', root='./')

@app.route('/static/<filepath:path>')
def server_static(filepath):
	print(filepath)
	return static_file(filepath, root='web_app/static/')

if __name__ == "__main__":
  app.run(host='localhost', port=8080, debug="True")
