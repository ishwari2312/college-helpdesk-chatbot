from flask import Flask, request, jsonify, render_template
import json
from openai import OpenAI

app = Flask(__name__)

# 🔹 Load JSON data
with open('data.json') as f:
    data = json.load(f)

# 🔹 OpenAI client
client = OpenAI(api_key="Ysk-proj-iuVxMnlQRRInza9Y_VP21ooBavijIIcZOEmD9uluLQLjPc3E8j2jupE1P4GP0PxNvyZD0Y5qM1T3BlbkFJdIN4iXcW26JJ9hKKVkp06Jkn0je8plUni41XU8K8eruSVJ2hhfaCaCOxxkqcYACa4CLs8FG6cA")  # replace this

# 🔹 Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()
    print("User:", user_message)

    # ✅ Improved keyword matching
    for item in data:
        keywords = item["question"].lower().split()

        for word in keywords:
            if word in user_message:
                print("Matched:", item["answer"])
                return jsonify({"reply": item["answer"]})

    # ✅ OpenAI fallback (optional)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Sorry, please contact the college office."})

if __name__ == '__main__':
    app.run(debug=True)