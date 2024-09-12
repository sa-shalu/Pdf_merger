# Pdf_merger
Code Explanation: Merging PDF Files
Purpose:
This Python script merges multiple PDF files into a single output PDF.

Libraries:

PyPDF2: A library used for working with PDF documents.
# Breakdown:

# Import Necessary Libraries:
~~~ python
import PyPDF2
import sys
~~~

PyPDF2 is imported for PDF manipulation.
sys is imported to access command-line arguments.
Get Input PDF Files:

~~~python
inputs = sys.argv[1:]
~~~

# The script retrieves the PDF file paths provided as command-line arguments after the script name.
Define the pdf_combo Function:

~~~python
def pdf_combo(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdfs in pdf_list:
        merger.append(pdfs)
    merger.write('super.pdf')
~~~

This function takes a list of PDF file paths as input.
It creates a PdfMerger object from the PyPDF2 library.
Iterates through the list of PDF files and appends each one to the merger.
Finally, it writes the merged PDF to a file named super.pdf.
Call the pdf_combo Function:

~~~python
pdf_combo(inputs)
~~~

The pdf_combo function is called with the list of input PDF files obtained from command-line arguments.
# How to Use:

Save this code as a Python file (e.g., merge_pdfs.py).
Open your terminal or command prompt.
Navigate to the directory where you saved the script.
Run the script with the PDF file paths as arguments:
~~~bash
py merge_pdfs.py file1.pdf file2.pdf file3.pdf
~~~

Replace file1.pdf, file2.pdf, and file3.pdf with the actual paths to your PDF files.
Output:
A new PDF file named super.pdf will be created in the same directory, containing the merged content from all the input PDF files you can also give your n.
