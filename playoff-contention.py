import pandas
import operator


class team(object):
	def __init__(self, name, division, conference):
		self.id = id
		self.name = name
		self.division = division
		self.conference = conference
		self.wins = 0
		self.games_played = 0
		self.eliminateDate = None



class game(object):
	def __init__(self, date, home, away, home_score, away_score, winner):
		self.date = date
		self.home = home
		self.away = away
		self.home_score = home_score
		self.away_score = away_score
		self.winner = winner

class partial(object):
	def __init__(self, name, best_poss, worst_poss):
		self.name = name
		self.best_poss = best_poss
		self.worst_poss = worst_poss

	def __cmp__(self, other):
		return cmp(self.best_poss, other.best_poss)

df = pandas.read_excel('teams.xlsx')
FORMAT = ['Team_Name','Division_id','Conference_id']
df_selected = df[FORMAT]
teams = {}
for index, row in df.iterrows():
	newTeam = team(row['Team_Name'],row['Division_id'],row['Conference_id'])
	teams[row['Team_Name']] = newTeam

df = pandas.read_excel('results.xlsx')
FORMAT = ['Date','Home Team','Away Team', 'Home Score', 'Away Score', 'Winner']
df_selected = df[FORMAT]
games = []
for index, row in df.iterrows():
	newGame = game(row['Date'], row['Home Team'], row['Away Team'], row['Home Score'], row['Away Score'], row['Winner'])
	games.append(newGame)


current_date = games[0].date
for game in games:
	if game.date != current_date:
		#check here if the last day eliminated anyone
		west = []
		east = []
		for key,value in sorted(teams.items()):
			best_poss = (teams[key].wins + 82 - teams[key].games_played)/82.0
			worst_poss = (teams[key].wins)/82.0
			if teams[key].conference == "East":
				east.append(partial(key,best_poss,worst_poss))
			else:
				west.append(partial(key,best_poss,worst_poss))
		westBest = sorted(west, key=lambda x: x.best_poss, reverse=True)
		westWorst = sorted(west, key=lambda x: x.worst_poss, reverse=True)
		eastBest = sorted(east, key=lambda x: x.best_poss, reverse=True)
		eastWorst = sorted(east, key=lambda x: x.worst_poss, reverse=True)
		westCut = westWorst[7].worst_poss
		eastCut = eastWorst[7].worst_poss

		for teamPartial in east:
			if teams[teamPartial.name].eliminateDate == None and teamPartial.best_poss < eastCut:
				teams[teamPartial.name].eliminateDate = current_date

		for teamPartial in west:
			if teams[teamPartial.name].eliminateDate == None and teamPartial.best_poss < westCut:
				teams[teamPartial.name].eliminateDate = current_date

		current_date = game.date
	
	
	if game.winner == 'Home':
		teams[game.home].wins += 1
	else:
		teams[game.away].wins += 1
	teams[game.away].games_played += 1
	teams[game.home].games_played += 1

for key,value in sorted(teams.items()):
	print key, str(teams[key].wins) + '-' + str(teams[key].games_played - teams[key].wins), teams[key].eliminateDate


