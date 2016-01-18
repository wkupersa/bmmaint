#!/usr/bin/env python

import json
import sys
import getopt

class BookMarkFile(object):


    def __init__(self, filename):
        self.bm_file = None
        self.log_file = sys.stderr

        print filename
        try:
            self.bm_file=open(filename,"r")

        except Exception as e:
            self.log_file.write("Can't open bookmark file %s\n" % str(e))
            sys.exit(-1)

        for line in  self.bm_file:
            print line


def usage():
    usage = """
    -f, --filename\tfilename of bookmark file
    -h, --help\t\tthis help information
    """
    print usage
    sys.exit(0)

def main(argv):
    
    try:
        options, args = getopt.getopt(argv,"f:h", ["filename=","help"])
    except getopt.GetoptError as e:
            sys.stderr.write("Option not recognized %s\n" % str(e))
            usage()
            
    for o,a in options:
        if o in ("-f", "--filename"):
            filename = a
        if o in ("-h", "--help"):
            usage()
        
    bmf = BookMarkFile(filename)    
    

    
            
if __name__  == "__main__":
    main(sys.argv[1:])
        
