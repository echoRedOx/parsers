from pdf_tools import extract_pdf_to_md
from txt_tools import split_text_to_sentences
import sys


def pdf_to_json():
    """
    Imports extraction and sentence parser form included modules. CLI entry point "pdf_to_json"
    """
    filepath = sys.argv[1]
    md_filepath = extract_pdf_to_md(filepath)
    json_filepath = split_text_to_sentences(md_filepath)
    
    return json_filepath


def main():
    pass


if __name__ == "__main__":
    main()