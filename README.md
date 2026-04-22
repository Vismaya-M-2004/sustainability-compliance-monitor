# Sustainability Compliance Monitor

A tool-based AI solution to monitor and ensure sustainability compliance.

## Project Progress

### 📅 Day 1
* Set up project folders and basic structure.
* Configured API keys and environment variables (.env).
* Initialized Git for version control.
* Verified the initial connection to the Groq AI API.

### 📅 Day 2
* Developed a robust and reusable GroqClient.
* Added error handling and automatic retries for better reliability.
* Integrated logging to track service performance.
* Created test scripts to verify AI responses and client stability.

### 📅 Day 3
* Built a Flask API with a POST endpoint (`/api/analyze`) for AI analysis.
* Implemented `flask-limiter` for rate limiting (30 requests/minute).
* Added security features to strip HTML and block prompt injection.
* Configured specialized system prompts for sustainability compliance expertise.