'''
from pypdf import PdfWriter  # Use the modern pypdf library

def merge_pdfs():
    merger = PdfWriter()
    
    try:
        n = int(input("How many PDFs do you want to merge? \n"))
        if n < 2:
            print("You need at least 2 files to merge.")
            return

        for i in range(n):
            file_path = input(f"Enter the name of PDF #{i+1} (include .pdf): ")
            try:
                # Appending the file to the merger object
                merger.append(file_path)
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' was not found. Skipping.")

        # Using a context manager to write the file safely
        output_filename = "merged-pdf.pdf"
        with open(output_filename, "wb") as output_file:
            merger.write(output_file)
            
        print(f"Success! Files merged into {output_filename}")

    except ValueError:
        print("Invalid input. Please enter a number.")
    finally:
        merger.close()

if __name__ == "__main__":
    merge_pdfs()
    
'''
from pypdf import PdfWriter
#from Pypdf2 import PdfWriter  # Use the modern pypdf library
merger = PdfWriter()

pdfs = []
n = int(input("How many PDFs do you want to merge? \n"))

for i in range(0,n):
    name = input(f"Enter the name of PDF {i+1}: ")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)
    
merger.write("mered-pdf.pdf")
merger.close()
