# Resume content template — copy this file to resume_data.py and fill in your details
# resume_data.py is gitignored so your personal information stays local

CONTACT_INFO = {
    "name": "Your Name",
    "phone": "000-000-0000",
    "email": "you@email.com",
    "location": "City, State"
}

COMPANY = "Company Name"
ROLE = "Job Title"

# Set this to the folder where you want .docx files saved
OUTPUT_FOLDER = r"C:\Path\To\Your\Output\Folder"

RESUME = {
    "summary": (
        "Your summary here."
    ),
    "experience": [
        {
            "employer": "Employer Name",
            "location": "City, State",
            "dates": "Month Year–Month Year",
            "roles": [
                {
                    "title": "Job Title",
                    "bullets": [
                        "Bullet point one.",
                        "Bullet point two.",
                    ]
                }
            ]
        }
    ],
    "education": [
        {
            "institution": "University Name",
            "location": "City, State",
            "degree": "Degree, Field. Honors."
        }
    ],
    "skills": [
        {"label": "Technical:", "content": "SQL, Python, R, ..."},
        {"label": "Methods:", "content": "Statistical analysis, A/B testing, ..."},
    ]
}
