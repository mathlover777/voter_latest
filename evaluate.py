import config
import utility
import random

def transition_prob(G, LastOpinion, currnode, X = None, isRandom = False):

	P = 0.0
	if(X == None):
		K = len(G[currnode])
		for i in xrange(0, K):
			temp_node = G[currnode][i]
			if LastOpinion[str(currnode)] != LastOpinion[str(temp_node)]:
				P += (1.0/float(K))
	else:
		for influence in G[currnode]:
			if LastOpinion[str(currnode)] != LastOpinion[str(influence)]:
				P = P + X[currnode][str(influence)]

	if isRandom:
		P = random.uniform(0,1)
		return P

	return P

def nextOpinion(G, LastOpinion, currnode, Opinions, X = None, isRandom = False):
	num_nodes = len(G)
	transProb = 0
	new_opinion = 0
	for currnode in xrange(0,num_nodes):
		transProb = transition_prob(G, LastOpinion,currnode,X, isRandom)
		# print transProb, currnode, time
		if transProb >= 0.5:
			# new_opinion = -1 * Opinions[str(time)][str(currnode)]
			new_opinion = -1 * int(LastOpinion[str(currnode)])
			# print 'transitoning node - ',currnode,' at time ',time,' from ',Opinions[time][currnode],' to ',new_opinion[currnode]
		else:
			new_opinion = LastOpinion[str(currnode)]
	return new_opinion


def findMatchPercentage(actualOpinions, predictedOpinions):	

	matching = 0.0
	total_opinions = 0
	opinions_matched = 0

	for node in predictedOpinions:

		preOp = predictedOpinions[node]
		actOp = actualOpinions[str(node)]

		if (preOp>=0 and actOp>=0) or (preOp<=0 and actOp<=0):
			opinions_matched = opinions_matched+1
		total_opinions = total_opinions+1


	matching = float(opinions_matched)/float(total_opinions)

	# print matching
	# print opinions_matched
	# print total_opinions
	return matching
		

def calculateCase1(actualOpinions,G,X):

	LastOpinion = actualOpinions[str(config.timestamp)]
	matchingCase1 = {}
	for time in xrange(config.timestamp, config.maxTime+1):

		new_opinion = {}

		for currnode in xrange(0,len(G)):
			new_opinion[str(currnode)] = nextOpinion(G,LastOpinion, currnode, actualOpinions, X)

		matchingCase1[time] = findMatchPercentage(actualOpinions[str(time)], new_opinion)
		LastOpinion = new_opinion

	print "case1: ", matchingCase1
	return matchingCase1


def calculateCase2(actualOpinions,G,X):

	# LastOpinion = actualOpinions[str(config.timestamp)]
	matchingCase2 = {}
	for time in xrange(config.timestamp, config.maxTime+1):

		LastOpinion = actualOpinions[str(time)]
		new_opinion = {}

		for currnode in xrange(0,len(G)):
			new_opinion[currnode] = nextOpinion(G,LastOpinion, currnode, actualOpinions, X)

		matchingCase2[time] = findMatchPercentage(actualOpinions[str(time)], new_opinion)


	print "case2: ", matchingCase2
	return matchingCase2


def randomCase1(actualOpinions,G,X):

	LastOpinion = actualOpinions[str(config.timestamp)]
	matchingCase1 = {}
	for time in xrange(config.timestamp, config.maxTime+1):

		new_opinion = {}

		for currnode in xrange(0,len(G)):
			new_opinion[str(currnode)] = nextOpinion(G,LastOpinion, currnode, actualOpinions, X, True)

		matchingCase1[time] = findMatchPercentage(actualOpinions[str(time)], new_opinion)
		LastOpinion = new_opinion

	print "Random case1: ", matchingCase1
	return matchingCase1


def randomCase2(actualOpinions,G,X):

	# LastOpinion = actualOpinions[str(config.timestamp)]
	matchingCase2 = {}
	for time in xrange(config.timestamp, config.maxTime+1):

		LastOpinion = actualOpinions[str(time)]
		new_opinion = {}

		for currnode in xrange(0,len(G)):
			new_opinion[currnode] = nextOpinion(G,LastOpinion, currnode, actualOpinions, X, True)

		matchingCase2[time] = findMatchPercentage(actualOpinions[str(time)], new_opinion)

	print "Random case2: ", matchingCase2
	return matchingCase2


def evaluate(actualOpinionFile):
	actualOpinions = utility.loadJsonObject(actualOpinionFile)	
	X = utility.loadJsonObject(config.adjacencyName)
	G = utility.loadJsonObject(config.synthetic_adjacency)

	calculateCase1(actualOpinions,G,X)
	calculateCase2(actualOpinions,G,X)
	randomCase1(actualOpinions,G,X)
	randomCase2(actualOpinions,G,X)
	# print actualOpinions['39']

def main():
	evaluate(config.synthetic_opinions)
	
if __name__ == "__main__":
	main()
