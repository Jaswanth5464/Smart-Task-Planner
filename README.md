

# Smart Task Planner 🧠

**AI-driven project planning made simple and efficient.**

Smart Task Planner is an intelligent web app that automatically converts your project goals into a structured, actionable plan — complete with tasks, timelines, and dependencies.

---

## 🌐 Live Links

🔹 **App:** [https://jaswanth5464.pythonanywhere.com/](https://jaswanth5464.pythonanywhere.com/)
🔹 **Demo Video:** [View on Google Drive](https://drive.google.com/file/d/1-GQ-lme1NGz_gEpbxRWq1EYRc-vjIRI-/view?usp=sharing)
🔹 **Source Code:** [GitHub Repository](https://github.com/Jaswanth5464/smart-task-planner)

---

## 📘 Overview

Planning complex projects manually can be time-consuming and inconsistent.
**Smart Task Planner** automates this by generating a clear, step-by-step task breakdown from a single goal.

**What it does:**

* Divides a goal into 5–10 well-defined tasks
* Allocates realistic timeframes (start/end dates)
* Maps dependencies between related tasks
* Prioritizes them by importance

### Example

**Input:** “Launch an e-commerce website in 30 days”
**Output:**

* Market Research (Day 1–3, High Priority)
* Design Mockups (Day 4–7, High Priority, depends on Task 1)
* Backend Setup (Day 8–15, High Priority)
* ... and so on

---

## ✨ Key Features

* 🧠 **AI-Powered Planning:** Automatically breaks goals into actionable tasks
* ⏳ **Smart Scheduling:** Distributes time efficiently across the deadline
* 🔗 **Dependency Tracking:** Identifies task order and relationships
* 🎯 **Prioritization:** Labels tasks as High, Medium, or Low priority
* 💻 **Modern UI:** Clean, responsive interface
* 🚀 **API-Ready:** Built with a modular, REST-based backend

---

## 🧩 Tech Stack

| Component      | Technology            |
| -------------- | --------------------- |
| **Backend**    | Python (Flask)        |
| **AI Engine**  | Google Gemini Pro     |
| **Frontend**   | HTML, CSS, JavaScript |
| **Deployment** | PythonAnywhere        |

---

## ⚙️ Setup & Installation

### Requirements

* Python 3.8 or later
* Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/smart-task-planner.git
   cd smart-task-planner
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   In `app.py`, replace the placeholder key:

   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Visit the app**

   ```
   http://localhost:5000
   ```

---

## 💡 How to Use

1. Enter your project goal (e.g., “Build a mobile app in 45 days”).
2. Specify the deadline in days.
3. Click **Generate Task Plan**.
4. Instantly view the AI-generated roadmap with priorities and dependencies.

**Try sample inputs:**

* “Organize a tech event in 90 days”
* “Write a research paper in 21 days”
* “Develop a REST API in 20 days”

---

## 📁 Folder Structure

```
smart-task-planner/
├── app.py              # Flask server + AI logic
├── templates/
│   └── index.html      # Frontend page
├── requirements.txt    # Dependencies
└── README.md
```

---

## 📡 API Reference

### `POST /api/generate-plan`

**Request Body:**

```json
{
  "goal": "Launch a mobile app in 45 days",
  "deadline_days": 45
}
```

**Sample Response:**

```json
{
  "project_name": "Mobile App Launch",
  "total_duration": 45,
  "tasks": [
    {
      "id": 1,
      "name": "Market Research",
      "description": "Analyze competitors and target audience",
      "start_day": 1,
      "end_day": 3,
      "priority": "high",
      "start_date": "2025-10-17",
      "end_date": "2025-10-19"
    }
  ]
}
```

---

## 🧠 How It Works

1. **User Input:** Goal + Deadline provided through the UI
2. **Request Sent:** Frontend sends data to Flask API
3. **Processing:** The backend sends a structured prompt to Gemini AI
4. **AI Response:** A complete, logical task plan is returned
5. **Result Display:** Tasks are shown with durations, dependencies, and priorities

---

## 📦 Configuration

**requirements.txt**

```
flask==3.0.0
google-generativeai==0.3.2
```

**Python Version:** 3.8+
**API Key:** Insert your Gemini key in `app.py`

---

📊 System Architecture:
┌─────────────┐         HTTP POST          ┌──────────────┐
│   Browser   │ ────────────────────────► │ Flask Server │
│  (Frontend) │                            │  (Backend)   │
└─────────────┘                            └──────────────┘
                                                   │
                                                   │ API Call
                                                   ▼
                                           ┌──────────────┐
                                           │  Gemini AI   │
                                           │   (LLM)      │
                                           └──────────────┘
                                                   │
                                                   │ Response
                                                   ▼
┌─────────────┐         JSON Response      ┌──────────────┐
│   Browser   │ ◄──────────────────────── │ Flask Server │
│  (Results)  │                            │  (Processing)│
└─────────────┘                            └──────────────┘
## ☁️ Deployment

Hosted on **PythonAnywhere** for continuous availability.

**Live Demo:** [https://jaswanth5464.pythonanywhere.com](https://jaswanth5464.pythonanywhere.com)

**Steps (Summary):**

1. Upload project to PythonAnywhere
2. Create virtual environment
3. Install dependencies
4. Configure the web app (WSGI)
5. Reload to go live

---

## 📈 Highlights

* Generates **detailed, realistic** project plans
* Automatically adjusts timelines within deadlines
* Uses dependency mapping for better workflow sequencing
* Written with **clean, readable Python code**
* Fully functional **REST API**

---

## 🧑‍💻 Author

**Jaswanth Kanamarlapudi**

* Email: [jaswanth5464@gmail.com](mailto:jaswanth5464@gmail.com)
* GitHub: [@Jaswanth5464](https://github.com/Jaswanth5464)

---

## 🪄 Credits

* **Google Gemini Pro** – for task generation logic
* **Flask** – backend web framework
* **PythonAnywhere** – for deployment hosting

---

## 📬 Contact

For feedback or suggestions:
📧 **[jaswanth5464@gmail.com](mailto:jaswanth5464@gmail.com)**
🐙 [GitHub Issues](https://github.com/Jaswanth5464/smart-task-planner/issues)

---

**If you found this project useful, give it a ⭐ on GitHub!**
*Last updated: October 2025*

