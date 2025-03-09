# What Is LSTM

LSTMs are a special kind of recurrent neural network (RNN) architecture designed to handle the vanishing gradient problem that traditional RNNs face when dealing with long  
sequences of data. In simpler terms, they're good at remembering information from a long time ago, which is crucial for tasks where context matters over extended periods. 

>[!info]+ lstm
>Long Short-Term Memory (LSTM): LSTMs address the vanishing gradient problem by introducing a more sophisticated memory mechanism. Instead of a single hidden state, LSTMs have a "cell state" which acts as a long-term memory, and several "gates" that control the flow of information into and out of the cell state.

## Key Components of an LSTM Cell:

 1. Cell State (C_t):  This is the "memory" of the LSTM. It carries information across many time steps. Think of it as a conveyor belt that transports relevant information   
    throughout the sequence.
 2. Forget Gate (f_t): This gate decides what information to throw away from the cell state. It looks at the current input and the previous hidden state and outputs a number 
    between 0 and 1 for each number in the cell state. 0 means "completely forget this," and 1 means "completely keep this."
 3. Input Gate (i_t): This gate decides what new information to store in the cell state. It has two parts:
    -  A sigmoid layer that decides which values to update.
    -  A tanh layer that creates a vector of new candidate values that could be added to the cell state.
 4. Output Gate (o_t): This gate decides what information to output based on the cell state. It looks at the current input and the previous hidden state to determine what
    parts of the cell state to output. The cell state is put through a tanh layer and multiplied by the output of the output gate.







