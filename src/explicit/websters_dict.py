import re
import json

def process_websters_dictionary(file_path: str, output_file: str) -> None:
    """
    Processes the .txt file for Webster's Unabridged English Dictionary and saves it as a JSON file with custom token definitions. This is probably overboard and i know i can just chunk though it but my brain cannot allow me to no discriminately take apart the data yielding a super pretty JSONized webster's dictionary. I'm not sorry.

    :param file_path: Path to the .txt file for Webster's Unabridged English Dictionary
    :param output_file: Path to the output JSON file
    :return: None
    :usage:
        >>>parse_dictionary(dataset_path, output_path)
        >>>with open(output_path, 'r') as file:
        >>>data = json.load(file)

        >>>print(f"Number of entries in dataset: {len(data)}")
        >>>print(f"Example entry: {data[1]}")
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Regex pattern for entries (starts with all caps, excluding specific patterns)
    pattern = re.compile(r'\n\n(?=[A-Z][A-Z\s,.]*\n(?![0-9]|Defn))', re.MULTILINE)

    # Split text into entries
    records = pattern.split(text)

    entries = [
        {
            "word": "<|im_start|>",
            "definition": "see START-TOKEN",
            "content": "<|im_start|> is defined as: see START-TOKEN"
        },
        {
            "word": "START-TOKEN",
            "definition": "Start Token (also known as Beginning-of-Sequence Token)\nDefn: A Start Token is a special marker used in the field of natural language processing (NLP) and machine learning, particularly in the training and operation of large language models (LLMs). It signifies the beginning of a text sequence or input. In sequence modeling and generation tasks, a Start Token is used as an initial input to signal the model to begin processing or generating text. It acts as a standardized cue for the model to start formulating a response, prediction, or continuation of text.\nUsage: In training language models, the Start Token is prepended to each text example in the training dataset. This consistent practice enables the model to learn the token as a universal indicator that marks the commencement of a new sequence of text. During the model's inference phase, the Start Token is provided as the initial input, prompting the model to commence generating text that logically follows.\nPurpose: The primary purpose of the Start Token is to provide a clear and unambiguous signal to the model for the beginning of text generation tasks. It helps in delineating the start of a new sequence in cases where multiple sequences are processed in a batch or in a streaming manner. The Start Token is crucial for models that generate text autonomously, as it provides a standardized starting point for text generation.\nSyn: Beginning-of-Sequence Token, Start Marker, Sequence Initiation Token",
            "content": "START-TOKEN is defined as: Start Token (also known as Beginning-of-Sequence Token)\nDefn: A Start Token is a special marker used in the field of natural language processing (NLP) and machine learning, particularly in the training and operation of large language models (LLMs). It signifies the beginning of a text sequence or input. In sequence modeling and generation tasks, a Start Token is used as an initial input to signal the model to begin processing or generating text. It acts as a standardized cue for the model to start formulating a response, prediction, or continuation of text.\nUsage: In training language models, the Start Token is prepended to each text example in the training dataset. This consistent practice enables the model to learn the token as a universal indicator that marks the commencement of a new sequence of text. During the model's inference phase, the Start Token is provided as the initial input, prompting the model to commence generating text that logically follows.\nPurpose: The primary purpose of the Start Token is to provide a clear and unambiguous signal to the model for the beginning of text generation tasks. It helps in delineating the start of a new sequence in cases where multiple sequences are processed in a batch or in a streaming manner. The Start Token is crucial for models that generate text autonomously, as it provides a standardized starting point for text generation.\nSyn: Beginning-of-Sequence Token, Start Marker, Sequence Initiation Token"
        },
        {
            "word": "<|im_end|>",
            "definition": "see STOP-TOKEN",
            "content": "<|im_end|> is defined as: see STOP-TOKEN"
        },
        {
            "word": "STOP-TOKEN",
            "definition": "Stop Token (also known as End-of-Sequence Token)\nDefn: A Stop Token is a specialized marker used in natural language processing (NLP) and machine learning, particularly in the context of large language models (LLMs). It is employed to indicate the end of a text sequence or input. In tasks involving sequence modeling, generation, and processing, a Stop Token serves as a signal for the model to terminate its current text generation or processing task. This token is an essential component in controlling the output of language models, ensuring they produce coherent and appropriately bounded text sequences.\nUsage: During the training of language models, the Stop Token is appended to the end of each text example in the dataset. This consistent application teaches the model to recognize the token as a universal signal for concluding a text sequence. In the inference phase, the model generates text until it outputs the Stop Token, at which point it ceases further text generation.\nPurpose: The Stop Token's primary role is to provide a definitive and clear endpoint for generated text. This is crucial in applications where the length of output text needs to be dynamic yet bounded, such as in conversational AI, text summarization, or content generation tasks. The Stop Token helps prevent run-on generations, ensuring that the output is concise and relevant.\nSyn: End-of-Sequence Token, Termination Token, Sequence Termination Marker",
            "content": "STOP-TOKEN is defined as: Stop Token (also known as End-of-Sequence Token)\nDefn: A Stop Token is a specialized marker used in natural language processing (NLP) and machine learning, particularly in the context of large language models (LLMs). It is employed to indicate the end of a text sequence or input. In tasks involving sequence modeling, generation, and processing, a Stop Token serves as a signal for the model to terminate its current text generation or processing task. This token is an essential component in controlling the output of language models, ensuring they produce coherent and appropriately bounded text sequences.\nUsage: During the training of language models, the Stop Token is appended to the end of each text example in the dataset. This consistent application teaches the model to recognize the token as a universal signal for concluding a text sequence. In the inference phase, the model generates text until it outputs the Stop Token, at which point it ceases further text generation.\nPurpose: The Stop Token's primary role is to provide a definitive and clear endpoint for generated text. This is crucial in applications where the length of output text needs to be dynamic yet bounded, such as in conversational AI, text summarization, or content generation tasks. The Stop Token helps prevent run-on generations, ensuring that the output is concise and relevant.\nSyn: End-of-Sequence Token, Termination Token, Sequence Termination Marker"
        },
        {
            "word": "<|com_start|>",
            "definition": "see COMMAND-START-TOKEN",
            "content": "<|com_start|> is defined as: see COMMAND-START-TOKEN"
        },
        {
            "word": "COMMAND-START-TOKEN",
            "definition": "Command-Start-Token, n. Etym: [AI Command Processing, User-AI Interaction]\nDefn: A Command-Start-Token is a specialized marker used in advanced AI systems, particularly those involving interactive user interfaces and command-driven functionalities. It signifies the beginning of an explicit command directive within a user's input. This token is designed to isolate and prioritize command instructions from the rest of the textual input, ensuring that the AI system accurately recognizes and processes user commands.\nUsage: In user-AI interaction models, the Command-Start-Token is used to enclose the start of a command phrase or instruction. When the AI detects this token, it switches its focus to command processing mode, prioritizing the enclosed command over other contextual elements in the input. This ensures a direct and unambiguous interpretation of user commands, leading to precise execution of AI functionalities or library calls.",
            "content": "COMMAND-START-TOKEN is defined as: Command-Start-Token, n. Etym: [AI Command Processing, User-AI Interaction]\nDefn: A Command-Start-Token is a specialized marker used in advanced AI systems, particularly those involving interactive user interfaces and command-driven functionalities. It signifies the beginning of an explicit command directive within a user's input. This token is designed to isolate and prioritize command instructions from the rest of the textual input, ensuring that the AI system accurately recognizes and processes user commands.\nUsage: In user-AI interaction models, the Command-Start-Token is used to enclose the start of a command phrase or instruction. When the AI detects this token, it switches its focus to command processing mode, prioritizing the enclosed command over other contextual elements in the input. This ensures a direct and unambiguous interpretation of user commands, leading to precise execution of AI functionalities or library calls."
        },
        {
            "word": "<|com_end|>",
            "definition": "see COMMAND-STOP-TOKEN",
            "content": "<|com_end|> is defined as: see COMMAND-STOP-TOKEN"
        },
        {
            "word": "COMMAND-STOP-TOKEN",
            "definition": "Command-Stop-Token, n. Etym: [AI Command Processing, User-AI Interaction]\nDefn: A Command-Stop-Token is a specialized marker utilized in AI systems to indicate the end of an explicit command within a user's input. This token works in tandem with the Command-Start-Token to clearly define the bounds of a command phrase or instruction, facilitating accurate command processing by the AI.\nUsage: The Command-Stop-Token is appended to the end of a command sequence. Its presence signals the AI system that the command instruction has concluded, allowing the system to process the command and then return to its standard input processing mode. This token is critical in scenarios where commands are embedded within longer text passages, ensuring that only the intended portion of the text is executed as a command.\nPurpose: The primary role of the Command-Stop-Token is to establish a clear and precise endpoint for user commands within an AI interaction. This clarity is essential for the AI to effectively separate and execute command instructions from conversational or other types of input, thereby enhancing the system's responsiveness and reliability in fulfilling user commands.",
            "content": "COMMAND-STOP-TOKEN is defined as: Command-Stop-Token, n. Etym: [AI Command Processing, User-AI Interaction]\nDefn: A Command-Stop-Token is a specialized marker utilized in AI systems to indicate the end of an explicit command within a user's input. This token works in tandem with the Command-Start-Token to clearly define the bounds of a command phrase or instruction, facilitating accurate command processing by the AI.\nUsage: The Command-Stop-Token is appended to the end of a command sequence. Its presence signals the AI system that the command instruction has concluded, allowing the system to process the command and then return to its standard input processing mode. This token is critical in scenarios where commands are embedded within longer text passages, ensuring that only the intended portion of the text is executed as a command.\nPurpose: The primary role of the Command-Stop-Token is to establish a clear and precise endpoint for user commands within an AI interaction. This clarity is essential for the AI to effectively separate and execute command instructions from conversational or other types of input, thereby enhancing the system's responsiveness and reliability in fulfilling user commands."
        },
        {
            "word": "<|pad_tok|>",
            "definition": "see PAD-TOKEN",
            "content": "<|pad_tok|> is defined as: see PAD-TOKEN"
        },
        {
            "word": "PAD-TOKEN",
            "definition": "Pad-Token, n. Etym: [Natural Language Processing, AI Data Preparation]\nDefn: A Pad-Token is a unique placeholder used extensively in natural language processing tasks within AI systems, especially in the context of training machine learning models. It serves to equalize the length of text sequences, allowing for uniform processing across different inputs. This token is inserted into shorter text sequences to pad them to a predetermined length, which is necessary for certain types of neural network architectures that require fixed-length inputs.\nUsage: In tasks such as sentence classification or language translation, Pad-Tokens are added to the ends of shorter text segments to ensure they match the length of the longest segment within a dataset. This process allows for batch processing of data and maintains the structural integrity of neural network inputs. By using Pad-Tokens, AI models can efficiently handle varying lengths of textual data without compromising the accuracy of their processing or the integrity of their training.\nPurpose: The fundamental purpose of the Pad-Token is to facilitate the handling of linguistic data of varying lengths in a consistent manner within AI systems. It ensures that all text inputs conform to a standardized format, which is crucial for training and deploying efficient and effective machine learning models. This uniformity is particularly important in deep learning architectures like recurrent neural networks (RNNs) and transformers, where input length consistency is vital for model stability and performance.",
            "content": "PAD-TOKEN is defined as: Pad-Token (also known as <|pad_tok|> or Padding-Token), n. Etym: [Natural Language Processing, AI Data Preparation]\nDefn: A Pad-Token is a unique placeholder used extensively in natural language processing tasks within AI systems, especially in the context of training machine learning models. It serves to equalize the length of text sequences, allowing for uniform processing across different inputs. This token is inserted into shorter text sequences to pad them to a predetermined length, which is necessary for certain types of neural network architectures that require fixed-length inputs.\nUsage: In tasks such as sentence classification or language translation, Pad-Tokens are added to the ends of shorter text segments to ensure they match the length of the longest segment within a dataset. This process allows for batch processing of data and maintains the structural integrity of neural network inputs. By using Pad-Tokens, AI models can efficiently handle varying lengths of textual data without compromising the accuracy of their processing or the integrity of their training.\nPurpose: The fundamental purpose of the Pad-Token is to facilitate the handling of linguistic data of varying lengths in a consistent manner within AI systems. It ensures that all text inputs conform to a standardized format, which is crucial for training and deploying efficient and effective machine learning models. This uniformity is particularly important in deep learning architectures like recurrent neural networks (RNNs) and transformers, where input length consistency is vital for model stability and performance."
        },
    ]

    for record in records:
        lines = record.split('\n')
        word = lines[0].strip()

        definition = ' '.join(lines[1:]).strip()

        entries.append({'word': word, 'definition': definition, "content": f"{word} is defined as: {definition}"})
    
    # Saving to JSON file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(entries, out_file, ensure_ascii=False, indent=4)

    print(f'Dictionary parsed and saved to {output_file}')