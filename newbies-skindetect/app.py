import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
import mysql.connector

load_dotenv()

app = Flask(__name__)

# ✅ CORS configured for 127.0.0.1 and localhost
CORS(
    app,
    resources={r"/*": {"origins": ["http://127.0.0.1:5501", "http://localhost:5501"]}}
)

# ✅ Database config
db_config = {
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'host': 'localhost',
    'database': os.environ['DB_NAME']
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def insert_chat_history(user_message, bot_response):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO chat_history (user_message, bot_response)
        VALUES (%s, %s)
    """
    cursor.execute(query, (user_message, bot_response))
    conn.commit()
    cursor.close()
    conn.close()

# ✅ Gemini model configuration
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="hey you are a friendly personalized assistant for patients with skin disease queries..."
)

chat_session = model.start_chat()

def clean_response(text):
    formatted_text = text.replace('\n', '<br>').replace('* ', '<br>&bull; ')
    return formatted_text

# ✅ POST route
@app.route("/", methods=["POST"])
def chatbot():
    if not request.is_json:
        return jsonify({"error": "Invalid request format. JSON expected."}), 400

    user_input = request.json.get("message")
    app.logger.info(f"Received user message: {user_input}")

    response = chat_session.send_message(user_input)
    app.logger.info(f"Received model response: {response.text}")

    cleaned_text = clean_response(response.text)

    insert_chat_history(user_input, cleaned_text)

    return jsonify({"response": cleaned_text})

# ✅ GET route for health check
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Skin disease chatbot is running. Use POST to send messages."})

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # ✅ Bind to 127.0.0.1 explicitly
    app.run(debug=True, host="127.0.0.1", port=5000)
