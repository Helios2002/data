class Movie:
    def __init__(self, name, year, director, box):
        self.name = str(name)
        self.year = int(year)
        self.director = str(director)
        self.box = list(box)
        
    def is_earlier_than(self, other_movie):
        return self.year < other_movie.year
        
    def box_office(self):
        accu = 0
        for data in self.box:
            accu += int(data)
        result = '$%d millions'%accu
        return result
        
frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200])
lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])
print(frozen.year) # 2013
print(frozen.box) # [1000, 200]
print(frozen.box_office()) # $1200 millions
print(frozen.is_earlier_than(lionKing)) # False