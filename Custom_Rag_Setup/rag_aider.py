#!/usr/bin/env python3
"""
RAG-Enhanced Aider Wrapper

This script enhances Aider with Retrieval-Augmented Generation (RAG) capabilities.
It intercepts queries, retrieves relevant context using the VectorStorage class,
updates a context file that's part of Aider's working set, and then passes
the original query to Aider.

Usage:
    python rag_aider.py "your query here"
    python rag_aider.py /command  # Passes Aider commands through directly
"""

import sys
import os
import subprocess
import time
from rag_handler import VectorStorage

# Configuration
CONTEXT_FILE = r"E:\Artifical Intelligence\Research\Finance Research\Custom_Rag_Setup\rag_context.md"  # File that will be added to Aider's working set
AIDER_PATH = r"C:\Users\Aditya\.local\bin\aider.exe"  # Path to Aider executable (modify if needed)
MAX_CONTEXT_CHUNKS = 8  # Maximum number of context chunks to include

def update_context_file(query, context_chunks):
    """
    Update the context file with new RAG results.
    
    Args:
        query (str): The user's original query
        context_chunks (list): List of text chunks retrieved as context
    """
    # Format the header with timestamp for freshness indication
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    content = f"""# RAG Context (Updated: {timestamp})

## Query
{query}

## Retrieved Context
"""
    
    # Add each context chunk with a header for readability
    for i, chunk in enumerate(context_chunks[:MAX_CONTEXT_CHUNKS], 1):
        content += f"\n### Context Chunk {i}\n{chunk}\n"
    
    # Add a footer with usage instructions
    content += """
---
*This context is automatically updated based on your queries. 
Aider will consider this information when responding.*
"""
    
    # Write the formatted content to the context file
    with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"+ Updated {CONTEXT_FILE} with {len(context_chunks[:MAX_CONTEXT_CHUNKS])} context chunks for: {query}")

def check_context_file_exists():
    """
    Ensure the context file exists, create it if it doesn't.
    Returns True if the file already existed, False if it was created.
    """
    if not os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
            f.write("""# RAG Context

This file contains automatically retrieved context for your queries.

Context will appear here when you use the RAG-enhanced query system.
""")
        print(f"Created {CONTEXT_FILE} - make sure to add it to Aider with '/add {CONTEXT_FILE}'")
        return False
    return True

def main():
    """
    Main function that processes arguments and orchestrates the RAG-enhanced Aider workflow.
    """
    # Check if the context file exists
    file_existed = check_context_file_exists()
    
    # Get command line arguments
    args = sys.argv[1:]
    
    if not args:
        # No arguments provided, show usage information
        print("RAG-Enhanced Aider")
        print("Usage:")
        print("  python rag_aider.py \"your query here\"")
        print("  python rag_aider.py /command  # Passes Aider commands through directly")
        
        # If the context file was just created, suggest adding it to Aider
        if not file_existed:
            print("\nImportant: Start Aider and add the context file:")
            print(f"  aider")
            print(f"  /add {CONTEXT_FILE}")
        
        return
    
    # Check if this is an Aider command (starts with /)
    if args[0].startswith('/'):
        # Just pass through to Aider if it's a command
        # print(f"Passing command directly to Aider: {' '.join(args)}")
        # subprocess.run([AIDER_PATH] + args)
        print("We only accept queries")
        return
    
    # Otherwise, treat as a query that needs RAG enhancement
    query = " ".join(args)
    print(f"Processing query with RAG: {query}")
    
    try:
        # Initialize the vector storage
        print("Retrieving relevant context...")
        vs = VectorStorage()
        
        # Get relevant context
        context = vs.query_context(query, n_results=MAX_CONTEXT_CHUNKS)
        
        if not context:
            print("No relevant context found. Proceeding with Aider anyway.")
        else:
            # Update the context file with retrieved information
            update_context_file(query, context)
        
        # Now run Aider with the original query
        # The context file is already part of Aider's working set
        #print(f"Starting Aider with query: {query}")
        
        # subprocess.run([AIDER_PATH, query])
        print("Context Saved ")
        
    except Exception as e:
        print(f"Error during RAG processing: {str(e)}")
        print("Falling back to standard Aider...")
        # subprocess.run([AIDER_PATH] + args)

if __name__ == "__main__":
    main()
