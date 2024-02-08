# Stanford-NLP-CS224n
Collection of coding assignments and written solutions for Stanford NLP class  
[Link](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/) to the course  
Thoughts:  
hw1 - Introduction to NLP word embedding. Notebook is pretty self-explanatory.  
hw2 - Implementation of naive softmax loss and gradient and negative sampling loss and gradient, then SkipGram. Follow the handout, hand calculating the losses and gradients was not hard and is really helpful clarifying the model design. A little more thinking and patience are required in implementing in code assignment in vectorized fashion. Always do dimension check. In my final SkipGram model, loss was brought down to ~9.9 after 45k SGD iters. m2pro chip is much faster comparing to 10th gen i9! Fun! 
