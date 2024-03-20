import string
from graph import Vertex, Graph
import random
import re
import os

def get_words_from_text(text_path):
    with open(text_path, 'rb') as f:
        text = f.read().decode("utf-8")

        # remove [text in the box]
        text = re.sub(r'\[(.+)\]', '', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = words[:1000]
    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:
        # check if word is in the graph, if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if it does not already exist in the graph
        # otherwise, increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)
        
        # set the word to the previous word and iterate
        previous_word = word_vertex

    # generate the probability mappings before composing
    g.generate_probability_mappings()

    return g

def compose(g, words, length = 50):
    composition = []
    # choose a random word to start
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    # get words from text
    # words = get_words_from_text('GRAPH_COMPOSER/texts/hp_sorcerer_stone.txt')

    # get words from song
    words = []
    for song_file in os.listdir(f'GRAPH_COMPOSER/songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'GRAPH_COMPOSER/songs/{artist}/{song_file}')
        words.extend(song_words)

    # make a graph using those words
    g = make_graph(words)

    # get the next word for x number of words (defined by user)
    composition = compose(g, words, 100)

    # show the result
    return ' '.join(composition)

if __name__ == '__main__':
    print(main('taylor_swift'))