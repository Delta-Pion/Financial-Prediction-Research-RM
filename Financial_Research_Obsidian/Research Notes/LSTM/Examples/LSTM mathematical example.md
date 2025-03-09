## LSTM Mathematical Example

Alright, let's walk through a simplified example of an LSTM cell calculation with some hypothetical values. I'll keep the vector dimensions small for clarity. It is based on the equations given in [[LSTM Basic Mathematical Model]].

**Assumptions:**

- Input vector `x_t` is a 2-dimensional vector.
- Hidden state `h_t` is a 2-dimensional vector.
- Cell state `C_t` is a 2-dimensional vector.
- We'll use randomly chosen weights and biases for demonstration. In a real-world scenario, these would be learned during training.
- We'll use the NumPy library for calculations.

## Complete Code:

``` python 
 import numpy as np

 # Input at time t
 x_t = np.array([0.5, -0.2])

 # Previous hidden state
 h_t_1 = np.array([0.1, 0.3])

 # Previous cell state
 C_t_1 = np.array([0.4, -0.1])

 # Forget gate weights and bias
 W_f = np.array([[0.2, -0.1, 0.3, 0.0],
                 [0.1, 0.2, -0.1, 0.1]])  # Shape: (2, 4)
 b_f = np.array([0.1, -0.2])  # Shape: (2,)
 
 # Input gate weights and bias
 W_i = np.array([[0.3, 0.1, -0.2, 0.1],
                 [-0.1, 0.3, 0.1, -0.2]])  # Shape: (2, 4)
 b_i = np.array([-0.1, 0.2])  # Shape: (2,)

 # Candidate cell state weights and bias
 W_C = np.array([[0.1, -0.2, 0.1, 0.3],
                 [0.2, 0.1, 0.3, -0.1]])  # Shape: (2, 4)
 b_C = np.array([0.2, 0.1])  # Shape: (2,)

 W_o = np.array([[-0.2, 0.1, 0.1, 0.2],
                 [0.1, 0.3, -0.2, 0.1]])  # Shape: (2, 4)
 b_o = np.array([0.0, -0.1])  # Shape: (2,)

 def sigmoid(x):
     return 1 / (1 + np.exp(-x))

 def tanh(x):
     return np.tanh(x)

 # Concatenate h_t_1 and x_t
 concat = np.concatenate([h_t_1, x_t])  # Shape: (4,)

 # Calculate the forget gate activation
 f_t = sigmoid(np.dot(W_f, concat) + b_f)  # Shape: (2,)
 print("Forget Gate (f_t):", f_t)

 # Calculate the input gate activation
 i_t = sigmoid(np.dot(W_i, concat) + b_i)  # Shape: (2,)
 print("Input Gate (i_t):", i_t)

 # Calculate the candidate cell state
 C_tilde_t = tanh(np.dot(W_C, concat) + b_C)  # Shape: (2,)
 print("Candidate Cell State (C_tilde_t):", C_tilde_t)

 # Update the cell state
 C_t = f_t * C_t_1 + i_t * C_tilde_t  # Shape: (2,)
 print("Cell State (C_t):", C_t)

 # Calculate the output gate activation
 o_t = sigmoid(np.dot(W_o, concat) + b_o)  # Shape: (2,)
 print("Output Gate (o_t):", o_t)

 # Calculate the hidden state
 h_t = o_t * tanh(C_t)  # Shape: (2,)
 print("Hidden State (h_t):", h_t)

```

### Explanation:

 1. We start with an input x_t, a previous hidden state h_t_1, and a previous cell state C_t_1.
 2. We concatenate h_t_1 and x_t to create a single input vector for the gates.
 3. We calculate the forget gate f_t, input gate i_t, and candidate cell state C_tilde_t using their respective weight matrices, biases, and activation functions.
 4. We update the cell state C_t by combining the previous cell state with the candidate cell state, weighted by the forget and input gates.
 5. We calculate the output gate o_t.
 6. Finally, we calculate the hidden state h_t by applying the tanh function to the updated cell state and multiplying it by the output gate.

### Important Notes:

 - This is a very simplified example. Real-world LSTMs often have much larger input and hidden state dimensions.
 - The weights and biases in a real LSTM are learned during training using backpropagation through time.
 - This example only shows the calculation for a single time step. A complete LSTM network would process a sequence of inputs over multiple time steps.

If you run this code, you'll see the values of each gate, the cell state, and the hidden state after each calculation. This should give you a more concrete understanding of 
how the LSTM cell works mathematically.

>[!note] Why is the weight vector of shape (2,4)
>Shape of concat:  Since h_t_1 has a shape of (2,) and x_t has a shape of (2,), the resulting concat vector has a shape of (4,).
>
>Weight Matrix Multiplication: The weight matrices (e.g., W_f, W_i, W_C, W_o) are then multiplied by this concat vector.  To produce an output of shape (2,) (which is the 
   desired shape for the gates and cell state in this example), the weight matrices must have a shape of (2, 4). 
   >>[!warning]
   >If the weight matrices were only (2,2) then they could only operate on either the input or the hidden state, and not both together.
   
## What does concat do?
Mathematically, *concat* (short for concatenate) combines two or more vectors (or matrices, or tensors in general) into a single, larger vector (or matrix, or tensor). It     
essentially "stacks" the input vectors end-to-end.

Let's illustrate with the example from the LSTM code:

We have two vectors:

 - h_t_1 = [a, b]  (shape: (2,))
 - x_t = [c, d]  (shape: (2,))

Where a, b, c, and d are numerical values.

The concatenation concat = np.concatenate([h_t_1, x_t]) results in a new vector:

 • concat = [a, b, c, d] (shape: (4,))

In more general terms:

If you have vectors  v1, v2, ..., vn with shapes (d1,), (d2,), ..., (dn,) respectively, then concatenating them results in a vector v with shape (d1 + d2 + ... + dn,). The  
elements of v are simply the elements of v1, v2, ..., vn placed one after another in that order.

## Code Example using pytorch : [[LSTM pytorch example]]

   



