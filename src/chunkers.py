from nltk import sent_tokenize, word_tokenize
import json
import sys
import os


def chunk_sentences(filepath: str, chunk_size: int, overlap_size: int) -> None:
    """
    Do not use. Have not validated outputs.

    :param filepath: Source of text
    :param max_chunk_size: Number of tokens per chunk
    :param overlap_size: Overlap
    :param output_path: Filepath for json output.
    """
    output_path = os.path.splitext(filepath)[0] + ".json"

    with open(filepath
    , 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)

    chunks = []
    current_chunk = []
    chunk_counter = 0

    for sentence in sentences[:1000]:
        tokenized_content = word_tokenize(sentence)
        sent_counter = len(tokenized_content)

        if chunk_counter + sent_counter > chunk_size:
            chunks.append(' '.join(current_chunk))
            start_overlap = max(0, (chunk_counter - overlap_size))
            current_chunk = current_chunk[start_overlap:]
            chunk_counter = overlap

        current_chunk.append(sentence)
        chunk_counter += sent_counter
        sent_counter = 0

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(chunks, json_file, indent=4)

    print(f"Saved chunks to {output_path}")


def main(filepath: str, chunk_size: int, overlap_size: int):
    chunk_sentences(filepath, chunk_size, overlap_size)
    

if __name__ == "__main__":
    source = sys.argv[1]
    chunk_size = int(sys.argv[2])
    overlap = int(sys.argv[3])
    main(source, chunk_size, overlap)