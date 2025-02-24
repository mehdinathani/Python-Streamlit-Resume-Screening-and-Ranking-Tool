def score_resume(resume_text, skills):
    """
    Scores a resume based on the presence of keywords.
    
    Parameters:
    - resume_text (str): The text from the resume.
    - skills (list): A list of skills/keywords to look for.
    
    Returns:
    - score (int): The count of skills found in the resume.
    """
    score = 0
    resume_text_lower = resume_text.lower()
    for skill in skills:
        count = resume_text_lower.count(skill.lower())
        score += count
    return score