# Average Frame

Produce one frame from a sequence of frames such that resulting
frame represents an average of a sequence.


### Algorithm

Algorithm can be expressed as

<img src="https://latex.codecogs.com/gif.latex?(\sum_{i=1}^{l}&space;X_i)&space;\;&space;/&space;\;&space;m" title="(\sum_{i=1}^{l} X_i) \; / \; l" />

Where, _l_ is a sequence length and

<img src="https://latex.codecogs.com/gif.latex?X_i&space;\in&space;\mathbb{R}^m^^&space;\times&space;\;&space;n" title="X_i \in \mathbb{R}^m^^ \times \; n" />


### Implementation

Sum up all matrices into one matrice and divide this matrix
by scalar _l_, where _l_ is count of the summed frames.
