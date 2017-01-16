import sys
import ABINITIO_dao
import BIE_dao

#collections
COLLECTIONS = {
    'BIE': 'BIE',
    'ABINITIO': 'ABINITIO'
}

def searchByKey(key, collection):

    if collection == COLLECTIONS['BIE']:
        return BIE_dao.searchByKey(key)
    elif collection == COLLECTIONS['ABINITIO']:
        return ABINITIO_dao.searchByKey(key)
    else:
        raise Exception("Collection Does Not Exist.")
    


################################################################################
if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchByKey(sys.argv[1])
    else:
        print "Enter a value!!"
