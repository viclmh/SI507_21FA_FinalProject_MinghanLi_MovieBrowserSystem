from flask import Flask, render_template, request
app = Flask(__name__)
from readJson import retrieveMovieByName, retrieveMovieByGenre, retrieveMovieByRating, retrieveMovieByCertificate, retrieveMovieByVotes

@app.route('/')
def index():
    return render_template('FlaskInput.html')

@app.route('/name')
def index_name():
    return render_template('input1.html')

@app.route('/handle_form_name', methods=['POST'])
def handle_the_form_name():
    name = request.form["name"]
    if name != "":
        movieDict = retrieveMovieByName(str(name))
        name = movieDict['name']
        # print(name)
        return render_template('option1.html', movieDict=movieDict)

@app.route('/genre')
def index_genre():
    return render_template('input2.html')

@app.route('/handle_form_genre', methods=['POST'])
def handle_form_genre():
    genre = request.form["genre"]
    if genre != "":
        nodeList = retrieveMovieByGenre(str(genre))
        # print(nodeList)
        # print(name)
        return render_template('option2.html', genre=genre, nodeList=nodeList)

@app.route('/rating')
def index_rating():
    return render_template('input3.html')

@app.route('/handle_form_rating', methods=['POST'])
def handle_form_rating():
    rating = request.form["rating"]
    if rating != "":
        nodeList = retrieveMovieByRating(int(rating))
        return render_template('option3.html', nodeList=nodeList)

@app.route('/certificate')
def index_certificate():
    return render_template('input4.html')

@app.route('/handle_form_certificate', methods=['POST'])
def handle_form_certificate():
    certificate = request.form["certificate"]
    if certificate != "":
        nodeList = retrieveMovieByCertificate(certificate)
        return render_template('option4.html', nodeList=nodeList)

@app.route('/votes')
def index_votes():
    return render_template('input5.html')

@app.route('/handle_form_votes', methods=['POST'])
def handle_form_votes():
    try:
        votes = request.form["votes"]
    except:
        votes=''
    if votes != "":
        nodeList = retrieveMovieByVotes()
        return render_template('option5.html', nodeList=nodeList)


# @app.route('/handle_form', methods=['POST'])
# def handle_the_form():
#     name = request.form["name"]
#     genre = request.form["genre"]
#     certificate = request.form["certificate"]
#     rating = request.form["rating"]
#     try:
#         votes = request.form["votes"]
#     except:
#         votes=''
#     if name != "":
#         movieDict = retrieveMovieByName(str(name))
#         name = movieDict['name']
#         # print(name)
#         return render_template('option1.html', movieDict=movieDict)
#     elif genre != "":
#         nodeList = retrieveMovieByGenre(str(genre))
#         # print(nodeList)
#         # print(name)
#         return render_template('option2.html', genre=genre, nodeList=nodeList)
#     elif rating != "":
#         nodeList = retrieveMovieByRating(int(rating))
#         return render_template('option3.html', nodeList=nodeList)
#     elif certificate != "":
#         nodeList = retrieveMovieByCertificate(certificate)
#         return render_template('option4.html', nodeList=nodeList)
#     elif votes != "":
#         nodeList = retrieveMovieByVotes()
#         return render_template('option5.html', nodeList=nodeList)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
