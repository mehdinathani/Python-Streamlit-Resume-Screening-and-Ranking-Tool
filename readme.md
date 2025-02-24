# Resume Screening and Ranking Tool

## Overview
The **Resume Screening and Ranking Tool** is a web application built with **Streamlit** and **Python** that allows users to upload resumes (PDF or DOCX), score them based on skills, and rank them using an **Applicant Tracking System (ATS)**-style scoring method. It also provides **AI-powered feedback** to help candidates improve their resumes.

## Features
- **Resume Scoring:**
  - Upload multiple resumes (PDF or DOCX).
  - Extract text and rank resumes based on keyword matching.
  - View ranked resumes in a structured table.
- **ATS Scoring:**
  - Paste a job description and compare resumes to determine ATS compatibility.
  - Uses **keyword frequency matching** to generate an ATS score.
- **AI Feedback:**
  - AI-generated constructive feedback on resumes using OpenAI's GPT.
- **Logging and Analytics:**
  - Uses **MongoDB** to log user actions (file uploads, processing, scoring, etc.).
- **Enhanced UI/UX:**
  - Beautiful and interactive UI with **animations, CSS styling, and Streamlit widgets**.
  
## How to Use
1. **Run the App Locally**
   ```bash
   streamlit run app.py
   ```
2. **Upload resumes and enter required skills**
3. **View scored and ranked resumes**
4. **Generate AI feedback**
5. **Analyze ATS scoring based on job descriptions**

## Technologies Used
- **Python** (Backend processing)
- **Streamlit** (Web framework for interactive UI)
- **Pandas** (Data manipulation)
- **PyPDF2 & python-docx** (Resume text extraction)
- **pymongo** (MongoDB for logging user actions)
- **OpenAI API** (For AI-generated feedback)
- **CSS & Streamlit Themes** (For UI enhancements)

## Deployment
This app is deployed on **Streamlit Cloud**.
### Steps to Deploy:
1. Push your project to **GitHub**.
2. Deploy on **Streamlit Cloud**.
3. Configure **Secrets Management** for MongoDB and OpenAI API keys.
4. Click **Deploy** and enjoy!

## Installation
To install dependencies, run:
```bash
pip install -r requirements.txt
```

## Environment Variables
Ensure the following secrets are set up before running the app:
```
MONGODB_URI=your_mongodb_connection_string
OPENAI_API_KEY=your_openai_api_key
```

## Live Demo
Try it out: [Resume Screening App](https://your-streamlit-app-link.com)

## License
This project is open-source and free to use.

---
🚀 **Enhance Your Resume Screening Process Today!** 🚀

