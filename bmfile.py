import json
import sys
import getopt

class BookMarkFile(object):


    def __init__(self, fileName):
        self.bm_file = None

        try:
            self.bm_file=open(fileName,"r")

        except Exception as e:
            print("Can't open bookmark file %s" % str(e), file=sys.stderr)
            sys.exit(-1)

        while bm_file:
            print _



def main():
    try:
        options, args = getopt.getopt(sys.argv[1:],"fh", ["file-name","help"])
    except getopt.GetoptError as e:
            print("Option not recognized %s" % str(e), file=sys.stderr)
            sys.exit(-1)

    for o,a in opts:
        print ("%s = %s" % (str(o),str(a)))
            


    
            
if __name__  == "__main__":
    main()
        
