import random 


def simulate(numSimulations, winPercentage):
	badSeasons = 0
	numberOfSimulations = numSimulations

	for x in range(numberOfSimulations):

		season = [random.uniform(0, 1) for x in range(82)]
		wins = []
		for game in season:
			if game > winPercentage:
				wins.append(False)
			else:
				wins.append(True)

		streak = True
		for result in wins:
			if not result and not streak:
				badSeasons += 1
				break
			streak = result 
	likelihood = float(numberOfSimulations - badSeasons)/numberOfSimulations
	return likelihood

def converge(numSimulations, desiredLikelihood):
	winLikelihood = .8
	baseline = simulate(numSimulations, winLikelihood)
	while baseline < desiredLikelihood:
		print winLikelihood, baseline
		winLikelihood += .001
		baseline = simulate(numSimulations, winLikelihood)
	return winLikelihood
	


def main():
	# first question
	# print simulate(100000, .8)

	# second question
	print converge(10000, .5)






if __name__ == "__main__":
    main()



