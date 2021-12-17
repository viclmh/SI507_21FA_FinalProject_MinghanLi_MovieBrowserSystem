## Introduction
This project is about a movie browser system to display the newly released movies in 2021 to people according to their preferences. 

This project can be divided into three parts.

1. Collect Data
   - collection.py
     - This file is used to scrape 300 movies from IMDb and store them in movies.json
   - movies.json
     - Store the scraped movie data in json format

2. Organize Data
   - storageData.py
     - This file contains functions such as storeMovieOfOneGenre(), sortMovieByRating(), storeMovieByRating(), sortMovieByCertificate(), storeMovieByCertificate(). These functions are used to organize data into graphs by genre or rating or certificate and store them into graph.json.
   - readJson.py
     - This file contains functions such as retrieveMovieByName(), retrieveMovieByGenre(), retrieveMovieByRating(),
     retrieveMovieByCertificate(),
     retrieveMovieByVotes(). These functions are used to read the json of the graph and retrieve  data by genre or rating or certificate... These functions are used by Flask App to retrieve results according to users' preference.
   - graph.json
     - Store the organized graph data.
3. Interaction and Presentation
   - MovieSearchFlaskApp.py
     - To run the Flask app.


## Package Requirement
Packages such as BeautifulSoup, requests, json, and time are used for this final project to work.
1. BeautifulSoup

Module BeautifulSoup is used to help analyse the html tags and filter out the tags containing the information we want in the html file.

2. Requests

Module requests is used to get the html response of to the website URL

3. Json

Module json is used when we would like to read or write json files.

4. Time

Module time is used to create a sleep time when we are requesting the html response in the process of scraping multiple pages. If our requests is too frequent, we will be identified as robots and get 403 forbidden error.

## Data Structure

About the graph data structure, I realized several kinds of graphs. I first created a class named Movie, and created an object for each movie in the dataset. Then I created another class named Vertex that has two fields: name and a dictionary connectedTo, and has methods addNeighbors() and getConnections().

One type of graph I created is about the genre of movies, for example, I created a central Vertex called Comedy, then if one movie object has the attribute “Comedy”, I will add this object to the neighbor of the Vertex Comedy with a weight 1. In this way, I created some graphs such as comedy, action, fantasy. I then stored the graph in graph.json file as Fig. 3. The graph has 5 keys named type, directed, label, nodes and edges. Take this graph whose label is Romance as an example, this graph contains all the movies of the genre Romance. It is an undirected graph, and the information of each movie is stored in every node like Fig. 4. Also, the edges in the graph store the relationship between every node and its source node (e.g. the central vertex) like Fig. 5. 

Some other type of graph I created like the Rating graph is organized in this way: If the rating of a movie object is above 8, I will add this object to the neighbor of the Vertex Rating with a weight 3, and if the rating is in range (7,8), I will add it and give it a weight 2 and (5,7) with weight 1 and object whose rating is below 5 is given weight 0. I also created the certificate graph that stores the movies of certain certificates, and it is organized in similar ways. It has four central vertices named R, PG, PG-13 and G. The movies are connected to these nodes according to which certificate they belong to.
