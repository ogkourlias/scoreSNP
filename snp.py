#!/usr/bin/env python3

"""
    usage:
        python3 snp.py .\POU5F1.aln
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "WIP"
__version__ = "0.1"

# IMPORTS
import sys
from Bio import AlignIO

# CLASSES
class aln_file():
    """ Creates object out of a provided ALN file. """
    def __init__(self, file):
        self.file = AlignIO.read(sys.argv[1], "fasta")

    def __str__(self):
        return self.file





# FUNCTIONS
def get_counts(file):
    """ Counts the SNP variations and stores them in a list. """
    pos_list = []
    for pos in range(0, len((file[1].seq))):
        snp_dict = {}
        for aa in range(0,len(file)):
            if file[aa, pos] == "-":
                break
            if file[aa, pos] not in snp_dict.keys():
                snp_dict[file[aa, pos]] = 1
            else:
                snp_dict[file[aa, pos]] += 1
        pos_list.append(snp_dict)
    return pos_list

def count_conflicts(pos_list):
    """ Detects whether amino acids are differing in class
     and returns countamount of said positions. """
    classi_conflict = 0

    for dict in pos_list:
        aa_clases = {
            "GAVLI": 0,
            "SCUTM": 0,
            "P": 0,
            "FYW": 0,
            "HKR": 0,
            "DENQ": 0
        }
        if len(dict) > 1:
            for aa in dict:
                for classi in aa_clases:
                    if aa in classi:
                        aa_clases[classi] = 1

            if sum(aa_clases.values()) > 1:
                classi_conflict += 1

    return classi_conflict

def rate_harm(conflict_count, file):
    """ Receives amount of amino acid class changes
    and determines a score based on a calculated percentage. """
    ratio = conflict_count / len(file[1].seq)

    return f"The MSA receives a conservation score of {round(10-ratio*10)}, " \
           f"because {round(ratio*100)}% of the sequence positions contain an AA class conflict."


# MAIN
def main(args):
    """ Main function. """
    file = AlignIO.read(sys.argv[1], "fasta")
    pos_list = get_counts(file)
    conflict_count = count_conflicts(pos_list)
    print(rate_harm(conflict_count, file))
    # FINISH
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
