import re
from nltk import sent_tokenize, word_tokenize
import json
import os


def split_text_to_paragraphs(filepath: str) -> list:
    """
    Splits the text from a file into paragraphs, using double newlines as the delimiter and outputs to json file.
    
    :param filepath: Path to the .txt file to be split
    :return: paragraphs | json file
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    output_filepath = os.path.splitext(filepath)[0] + ".json"

    paragraphs = []
    buffer = []
    pattern = re.compile(r"^\s*\d+(\.\d+)?")

    for line in text.splitlines():
        if line.strip():  # Line is not empty
            buffer.append(line.strip())
        elif buffer:  # Encountered a blank line and buffer has content
            paragraphs.append(" ".join(buffer))
            buffer = []

    # Append the last buffered paragraph if there's no trailing newline
    if buffer:
        next_line_index = text.splitlines().index(line) + 1
        if next_line_index < len(text.splitlines()):
            next_line = text.splitlines()[next_line_index]
            if pattern.match(next_line.strip()):
                buffer.append("")  # Maintain the blank line within the paragraph

        paragraphs.append(" ".join(buffer))
        buffer = []

    with open(output_filepath, 'w', encoding='utf-8') as json_file:
        json.dump(paragraphs, json_file, ensure_ascii=False, indent=4)
    


def split_text_to_sentences(filepath: str):
    """
    Splits text into sentences using NLTK's sent_tokenize. Outputs to a new json file.

    :param filepath: str, text source
    :param json_output: str, preferred filepath for json output
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    output_filepath = os.path.splitext(filepath)[0] + ".json"

    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Save the sentences into a JSON file
    with open(output_filepath, 'w', encoding='utf-8') as json_file:
        json.dump(sentences, json_file, ensure_ascii=False, indent=4)

    return output_filepath



split_text_to_sentences("data/pdfs/poweron-cd-renew.md")