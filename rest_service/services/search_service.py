#imports
import sys
import main_dao

def searchByKey(key, collection):

	#create a response
	# response = new HttpResponse()
	# status code
	# set body

	try:
		response = main_dao.searchByKey(key, collection)
	except Exception as e:
		print("invalid collection", e)
		response = []
	
	return response

if __name__ == '__main__':
    if len(sys.argv) > 1:
        searchByKey(sys.argv[1])
    else:
        print "Please provide search key as command line argument"
