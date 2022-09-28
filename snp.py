#!/usr/bin/env python3

"""
    usage:
        python3 orfeas_gkourlias_deelopdracht01.py
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "WIP"
__version__ = "0.1"

# IMPORTS
import sys
import biopython

# CLASSES
class aln_file():
    """ Creates object out of a provided ALN file. """
    def __init__(self, file):
        self.file = open(file, "r")
        self.raw = self.file.read()

    def __str__(self):
        return self.raw




# FUNCTIONS
def y():
    """ Desc """
    return 0


# MAIN
def main(args):
    """ Main function """
    main_file = aln_file(sys.argv[1])
    print(main_file)
    # FINISH
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
