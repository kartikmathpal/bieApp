#imports
import sys
import main_dao

def searchByKey(key):
    response = main_dao.searchByKey(key)
    print  response
    return response

if __name__ == '__main__':
    if len(sys.argv) > 1:
        searchByKey(sys.argv[1])
    else:
        print "Please provide search key as command line argument"
