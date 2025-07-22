import fitz
import openai
from openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI()


def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

resume_text = extract_text_from_pdf("example_resume.pdf")
print(resume_text[:500]) #The first 500 characters

summary = """
**Professional Summary:**  
Jordan Taylor is a computer science student with experience in Python, automation, and AI tools. They are passionate about building real-world applications using machine learning and cloud services.

**Top 5 Skills:**  
1. Python  
2. Git & GitHub  
3. OpenAI API  
4. Automation  
5. Cloud Integration

**Suggested Role:**  
AI Developer Intern
"""

print("\n==== GPT Summary ====\n")
print(summary)

'''
def summarize_resume(resume_text):
    prompt = f"""

You are a career coach and mentor. Please read the resume text and:
1. Write a 3-5 sentence professional summary.
2. List the top 5 technical or soft skills.
3. Suggest one type of job this person is a good fit for.

Resume:
\"\"\"
{resume_text}
\"\"\"

"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that specializes in resumes."},
            {"role": "user", "content": prompt}
        ],
        temperature = 0.7
    )

    return response.choices[0].message.content

summary = summarize_resume(resume_text)

print("\n==== GPT Summary ====\n")
print(summary)
'''
