# cli_client.py
# This script provides a command-line interface (CLI) client for interacting with an MCP server.

import asyncio  # For asynchronous operations
import argparse # For parsing command-line arguments
import json     # For working with JSON data (for passing arguments to tools)
from mcp import ClientSession, StdioServerParameters  # MCP client components
from mcp.client.stdio import stdio_client # For communicating with the server via standard input/output

# Define an asynchronous function to call a tool on the MCP server
async def call_tool(server_command, tool_name, arguments):
    # Configure the server parameters.  This tells the client how to start the server.
    server_params = StdioServerParameters(
        command="python",  # The command to execute (Python interpreter)
        args=[server_command],  # The arguments to pass to the command (the server script)
    )

    # Establish a connection to the server using stdio.
    # The 'async with' statement ensures that the connection is properly closed when finished.
    async with stdio_client(server_params) as (read, write):
        # Create a client session to manage communication with the server.
        async with ClientSession(read, write) as session:
            # Initialize the session.  This must be done before calling any tools.
            await session.initialize()

            try:
                # Call the specified tool with the given arguments.
                result = await session.call_tool(tool_name, arguments=arguments)
                return result  # Return the result from the tool
            except Exception as e:
                return f"Error: {e}"  # If an error occurs, return an error message

# Define the main asynchronous function
async def main():
    # Create an argument parser to handle command-line arguments
    parser = argparse.ArgumentParser(description="MCP CLI Client")

    # Add the 'server_command' argument: the command to start the MCP server (e.g., my_server.py)
    parser.add_argument("server_command", help="The command to start the MCP server (e.g., my_server.py)")

    # Add the 'tool_name' argument: the name of the tool to call
    parser.add_argument("tool_name", help="The name of the tool to call")

    # Add the '--arguments' argument: a JSON string of arguments to pass to the tool
    # It defaults to an empty JSON object ({}) if no arguments are provided.
    parser.add_argument(
        "--arguments",
        help="JSON string of arguments to pass to the tool",
        default="{}",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Try to parse the arguments as a JSON object
    print(f"Raw arguments: {args.arguments}")
    try:
        arguments = json.loads(args.arguments)
    except json.JSONDecodeError:
        print("Error: Invalid JSON for arguments.")  # Print an error message if the JSON is invalid
        return  # Exit the program

    # Call the tool and get the result
    result = await call_tool(args.server_command, args.tool_name, arguments)

    # Print the result as a formatted JSON string
    print(json.dumps(result, indent=2))

# Entry point of the script
if __name__ == "__main__":
    # Run the main asynchronous function
    asyncio.run(main())
