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

## Stack
<!-- Frontend -->
<p>
  <span style="background-color: #555; color: white; padding: 5px 10px; border-radius: 5px;">Frontend</span>
  <span style="background-color: #e34c26; color: white; padding: 5px 10px; border-radius: 5px;">HTML</span>
  <span style="background-color: #264de4; color: white; padding: 5px 10px; border-radius: 5px;">CSS</span>
  <span style="background-color: #f0db4f; color: black; padding: 5px 10px; border-radius: 5px;">JavaScript</span>
</p>

<!-- Backend -->
<p>
  <span style="background-color: #555; color: white; padding: 5px 10px; border-radius: 5px;">Backend</span>
  <span style="background-color: #3776AB; color: white; padding: 5px 10px; border-radius: 5px;">Python</span>
  <span style="background-color: #000000; color: white; padding: 5px 10px; border-radius: 5px;">Flask</span>
</p>

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




## to Run the Code
```bash
python3 Sequence_Analyzer.py
```
