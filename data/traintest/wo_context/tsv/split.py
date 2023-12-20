

"""
RUN
---
python split.py aspell_big.tsv
python split.py aspell_small.tsv
python split.py combined_data.tsv
python split.py homophones.tsv
"""

import os
import sys

if __name__=="__main__":

	READ_FILE = sys.argv[1]
	WRITE_FILE_PATH = ".".join( READ_FILE.split(".")[:-1] )

	clean_data = []
	corrupt_data = []

	opfile = open(READ_FILE,"r")
	for line in opfile:
		words = line.strip().split("\t")
		corrupt_data.append(words[0].strip())
		clean_data.append(words[1].strip())
	opfile.close()

	opfile = open(WRITE_FILE_PATH,"w")
	for line in clean_data[:-1]:
		opfile.write("{}\n".format(line))
	opfile.write("{}".format(clean_data[-1]))
	opfile.close()

	opfile = open(WRITE_FILE_PATH+".noise","w")
	for line in corrupt_data[:-1]:
		opfile.write("{}\n".format(line))
	opfile.write("{}".format(corrupt_data[-1]))
	opfile.close()

