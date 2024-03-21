from graph import Vertex, Graph
import string
import random
import re
import os

def get_words_from_text(text_path):
    """Get all the words from a text file."""
    with open(text_path, 'r') as file:
        # open file
        text = file.read()

        # get words & remove whitespace
        text = ' '.join(text.split())

        # lowercase
        text = text.lower()

        # remove punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def get_words_from_song(song_path):
    """Get all the words from a song file."""
    with open(song_path, 'r') as file:
        # open file
        text = file.read()

        # remove [verse 1: artist]
        text = re.sub(r'\[(.+)\]', ' ', text)

        # get words & remove whitespace
        text = ' '.join(text.split())

        # lowercase
        text = text.lower()

        # remove punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def make_graph(words):
    """Create a Markov chain graph from the given words."""
    graph = Graph()
    # previous_word is a Vertex
    previous_word = None

    for word in words:
        # check if word is in the graph, and if not then add it
        word_vertex = graph.get_vertex(word)
        # if there was a previous word, then add an edge
        # if edge does not exist, add an edge; if does exist, add 1
        if previous_word:
            # check if edge exists from previous word to current word
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex
    
    graph.generate_probability_mappings()
    return graph

def compose(graph, words, length = 50):
    """Compose the result text from the given graph.
    graph       Graph       a Markov chain graph generated from the text
    words       []          a list of words taken from the text
    length      int         the desired length of the result (default 50)
    """
    composition = []
    # choose a starting word
    word = graph.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = graph.get_next_word(word)

    return composition

def text_main(text, text_length):
    # 1. get words from text
    words = get_words_from_text(f'GRAPH_COMPOSER/texts/{text}')

    # 2. make a graph using those words
    text_graph = make_graph(words)

    # 3. get the next word for x number of words
    composition = compose(text_graph, words, text_length)

    # 4. show result
    print(f'Text is from: {text}')
    print(' '.join(composition))
    print()

def song_main(artist, song_length):
    # 1. get words from song
    words = []
    for song_file in os.listdir(f'GRAPH_COMPOSER/songs/{artist}'):
        song_words = get_words_from_song(f'GRAPH_COMPOSER/songs/{artist}/{song_file}')
        words.extend(song_words)

    # 2. make a graph using those words
    text_graph = make_graph(words)

    # 3. get the next word for x number of words
    composition = compose(text_graph, words, song_length)

    # 4. show result
    print(f"Artist: {artist}")
    print(' '.join(composition))
    print()

if __name__ == '__main__':
    text_main('hp_sorcerer_stone.txt', 100)
    song_main('avicii', 100)