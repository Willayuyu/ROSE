from ..data import Reader
from typing import List
import json

def load_feedback(fpath="cornac/datasets/Yelp/yelp_ratings.txt", fmt="UIR", sep=",", skip_lines=0, reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt=fmt, sep=sep, skip_lines=skip_lines)

def load_review(fpath="cornac/datasets/Yelp/yelp_reviews.txt", reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt="UIReview", sep="\t")

def load_sentiment(fpath="cornac/datasets/Yelp/yelp_lexicon.txt", reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt="UITup", sep=",", tup_sep=':')

# After downloading the yelp dataset, prepare_yelp() needs to be run once to prepare the data
def prepare_yelp():
    reviews = []
    ratings = []
    
    with open("cornac/datasets/yelp/yelp_academic_dataset_review.json", 'r') as f:
        for line in f:
            review = json.loads(line)
            user_id = review['user_id']
            item_id = review['business_id']
            rating = review['stars']
            text = review['text'].replace("\n", " ").replace('\r', '').strip()
            reviews.append(f"{user_id}\t{item_id}\t{text}")
            ratings.append(f"{user_id},{item_id},{rating}")
    
    with open("cornac/datasets/yelp/yelp_reviews.txt", 'w') as f:
        for review in reviews:
            f.write(review + "\n")
    
    with open("cornac/datasets/yelp/yelp_ratings.txt", 'w') as f:
        for rating in ratings:
            f.write(rating + "\n")

    print("Yelp dataset prepared and saved to yelp_reviews.txt and yelp_ratings.txt")

# prepare_yelp()