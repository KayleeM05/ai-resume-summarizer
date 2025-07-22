# ai-resume-summarizer
Python tool which used chatgpt to summarize your resume.

# AI Resume Summarizer 🧠📄

This project is a Python script that reads a PDF resume and uses OpenAI's GPT to generate:
- A professional summary
- Top 5 skills
- A suggested job role

## Features
- Reads any resume PDF using PyMuPDF
- Sends the text to OpenAI (simulated here)
- Prints out a clean, professional summary

## Example Output

==== GPT Summary ====

Professional Summary:
Jordan Taylor is a computer science student with experience in Python, automation, and AI tools. They are passionate about building real-world applications using machine learning and cloud services.

Top 5 Skills:

Python

Git & GitHub

OpenAI API

Automation

Cloud Integration

Suggested Role:
AI Developer Intern


## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the script:
    python app.py

3. Replace example_resume.pdf with any resume PDF you like.

Tech Stack:

Python 3.10+
OpenAI API (mocked here due to quota limits)
PyMuPDF
dotenv

NOTE: If you have OpenAI API access, you can uncomment the GPT section in resumesum.py to get live results.
