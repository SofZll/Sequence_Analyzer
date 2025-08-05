# Sequence Analyzer

A DNA sequence analyzer of FASTA file.

*Programming team project - University of Bologna (Bachelor Genomics, a.y. 2023-2024)*


<div style="display: flex; justify-content: center; flex-wrap: wrap;">
  <img src="doc/img/HomePage.png" alt="Homepage screenshot" width="350" />
</div>
<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
  <img src="doc/img/TranslationTranscriptionPage.png" alt="Transcription and Translation page screenshot" width="350" /> 
  <img src="doc/img/AminoacidChainsPage.png" alt="Aminoacid Chains page screenshot" width="350" /> 
</div>


## Contributors

- Sofia Zanelli: [@SofZll](https://github.com/SofZll)
- Christian Guernelli: [@Jupiter929](https://github.com/Jupiter929)
- Giulia Mengoni: [@GiuliaMengoni](https://github.com/GiuliaMengoni)
- Nicolas Schiappa: [@NickSapphire](https://github.com/NickSapphire)

## Description

Web App that given a FASTA file is able to:
- parse the FASTA file and generates the trancription of a DNA sequence,
- show stats and frequency of nitrogenous bases,
- generates the DNA translations and show the obtained tRNA,
- allows amino acid chaining, and protein identification

## Input
The input consists of the complete genome sequence previously saved in the directory *"./fasta_file"*.
The alowed FASTA file extension are: *.fasta*, *.fna*, and *.fa*.

## Stack
<!-- Frontend -->
<p>
  <img src="https://img.shields.io/badge/Frontend-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-264de4?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
</p>

<!-- Backend -->
<p>
  <img src="https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
</p>

## to Run the Code
```bash
python3 Sequence_Analyzer.py
```
