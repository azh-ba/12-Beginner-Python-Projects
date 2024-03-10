from sample_madlibs import hp, hungergames, zombie, code
import random

if __name__ == '__main__':
    m = random.choice([hp, code, hungergames, zombie])
    m.madlib()