from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

responses = {
    "hello": "Hello! Welcome to XYZ Hospital. How can I assist you today?",
    "hi": "Hello! Welcome to XYZ Hospital. How can I assist you today?",
    "fever":"Paracetamol (Acetaminophen) , Take rest, stay hydrated.",
    "headache": "Ibuprofen or Paracetamol , Rest in a quiet, dark room.",
    "cold (Common Cold)": "Decongestants (e.g., Pseudoephedrine) or Antihistamines (e.g., Diphenhydramine) , Drink fluids, rest.",
    "cough": "Cough syrup (e.g., Dextromethorphan) or Honey , Stay hydrated, rest.",
    "sore throat": "Lozenges (e.g., Strepsils) or Warm salt water gargles , Drink warm liquids, avoid irritants.",
    "indigestion": "Antacids (e.g., Tums, Ranitidine) , Avoid heavy meals, drink ginger tea.",
    "stomach ache": "Antispasmodics (e.g., Hyoscine) or Antacids , Eat light meals, avoid fatty foods.",
    "diarrhea": "Loperamide (Imodium) or Oral Rehydration Solutions (ORS) , Stay hydrated, eat bland foods.",
    "constipation":"Laxatives (e.g., Senna or Fiber Supplements) , Drink plenty of water, eat fiber-rich foods.",
    "skinrash": "Antihistamines (e.g., Loratadine) or Hydrocortisone Cream , Avoid scratching, moisturize skin.",
    "allergies": "Antihistamines (e.g., Cetirizine, Loratadine) , Avoid allergens, rest.",
    "book appointment": "Sure! Please provide your name, preferred date, and department.",
    "departments": "We have Cardiology, Neurology, Orthopedics, and General Medicine.",
    "contact": "You can reach us at +1234567890 or email us at contact@xyzhospital.com",
    "bye": "Goodbye! Take care and stay healthy."
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()
    response = responses.get(user_message, "I'm sorry, I didn't understand that. Can you please rephrase?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
