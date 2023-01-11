### Import essential modules
import spacy

# Load Spacy English core
nlp = spacy.load('en_core_web_md')

# Read movies.txt and save into a dictionary of movie - description_token
# Read the file
movies_txt_content = list()
with open("movies.txt", "r") as file_reader:
    movies_txt_content = file_reader.readlines()

# Digest the list of string into dictionary
movie_token_dict = dict()
for txt_line in movies_txt_content:
    movie_desc = txt_line.split(":")
    movie = movie_desc[0].strip()
    description = movie_desc[1].strip()
    desc_token = nlp(description)
    movie_token_dict[movie] = desc_token

# Function to return which movies a user would watch next
def which_movie_next(user_description):
    """
    Function to return which movies a user would watch next

    Parameters
    ----------
    user_description : str      User description after watching Planet Hulk

    Return
    ------
    Which movies a user watch next most likely
    """
    # Tokenisation of user description
    user_desc_token = nlp(user_description)

    # loop all tokens and find the largest value of similarity
    resulted_movie = ""
    largest_similarity = -1
    for movie, token in movie_token_dict.items():
        similarity = token.similarity(user_desc_token)
        if similarity > largest_similarity:
            resulted_movie = movie
            largest_similarity = similarity
    
    # return the resulted movie
    return resulted_movie

given_user_desc = "Will he save their world or destroy it? When the Hulk becomes too dangereous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
next_movie = which_movie_next(given_user_desc)
# Show the title of most similar movie
print(f"The user may watch the movie called {next_movie} next most likely.")
