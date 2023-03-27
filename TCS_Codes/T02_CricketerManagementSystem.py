class Cricketer:
    def __init__(self, cricketerId:int, matchesPlayed:int, totalRuns:int, cricketerName:str, team:str):
        self.cricketerId = cricketerId
        self.matchesPlayed = matchesPlayed
        self.totalRuns = totalRuns
        self.cricketerName = cricketerName
        self.team = team

    
class Solution: 
    def main(self):
        all_cricketers = []
        n = int(input())
        while n:
            n -= 1
            id = int(input())
            matches = int(input())
            runs = int(input())
            name = input()
            team = input()

            player = Cricketer(id, matches, runs, name, team)
            all_cricketers.append(player)

        find = int(input())
        min_match = Solution.findCricketerWithMinimumMatchesPlayed(all_cricketers)
        print(min_match.cricketerId)

        searched = Solution.searchCricketerById(all_cricketers, find)
        if searched == None:
            print("No Such Cricketer")
        else:
            print(searched.cricketerId)
            print(searched.cricketerName)


    def findCricketerWithMinimumMatchesPlayed(cricketers:list):
        min_match = float('inf')
        idx = 0
        for i, cric in enumerate(cricketers):
            match = cric.matchesPlayed
            if match <= min_match:
                min_match = match
                idx = i
        return cricketers[idx] 


    def searchCricketerById(cricketers:list, lookup:int):
        for i, cric in enumerate(cricketers):
            cric_id = cric.cricketerId
            if cric_id == lookup:
                return cricketers[i]
        return None


solution = Solution()
solution.main()



