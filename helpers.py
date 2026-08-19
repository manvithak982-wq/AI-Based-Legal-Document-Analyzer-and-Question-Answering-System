import os
import hashlib
from datetime import datetime



# ---------------------------------------
# File Utilities
# ---------------------------------------

def get_file_extension(filename):

    return os.path.splitext(
        filename
    )[1].lower()



def is_pdf(filename):

    return get_file_extension(filename) == ".pdf"





def file_size(filepath):

    if os.path.exists(filepath):

        return os.path.getsize(filepath)

    return 0





# ---------------------------------------
# Text Utilities
# ---------------------------------------

def clean_filename(filename):

    characters = [
        " ",
        "/",
        "\\",
        ":",
        "*",
        "?",
        "\"",
        "<",
        ">",
        "|"
    ]


    for char in characters:

        filename = filename.replace(
            char,
            "_"
        )


    return filename





def count_words(text):

    if not text:

        return 0


    return len(
        text.split()
    )





def shorten_text(
    text,
    length=200
):


    if len(text) <= length:

        return text


    return text[:length] + "..."





# ---------------------------------------
# Security Utilities
# ---------------------------------------

def generate_hash(text):


    return hashlib.sha256(

        text.encode()

    ).hexdigest()





# ---------------------------------------
# Date Utilities
# ---------------------------------------

def current_time():


    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )





# ---------------------------------------
# Folder Utilities
# ---------------------------------------

def create_folder(path):


    if not os.path.exists(path):

        os.makedirs(path)



# ---------------------------------------
# Document Statistics
# ---------------------------------------

def document_statistics(pages):


    total_words = 0


    for page in pages:


        total_words += count_words(

            page.get(
                "text",
                ""
            )

        )


    return {


        "pages":len(pages),


        "words":total_words


    }





if __name__ == "__main__":


    print(
        "Helper utilities ready"
    )