# Use this C:\Users\Aditya\AppData\Roaming\uv\tools\aider-chat\Scripts\python.exe 
from dotenv import load_dotenv
from aider.coders import Coder
from aider.models import Model

load_dotenv()
# This is a list of files to add to the chat
fnames = ["greeting.py"]

model = Model("openrouter/google/gemini-2.0-flash-001")

# Create a coder object
coder = Coder.create(main_model=model)

# This will execute one instruction on those files and then return
# coder.run("make a script that prints hello world")

# # Send another instruction
# coder.run("make it say goodbye")

coder.run("hello wassup")

# You can run in-chat "/" commands too
coder.run("/tokens")

