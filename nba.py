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
	
def convergeBinarySearch(numSimulations, desiredLikelihood):
	#more effiecient but potentially flawed due to randomness
	low = 0.0 #always lose
	high = 1.0 #always win
	while high - low > .001:
		guess = (high + low)/2.0
		baseline = simulate(numSimulations, guess)
		if baseline > desiredLikelihood:
			high = guess
		else:
			low = guess
	return guess


def main():
	# first question
	print simulate(1000000, .8)

	# second question
	print convergeBinarySearch(10000, .5)






if __name__ == "__main__":
    main()



