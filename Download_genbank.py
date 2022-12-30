#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Email       :   h2624366594@163.com
@Author      :   Fuchuan Han 
@Time        :   2022/12/29 16:26:15
"""

from Bio import Entrez
import argparse
import os

# Set the email address to use for Entrez queries
Entrez.email = "h2624366594@163.com"


def Argparse():
    '''
    Adding parameters
    '''
    parser = argparse.ArgumentParser(description='Obtain fasta and pep from genbank')
    parser.add_argument('-i', '--ids', help='Please input the id file', type=str, required=True)
    return parser.parse_args()


def Get_gb(numb):

    # Search for the GenBank record using its identifier
    handle = Entrez.efetch(db="nucleotide", id=numb, rettype="gb", retmode="text")

    # Gb_path = os.path.join(os.getcwd(), '%s'%numb)
    # Open a file to write the GenBank record to
    with open(os.getcwd()+"/"+numb+".gb", "w") as out_file:
        # Write the GenBank record to the file
        out_file.write(handle.read())

    # Close the handle
    handle.close()


if __name__ == "__main__":
    args = Argparse()

    with open(args.ids, 'r') as input_id:
        for numb in input_id:
            numb = numb.strip()
            # Try to download the GenBank file
            try:
                Get_gb(numb)
                print("{} had download".format(numb))
            # Catch any errors that may occur    
            except Exception as e:
                # Print an error message
                print("Error: {}".format(e))