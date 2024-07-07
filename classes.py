from pandas import *
import matplotlib
matplotlib.use('Agg')  # problem with matplotlib UI, only works with this for me (Nick)
import matplotlib.pyplot as plt
import base64
from io import BytesIO
#import requests


class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)
    
    def __del__(self):
        return 0

class DNA(Sequence):

    def __init__(self, sequence):
        super().__init__(sequence)

    def view_statistics(self):
        dic_nucleotides = {}
        for i, j in self.sequence.value_counts().items():
            dic_nucleotides[i] = j
            
        statistics = {
            'freq': dic_nucleotides,
            'Count': self.sequence.count(),
            'MaxFreqValue': self.sequence.value_counts().idxmax(),
            'MinFreqValue': self.sequence.value_counts().idxmin()
        }
        
        return statistics
        
    def transcription(self):
        trs = self.sequence.replace("T", "U")
        return trs

    def get_complement(self):  
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
        return ''.join([complement[base] for base in self.sequence])

    def bar_chart(self, xlabel, ylabel, title):
        fig, ax = plt.subplots()
        ax.bar(self.sequence.value_counts().index, self.sequence.value_counts(),
               color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], width=0.5)
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)

        # Ottieni i dati dell'immagine come base64 senza salvarla
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return img_base64

    def pie_chart(self, title):
        fig, ax = plt.subplots()
        ax.pie(self.sequence.value_counts(), labels=self.sequence.value_counts().index, autopct='%1.1f%%')
        ax.set(title=title)

        # Ottieni i dati dell'immagine come base64 senza salvarla
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return img_base64


class mRNA(Sequence):
    codon = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L',
             'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 'AUC': 'I',
             'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
             'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
             'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T',
             'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
             'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H',
             'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
             'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
             'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CGU': 'R',
             'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S',
             'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
             'GGG': 'G'}

    def __init__(self, sequence):
        super().__init__(sequence)

    @staticmethod
    def convert_codon(codon: Series) -> str:
        out = ""
        for base in codon:
            out += base
        return out

    def find_ORFs(self):
        start_codon = ['A', 'U', 'G']
        stop_codons = ["UAA", "UGA", "UAG"]
        orfs = []
        seq_array = self.sequence.values.tolist()
        i = 0
        while i < len(seq_array):
            if seq_array[i:i+3] == start_codon:
                orf = ['AUG']
                i += 3
                codon = self.convert_codon(seq_array[i:i + 3])
                valid_codon = True
                while codon not in stop_codons:
                    orf.append(codon)
                    i += 3
                    codon = self.convert_codon(seq_array[i:i + 3])
                    if i > len(seq_array):
                        valid_codon = False
                        break
                if valid_codon:
                    orf.append(codon)
                    orfs.append(orf)
            i += 1
        return orfs
    
    def translation(self):
        aa = []
        ORFs = self.find_ORFs()
        for i in range(len(ORFs)):
            prov = []
            for j in ORFs[i]:
                if j in self.codon.keys():
                    prov.append(self.codon[j])
            aa.append(prov)
        return aa

#TODO: subclass one o the other
class Protein(Sequence):
    list_protein = []
    count = 0

    def __init__(self, sequence):
        super().__init__(sequence)
        Protein.count += 1 
        name = "Protein " + str(Protein.count)
        self.name = name
        self.list_protein.append(self)

    def get_sequence(self):
        return ''.join(self.sequence)
    
    def get_name(self):
        return self.name
    
    @staticmethod
    def empty_queue():
        for protein in Protein.list_protein:
            del protein
        Protein.count = 0
        Protein.list_protein = []

    @staticmethod
    def get_list_protein():
        return Protein.list_protein

    @staticmethod
    def show_proteins(ascending=False):
        return sorted(Protein.list_protein, key=len, reverse=ascending)


class OligoPeptide(Sequence):
    list_oligo = []
    count = 0

    def __init__(self, sequence):
        super().__init__(sequence)
        OligoPeptide.count += 1
        name = "OligoPeptide " + str(OligoPeptide.count)
        self.name = name
        self.list_oligo.append(self)

    def get_sequence(self):
        return ''.join(self.sequence)
    
    def get_name(self):
        return self.name
    
    @staticmethod
    def empty_queue():
        for oligo in OligoPeptide.list_oligo:
            del oligo
        OligoPeptide.count = 0
        OligoPeptide.list_oligo = []

    @staticmethod
    def get_list_oligo():
        return OligoPeptide.list_oligo       

    @staticmethod
    def show_oligos(ascending=False):
        return sorted(OligoPeptide.list_oligo, key=len, reverse=ascending)
    

