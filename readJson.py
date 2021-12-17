import json

def retrieveMovieByName(name):
    with open('movies.json') as file:
        movieInfo = json.load(file)
        for movie in movieInfo:
            if movie['name'] == name:
                return movie

def retrieveMovieByGenre(genre):
    with open('graph.json') as file:
        graphInfo = json.load(file)
        targetList = []
        for graphDict in graphInfo:
            if graphDict['label'] == genre:
                graphEdges = graphDict['edges'] # this is a list
                graphNodes = graphDict['nodes'] # this is a dictionary
                for edge in graphEdges:
                    targetList.append(edge['target'])
                break
        nodeList = []
        for id in targetList:
            nodeList.append(graphNodes[id]['metadata']['value']) # nodeList contains all the dictonary of one movie genre
        return nodeList

def retrieveMovieByRating(rating):
    with open('graph.json') as file:
        graphInfo = json.load(file)
        targetList = []
        for graphDict in graphInfo:
            if graphDict['label'] == "Rating":
                graphEdges = graphDict['edges'] # this is a list
                graphNodes = graphDict['nodes'] # this is a dictionary
                for edge in graphEdges:
                    if edge['weight'] == rating:
                        targetList.append(edge['target'])
                break
        nodeList = []
        for id in targetList:
            nodeList.append(graphNodes[id]['metadata']['value']) # nodeList contains all the dictonary of one movie genre
        return nodeList

def retrieveMovieByCertificate(certificate):
    with open('graph.json') as file:
        graphInfo = json.load(file)
        targetList = []
        for graphDict in graphInfo:
            if graphDict['label'] == "Certificate":
                graphEdges = graphDict['edges'] # this is a list
                graphNodes = graphDict['nodes'] # this is a dictionary
                for edge in graphEdges:
                    if edge['source'] == str(certificate):
                        targetList.append(edge['target'])
                break
        nodeList = []
        for id in targetList:
            if id not in ["0", "1", "2", "3"]:
                nodeList.append(graphNodes[id]['metadata']['value']) # nodeList contains all the dictonary of one movie genre
        return nodeList

def retrieveMovieByVotes():
    def quickSort(movieList, left, right):
        if left < right:
            index = partition(movieList, left, right)
            quickSort(movieList, left, index - 1)
            quickSort(movieList, index + 1, right)

    def partition(dictList, l, r):
        i = l - 1
        pivot = int(dictList[r]["votes"])

        for j in range(l, r):
            if int(dictList[j]["votes"]) >= pivot:
                i += 1
                dictList[i], dictList[j] = dictList[j], dictList[i]
        dictList[i + 1], dictList[r] = dictList[r], dictList[i + 1]
        return i + 1

    with open('movies.json') as file:
        movieInfo = json.load(file) # List of dictionary
        movieList = []
        for movie in movieInfo:
            if isinstance(movie['votes'], int):
                movieList.append(movie)
        l = 0
        r = len(movieList)
        quickSort(movieList, l, r - 1)
        return movieList[:100]


# movieDict = retrieveMovieByName('Old Henry')
# print(movieDict)
# nodeList = retrieveMovieByGenre('Romance')# nodeList contains all the dictonary of one movie genre
# for node in nodeList:
#     print(node['genre'])

# nodeList = retrieveMovieByRating(0)
# for node in nodeList:
#     print(node['rating'])

# nodeList = retrieveMovieByCertificate(1)
# for node in nodeList:
#     print(node['certificate'])

# nodeList = retrieveMovieByVotes()
# for node in nodeList:
#     print(node['votes'])