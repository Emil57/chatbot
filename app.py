from flask import Flask, request, jsonify
from chatbot import load_cars, answer_question

app = Flask(__name__)
cars = load_cars()

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question', '')
    answer = answer_question(question, cars)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
