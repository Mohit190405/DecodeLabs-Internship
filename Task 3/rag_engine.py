try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
   
    print("langchain_text_splitters module not found. Please install it using 'pip install langchain_text_splitters'.")

def split_document(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks