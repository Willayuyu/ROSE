import json
from cornac.data import Reader
from typing import List

def load_feedback(fpath="cornac/datasets/RateBeer/ratebeer_ratings.txt", fmt="UIR", sep=",", skip_lines=0, reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt=fmt, sep=sep, skip_lines=skip_lines)

def load_review(fpath="cornac/datasets/RateBeer/ratebeer_reviews.txt", reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt="UIReview", sep="\t")

def load_sentiment(fpath="cornac/datasets/RateBeer/ratebeer_lexicon.txt", reader: Reader = None) -> List:
    reader = Reader() if reader is None else reader
    return reader.read(fpath, fmt="UITup", sep=",", tup_sep=':')

def prepare_ratebeer():
    reviews = []
    ratings = []
    with open("cornac/datasets/RateBeer/orig/ratebeer.json", 'r') as f:
        for line in f:
            review = json.loads(line)
            user_id = review['review/profileName']
            item_id = review['beer/beerId']
            
            try:
                rating = review['review/overall'].split('/')[0]
                ratings.append(f"{user_id},{item_id},{rating}")
            except AttributeError:
                continue
            
            try:
                text = review['review/text'].replace("\n", " ").replace('\r', ' ').replace('\t', ' ').strip()
                if text:
                    reviews.append(f"{user_id}\t{item_id}\t{text}")
            except AttributeError:
                continue
            
    
    with open("cornac/datasets/RateBeer/ratebeer_reviews.txt", 'w') as f:
        for review in reviews:
            f.write(review + "\n")
    
    with open("cornac/datasets/RateBeer/ratebeer_ratings.txt", 'w') as f:
        for rating in ratings:
            f.write(rating + "\n")

# prepare_ratebeer()