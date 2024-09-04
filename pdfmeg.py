import PyPDF2
import sys
inputs = sys.argv[1:]
def pdf_como(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdfs in pdf_list:
        merger.append(pdfs)
    merger.write('super.pdf')
pdf_como(inputs)
