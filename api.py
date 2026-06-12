from flask import Flask, request, jsonify
from flask_cors import CORS
from crawler.agent import ask_question

app = Flask(__name__)
CORS(app)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "")

    result = ask_question(question)

    return jsonify({
        "answer": result["answer"],
        "sources": result["sources"]
    })


if __name__ == "__main__":
    app.run(debug=True)