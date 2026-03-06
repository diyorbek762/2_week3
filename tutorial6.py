class MovieQueue:
    def __init__(self):
        self.movies_lst = []

    def add(self, movie):
        self.movies_lst.append(movie)
    
    def __str__(self):
        return f"MovieQueue: {len(self.movies_lst)} movies"
    
    def __getitem__(self, key):
        return self.movies_lst[key]
    

q = MovieQueue()
q.add("Inception")
q.add("Interstellar")
q.add("The Matrix")
print(q[0])
print(q[2])
print(q)