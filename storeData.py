import json

class Movie:
    def __init__(self, json):
        self.number = json['number']
        self.name = json['name']
        self.runtime = json['runtime']
        self.genre = json['genre']
        self.certificate = json['certificate']
        self.rating = json['rating']
        self.votes = json['votes']
        self.director = json['director']
        self.star = json['star']


class Vertex:
    def __init__(self, name):
        self.name = name
        self.connectedTo = {}

    def addNeighbor(self, nbr, id, weight):
        self.connectedTo[nbr] = (id, weight)

    def getConnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        for name in self.connectedTo.keys():
            print(name, self.connectedTo[name])
        return "success"


def getMovieOfOneGenre(movieGenre, movieObj):
    genre = Vertex(movieGenre)
    for obj in movieObj:
        if movieGenre in obj.genre:
            genre.addNeighbor(obj.name, obj.number, 1)
    return genre

def storeMovieOfOneGenre(genre, filename, movieJson):
    genreDict = {}
    genreDict['label'] = genre.name
    genreDict['type'] = 'graph'
    genreDict['directed'] = False
    genreDict['nodes'] = {}
    genreDict['nodes']['0'] = {
        'label': genre.name,
        'metedata':{
            'type': "node",
            'value':genre.name
        }
    }
    genreDict['edges'] = []
    for nei in genre.getConnections():
        id = genre.connectedTo[nei][0]
        genreDict['nodes'][id] = {
            'label': nei,
            'metadata':{
                'type':"node",
                'value':movieJson[id - 1]
            }
        }
        edgeDict = {
            'source': "0",
            'target': str(id),
            'relation': 'edge',
            'directed': False,
            'weight': genre.connectedTo[nei][1]
        }
        genreDict['edges'].append(edgeDict)
    with open(filename, 'a') as jsonfile:
        json.dump(genreDict, jsonfile, indent=' ')
        jsonfile.write(',\n')

def sortMovieByRating(movieObj):
    rating = Vertex('Rating')
    for obj in movieObj:
        if obj.rating == "No rating so far":
            continue
        elif obj.rating >= 8:
            rating.addNeighbor(obj.name, obj.number, 3)
        elif obj.rating < 8 and obj.rating >= 7:
            rating.addNeighbor(obj.name, obj.number, 2)
        elif obj.rating < 7 and obj.rating >= 5:
            rating.addNeighbor(obj.name, obj.number, 1)
        elif obj.rating < 5:
            rating.addNeighbor(obj.name, obj.number, 0)
    return rating


def storeMovieByRating(rating, filename, movieJson):
    ratingDict = {}
    ratingDict['label'] = rating.name
    ratingDict['type'] = 'graph'
    ratingDict['directed'] = False
    ratingDict['nodes'] = {}
    ratingDict['nodes']['0'] = {
        'label': rating.name,
        'metedata':{
            'type': "node",
            'value':rating.name
        }
    }
    ratingDict['edges'] = []
    for nei in rating.getConnections():
        id = rating.connectedTo[nei][0]
        ratingDict['nodes'][id] = {
            'label': nei,
            'metadata':{
                'type':"node",
                'value':movieJson[id - 1]
            }
        }
        edgeDict = {
            'source': "0",
            'target': str(id),
            'relation': 'edge',
            'directed': False,
            'weight': rating.connectedTo[nei][1]
        }
        ratingDict['edges'].append(edgeDict)
    with open(filename, 'a') as jsonfile:
        json.dump(ratingDict, jsonfile, indent=' ')
        jsonfile.write(',\n')


def sortMovieByCertificate(movieObj):
    R = Vertex('R')
    PG_13 = Vertex('PG-13')
    PG = Vertex('PG')
    G = Vertex('G')
    for obj in movieObj:
        if obj.certificate == "R":
            R.addNeighbor(obj.name, obj.number, 1)
        elif obj.certificate == "PG-13":
            PG_13.addNeighbor(obj.name, obj.number, 1)
        elif obj.certificate == "PG":
            PG.addNeighbor(obj.name, obj.number, 1)
        elif obj.certificate == "G":
            G.addNeighbor(obj.name, obj.number, 1)
    certificateList = [R, PG_13, PG, G]
    return certificateList

def storeMovieByCertificate(certificateList, filename, movieJson):
    certificateDict = {}
    certificateDict['label'] = 'Certificate'
    certificateDict['type'] = 'graph'
    certificateDict['directed'] = False
    certificateDict['nodes'] = {}
    certificateDict['edges'] = []
    for i in range(4):
        certificateDict['nodes'][i] = {
            'label': certificateList[i].name,
            'metedata':{
                'type': "node",
                'value':certificateList[i].name
            }
        }
        for nei in certificateList[i].getConnections():
            id = certificateList[i].connectedTo[nei][0]
            certificateDict['nodes'][id] = {
                'label': nei,
                'metadata':{
                    'type':"node",
                    'value':movieJson[id - 1]
                }
            }
            edgeDict = {
            'source': str(i),
            'target': str(id),
            'relation': 'edge',
            'directed': False,
            'weight': certificateList[i].connectedTo[nei][1]
        }
            certificateDict['edges'].append(edgeDict)
    with open(filename, 'a') as jsonfile:
        json.dump(certificateDict, jsonfile, indent=' ')
        jsonfile.write(',\n')


jsonFile = 'movies.json'
graphFile = 'graph.json'
movieObj = []

with open(jsonFile) as file:
    movieInfo = json.load(file)

for movie in movieInfo:
    movieObj.append(Movie(movie))

# genre = getMovieOfOneGenre("Fantasy", movieObj)

# rating = sortMovieByRating(movieObj)
# certificateList = sortMovieByCertificate(movieObj)


# for nei in rating.getConnections():
#     if rating.connectedTo[nei][1] == 0:
#         print(nei, rating.connectedTo[nei])

# for nei in genre.getConnections():
#     print(nei, genre.connectedTo[nei])

# for nei in genre.getConnections():
#     print(nei, genre.connectedTo[nei])

# for certificate in certificateList:
#     print(certificate.name)
#     for nei in certificate.getConnections():
#         print(nei, certificate.connectedTo[nei])

## Store graph about genre
# storeMovieOfOneGenre(genre, graphFile, movieInfo)

### Store graph about rating
# storeMovieByRating(rating, graphFile, movieInfo)

## Store graph about certificate
# storeMovieByCertificate(certificateList, graphFile, movieInfo)