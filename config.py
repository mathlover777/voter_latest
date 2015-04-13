# datasetName = 'Reddit'
# datasetName = 'Twitter'
datasetName = 'Synthetic'

# timestamp = 1355750721
timestamp = 40
maxTime = 50
adjacencyName = datasetName + '_' + str(timestamp) + '_adjacency.json'

nodeListFile = '/nodeList.txt'
edgeListFile = '/edgeList.txt'
postFile = '/post.txt'

nodeListFile_clean = '/nodeList_clean.txt'
edgeListFile_clean = '/edgeList_clean.txt'
postFile_clean = '/post_clean.txt'

synthetic_nodeList = 'Synthetic/nodeList_clean.txt'
synthetic_edgeList = 'Synthetic/edgeList_clean.txt'
synthetic_postFile = 'Synthetic/post_clean.txt'

synthetic_positive_opinion = 1 # the opposite one will be negative of this

nodeIdToIndexMap = '/nodeIdToIndexMap.txt' # these are not required for train.py
nodeIndexToIdMap = '/nodeIndexToIdMap.txt' # only required for recovering , module not implemented yet

synthetic_weights = 'Synthetic/random_weights.json'
synthetic_adjacency = 'Synthetic/adjacency.json'
synthetic_opinions = 'Synthetic/opinions.json'

failureLog = 'failure.txt'


num_nodes = 200
edge_prob = .5