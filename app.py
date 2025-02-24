import streamlit as st
import pandas as pd
import os
from utils.text_extraction import extract_text_from_docx, extract_text_from_pdf
from utils.ranking import score_resume
from utils.logger import log_action  # Using our MongoDB logger
from utils.ai_feedback import generate_feedback


st.set_page_config(
    page_title="RankMyResume - AI Resume Screening & ATS Scoring",  # Browser tab title
    page_icon="📄",  # You can also use an emoji or a custom favicon URL
    layout="wide"
)
# Inject custom CSS for improved styling
st.markdown("""
    <style>
    /* Overall body style */
    body {
      background-color: #f0f2f6;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #333;
    }
    /* Header styles */
    .main-title {
      font-size: 2.8rem;
      color: #2c3e50;
      text-align: center;
      margin-bottom: 1rem;
    }
    .subheader {
      font-size: 1.8rem;
      color: #34495e;
      margin-top: 2rem;
    }
    /* Button styling (Streamlit buttons use default styling, but you can override with themes) */
    .stButton>button {
      background-color: #3498db;
      color: white;
      font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Display a banner image at the top (replace URL with your own image if available)
st.image("https://cdn-ilblhgp.nitrocdn.com/iNguFFPdcQkxwgnKqNudeMEbsKyWoDgp/assets/images/optimized/rev-36d96be/www.recruiterslineup.com/wp-content/uploads/2022/06/resume-screening-software.png", use_container_width=True)





# Sidebar with navigation buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Resume Scoring", use_container_width=True, key="resume_scoring"):
    st.session_state.page = "Resume Scoring"

if st.sidebar.button("ATS Scoring", use_container_width=True, key="ats_scoring"):
    st.session_state.page = "ATS Scoring"


# Set up session state for navigation (only if not already set)
if "page" not in st.session_state:
    st.session_state.page = "Resume Scoring"

if st.session_state.page == "Resume Scoring":
    st.markdown('<h1 class="main-title">Resume Screening and Ranking Tool</h1>', unsafe_allow_html=True)
    st.write("Upload your PDF or DOCX resumes and get a ranked list of candidates based on skills.")

    uploaded_files = st.file_uploader("Upload Resume Files", type=['pdf', 'docx'], accept_multiple_files=True)
    skills_input = st.text_input("Enter skills (comma-separated)", "flutter, python, machine learning, data analysis")
    skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

    if st.button("Process Resumes"):
        results = []
        with st.spinner("Processing resumes..."):
            for file in uploaded_files:
                file_ext = os.path.splitext(file.name)[-1].lower()
                log_action(file.name, "File Uploaded", f"Extension: {file_ext}")

                if file_ext == ".pdf":
                    resume_text = extract_text_from_pdf(file)
                    st.write("Extracted text preview:", repr(resume_text[:500]))
                elif file_ext == ".docx":
                    resume_text = extract_text_from_docx(file)
                else:
                    st.error(f"Unsupported file type: {file_ext}")
                    continue

                resume_score = score_resume(resume_text, skills)
                results.append({
                    "Filename": file.name,
                    "Score": resume_score,
                    "Snippet": resume_text[:100] + "..." if len(resume_text) > 100 else resume_text
                })
                log_action(file.name, "Processed Resume", f"Keyword Score: {resume_score}")

            if results:
                df_results = pd.DataFrame(results)
                df_results = df_results.sort_values(by="Score", ascending=False)
                st.subheader("Ranked Resumes")
                st.dataframe(df_results)
                st.balloons()  # Celebration animation when done
            else:
                st.write("No Resumes Processed.")

else:
    st.markdown('<h1 class="main-title">ATS Scoring</h1>', unsafe_allow_html=True)
    st.write("Paste a Job Description to compute an ATS score for each resume.")

    job_desc = st.text_area("Enter Job Description", "Enter the job description here...")
    uploaded_files = st.file_uploader("Upload Resume Files", type=['pdf', 'docx'], accept_multiple_files=True)

    if st.button("Process Resume for ATS Scoring"):
        results = []
        import re
        def ats_score(resume_text, job_desc):
            resume_text_lower = resume_text.lower()
            job_desc_lower = job_desc.lower()
            keywords = re.findall(r'\b\w+\b', job_desc_lower)
            score = 0
            for word in keywords:
                score += resume_text_lower.count(word)
            return score

        with st.spinner("Processing resumes for ATS scoring..."):
            for file in uploaded_files:
                file_ext = os.path.splitext(file.name)[-1].lower()
                log_action(file.name, "File Uploaded", f"Extension: {file_ext}")

                if file_ext == ".pdf":
                    resume_text = extract_text_from_pdf(file)
                elif file_ext == ".docx":
                    resume_text = extract_text_from_docx(file)
                else:
                    st.error(f"Unsupported file type: {file_ext}")
                    continue

                simple_ats = ats_score(resume_text, job_desc)
                results.append({
                    "Filename": file.name,
                    "Simple ATS Score": simple_ats,
                    "Snippet": resume_text[:100] + "..." if len(resume_text) > 100 else resume_text
                })
                # Generate AI feedback and display it inline
                feedback = generate_feedback(resume_text)
                st.markdown(f"**AI Feedback for {file.name}:** {feedback}")
                log_action(file.name, "Processed ATS Resume", f"Simple ATS Score: {simple_ats}, {feedback}")

            if results:
                df_results = pd.DataFrame(results)
                df_results = df_results.sort_values(by="Simple ATS Score", ascending=False)
                st.subheader("Ranked Resumes by ATS Score")
                st.dataframe(df_results)
                st.balloons()
            else:
                st.write("No Resumes Processed.")


# Footer with social media links
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p style="font-size: 16px;">👨‍💻 Developed by <strong>Mehdi Abbas Nathani</strong></p>
        <p>📢 Connect with me:</p>
        <a href="https://www.linkedin.com/in/mehdinathani/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
        </a>
        &nbsp;&nbsp;
        <a href="https://github.com/mehdinathani" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
        </a>
        &nbsp;&nbsp;
        <a href="https://www.fiverr.com/sellers/mehdinathani/" target="_blank">
            <img src="https://cdn.worldvectorlogo.com/logos/fiverr-1.svg" width="30">
        </a>
    </div>
""", unsafe_allow_html=True)
st.success("Thank you for using RankMyResume! 🚀")
