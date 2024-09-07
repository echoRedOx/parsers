from nltk import sent_tokenize, word_tokenize
import json


def chunk_text(filepath: str, max_chunk_size: int, overlap_size: int, output_path: str) -> None:
    """
    Do not use. Have not validated outputs.

    :param filepath: Source of text
    :param max_chunk_size: Number of tokens per chunk
    :param overlap_size: Overlap
    :param output_path: Filepath for json output.
    """
    with open(filepath
    , 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        tokenized_content = word_tokenize(sentence)
        word_count = len(tokenized_content)

        if current_word_count + word_count > max_chunk_size:
            chunks.append(' '.join(current_chunk))
            start_overlap = max(0, len(current_chunk) - overlap_size)
            current_chunk = current_chunk[start_overlap:]
            current_word_count = len(word_tokenize(' '.join(current_chunk)))

        current_chunk.append(sentence)
        current_word_count += word_count

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(chunks, json_file, indent=4)

    print(f"Saved chunks to {output_path}")


def json_to_chunks(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print(data)

