from src.pdf_tools import extract_pdf_to_md
from src.txt_tools import split_text_to_sentences
import sys
from time import time


def pdf_to_json():
    """
    Imports extraction and sentence parser form included modules. CLI entry point "pdf_to_json path/to/your/file.pdf"
    """
    filepath = sys.argv[1]
    md_filepath = extract_pdf_to_md(filepath)
    json_filepath = split_text_to_sentences(md_filepath)
    
    return json_filepath


def remove_blank_lines(md_filepath):
    with open(md_filepath, 'r') as f:
        lines = f.readlines()

    cleaned_lines = [line for line in lines if line.strip()]
    with open(md_filepath, 'w') as f:
        f.writelines(cleaned_lines)
    

def main(pdf_filepath):
    md_filepath = extract_pdf_to_md(pdf_filepath)
    remove_blank_lines(md_filepath)


if __name__ == "__main__":
    pdf_filepath = sys.argv[1]
    start = time()
    main(pdf_filepath)
    end = time()
    duration = end - start
    print(f"Extraction completed in {duration} seconds.")