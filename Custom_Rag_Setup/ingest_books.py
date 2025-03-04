#!/usr/bin/env python3
"""
Book Ingestion Script for RAG Database

This script processes text files containing books and stores them in the ChromaDB vector database
for later retrieval using the RAG system.

Usage:
    python ingest_books.py --files path/to/book.txt [path/to/another/book.txt ...]
    python ingest_books.py --directory path/to/books/folder
"""

import os
import sys
import argparse
from pathlib import Path
from tqdm import tqdm

from rag_handler import VectorStorage
from chunking import clean_text, chunk_text

def process_book(file_path):
    """
    Process a single book file and store its chunks in the vector database.
    
    Args:
        file_path (str): Path to the book text file
    
    Returns:
        int: Number of chunks stored
    """
    print(f"Processing book: {os.path.basename(file_path)}")
    
    # Read the book content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with a different encoding if utf-8 fails
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
            return 0
    
    # Clean the text
    cleaned_content = clean_text(content)
    
    # Extract book metadata
    book_name = os.path.basename(file_path)
    book_path = os.path.abspath(file_path)
    
    # Create metadata for each chunk
    metadata = {
        "source": book_name,
        "path": book_path,
        "type": "book"
    }
    
    # Chunk the text
    chunks = chunk_text(cleaned_content)
    print(f"Created {len(chunks)} chunks from {book_name}")
    
    # Initialize vector storage
    vs = VectorStorage()
    
    # Store chunks with metadata
    # Create a list of metadata dictionaries, one for each chunk
    metadata_list = [metadata.copy() for _ in chunks]
    
    # Add chunk index to metadata
    for i, meta in enumerate(metadata_list):
        meta["chunk_index"] = i
    
    # Store chunks with progress bar
    with tqdm(total=len(chunks), desc="Storing chunks") as pbar:
        # Store chunks in smaller batches to avoid memory issues
        batch_size = 50
        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i+batch_size]
            batch_metadata = metadata_list[i:i+batch_size]
            vs.store_chunks(batch_chunks, batch_metadata)
            pbar.update(len(batch_chunks))
    
    print(f"Successfully stored {len(chunks)} chunks from {book_name}")
    return len(chunks)

def main():
    """
    Main function to parse arguments and process books.
    """
    parser = argparse.ArgumentParser(description="Ingest books into the RAG database")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--files", nargs="+", help="Paths to book files")
    group.add_argument("--directory", help="Path to directory containing book files")
    
    args = parser.parse_args()
    
    # Get list of files to process
    files_to_process = []
    
    if args.files:
        files_to_process = args.files
    elif args.directory:
        dir_path = Path(args.directory)
        if not dir_path.exists() or not dir_path.is_dir():
            print(f"Error: {args.directory} is not a valid directory")
            return
        
        # Get all .txt files in the directory
        files_to_process = [str(f) for f in dir_path.glob("*.txt")]
        
        if not files_to_process:
            print(f"No .txt files found in {args.directory}")
            return
    
    # Process each book
    total_chunks = 0
    successful_books = 0
    
    print(f"Found {len(files_to_process)} books to process")
    
    for file_path in files_to_process:
        try:
            chunks_stored = process_book(file_path)
            if chunks_stored > 0:
                successful_books += 1
                total_chunks += chunks_stored
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    print(f"\nIngestion complete!")
    print(f"Successfully processed {successful_books}/{len(files_to_process)} books")
    print(f"Total chunks stored: {total_chunks}")
    print("\nYou can now query your books using the RAG system.")

if __name__ == "__main__":
    main()
