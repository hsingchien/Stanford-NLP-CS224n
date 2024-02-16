# Stanford-NLP-CS224n
Collection of coding assignments and written solutions for Stanford NLP class  
[Link](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/) to the course  
Thoughts:  
hw1 - Introduction to NLP word embedding. Notebook is pretty self-explanatory.  
hw2 - Implementation of naive softmax loss and gradient and negative sampling loss and gradient, then SkipGram. Follow the handout, hand calculating the losses and gradients was not hard and is really helpful clarifying the model design. A little more thinking and patience are required in implementing in code assignment in vectorized fashion. Always do dimension check. In my final SkipGram model, loss was brought down to ~9.9 after 45k SGD iters. m2pro chip is much faster comparing to 10th gen i9! Fun!  
hw3 - Implementation of the transition-based sentence parse with a simple neural network classifier. Replicating the results of [2014 Chen & Manning](https://nlp.stanford.edu/pubs/emnlp2014-depparser.pdf) using pytorch. Quite easy because the boilerplate code and frames are all done by the course. All I have to do was to fill in the parser transition operations and define weights/biases and implement NN forward etc. Eventually my NN achieved UAS of 88.9, met the expectation. A deeper network will probably provide a better result. 
