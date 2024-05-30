import re
import json
import os
from collections import Counter
import random
import string


def def_word_cnt(input_text):
    # Remove all commas and periods from the text
    text = re.sub(r',|\.', '', input_text)
    
    # Split the text and count each word using Counter
    word_count = dict(Counter(text.split()))
    return word_count
    

# Function to generate 100 json files without using loop
def write_json_files(data, count=1, max_files=100):
    """
    Writes JSON files to disk based on the input data and file count.
    
    Parameters:
        data (dict): The dictionary containing the data to be written to the JSON files.
        count (int): The current file count, starting from 1.
        max_files (int): The maximum number of files to write.
    """
    # Check if the file count is greater than the maximum allowed
    if count > max_files:
        return
    
    # Generate a unique file name for each JSON file
    file_name = f"result_{count}.json"
    
    # Create a path to the JSON file using the current working directory and the generated file name
    file_path = os.path.join(os.getcwd(), "question_1", file_name)
    
    # Open the JSON file in write mode and dump the data into it
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
    write_json_files(data, count + 1, max_files)

# Test input_text
input_text = "hello world hello"
word_counts = def_word_cnt(input_text)
write_json_files(word_counts)