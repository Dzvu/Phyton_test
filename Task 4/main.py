# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.
#
# Savybės:
# title: string
# director: string
# budget: number
#
# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        return self.budget > 100000000


movie1 = Movie("Jurassic Park", "Steven Spielberg", 63000000)
movie2 = Movie("The Shawshank Redemption", "Frank Darabont", 25000000)

print(movie1.was_expensive())
print(movie2.was_expensive())
