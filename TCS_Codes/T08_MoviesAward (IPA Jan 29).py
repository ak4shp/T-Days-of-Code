class MovieInfo:
    def __init__(self, title:str, year:int, awards:int, nominations:int, country:str):
        self.title = title
        self.year = year
        self.awards = awards
        self.nominations = nominations
        self.country = country
        
        
class Award:
    def __init__(self, mv:list):
        self.mv_objs = mv
        
    #def set_movie_info(self, mv):
     #   self.mv_objs.append(mv)
        
    def get_non_american(self, year:int):
        ans = []
        for a_mv in self.mv_objs:
            if a_mv.year == year:
                if a_mv.country.lower() != "america":
                    ans.append(a_mv)
        return ans if len(ans) > 0 else None
    
    def sort_movies_success_rate(self):
        success_movies = {}
        
        for a_mv in self.mv_objs:
            name = a_mv.title
            awd = a_mv.awards
            nomi = a_mv.nominations
            succ_rate = int((awd/nomi)*100)
            success_movies[name] = succ_rate
            
        sorted_movies = dict(sorted(success_movies.items(), key = lambda x: x[1], reverse =True))
        return sorted_movies if len(sorted_movies) > 0 else None
                    
                    
# main
n = int(input())
movies = []
for _ in range(n):
    t = input()
    y = int(input())
    aw = int(input())
    nm = int(input())
    c = input()
    
    mv_info = MovieInfo(t, y, aw, nm, c)
    movies.append(mv_info)

award = Award(movies)

compare_year = int(input())
non_american_mv = award.get_non_american(compare_year)
sorted_succ_mv = award.sort_movies_success_rate()


if non_american_mv is not None:
    for mv in non_american_mv:
        print(mv.title)
        print(mv.year)
        print(mv.awards)
        print(mv.nominations)
        print(mv.country)
else:
    print("No Movie found")
    
    
if sorted_succ_mv is not None:
    for k, v in sorted_succ_mv.items():
        print(k, v)
else:
    print("Unable to create dictionary")
        