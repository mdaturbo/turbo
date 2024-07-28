# from flask import Flask, request, jsonify, render_template, session
# from flask_session import Session
# from transformers import pipeline
# import os

# # Initialize Flask app
# app = Flask(__name__, static_folder='.', static_url_path='')

# # Configure session to use filesystem (instead of signed cookies)
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = os.urandom(24)
# Session(app)

# # Initialize the Hugging Face pipeline for natural language processing
# nlp = pipeline('sentiment-analysis')

# # Example set of traffic rules and penalties
# traffic_rules = {
#     "speeding": "A fine of Rs. 2000 and attendance at a traffic safety course.",
#     "running red light": "A fine of Rs. 1000 and 3 penalty points on the license.",
#     "drunk driving": "A fine of Rs. 10000 and imprisonment up to 6 months.",
#     "not wearing seatbelt": "A fine of Rs. 1000 for both driver and front-seat passenger.",
#     "using mobile while driving": "A fine of Rs. 5000 and possible suspension of the license."
# }

# # Example function to analyze and determine fault
# def analyze_statements(statement1, statement2):
#     analysis1 = nlp(statement1)
#     analysis2 = nlp(statement2)
#     # Example logic for determining fault based on sentiment (can be expanded)
#     if 'speeding' in statement1.lower():
#         fault = "Party 1"
#         penalty = traffic_rules["speeding"]
#     elif 'speeding' in statement2.lower():
#         fault = "Party 2"
#         penalty = traffic_rules["speeding"]
#     else:
#         fault = "Inconclusive"
#         penalty = "Further investigation needed."
#     return fault, penalty

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit_statements', methods=['POST'])
# def submit_statements():
#     data = request.get_json()
#     statement1 = data.get('statement1')
#     statement2 = data.get('statement2')
#     fault, penalty = analyze_statements(statement1, statement2)
    
#     # Store result in session for current user
#     session['result'] = {
#         "fault": fault,
#         "penalty": penalty
#     }
    
#     return jsonify({
#         "fault": fault,
#         "penalty": penalty
#     })

# @app.route('/get_result', methods=['GET'])
# def get_result():
#     # Retrieve result from session for current user
#     result = session.get('result', {"fault": "No data", "penalty": "No data"})
#     return jsonify(result)

# if _name_ == '_main_':
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from transformers import pipeline
import os

# Initialize Flask app
app = Flask(
    __name__, 
    static_folder=r'.',  # Serving static files from the current directory
    static_url_path='',  # URL path for static files
    template_folder=r'D:\Downloads\Telegram Desktop\Impress crush\Impress crush\prajwal\templates'  # Path to your templates
)
# Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
Session(app)

# Initialize the Hugging Face pipeline for natural language processing
nlp = pipeline('sentiment-analysis')

# Example set of traffic rules and penalties
traffic_rules = {
    "speeding": "A fine of Rs. 2000 and attendance at a traffic safety course.",
    "running red light": "A fine of Rs. 1000 and 3 penalty points on the license.",
    "drunk driving": "A fine of Rs. 10000 and imprisonment up to 6 months.",
    "not wearing seatbelt": "A fine of Rs. 1000 for both driver and front-seat passenger.",
    "using mobile while driving": "A fine of Rs. 5000 and possible suspension of the license."
}

# Example function to analyze and determine fault
def analyze_statements(statement1, statement2):
    analysis1 = nlp(statement1)
    analysis2 = nlp(statement2)
    # Example logic for determining fault based on keywords
    if 'speeding' in statement1.lower():
        fault = "Party 1"
        penalty = traffic_rules["speeding"]
    elif 'speeding' in statement2.lower():
        fault = "Party 2"
        penalty = traffic_rules["speeding"]
    else:
        fault = "Inconclusive"
        penalty = "Further investigation needed."
    return fault, penalty

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_statements', methods=['POST'])
def submit_statements():
    data = request.get_json()
    statement1 = data.get('statement1')
    statement2 = data.get('statement2')
    fault, penalty = analyze_statements(statement1, statement2)
    
    # Store result in session for the current user
    session['result'] = {
        "fault": fault,
        "penalty": penalty
    }
    
    return jsonify({
        "fault": fault,
        "penalty": penalty
    })

@app.route('/get_result', methods=['GET'])
def get_result():
    # Retrieve result from session for the current user
    result = session.get('result', {"fault": "No data", "penalty": "No data"})
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
