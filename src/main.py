from pdf_tools import extract_pdf_to_md
from txt_tools import split_text_to_sentences


def pdf_to_json(filepath):
    extract_pdf_to_md(filepath)
    split_text_to_sentences()

def main():
    pass


if __name__ == "__main__":
    main()