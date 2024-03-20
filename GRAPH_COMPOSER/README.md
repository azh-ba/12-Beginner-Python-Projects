**GRAPH_COMPOSER**

A **Markov chain** is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. Informally, this may be thought of as, "What happens next depends only on the state of affairs *now*." A countably infinite sequence, in which the chain moves state at discrete time steps, gives a discrete-time Markov chain (DTMC). A continous-time process is called a continuous-time Markov chain (CTMC). It is named after the Russian mathematician Andrey Markov. [Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)

This is a project which uses Markov chain to show the relationships between words in song lyrics, hence generating new lyrics from the graph.

> `compose.py`: Main file contains functions to generate words from the Markov chain model.

> `graph.py`: Contains definitions for the Vertex and Graph.

> *songs* and *texts* are folders contains lyrics and texts for feeding into the Markov chain model.