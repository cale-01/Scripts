from PyPDF2 import PdfMerger

def merge_pdfs(input_paths, output_path):
    merger = PdfMerger()

    for path in input_paths:
        merger.append(path)

    merger.write(output_path)
    merger.close()

# Example usage
input_files = [r"path\file.pdf", r"path\file2.pdf"]  # Use raw string literals (r"") or escape backslashes (\\)
output_file = "merged.pdf"

merge_pdfs(input_files, output_file)
