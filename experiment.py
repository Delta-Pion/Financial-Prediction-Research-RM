from chunking import clean_text, chunk_text
from rag_handler import VectorStorage

# Example document (replace with your actual content)
long_document = """The Nonnecessity of Marketing
Here is the biggest and most obvious difference between quantitative trading and other small businesses. Marketing is crucial to most small businessesafter all, you generate your revenue from other people, who base their purchase decisions on things other than price alone. In trading, your counterparties in the financial marketplace base their purchase decisions on nothing but the price. Unless you are managing money for other people (which is beyond the scope of this book), there is absolutely no marketing to do in a quantitative trading business. This may seem obvious and trivial but is actually an important difference, since the business of quantitative trading allows you to focus exclusively on your product (the strategy and the software), and not on anything that has to do with influencing other peoples perception of yourself. To many people, this may be the ultimate beauty of starting your own quantitative trading business.
THE WAY FORWARD

If you are convinced that you want to become a quantitative trader, a number of questions immediately follow: How do you find the right strategy to trade? How do you recognize a good versus a bad strategy even before devoting any time to backtesting them? How do you rigorously backtest them? If the backtest performance is good, what steps do you need to take to implement the strategy, in terms of both the business structure and the technological infrastructure? If the strategy is profitable in initial real-life trading, how does one scale up the capital to make it into a growing income stream while managing the inevitable (but, hopefully, only occasional) losses that come with trading? These nuts and bolts of quantitative trading will be tackled in Chapters 2 through 6.
   Though the list of processes to go through in order to get to the final destination of sustained and growing profitability may seem long and daunting, in reality it may be faster and easier than many other businesses. When I first started as an independent trader, it took me only three months to find and backtest my first new strategy, set up a new brokerage account with $100,000 capital, implement the execution system, and start trading the strategy. The strategy immediately became profitable in the first month. Back in the dot-com era, I started an Internet software firm. It took about 3 times more investment, 5 times more human-power, and 24 times longer to find out that the business model didnt work, whereupon all investors including myself lost 100 percent of their investments. Compared to that experience, it really has been a breeze trading quantitatively and profitably.
"""

# Initialize RAG system
vs = VectorStorage()

# Process document
cleaned = clean_text(long_document)
chunks = chunk_text(cleaned)
print(f"Chunked document into {len(chunks)} chunks")

# Store in vector DB
vs.store_chunks(chunks)

# Query example
query = "What are the main differences between quantitative trading and other businesses?"
context = vs.query_context(query)
print("\nRetrieved Context:")
print("\n".join(context))
