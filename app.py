from flask import Flask, render_template, request, jsonify
from nlp_processing import process_natural_language
from vakt_integration import enforce_policy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_policy', methods=['POST'])
def process_policy():
    input_policy = request.form['policy_text']
    
    # Process the policy using NLP and generate XACML
    result = process_natural_language(input_policy)
    
    # Simulate policy enforcement
    enforcement_result = enforce_policy(result['entities'])
    
    return jsonify({
        'entities': result['entities'],
        'xacml_policy': result['xacml_policy'],
        'enforcement': enforcement_result
    })

if __name__ == '__main__':
    app.run(debug=True)
