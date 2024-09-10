import pymupdf
import pymupdf4llm
import os
import pathlib


def extract_pdf_to_txt(input_filepath):
    """
    This method is less effective than converting .pdf -> .md. Recommend using the extract_pdf_to_md() method first for cleaner results.
    
    :param input_filepath: str
    """
    doc = pymupdf.open(input_filepath)
    output_filepath = os.path.splitext(input_filepath)[0] + ".txt"
    out = open(output_filepath, "wb")
    
    for page in doc:
        text = page.get_text().encode("utf8")
        out.write(text)
        out.write(bytes((12,)))
        
    out.close()


def extract_pdf_to_md(input_filepath: str) -> str:
    """
    Extract .pdf file contents into .md format using pymupdf4llm's to_markdown method. Markdown is often used in llm training and fine-tuning with parsers built into most chat interfaces. Returns the output filepath with .md extension for pipeline continuance (if needed)

    :returns output_filepath: str
    """
    doc = pymupdf.open(input_filepath)
    output_filepath = os.path.splitext(input_filepath)[0] + ".md"
    md_text = pymupdf4llm.to_markdown(doc)
    pathlib.Path(output_filepath).write_bytes(md_text.encode())
    
    return output_filepath
