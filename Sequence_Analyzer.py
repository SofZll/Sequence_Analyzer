from FASTA_Reader import *
from classes import *
from flask import Flask, render_template, request
import os

# Flask code goes here
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/submit', methods=['POST'])
def handle_form():
    action = request.form.get('action')
    file = request.form.get('file')

    if action == 'dna_mrna':
        with app.test_request_context('/analysis.html', method='POST', data={'file': file}):
            return analysis()
    elif action == 'aa_chain':
        with app.test_request_context('/aa_analysis.html', method='POST', data={'name_file': file}):
            return aa_analysis()


def enqueue(list_aaChain):
    for aaChain in list_aaChain:
        if len(aaChain) > 20:
            Protein(aaChain)
        else:
            OligoPeptide(aaChain)

def empty_queue():
    Protein.empty_queue()
    OligoPeptide.empty_queue()

                               
def analysis_request(file, requested_analysis):
    if not os.path.exists(f"fasta_file/{file}"):
        return render_template("homepage.html", message="File not found in fasta_file directory")
    else:
        while True:
            try:
                seq = FastaReader.scanfile(file)
                break
            except TypeError:
                return render_template("homepage.html", message="Not a .fasta/.fna/.fa file")
        
        seq_str = ''.join(seq.values.tolist())
        dna = DNA(seq)
        rna = ''.join(DNA.transcription(dna).values.tolist())

        if requested_analysis == "DNA":
            pie_chart = dna.pie_chart("DNA Sequence pie chart")
            bar_chart = dna.bar_chart("Nucleotide", "Count", "DNA Sequence bar chart")
            statistics = dna.view_statistics()
            
            return render_template("analysis.html", file=file, sequence=seq_str, mrna=rna, pie_chart=pie_chart,
                                bar_chart=bar_chart, max=statistics['MaxFreqValue'], min=statistics['MinFreqValue'],
                                count=statistics['Count'], freq=statistics['freq'])
        
        elif requested_analysis == "AA":
            mrna = mRNA(dna.transcription())
            chain_list = mrna.translation()
            empty_queue()
            enqueue(chain_list)
            oligos_ascending = OligoPeptide.show_oligos(ascending=True)
            oligos_descending = OligoPeptide.show_oligos()
            oligos_list = OligoPeptide.get_list_oligo()
            proteins_ascending = Protein.show_proteins(ascending=True)
            proteins_descending = Protein.show_proteins()
            proteins_list = Protein.get_list_protein()
            name_file = file
            return render_template("aa_analysis.html", file=name_file, mRna=rna, oligos_ascending=oligos_ascending,
                                   oligos_descending=oligos_descending, oligos_list=oligos_list, proteins_ascending=proteins_ascending,
                                   proteins_descending=proteins_descending, proteins_list=proteins_list)
        
        else:
            return render_template("homepage.html", message="Invalid analysis request")


@app.route('/analysis.html', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        file = request.form.get('file')
        return analysis_request(file, "DNA")


@app.route('/aa_analysis.html', methods=['POST'])
def aa_analysis():
    if request.method == 'POST':
        name_file = request.form.get('name_file')
        return analysis_request(name_file, "AA")


if __name__ == "__main__":
    app.run(debug=True)
