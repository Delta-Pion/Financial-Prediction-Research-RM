## LSTM Basic Mathematical Model

Alright, let's break down the mathematical model of an [[LSTM]]. I'll use standard notation to represent the different components.

**Notation:**

*   `x_t`: Input vector at time step `t`
*   `h_t`: Hidden state vector at time step `t`
*   `C_t`: Cell state vector at time step `t`
*   `W`: Weight matrices (e.g., `W_f`, `W_i`, `W_C`, `W_o`)
*   `b`: Bias vectors (e.g., `b_f`, `b_i`, `b_C`, `b_o`)
*   `σ`: Sigmoid activation function
*   `tanh`: Hyperbolic tangent activation function

**LSTM Equations:**

The LSTM cell operates through a series of equations that govern the flow of information. Here's a step-by-step breakdown:

1.  **Forget Gate (f_t):**

    *   `f_t = σ(W_f * [h_{t-1}, x_t] + b_f)`

    *   This gate determines how much of the previous cell state `C_{t-1}` to forget.
    *   `W_f` is the weight matrix for the forget gate.
    *   `[h_{t-1}, x_t]` represents the concatenation of the previous hidden state `h_{t-1}` and the current input `x_t`.
    *   `b_f` is the bias vector for the forget gate.
    *   `σ` (sigmoid) squashes the output to a range between 0 and 1.  A value close to 0 means "forget," and a value close to 1 means "remember."

2.  **Input Gate (i_t):**

    *   `i_t = σ(W_i * [h_{t-1}, x_t] + b_i)`

    *   This gate determines which values from the new candidate values to update in the cell state.
    *   `W_i` is the weight matrix for the input gate.
    *   `b_i` is the bias vector for the input gate.
    *   `σ` (sigmoid) squashes the output to a range between 0 and 1.

3.  **Candidate Cell State (C̃_t):**

    *   `C̃_t = tanh(W_C * [h_{t-1}, x_t] + b_C)`

    *   This creates a vector of new candidate values that could be added to the cell state.
    *   `W_C` is the weight matrix for the candidate cell state.
    *   `b_C` is the bias vector for the candidate cell state.
    *   `tanh` squashes the output to a range between -1 and 1.

4.  **Update Cell State (C_t):**

    *   `C_t = f_t * C_{t-1} + i_t * C̃_t`

    *   This updates the cell state by forgetting some of the old information (controlled by `f_t`) and adding some of the new information (controlled by `i_t` and `C̃_t`).

5.  **Output Gate (o_t):**

    *   `o_t = σ(W_o * [h_{t-1}, x_t] + b_o)`

    *   This gate determines what parts of the cell state to output.
    *   `W_o` is the weight matrix for the output gate.
    *   `b_o` is the bias vector for the output gate.
    *   `σ` (sigmoid) squashes the output to a range between 0 and 1.

6.  **Hidden State (h_t):**

    *   `h_t = o_t * tanh(C_t)`

    *   This is the output of the LSTM cell, which is also passed to the next time step.
    *   The cell state is put through `tanh` (squashing it between -1 and 1) and then multiplied by the output of the output gate.

**In Summary:**

*   The LSTM cell receives an input `x_t` and the previous hidden state `h_{t-1}`.
*   The forget gate decides what to forget from the previous cell state `C_{t-1}`.
*   The input gate decides what new information to add to the cell state.
*   The cell state is updated by combining the forgotten information and the new information.
*   The output gate decides what to output based on the updated cell state.
*   The hidden state `h_t` is the output of the LSTM cell and is passed to the next time step.

These equations describe the core operations of a single LSTM cell.  A complete LSTM network consists of multiple LSTM cells arranged in a sequence, allowing the network to process sequential data over time. The weights (`W`) and biases (`b`) are learned during the training process using optimization algorithms like backpropagation through time.

The example for these equations is [[LSTM mathematical example|here]]]
