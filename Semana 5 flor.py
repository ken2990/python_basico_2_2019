# https://github.com/PythonClassRoom/PythonClassBook/wiki/Python-Class:-use-case.-Flowers-and-roses

# Misc classes

class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__

    # Define lemma class
class lemma(misc):
    def __init__(self):
        self.color = None

# Define pedicel class
class pedicel(misc):
    def __init__(self):
        self.color = None

# Define stigma class
class stigma(misc):
    def __init__(self):
        self.color = None

# Define filament class
class filament(misc):
    def __init__(self):
        self.color = None

# Define simple flower class
class flower(misc):
    def __init__(self, n_lemma=1, n_stigmas=1, n_filaments=1):
        self.n_lemma = n_lemma
        self.lemmas = [lemma() for i in range(self.n_lemma)]
        self.pedicel = pedicel()
        self.n_stigmas = n_stigmas
        self.stigmas = [stigma() for i in range(self.n_stigmas)]
        self.n_filaments = n_filaments
        self.filaments = [filament() for i in range(self.n_filaments)]

    def grow(self):
        print(f'The {self.__str__()} is growning')

    def dead(self):
        print(f'The {self.__str__()} was gone')

    def __add__(self, other):
        # In case of addition, create a self's like class instance
        a_flower = self.__class__()
        # Compose list of lemmas based on their sources, self and other objects
        a_flower.lemmas = self.lemmas[::2] + other.lemmas[1::2]
        a_flower.n_lemma = len(a_flower.lemmas)
        # filaments and stigmas as self has.
        a_flower.filaments = self.filaments
        a_flower.stigmas = self.stigmas
        return a_flower

class rose(flower):

    def __init__(self, lemma_color='red',
                 stigma_color='green',
                 filament_color ='yellow',
                 n_lemma=1, n_stigmas=1, n_filaments=1):
        super().__init__(n_lemma, n_stigmas, n_filaments)
        for lemma in self.lemmas:
            lemma.color = lemma_color

        for stigma in self.stigmas:
            stigma.color = stigma_color

        for filament in self.filaments:
            filament.color = filament_color

my_rose_orange = rose('orange',n_lemma=6)
my_rose_blue = rose('blue',n_lemma=6)

hibrid_rose = my_rose_blue + my_rose_orange




