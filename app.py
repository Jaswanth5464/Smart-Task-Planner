from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Configure Gemini API (Replace with your API key)
genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxx")
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_task_plan(goal, deadline_days):
    """
    Uses Gemini AI to break down a goal into actionable tasks
    """
    prompt = f"""
You are a professional project manager. Break down the following goal into actionable tasks.

Goal: {goal}
Timeline: {deadline_days} days

Provide the output in this EXACT JSON format:
{{
  "project_name": "Short descriptive name",
  "total_duration": {deadline_days},
  "tasks": [
    {{
      "id": 1,
      "name": "Task name",
      "description": "Brief description",
      "start_day": 1,
      "end_day": 3,
      "duration_days": 3,
      "dependencies": [],
      "priority": "high/medium/low"
    }}
  ]
}}

Rules:
1. Create 5-10 realistic tasks
2. Tasks should be sequential and logical
3. Include dependencies (task IDs that must be completed first)
4. Distribute tasks across the entire timeline
5. Assign priority levels
6. Make sure start_day and end_day are within 1 to {deadline_days}
"""

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        response_text = response_text.strip()
        
        # Parse JSON
        task_plan = json.loads(response_text)
        
        # Add absolute dates
        today = datetime.now()
        for task in task_plan["tasks"]:
            task["start_date"] = (today + timedelta(days=task["start_day"]-1)).strftime("%Y-%m-%d")
            task["end_date"] = (today + timedelta(days=task["end_day"]-1)).strftime("%Y-%m-%d")
        
        return task_plan
    
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        print(f"Response: {response_text}")
        return {
            "error": "Failed to parse AI response",
            "raw_response": response_text
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "error": str(e)
        }

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    """API endpoint to generate task plan"""
    try:
        data = request.json
        goal = data.get('goal', '')
        deadline_days = int(data.get('deadline_days', 30))
        
        if not goal:
            return jsonify({"error": "Goal is required"}), 400
        
        if deadline_days < 1 or deadline_days > 365:
            return jsonify({"error": "Deadline must be between 1 and 365 days"}), 400
        
        # Generate plan using Gemini
        plan = generate_task_plan(goal, deadline_days)
        
        return jsonify(plan)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
