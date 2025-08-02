import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
def load_cars():
    with open('audi_cars.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def answer_question(question, cars):
    question = question.lower()
    tokens = word_tokenize(question)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
    if 'price' in stemmed_tokens or 'cost' in stemmed_tokens:
        for car in cars:
            if car['model'].lower() in question:
                return f"The price of {car['model']} is {car['price']}."
        return "Which Audi model do you want to know the price of?"
    elif 'feature' in question or 'have' in question:
        for car in cars:
            if car['model'].lower() in question or car['model'].lower() in ' '.join(tokens):
                return f"{car['model']} features: {', '.join(car['features'])}."
        return "Which Audi model do you want to know the features of?"
    elif 'available' in tokens or 'in stock' in tokens:
        for car in cars:
            if car['model'].lower() in question or car['model'].lower() in ' '.join(tokens):
                return f"{car['model']} is {'available' if car['available'] else 'not available'} for sale."
        return "Which Audi model do you want to know the availability of?"
    elif 'models' in question or 'cars' in question:
        models = ', '.join([car['model'] for car in cars])
        return f"Available Audi models: {models}."
    else:
        return "I can help you with information about Audi models, prices, features, and availability. What do you want to know?"
