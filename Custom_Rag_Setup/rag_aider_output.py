from dotenv import load_dotenv
from aider.coders import Coder
from aider.models import Model
import sys

load_dotenv(r"E:\Artifical Intelligence\Research\Finance Research\.env")
model = Model("openrouter/google/gemini-2.0-flash-001")
coder = Coder.create(main_model=model, edit_format="ask")

args = sys.argv[1:]
query = " ".join(args)

print(f"Starting Aider with query: {query}")

# Adding context file to aider context because this model is a fresh one we don't have history either
coder.run(r'''/add "E:\Artifical Intelligence\Research\Finance Research\Custom_Rag_Setup\rag_context.md"''')

coder.run(f"I want you to answer this : {query} with respect to the context and your own knowledge base")