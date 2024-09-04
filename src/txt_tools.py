import re


def split_text_into_paragraphs(file_path: str) -> list:
    """
    Splits the text from a file into paragraphs, using double newlines as the delimiter.
    
    :param file_path: Path to the .txt file to be split
    :return: List of paragraphs
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

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

    return paragraphs



