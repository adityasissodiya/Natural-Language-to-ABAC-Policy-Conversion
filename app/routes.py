from flask import request, jsonify
from flask import render_template
from .nlp_processing import process_natural_language
from .vakt_integration import enforce_policy

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/process_policy', methods=['POST'])
    def process_policy():
        try:
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
        except Exception as e:
            print(f"Error: {e}")  # Log the error for debugging
            return jsonify({"error": str(e)}), 500
