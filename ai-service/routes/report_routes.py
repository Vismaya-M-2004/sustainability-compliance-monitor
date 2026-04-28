from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()

        if not data or 'input_text' not in data:
            return jsonify({"error": "input_text is required"}), 400

        input_text = data['input_text']

        # Load prompt
        with open('prompts/generate_report.txt', 'r') as f:
            prompt_template = f.read()

        prompt = prompt_template.replace("{input_text}", input_text)

        # Call Groq
        response = call_groq(prompt)

        if response is None:
            return jsonify({
                "is_fallback": True,
                "message": "AI service unavailable"
            }), 200

        # Convert string → JSON
        try:
            parsed = json.loads(response)
        except:
            return jsonify({
                "error": "Invalid AI response format",
                "raw_response": response
            }), 500

        parsed["generated_at"] = datetime.utcnow().isoformat()

        return jsonify(parsed), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500