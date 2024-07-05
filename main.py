#main.py
import DustParser
import sys

#main method and entry point of application

def main(argv):
    """Main method calling a single debugger for an input script"""
    parser = DustParser
    parser.parse(argv)

if __name__ == '__main__':
    main(sys.argv) 
