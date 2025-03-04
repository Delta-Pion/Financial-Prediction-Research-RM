# Use this C:\Users\Aditya\AppData\Roaming\uv\tools\aider-chat\Scripts\python.exe 
from dotenv import load_dotenv
from aider.coders import Coder
from aider.models import Model

load_dotenv("E:\Artifical Intelligence\Research\Finance Research\.env")
# This is a list of files to add to the chat
fnames = ["greeting.py"]

model = Model("openrouter/google/gemini-2.0-flash-001")

# Create a coder object
coder = Coder.create(main_model=model, edit_format="ask")

# This will execute one instruction on those files and then return
# coder.run("make a script that prints hello world")

# # Send another instruction
# coder.run("make it say goodbye")
coder.run("I am just testing to see if I am able to run you through python script, can you tell me what chat history you are using and its path")
# coder.run(r'''/add "E:\Artifical Intelligence\Research\Finance Research\Custom_Rag_Setup\test scripts\chroma_testing.py"''')
# You can run in-chat "/" commands too
