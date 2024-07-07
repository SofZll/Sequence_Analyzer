import pandas as pd
import os

class FastaReader:
    @staticmethod
    def check_fasta(filename):
        _, extension = os.path.splitext(filename)
        if extension not in [".fasta", ".fna", ".fa"]:
            return False
        path = os.path.abspath(filename)
        bases = ["A", "C", "G", "T"]
        with open(path, "r") as file:
            if file.readlines()[0][0] != ">":
                return False
            for line in file.readlines()[1:]:
                for base in line:
                    if base not in bases:
                        return False
        return True


    @staticmethod
    def scanfile(filename):
        path = os.path.join("fasta_file/", filename)
        if FastaReader.check_fasta(path):
            with open(path, "r") as file:
                nt = ""  # String of all the nucleotides
                for line in file.readlines()[1:]:
                    nt += line
            nt = nt.replace('\n', '')
            nt_series = pd.Series(list(nt))
            return nt_series
        else:
            raise TypeError("File is not a FASTA file")
    

