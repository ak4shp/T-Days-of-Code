class Team:
    def __init__(self, rank, conf, name):
        self.rank = rank
        self.conf = conf
        self.name = name
        

class Tournament:
    def __init__(self, teams:list, details:dict):
        self.teams = teams
        self.details = details
        
    def count_teams(tmnt):  #First tournament object from list
        res = {}
        for a_team in tmnt.teams:
            cnf = a_team.conf
            if cnf not in res.keys():
                res[cnf] = 1
            else:
                res[cnf] += 1
        return res


def get_matching_hosts(times:int , all_tmnt:list):
    hosts = {}
    for a_tmnt in all_tmnt:
        if a_tmnt.details["Time"] == times:
            for a_tm in a_tmnt.teams:
                hosts[a_tm.name] = a_tm.rank

    ans_hosts = dict( sorted(hosts.items(), key = lambda x: x[1], reverse =False))
    return ans_hosts if len(ans_hosts) > 0 else None


# main
tournaments = []

t = int(input())
for i in range(t):
    teams = []
    
    n = int(input())
    for _ in range(n):
        rank = int(input())
        conf = input()
        name = input()
        
        a_team = Team(rank, conf, name)
        teams.append(a_team)
    det = {}
    det["Name"] = input()
    det["Host"] = input()
    det["Edition"] = int(input())
    det["Year"] = int(input())
    det["Participants"] = int(input())
    det["Time"] = int(input())
    
    a_tmnt = Tournament(teams, det)
    
    #print conf count of first tournament
    if i == 0:
        team_conf = Tournament.count_teams(a_tmnt)
        for k, v in team_conf.items():
            print(k, "-", v)
            
    tournaments.append(a_tmnt)
    
    
    
times = int(input())
match_hosts = get_matching_hosts(times, tournaments)

if match_hosts is not None:
    for k in match_hosts.keys():
        print(k)
else:
    print("No Team Found")
