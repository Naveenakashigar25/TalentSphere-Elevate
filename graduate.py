import streamlit as st
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
import PyPDF2
def generate_graduate_report():

    filename = "Graduate_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>TalentSphere Elevate</b>", styles["Title"]))

    story.append(Paragraph("Graduate Assessment Report", styles["Heading1"]))
    story.append(Paragraph("<b>Personal Information</b>", styles["Heading2"]))

    story.append(Paragraph(f"Name: {st.session_state.get('grad_name','')}", styles["Normal"]))
    story.append(Paragraph(f"Email: {st.session_state.get('grad_email','')}", styles["Normal"]))
    story.append(Paragraph(f"Phone: {st.session_state.get('grad_phone','')}", styles["Normal"]))
    story.append(Paragraph(f"College: {st.session_state.get('grad_college','')}", styles["Normal"]))
    story.append(Paragraph(f"Degree: {st.session_state.get('grad_degree','')}", styles["Normal"]))
    story.append(Paragraph(f"Branch: {st.session_state.get('grad_branch','')}", styles["Normal"]))
    story.append(Paragraph(f"CGPA: {st.session_state.get('grad_cgpa','')}", styles["Normal"]))
    story.append(Paragraph("<b>ATS Resume Checker</b>", styles["Heading2"]))
    story.append(Paragraph(
    f"ATS Score: {st.session_state.get('ats_score', 0)}/100",
    styles["Normal"]
    ))
    story.append(Paragraph(
    f"Recommendation : {st.session_state.get('ats_recommendation','')}",
        styles["Normal"]))
    
    # ---------------- Job Recommendation ----------------

    story.append(Paragraph("<b>Job Recommendation</b>", styles["Heading2"]))


    story.append(Paragraph(
    f"<b>Degree:</b> {st.session_state.get('job_degree', 'Not Selected')}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Preferred Domain:</b> {st.session_state.get('job_domain', 'Not Selected')}",
    styles["Normal"]
    ))

    skills = st.session_state.get("job_skills", [])

    story.append(Paragraph(
    f"<b>Skills:</b> {', '.join(skills) if skills else 'Not Selected'}",
    styles["Normal"]
    ))


    story.append(Paragraph("<b>Recommended Jobs:</b>", styles["Heading3"]))

    jobs = st.session_state.get("recommended_jobs", [])

    if jobs:
        for role, company in jobs:
            story.append(
                Paragraph(f"• {role} - {company}", styles["Normal"])
            )
    else:
        story.append(
            Paragraph("No job recommendations available.", styles["Normal"])
        )

    story.append(Paragraph("<b>Aptitude Assessment</b>", styles["Heading2"]))

    story.append(Paragraph(
    f"Score: {st.session_state.get('aptitude_score',0):.2f}%",
        styles["Normal"]
    ))

    # ---------------- Technical Skills Assessment ----------------

    story.append(Paragraph("<b>Technical Skills Assessment</b>", styles["Heading2"]))


    story.append(
    Paragraph(
        f"<b>Correct Answers:</b> "
        f"{st.session_state.get('technical_correct', 0)}/"
        f"{st.session_state.get('technical_total', 0)}",
        styles["Normal"]
    )
    )

    story.append(
    Paragraph(
        f"<b>Technical Score:</b> "
        f"{st.session_state.get('technical_score', 0):.2f}%",
        styles["Normal"]
    )
    )

    story.append(
    Paragraph(
        f"<b>Recommendation:</b> "
        f"{st.session_state.get('technical_recommendation', 'Not Attempted')}",
        styles["Normal"]
    )
    )

    
    story.append(Paragraph("<b>Mock Interview</b>", styles["Heading2"]))

    story.append(Paragraph(
    f"Score: {st.session_state.get('mock_score', 0)}%",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"Recommendation: {st.session_state.get('mock_recommendation', 'Not Attempted')}",
    styles["Normal"]
    ))
    story.append(Paragraph("<b>Skill Gap Analyzer</b>", styles["Heading2"]))

    story.append(Paragraph(
    f"<b>Target Role:</b> {st.session_state.get('skill_gap_role', 'Not Selected')}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Skill Match:</b> {st.session_state.get('skill_gap_score', 0):.2f}%",
    styles["Normal"]
    ))

    story.append(Paragraph("<b>Skills You Have:</b>", styles["Heading3"]))

    matched = st.session_state.get("skill_gap_matched", [])

    if matched:
        for skill in matched:
            story.append(Paragraph(f"• {skill}", styles["Normal"]))
    else:
        story.append(Paragraph("None", styles["Normal"]))

    story.append(Paragraph("<b>Skills to Learn:</b>", styles["Heading3"]))

    missing = st.session_state.get("skill_gap_missing", [])

    if missing:
        for skill in missing:
            story.append(Paragraph(f"• {skill}", styles["Normal"]))
    else:
        story.append(Paragraph("None", styles["Normal"]))
    
    

    story.append(Paragraph("<b>LinkedIn Profile Review</b>", styles["Heading2"]))

    story.append(Paragraph(
    f"<b>LinkedIn Profile:</b> {st.session_state.get('linkedin_profile', 'N/A')}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>LinkedIn Score:</b> {st.session_state.get('linkedin_score', 0)}/100",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Skills Added:</b> {st.session_state.get('linkedin_skills', 0)}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Certifications:</b> {st.session_state.get('linkedin_certifications', 0)}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Projects:</b> {st.session_state.get('linkedin_projects', 0)}",
    styles["Normal"]
    ))

    story.append(Paragraph(
    f"<b>Suggestions:</b><br/>{st.session_state.get('linkedin_recommendation', 'Not Reviewed').replace(chr(10), '<br/>')}",
    styles["Normal"]
    ))


    story.append(Paragraph("<b>Recommended Courses</b>", styles["Heading2"]))

    courses = st.session_state.get("recommended_courses", [])

    if courses:
        for course in courses:
            story.append(Paragraph(f"• {course}", styles["Normal"]))
    else:
        story.append(Paragraph("No course recommendations available.", styles["Normal"]))

    doc.build(story)
    return filename


def graduate_dashboard():

    st.title("🎓 Graduate Dashboard")

    feature = st.sidebar.selectbox(
        "Select Feature",
        [
            "Home",
            "👤 Personal Information",
            "Resume Builder",
            "ATS Resume Checker",
            "Job Recommendation",
            "Coding Practice",
            "Daily Coding Challenge",
            "Aptitude Practice",
            "Technical Skills",
            "Mock Interview",
            "Skill Gap Analyzer",
            "LinkedIn Profile Review",
            "Recommended Courses",
            "📄 Download Report"
        ]
    )

    # ---------------- HOME ----------------

    if feature == "Home":

        st.header("Welcome")

        st.write("""
TalentSphere Elevate helps graduate students prepare for placements,improve technical skills, build professional resumes, and become
industry ready.
""")
        
    #--------------personal information-------------------

    if feature == "👤 Personal Information":

        st.title("👤 Graduate Profile Information")

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
            "Full Name",
            value=st.session_state.get("grad_name", "")
            )

            email = st.text_input(
            "Email Address",
            value=st.session_state.get("grad_email", "")
            )

            phone = st.text_input(
            "Phone Number",
            value=st.session_state.get("grad_phone", "")
            )

            dob = st.date_input(
            "Date of Birth",
            value=date(2002, 1, 1),
            min_value=date(1995, 1, 1),
            max_value=date.today()
            )

            gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
            )

        with col2:

            college = st.text_input(
            "College Name",
            value=st.session_state.get("grad_college", "")
            )

            degree = st.selectbox(
                "Degree",
                [
                "B.E.",
                "B.Tech",
                "B.Sc",
                "BCA",
                "MCA",
                "M.Tech",
                "MBA",
                "Other"
                ]
            )

            branch = st.selectbox(
                "Branch",
                [
                "Computer Science",
                "Information Science",
                "Electronics & Communication",
                "Electrical",
                "Mechanical",
                "Civil",
                "Artificial Intelligence",
                "Data Science",
                "Other"
                ]
            )

            graduation_year = st.selectbox(
            "Graduation Year",
            list(range(2020, 2036))
            )

            cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            step=0.1
            )

        st.subheader("Skills")

        skills = st.multiselect(
            "Select Your Skills",
            [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "SQL",
            "HTML",
            "CSS",
            "React",
            "Node.js",
            "Machine Learning",
            "Artificial Intelligence",
            "Data Science",
            "Power BI",
            "Excel",
            "Communication",
            "Problem Solving"
            ],
            default=st.session_state.get("grad_skills", [])
        )

        st.subheader("Career Interest")

        interest = st.selectbox(
            "Preferred Career",
            [
            "Software Developer",
            "Web Developer",
            "Data Analyst",
            "AI Engineer",
            "ML Engineer",
            "Cyber Security",
            "Cloud Engineer",
            "Testing",
            "Business Analyst",
            "Not Decided"
            ]
        )

        if st.button("💾 Save Profile"):

            st.session_state.grad_name = name
            st.session_state.grad_email = email
            st.session_state.grad_phone = phone
            st.session_state.grad_dob = dob.strftime("%d-%m-%Y")
            st.session_state.grad_gender = gender
            st.session_state.grad_college = college
            st.session_state.grad_degree = degree
            st.session_state.grad_branch = branch
            st.session_state.grad_year = graduation_year
            st.session_state.grad_cgpa = cgpa
            st.session_state.grad_skills = skills
            st.session_state.grad_interest = interest

            st.success("✅ Profile Saved Successfully!")

            st.balloons()

        st.divider()  
       

        st.subheader("Saved Profile")

        if "grad_name" in st.session_state:

            st.write("**Name:**", st.session_state.grad_name)
            st.write("**Email:**", st.session_state.grad_email)
            st.write("**Phone:**", st.session_state.grad_phone)
            st.write("**Date of Birth:**", st.session_state.grad_dob)
            st.write("**Gender:**", st.session_state.grad_gender)
            st.write("**College:**", st.session_state.grad_college)
            st.write("**Degree:**", st.session_state.grad_degree)
            st.write("**Branch:**", st.session_state.grad_branch)
            st.write("**Graduation Year:**", st.session_state.grad_year)
            st.write("**CGPA:**", st.session_state.grad_cgpa)
            st.write("**Skills:**", ", ".join(st.session_state.grad_skills))
            st.write("**Career Interest:**", st.session_state.grad_interest)

    # ---------------- RESUME BUILDER ----------------

    elif feature == "Resume Builder":

        st.header("Resume Builder")

        st.write("Fill in your details to generate your resume.")

    # -----------------------------
    # Personal Information
    # -----------------------------

        st.header("👤 Personal Information")

        name = st.text_input("Full Name")

        email = st.text_input("Email")

        phone = st.text_input("Phone Number")

        address = st.text_area("Address")

        linkedin = st.text_input("LinkedIn Profile")

        github = st.text_input("GitHub Profile")

    # -----------------------------
    # Career Objective
    # -----------------------------

        st.header("🎯 Career Objective")

        objective = st.text_area("Career Objective")

    # -----------------------------
    # Education
    # -----------------------------

        st.header("🎓 Education")

        college = st.text_input("College Name")

        degree = st.text_input("Degree")

        branch = st.text_input("Branch")

        cgpa = st.text_input("CGPA")

        year = st.text_input("Graduation Year")

    # -----------------------------
    # Skills
    # -----------------------------

        st.header("💻 Skills")

        skills = st.text_area(
            "Enter skills separated by commas"
        )

    # -----------------------------
    # Projects
    # -----------------------------

        st.header("📁 Projects")

        project = st.text_area("Project Details")

    # -----------------------------
    # Internship
    # -----------------------------

        st.header("💼 Internship")

        internship = st.text_area("Internship Details")

    # -----------------------------
    # Certifications
    # -----------------------------

        st.header("🏆 Certifications")

        certificates = st.text_area("Certificates")

    # -----------------------------
    # Languages
    # -----------------------------

        st.header("🌍 Languages")

        languages = st.text_input(
            "Languages Known"
        )

    # -----------------------------
    # Generate Resume
    # -----------------------------

        if st.button("📄 Generate Resume"):

            filename = "Resume.pdf"

            doc = SimpleDocTemplate(filename)

            styles = getSampleStyleSheet()

            story = []

            story.append(Paragraph(f"<b><font size=18>{name}</font></b>", styles["Title"]))

            story.append(Paragraph(f"<b>Email:</b> {email}", styles["Normal"]))
            story.append(Paragraph(f"<b>Phone:</b> {phone}", styles["Normal"]))
            story.append(Paragraph(f"<b>Address:</b> {address}", styles["Normal"]))
            story.append(Paragraph(f"<b>LinkedIn:</b> {linkedin}", styles["Normal"]))
            story.append(Paragraph(f"<b>GitHub:</b> {github}", styles["Normal"]))

            story.append(Paragraph("<br/><b>Career Objective</b>", styles["Heading2"]))
            story.append(Paragraph(objective, styles["Normal"]))

            story.append(Paragraph("<br/><b>Education</b>", styles["Heading2"]))
            story.append(
                Paragraph(
                    f"{degree} ({branch})<br/>{college}<br/>CGPA : {cgpa}<br/>Graduation : {year}",
                    styles["Normal"],
                )
            )

            story.append(Paragraph("<br/><b>Skills</b>", styles["Heading2"]))
            story.append(Paragraph(skills, styles["Normal"]))

            story.append(Paragraph("<br/><b>Projects</b>", styles["Heading2"]))
            story.append(Paragraph(project, styles["Normal"]))

            story.append(Paragraph("<br/><b>Internship</b>", styles["Heading2"]))
            story.append(Paragraph(internship, styles["Normal"]))

            story.append(Paragraph("<br/><b>Certifications</b>", styles["Heading2"]))
            story.append(Paragraph(certificates, styles["Normal"]))

            story.append(Paragraph("<br/><b>Languages</b>", styles["Heading2"]))
            story.append(Paragraph(languages, styles["Normal"]))

            doc.build(story)

            st.success("✅ Resume Generated Successfully!")

            with open(filename, "rb") as pdf:
                st.download_button(
                    label="⬇ Download Resume",
                    data=pdf,
                    file_name="Resume.pdf",
                    mime="application/pdf"
                )

            if os.path.exists(filename):
                os.remove(filename)

    # ---------------- ATS ----------------

    elif feature == "ATS Resume Checker":

        st.header("ATS Resume Checker")

        st.info("Upload your resume for ATS analysis.")
        st.header("📊 ATS Resume Checker")

        uploaded_file = st.file_uploader(
            "Upload Resume",
            type=["pdf", "docx"]
        )

        if uploaded_file is not None:

            resume_text = ""

        # Read PDF
            if uploaded_file.type == "application/pdf":
                pdf = PyPDF2.PdfReader(uploaded_file)

                for page in pdf.pages:
                    if page.extract_text():
                        resume_text += page.extract_text()

        # Read DOCX
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = Document(uploaded_file)

                for para in doc.paragraphs:
                    resume_text += para.text

            resume_text = resume_text.lower()

            score = 0

            st.subheader("Resume Analysis")

        # Contact Details
            if "@" in resume_text:
                st.success("✅ Email Found")
                score += 10
            else:
                st.error("❌ Email Missing")

        # Education
            if any(word in resume_text for word in ["b.e", "btech", "degree", "education"]):
                st.success("✅ Education Found")
                score += 15
            else:
                st.error("❌ Education Missing")

        # Skills
            skills = [
                "python",
                "java",
                "c",
                "C++",
                "C#",
                "sql",
                "html",
                "css",
                "javascript",
                "git",
                "github"
            ]

            found_skills = []

            for skill in skills:
                if skill in resume_text:
                    found_skills.append(skill)

            skill_score = min(len(found_skills) * 2, 20)
            score += skill_score

            st.success(f"✅ Skills Found : {len(found_skills)}")

        # Projects
            if "project" in resume_text:
                st.success("✅ Projects Added")
                score += 20
            else:
                st.error("❌ Projects Missing")

        # Internship
            if "internship" in resume_text:
                st.success("✅ Internship Found")
                score += 10
            else:
                st.warning("⚠ Internship Missing")

        # Certifications
            if "certification" in resume_text or "certificate" in resume_text:
                st.success("✅ Certifications Found")
                score += 10
            else:
                st.warning("⚠ Certifications Missing")

        # GitHub
            if "github" in resume_text:
                st.success("✅ GitHub Profile Added")
                score += 5
            else:
                st.warning("⚠ GitHub Missing")

        # LinkedIn
            if "linkedin" in resume_text:
                st.success("✅ LinkedIn Profile Added")
                score += 5
            else:
                st.warning("⚠ LinkedIn Missing")

        # Resume Length
            if len(resume_text.split()) > 200:
                score += 5

        # Score
            if score > 100:
                score = 100

            st.divider()

            st.subheader("📊 ATS Score")

            st.progress(score / 100)

            st.metric("ATS Score", f"{score}/100")
            st.session_state.ats_score = score
                       

            st.divider()

            st.subheader("💡 Suggestions")

            if score >= 90:
                st.success("Excellent! Your resume is ATS-friendly.")

            elif score >= 75:
                st.info("Good resume. Add more projects and certifications.")

            elif score >= 60:
                st.warning("Improve your technical skills and resume sections.")

            else:
                st.error("Your resume needs significant improvements.")

                st.subheader("🎯 Placement Readiness")

            if score >= 85:
                st.success("★★★★★ Excellent")

            elif score >= 70:
                st.success("★★★★ Good")

            elif score >= 50:
                st.warning("★★★ Average")

            else:
                st.error("★★ Needs Improvement")

    # ---------------- JOB ----------------

    elif feature == "Job Recommendation":

        st.header("Job Recommendation")

        st.info("Recommended jobs based on your skills.")

        st.write("Get job recommendations based on your skills and interests.")


        degree = st.selectbox(
            "Degree",
            ["B.E", "B.Tech", "BCA", "B.Sc", "MCA", "M.Tech"]
        )

        skills = st.multiselect(
            "Select Your Skills",
            [
                "Python",
                "Java",
                "C",
                "C++",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Machine Learning",
                "Data Analysis",
                "Git",
                "Communication",
                "Problem Solving"
            ]
        )

        interest = st.selectbox(
            "Interested Domain",
            [
                "Software Development",
                "Data Science",
                "Artificial Intelligence",
                "Cyber Security",
                "Web Development",
                "Cloud Computing",
                "Embedded Systems",
                "Testing",
                "Business Analyst"
            ]
        )

        cgpa = st.slider("CGPA", 5.0, 10.0, 7.5)

        if st.button("🔍 Recommend Jobs"):

            st.subheader("🎯 Recommended Jobs")
        
            recommendations = []

            if interest == "Software Development":
                recommendations.extend([
                    "Software Engineer",
                    "Python Developer",
                    "Full Stack Developer"
                ])

            if interest == "Data Science":
                recommendations.extend([
                "Data Analyst",
                "Data Scientist",
                "Business Intelligence Analyst"
                ])

            if interest == "Artificial Intelligence":
                recommendations.extend([
                "AI Engineer",
                "Machine Learning Engineer"
                ])

            if interest == "Cyber Security":
                recommendations.extend([
                "Cyber Security Analyst",
                "Security Engineer"
                ])

            if interest == "Web Development":
                recommendations.extend([
                "Frontend Developer",
                "Backend Developer",
                "Web Developer"
                ])

            if interest == "Cloud Computing":
                recommendations.extend([
                "Cloud Engineer",
                "DevOps Engineer"
                ])

            if interest == "Embedded Systems":
                recommendations.extend([
                "Embedded Engineer",
                "IoT Engineer"
                ])

            if interest == "Testing":
                recommendations.extend([
                "Software Test Engineer",
                "QA Engineer"
                ])

            if interest == "Business Analyst":
                recommendations.extend([
                "Business Analyst",
                "Product Analyst"
                ])
            st.session_state.job_degree = degree
            st.session_state.job_domain = interest
            st.session_state.job_skills = skills
            st.session_state.job_recommendations = recommendations


            for job in recommendations:
                st.success(f"✅ {job}")

                st.subheader("📚 Recommended Skills to Learn")

            if "Python" not in skills:
                st.write("• Learn Python")

            if "SQL" not in skills:
                st.write("• Learn SQL")

            if "Git" not in skills:
                st.write("• Learn Git & GitHub")

            if "Communication" not in skills:
                st.write("• Improve Communication Skills")

            if cgpa < 7.0:
                st.warning("Improve your CGPA if possible to increase placement opportunities.")

                st.subheader("🚀 Placement Readiness")

            if cgpa >= 8.5:
                st.success("Excellent! You are highly placement ready.")

            elif cgpa >= 7.5:
                st.info("Good! Continue improving your technical skills.")

            else:
                st.warning("Focus on technical skills, projects, and aptitude preparation.")
               
    # ---------------- CODING ----------------

    elif feature == "Coding Practice":

        st.header("Coding Practice")

        language = st.selectbox(
        "Select Programming Language",
        ["Python"]
        )

        difficulty = st.selectbox(
        "Select Difficulty Level",
        ["Easy", "Medium", "Hard"]
        )

        questions = {

            ("Python", "Easy"): [
                {
                    "title": "Print Hello World",
                    "question": "Write a program to print Hello World.",
                    "sample_output": "Hello World"
                },
                {
                    "title":"Even or Odd",
                    "description":"Read an integer and determine whether it is Even or Odd.",
                    "input":"15",
                    "output":"Odd"
                },
                {
                    "title":"Largest of Two Numbers",
                    "description":"Read two numbers and print the largest.",
                    "input":"15 20",
                    "output":"20"
                },
                {
                    "title":"Swap Two Numbers",
                    "description":"Swap two numbers without using a third variable.",
                    "input":"5 8",
                    "output":"8 5"
                },
                {
                    "title":"Area of Circle",
                    "description":"Calculate the area of a circle.",
                    "input":"7",
                    "output":"153.94"
                },

                {
                    "title":"Multiplication Table",
                    "description":"Print the multiplication table of a given number.",
                    "input":"5",
                    "output":"5 10 15 ... 50"
                },

                {
                    "title":"Factorial",
                    "description":"Find the factorial of a given number.",
                    "input":"5",
                    "output":"120"
                },

                {
                    "title":"Reverse Number",
                    "description":"Reverse the digits of a given integer.",
                    "input":"1234",
                    "output":"4321"
                },
                {
                    "title": "Sum of Two Numbers",
                    "question": "Read two integers and print their sum.",
                    "sample_input": "10 20",
                    "sample_output": "30"
                }
                
            ],

            ("Python", "Medium"): [
                {
                    "title": "Palindrome Number",
                    "question": "Check whether a number is palindrome.",
                    "sample_input": "121",
                    "sample_output": "Palindrome"
                },
           
                {
                    "title":"Remove Duplicate Characters",
                    "description":"Remove duplicate characters from a string.",
                    "sample_input":"programming",
                    "expected_output":"progamin"
                },

                {
                    "title":"Second Largest Element",
                    "description":"Find the second largest element in a list.",
                    "sample_input":"10 20 30 40 50",
                    "expected_output":"40"
                },

                {
                    "title":"Linear Search",
                    "description":"Search an element using Linear Search.",
                    "sample_input":"10 20 30 40 50\n30",
                    "expected_output":"Element Found"
                },

                {
                    "title":"Binary Search",
                    "description":"Perform Binary Search on a sorted list.",
                    "sample_input":"10 20 30 40 50\n20",
                    "expected_output":"Element Found"
                },

                {
                    "title":"Bubble Sort",
                    "description":"Sort a list using Bubble Sort.",
                    "sample_input":"5 4 3 2 1",
                    "expected_output":"1 2 3 4 5"
                },

                {
                    "title":"Selection Sort",
                    "description":"Sort a list using Selection Sort.",
                    "sample_input":"64 25 12 22 11",
                    "expected_output":"11 12 22 25 64"
                },

                {
                    "title":"Insertion Sort",
                    "description":"Sort a list using Insertion Sort.",
                    "sample_input":"12 11 13 5 6",
                    "expected_output":"5 6 11 12 13"
                },

                {
                    "title":"Matrix Addition",
                    "description":"Add two matrices.",
                    "sample_input":"2x2 Matrix",
                    "expected_output":"Result Matrix"
                },

                {
                    "title":"Matrix Multiplication",
                    "description":"Multiply two matrices.",
                    "sample_input":"2x2 Matrix",
                    "expected_output":"Result Matrix"
                },

                {
                    "title":"Transpose Matrix",
                    "description":"Find the transpose of a matrix.",
                    "sample_input":"2x3 Matrix",
                    "expected_output":"Transpose Matrix"
                },

                {
                    "title":"Find Common Elements",
                    "description":"Find common elements between two lists.",
                    "sample_input":"1 2 3 4\n3 4 5 6",
                    "expected_output":"3 4"
                },

                {
                    "title":"Frequency of Elements",
                    "description":"Count the frequency of each element in a list.",
                    "sample_input":"1 2 2 3 3 3",
                    "expected_output":"1:1 2:2 3:3"
                },

                {
                    "title":"Decimal to Binary",
                    "description":"Convert a decimal number into binary.",
                    "sample_input":"25",
                    "expected_output":"11001"
                },

                {
                    "title":"Binary to Decimal",
                    "description":"Convert a binary number into decimal.",
                    "sample_input":"10101",
                    "expected_output":"21"
                },

                {
                    "title":"Merge Two Lists",
                    "description":"Merge two sorted lists into a single sorted list.",
                    "sample_input":"1 3 5\n2 4 6",
                    "expected_output":"1 2 3 4 5 6"
                },

                {
                    "title":"Dictionary Sort",
                    "description":"Sort a dictionary based on values.",
                    "sample_input":"{'A':5,'B':2,'C':8}",
                    "expected_output":"{'B':2,'A':5,'C':8}"
            
                }
            ],

            ("Python", "Hard"): [
                {
                    "title": "Prime Numbers",
                    "question": "Print all prime numbers from 1 to N.",
                    "sample_input": "20",
                    "sample_output": "2 3 5 7 11 13 17 19"
                },
                {
                    "title":"N-Queens Problem",
                    "description":"Place N queens on an N×N chessboard such that no two queens attack each other.",
                    "sample_input":"4",
                    "expected_output":"One valid arrangement of queens"
                },

                {
                    "title":"Sudoku Solver",
                    "description":"Solve a given Sudoku puzzle using backtracking.",
                    "sample_input":"9x9 Sudoku Grid",
                    "expected_output":"Solved Sudoku Grid"
                },

                {
                    "title":"Rat in a Maze",
                    "description":"Find all possible paths for a rat to reach the destination in a maze.",
                    "sample_input":"4x4 Maze",
                    "expected_output":"All Valid Paths"
                },

                {
                    "title":"Knight's Tour",
                    "description":"Find a Knight's Tour for an N×N chessboard.",
                    "sample_input":"5",
                    "expected_output":"Valid Knight Tour"
                },
                {
                    "title":"0/1 Knapsack",
                    "description":"Solve the 0/1 Knapsack problem using Dynamic Programming.",
                    "sample_input":"Weights=10 20 30\nValues=60 100 120\nCapacity=50",
                    "expected_output":"220"
                },

                {
                    "title":"Dijkstra Algorithm",
                    "description":"Find the shortest path from a source vertex using Dijkstra's Algorithm.",
                    "sample_input":"Weighted Graph",
                    "expected_output":"Shortest Distances"
                },

                {
                    "title":"Breadth First Search",
                    "description":"Traverse a graph using BFS.",
                    "sample_input":"Graph",
                    "expected_output":"BFS Traversal"
                },
            ]
        }

        if (language, difficulty) in questions:

            question = st.selectbox(
                "Select Question",
                [q["title"] for q in questions[(language, difficulty)]]
            )

            selected = next(
                q for q in questions[(language, difficulty)]
                if q["title"] == question
            )

            st.subheader(selected["title"])

            st.write(selected["question"])

            if "sample_input" in selected:
                st.code(selected["sample_input"], language="text")

            st.write("### Expected Output")
            st.code(selected["sample_output"])

            code = st.text_area(
                "Write your code here",
                height=300
            )

            if language == "Python":

                if st.button("▶ Run Code"):

                    try:

                        exec_globals = {}

                        exec(code, exec_globals)

                        st.success("Program Executed Successfully")

                    except Exception as e:

                        st.error(f"Error:\n{e}")

            else:

                st.info(
                    "Code execution for C, C++, and Java requires an online compiler such as Judge0. You can still practice writing your code here."
                )

        else:

            st.warning("Questions will be added soon.")
        
    # ---------------- DAILY CHALLENGE ----------------

    elif feature == "Daily Coding Challenge":

        st.header("Daily Coding Challenge")

        from datetime import datetime

        daily_questions = [

            {
            "title": "Print Hello World",
            "difficulty": "Easy",
            "language": "Python",
            "question": "Write a program to print Hello World.",
            "sample_input": "No Input",
            "sample_output": "Hello World"
            },

            {
            "title": "Even or Odd",
            "difficulty": "Easy",
            "language": "Python",
            "question": "Check whether a number is Even or Odd.",
            "sample_input": "25",
            "sample_output": "Odd"
            },

            {
            "title": "Palindrome Number",
            "difficulty": "Medium",
            "language": "Python",
            "question": "Check whether a number is palindrome.",
            "sample_input": "121",
            "sample_output": "Palindrome"
            },

            {
            "title": "Second Largest Element",
            "difficulty": "Medium",
            "language": "Python",
            "question": "Find the second largest number in a list.",
            "sample_input": "10 20 40 30 50",
            "sample_output": "40"
            },

            {
            "title": "Merge Sort",
            "difficulty": "Hard",
            "language": "Python",
            "question": "Implement Merge Sort.",
            "sample_input": "38 27 43 3 9 82 10",
            "sample_output": "3 9 10 27 38 43 82"
            },

            {
            "title": "Dijkstra Algorithm",
            "difficulty": "Hard",
            "language": "Python",
            "question": "Find the shortest path using Dijkstra Algorithm.",
            "sample_input": "Weighted Graph",
            "sample_output": "Shortest Path"
            }  

        ]

    # Different question each day
        day = datetime.now().day

        today_question = daily_questions[day % len(daily_questions)]

        st.subheader(today_question["title"])

        st.write("**Difficulty:**", today_question["difficulty"])
        st.write("**Language:**", today_question["language"])

        st.write("### Problem Statement")
        st.write(today_question["question"])

        st.write("### Sample Input")
        st.code(today_question["sample_input"])

        st.write("### Expected Output")
        st.code(today_question["sample_output"])

        code = st.text_area(
            "Write your code here",
            height=300
        )

        if st.button("Submit Today's Solution"):

            st.success("✅ Solution Submitted Successfully!")

            st.balloons()

            st.session_state.daily_completed = True

        if st.session_state.get("daily_completed", False):

            st.success("🎉 Today's Coding Challenge Completed!")

    # ---------------- APTITUDE ----------------

    elif feature == "Aptitude Practice":

        st.header("Aptitude Practice")

        Aptitude_questions = [

        {
        "question":"1. If the ratio of two numbers is 3:5 and their sum is 64, what is the larger number?",
        "options":["24","40","36","48"],
        "answer":"40"
        },

        {
        "question":"2. A train 180 m long passes a pole in 9 seconds. What is its speed?",
        "options":["20 m/s","18 m/s","15 m/s","25 m/s"],
        "answer":"20 m/s"
        },

        {
        "question":"3. The average of 5 numbers is 28. If one number is removed, the average becomes 25. Find the removed number.",
        "options":["35","40","38","45"],
        "answer":"40"
        },

        {
        "question":"4. A sum amounts to ₹12,100 in 2 years at 10% simple interest. Find the principal.",
        "options":["₹10,000","₹11,000","₹9,000","₹12,000"],
        "answer":"₹11,000"
        },

        {
        "question":"5. If x + y = 15 and xy = 56, then x² + y² = ?",
        "options":["113","117","125","119"],
        "answer":"113"
        },

        {
        "question":"6. Find the next number: 2, 6, 12, 20, 30, ?",
        "options":["40","42","44","48"],
        "answer":"42"
        },

        {
        "question":"7. A shopkeeper gives 10% discount on an item marked ₹500. What is the selling price?",
        "options":["₹450","₹400","₹425","₹475"],
        "answer":"₹450"
        },

        {
        "question":"8. If 15 men can complete a work in 12 days, how many men are needed to complete it in 9 days?",
        "options":["20","18","15","25"],
        "answer":"20"
        },

        {
        "question":"9. Which number is odd one out?",
        "options":["27","64","125","216"],
        "answer":"27"
        },

        {
        "question":"10. A boat travels 30 km downstream in 2 hours. Speed of current is 3 km/h. Find speed of boat in still water.",
        "options":["12 km/h","15 km/h","18 km/h","20 km/h"],
        "answer":"12 km/h"
        },

        {
        "question":"11. Statement: All engineers are graduates. Some graduates are programmers. Conclusion?",
        "options":[
        "Some engineers are programmers",
        "Some programmers are graduates",
        "All programmers are engineers",
        "None"
        ],
        "answer":"Some programmers are graduates"
        },

        {
        "question":"12. Find the missing term: B, E, H, K, ?",
        "options":["M","N","O","P"],
        "answer":"N"
        },

        {
        "question":"13. If today is Wednesday, what day will it be after 45 days?",
        "options":["Thursday","Friday","Saturday","Sunday"],
        "answer":"Thursday"
        },

        {
        "question":"14. A cube has how many edges?",
        "options":["8","12","10","16"],
        "answer":"12"
        },

        {
        "question":"15. A person walks 4 km North, then 3 km East. How far is he from the starting point?",
        "options":["5 km","6 km","7 km","4 km"],
        "answer":"5 km"
        },

        {
        "question":"16. Choose the correct synonym of 'Abundant'.",
        "options":["Scarce","Plentiful","Little","Rare"],
        "answer":"Plentiful"
        },

        {
        "question":"17. Fill in the blank: She ____ to the office every day.",
        "options":["go","goes","gone","going"],
        "answer":"goes"
        },

        {
        "question":"18. If the probability of an event is 0.25, what is the probability that it does not occur?",
        "options":["0.25","0.50","0.75","1"],
        "answer":"0.75"
        },

        {
        "question":"19. Which data structure follows FIFO?",
        "options":["Stack","Queue","Tree","Graph"],
        "answer":"Queue"
        },

        {
        "question":"20. Which SQL command is used to retrieve data?",
        "options":["INSERT","UPDATE","SELECT","DELETE"],
        "answer":"SELECT"
        },
          
        {
        "question":"21. If the cost price of an article is ₹800 and it is sold at a profit of 15%, what is the selling price?",
        "options":["₹900","₹920","₹880","₹950"],
        "answer":"₹920"
        },

        {
        "question":"22. Complete the series: 5, 10, 20, 40, ?",
        "options":["60","70","80","90"],
        "answer":"80"
        },

        {
        "question":"23. A man walks 8 km East and then 6 km North. What is the shortest distance from the starting point?",
        "options":["10 km","12 km","14 km","8 km"],
        "answer":"10 km"
        },

        {
        "question":"24. Which number should replace the question mark? 2, 6, 12, 20, 30, ?",
        "options":["40","42","44","46"],
        "answer":"42"
        },

        {
        "question":"25. If 12 workers complete a job in 15 days, how many workers are required to complete it in 9 days?",
        "options":["18","20","22","24"],
        "answer":"20"
        },

        {
        "question":"26. Which one is different?",
        "options":["Square","Rectangle","Triangle","Circle"],
        "answer":"Circle"
        },

        {
        "question":"27. A shopkeeper marks an article 25% above cost price and gives a 10% discount. His profit is?",
        "options":["10%","12.5%","15%","20%"],
        "answer":"12.5%"
        },

        {
        "question":"28. Which SQL clause is used to filter records?",
        "options":["ORDER BY","GROUP BY","WHERE","HAVING"],
        "answer":"WHERE"
        },

        {
        "question":"29. If today is Monday, what day will it be after 100 days?",
        "options":["Tuesday","Wednesday","Thursday","Friday"],
        "answer":"Wednesday"
        },

        {
        "question":"30. Which data structure is used for recursion?",
        "options":["Queue","Stack","Array","Linked List"],
        "answer":"Stack"
        },

        {
        "question":"31. The average of 10 numbers is 50. If one number is removed, the average becomes 48. Find the removed number.",
        "options":["68","70","72","66"],
        "answer":"68"
        },

        {
        "question":"32. Choose the synonym of 'Precise'.",
        "options":["Accurate","Wrong","Confused","Large"],
        "answer":"Accurate"
        },

        {
        "question":"33. Which number is missing? 3, 6, 11, 18, 27, ?",
        "options":["36","38","40","42"],
        "answer":"38"
        },

        {
        "question":"34. Find the odd one out.",
        "options":["Python","Java","HTML","C++"],
        "answer":"HTML"
        },

        {
        "question":"35. A train travels 360 km in 6 hours. What is its speed?",
        "options":["50 km/h","60 km/h","70 km/h","80 km/h"],
        "answer":"60 km/h"
        },

        {
        "question":"36. If A = 1, B = 2, C = 3, then CAB = ?",
        "options":["312","321","123","213"],
        "answer":"312"
        },

        {
        "question":"37. Which company developed Python?",
        "options":["Microsoft","Google","Python Software Foundation","Apple"],
        "answer":"Python Software Foundation"
        },
 
        {
        "question":"38. Fill in the blank: Neither Ram nor his friends ____ present.",
        "options":["is","are","was","be"],
        "answer":"are"
        },

        {
        "question":"39. Which sorting algorithm has the best average time complexity?",
        "options":["Bubble Sort","Selection Sort","Merge Sort","Insertion Sort"],
        "answer":"Merge Sort"
        },

        {
        "question":"40. A cube has how many faces?",
        "options":["4","5","6","8"],
        "answer":"6"
        }
    ]
        for i, q in enumerate(Aptitude_questions):

            st.subheader(f"Question {i+1}")

            st.radio(
            q["question"],
            q["options"],
            key=f"apt_q{i}"
        )

        st.divider()


        if st.button("Submit Aptitude Assessment"):

            score = 0

            for i, q in enumerate(Aptitude_questions):

                if st.session_state.get(f"apt_q{i}") == q["answer"]:
                    score += 1

            percentage = (score / len(Aptitude_questions)) * 100

            st.success(f"Score: {score}/{len(Aptitude_questions)}")
            st.success(f"Percentage: {percentage:.2f}%")       
            st.session_state.aptitude_score = percentage
            st.session_state.aptitude_correct = score
    


  
    # ---------------- TECHNICAL ----------------

    elif feature == "Technical Skills":

        st.header("Technical Skills Assessment")

# ---------------- PYTHON ----------------
        technical_questions = [
        {
        "question":"1. Which keyword is used to define a function in Python?",
        "options":["function","define","def","fun"],
        "answer":"def"
        },

        {
        "question":"2. Which data type is mutable in Python?",
        "options":["Tuple","String","List","Integer"],
        "answer":"List"
        },

        {
        "question":"3. Which symbol is used for comments in Python?",
        "options":["#","//","<!-- -->","/* */"],
        "answer":"#"
        },

        {
        "question":"4. Which function is used to find the length of a list?",
        "options":["count()","size()","len()","length()"],
        "answer":"len()"
        },

        {
        "question":"5. Which keyword is used for exception handling?",
        "options":["error","except","catch","throw"],
        "answer":"except"
        },

# ---------------- SQL ----------------

        {
        "question":"6. Which SQL command is used to retrieve data?",
        "options":["SELECT","INSERT","UPDATE","DELETE"],
        "answer":"SELECT"
        },

        {
        "question":"7. Which clause filters rows?",
        "options":["ORDER BY","GROUP BY","WHERE","HAVING"],
        "answer":"WHERE"
        },

        {
        "question":"8. Which SQL command removes a table?",
        "options":["REMOVE","DELETE","DROP","ERASE"],
        "answer":"DROP"
        },

        {
        "question":"9. Which SQL function counts rows?",
        "options":["COUNT()","SUM()","AVG()","TOTAL()"],
        "answer":"COUNT()"
        },

        {
        "question":"10. Which JOIN returns matching records from both tables?",
        "options":["LEFT JOIN","RIGHT JOIN","INNER JOIN","FULL JOIN"],
        "answer":"INNER JOIN"
        },

# ---------------- DBMS ----------------

        {
        "question":"11. DBMS stands for?",
        "options":[
        "Database Management System",
        "Data Base Memory System",
        "Digital Base Management System",
        "Data Memory Software"
        ],
        "answer":"Database Management System"
        },

        {
        "question":"12. Which key uniquely identifies a record?",
        "options":["Foreign Key","Primary Key","Candidate Key","Composite Key"],
        "answer":"Primary Key"
        },

        {
        "question":"13. Which normal form removes partial dependency?",
        "options":["1NF","2NF","3NF","BCNF"],
        "answer":"2NF"
        },

        {
        "question":"14. Which language is used to define database schema?",
        "options":["DML","DDL","DCL","TCL"],
        "answer":"DDL"
        },

        {
        "question":"15. Which property ensures all-or-nothing transactions?",
        "options":["Consistency","Isolation","Atomicity","Durability"],
        "answer":"Atomicity"
        },

# ---------------- OOP ----------------

        {
        "question":"16. Which OOP concept allows code reuse?",
        "options":["Polymorphism","Inheritance","Abstraction","Encapsulation"],
        "answer":"Inheritance"
        },

        {
        "question":"17. Which concept hides implementation details?",
        "options":["Inheritance","Polymorphism","Abstraction","Overloading"],
        "answer":"Abstraction"
        },

        {
        "question":"18. Which concept binds data and methods together?",
        "options":["Encapsulation","Inheritance","Abstraction","Polymorphism"],
        "answer":"Encapsulation"
        },

        {
        "question":"19. Which feature allows multiple methods with the same name?",
        "options":["Inheritance","Method Overloading","Abstraction","Constructor"],
        "answer":"Method Overloading"
        },

        {
        "question":"20. Which keyword creates an object in Java?",
        "options":["create","new","object","class"],
        "answer":"new"
        },

# ---------------- OPERATING SYSTEM ----------------

        {
        "question":"21. Which scheduling algorithm gives the shortest job first?",
        "options":["FCFS","SJF","Round Robin","Priority"],
        "answer":"SJF"
        },

        {
        "question":"22. Which memory is volatile?",
        "options":["ROM","SSD","RAM","Hard Disk"],
        "answer":"RAM"
        },

        {
        "question":"23. Which OS allows multiple users simultaneously?",
        "options":["Single User","Multi User","Batch OS","Embedded OS"],
        "answer":"Multi User"
        },

        {
        "question":"24. Which system call creates a new process in Unix?",
        "options":["exec()","fork()","wait()","exit()"],
        "answer":"fork()"
        },

        {
        "question":"25. Deadlock occurs when?",
        "options":[
        "CPU is idle",
        "Processes wait indefinitely",
        "Memory is full",
        "Disk is busy"
        ],
        "answer":"Processes wait indefinitely"
        },

# ---------------- COMPUTER NETWORKS ----------------

        {
        "question":"26. Which layer of the OSI model handles routing?",
        "options":["Transport","Network","Application","Session"],
        "answer":"Network"
        },

        {
        "question":"27. HTTP uses which port by default?",
        "options":["20","21","80","443"],
        "answer":"80"
        },

        {
        "question":"28. Which protocol is used to transfer files?",
        "options":["FTP","SMTP","HTTP","DNS"],
        "answer":"FTP"
        },

        {
        "question":"29. What does IP stand for?",
        "options":[
        "Internet Protocol",
        "Internal Process",
        "Internet Process",
        "Internal Protocol"
        ],
        "answer":"Internet Protocol"
        },

        {
        "question":"30. Which device forwards packets between networks?",
        "options":["Hub","Switch","Router","Repeater"],
        "answer":"Router"
        }
    ]
        for i, q in enumerate(technical_questions):

            st.write(f"### Question {i+1}")

            st.radio(
                q["question"],
                q["options"],
                key=f"tech_q{i}"
            )
        if st.button("Submit Technical Assessment"):

            score = 0

            for i, q in enumerate(technical_questions):

                answer = st.session_state.get(f"tech_q{i}")

                if answer == q["answer"]:
                    score += 1

            total = len(technical_questions)
            percentage = (score / total) * 100

    # Recommendation
            if percentage >= 90:
                technical_recommendation = "Excellent technical knowledge. Ready for product-based companies."

            elif percentage >= 75:
                technical_recommendation = "Good technical knowledge. Continue practicing coding and core CS subjects."

            elif percentage >= 60:
                technical_recommendation = "Average performance. Revise Python, SQL, DBMS, OOP, OS and CN."

            else:
                technical_recommendation = "Needs improvement. Strengthen your fundamentals before placements."

    # Save everything
            st.session_state.technical_correct = score
            st.session_state.technical_total = total
            st.session_state.technical_score = percentage
            st.session_state.technical_recommendation = technical_recommendation

            st.success(f"Correct Answers: {score}/{total}")
            st.success(f"Technical Score: {percentage:.2f}%")
            st.info(f"Recommendation: {technical_recommendation}")

            st.progress(percentage / 100)

    # ---------------- MOCK INTERVIEW ----------------

    elif feature == "Mock Interview":

        st.header("Mock Interview")

        st.info("Practice HR and Technical interviews.")
       

        st.write("Answer the following interview questions.")

        interview_questions = [

        "1. Tell me about yourself.",

        "2. Why should we hire you?",

        "3. What are your strengths?",

        "4. What is your biggest weakness?",

        "5. Why do you want to work for our company?",

        "6. Explain one project that you have worked on.",

        "7. What programming languages do you know?",

        "8. What is OOP? Explain its four pillars.",

        "9. What is the difference between SQL and NoSQL?",

        "10. Where do you see yourself in 5 years?"

        ]

        answers = []

        for i, question in enumerate(interview_questions):

            st.subheader(question)

            ans = st.text_area(
            "Your Answer",
            key=f"mock_{i}",
            height=120
            )

            answers.append(ans)

        if st.button("Submit Interview"):

            score = 0

            for ans in answers:

                answer = ans.strip()

                if len(answer) > 50:
                    score += 10
                elif len(answer) > 20:
                    score += 7
                elif len(answer) > 5:
                    score += 5

            percentage = score

    # Recommendation
            if percentage >= 90:
                recommendation = "Excellent Interview Performance"

            elif percentage >= 75:
                recommendation = "Very Good Performance"

            elif percentage >= 60:
                recommendation = "Good Performance"

            elif percentage >= 40:
                recommendation = "Needs More Practice"

            else:
                recommendation = "Improve Communication and Technical Skills"

    # Save everything
            st.session_state.mock_score = percentage
            st.session_state.mock_recommendation = recommendation

            st.success(f"Interview Score: {percentage}%")
            st.progress(percentage / 100)
            st.info(recommendation)

    
    # ---------------- SKILL GAP ----------------

    elif feature == "Skill Gap Analyzer":

        st.title("📊 AI Skill Gap Analyzer")

        st.write("Analyze your skills and compare them with your desired career role.")

    # -------------------------------
    # Career Role
    # -------------------------------

        role = st.selectbox(
            "🎯 Select Your Career Goal",
            [
                "Software Developer",
                "Data Analyst",
                "AI/ML Engineer",
                "Full Stack Developer",
                "Cloud Engineer",
                "Cybersecurity Analyst",
                "Testing Engineer"
            ]
        )

    # -------------------------------
    # Skills
    # -------------------------------

        skills = [
            "Python","Java","C","C++",
            "SQL","DBMS","Operating System",
            "Computer Networks","OOP",
            "HTML","CSS","JavaScript",
            "React","Node.js",
            "Git","GitHub",
            "Data Structures","Algorithms",
            "Linux","AWS","Docker","Kubernetes",
            "Machine Learning","Deep Learning",
            "TensorFlow","Pandas","NumPy",
            "Excel","Power BI","Statistics",
            "Communication","Problem Solving",
            "Leadership","Teamwork"
        ]

        selected_skills = st.multiselect(
            "Select the skills you already know",
            skills
        )

    # -------------------------------
    # Required Skills
    # -------------------------------

        role_skills = {

            "Software Developer":{
                "Python","Java","SQL","DBMS","OOP",
                "Operating System","Computer Networks",
                "Data Structures","Algorithms",
                "Git","GitHub","Communication",
                "Problem Solving"
            },

            "Data Analyst":{
                "Python","SQL","Excel","Power BI",
                "Statistics","Pandas","NumPy",
                "Communication"
            },

            "AI/ML Engineer":{
                "Python","Machine Learning",
                "Deep Learning","TensorFlow",
                "Pandas","NumPy","Statistics","Git"
            },

            "Full Stack Developer":{
                "HTML","CSS","JavaScript",
                "React","Node.js","SQL",
                "Git","GitHub"
            },

            "Cloud Engineer":{
                "Linux","AWS","Docker",
                "Kubernetes","Python",
                "Computer Networks","Git"
            },

            "Cybersecurity Analyst":{
                "Linux","Python",
                "Operating System",
                "Computer Networks",
                "Problem Solving"
            },

            "Testing Engineer":{
                "Java","Python","SQL",
                "Communication",
                "Problem Solving"
            }

        }

    # -------------------------------
    # Analyze
    # -------------------------------

        if st.button("🔍 Analyze Skill Gap"):

            required_skills = role_skills[role]

            matched = required_skills.intersection(set(selected_skills))

            missing = required_skills.difference(set(selected_skills))

            percentage = (len(matched) / len(required_skills)) * 100

            st.subheader("📈 Skill Match")

            st.progress(percentage / 100)
            st.session_state.skill_gap_role = role
            st.session_state.skill_gap_score = percentage
            st.session_state.skill_gap_matched = list(matched)
            st.session_state.skill_gap_missing = list(missing)

            st.success(f"Skill Match : {percentage:.2f}%")

            st.subheader("✅ Skills You Have")

            if matched:
                for skill in sorted(matched):
                    st.success(skill)
            else:
                st.warning("No matching skills selected.")

            st.subheader("❌ Skills You Need")

            if missing:
                for skill in sorted(missing):
                    st.error(skill)
            else:
                st.success("Excellent! You already have all required skills.")


        # -------------------------------
        # Recommendations
        # -------------------------------

            st.subheader("🎯 Recommendations")

            recommendations = []

            for skill in missing:

                recommendations.append(f"Learn {skill} through online courses and hands-on projects.")

            if recommendations:

                for rec in recommendations:
                    st.write("✅", rec)

            else:

                st.success("You are ready for your selected career role!")

        # -------------------------------
        # Save for Report
        # -------------------------------

            st.session_state.skill_gap_score = percentage
            st.session_state.skill_gap_matched = list(matched)
            st.session_state.skill_gap_missing = list(missing)
            st.session_state.skill_gap_recommendations = recommendations

        

    # ---------------- LINKEDIN ----------------

    elif feature == "LinkedIn Profile Review":

        st.title("💼 LinkedIn Profile Review")

        st.write("Evaluate your LinkedIn profile and get improvement suggestions.")

        linkedin_url = st.text_input(
            "LinkedIn Profile URL"
        )

        profile_photo = st.radio(
            "Professional Profile Photo",
            ["Yes", "No"]
        )

        headline = st.radio(
            "Professional Headline",
            ["Yes", "No"]
        )

        about = st.radio(
            "About Section Completed",
            ["Yes", "No"]
        )

        education = st.radio(
            "Education Added",
            ["Yes", "No"]
        )

        experience = st.radio(
            "Experience / Internships Added",
            ["Yes", "No"]
        )

        skills = st.slider(
            "Number of Skills Added",
            0,
            50,
            10
        )

        certifications = st.slider(
            "Number of Certifications",
            0,
            20,
            2
        )

        projects = st.slider(
           "Number of Projects",
            0,
            20,
            2
        )


        if st.button("Analyze LinkedIn Profile"):

            score = 0

            if profile_photo == "Yes":
                score += 10

            if headline == "Yes":
                score += 15

            if about == "Yes":
                score += 15

            if education == "Yes":
                score += 10

            if experience == "Yes":
                score += 20

            score += min(skills, 15)

            score += min(certifications * 2, 10)

            score += min(projects * 2, 10)

            score = min(score, 100)

            st.subheader("📊 LinkedIn Profile Score")

            st.progress(score / 100)

            st.success(f"LinkedIn Score: {score}/100")

            st.subheader("🎯 Recommendations")

            suggestions = []

            if profile_photo == "No":
                suggestions.append("Add a professional profile photo.")

            if headline == "No":
                suggestions.append("Write a clear and professional headline.")

            if about == "No":
                suggestions.append("Complete the About section with your career goals and strengths.")

            if education == "No":
                suggestions.append("Add your education details.")

            if experience == "No":
                suggestions.append("Include internships, projects, or work experience.")

            if skills < 15:
                suggestions.append("Add more relevant technical and soft skills.")

            if certifications < 3:
                suggestions.append("Complete more industry certifications.")

            if projects < 4:
                suggestions.append("Showcase additional academic and personal projects.")
            
            if suggestions:
                for item in suggestions:
                    st.write("✅", item)
            else:
                st.success("Excellent! Your LinkedIn profile is well optimized.")

            # Create recommendation text for PDF
            if suggestions:
                linkedin_recommendation = "\n".join(suggestions)
            else:
                linkedin_recommendation = "Excellent! Your LinkedIn profile is well optimized."

# Save for PDF
            st.session_state.linkedin_profile = linkedin_url
            st.session_state.linkedin_score = score
            st.session_state.linkedin_skills = skills
            st.session_state.linkedin_certifications = certifications
            st.session_state.linkedin_projects = projects
            st.session_state.linkedin_recommendation = linkedin_recommendation


    # ---------------- COURSES ----------------

    elif feature == "Recommended Courses":

        st.title("📚 AI Recommended Learning Path")

        aptitude = st.session_state.get("aptitude_score", 0)
        technical = st.session_state.get("technical_score", 0)
    

        career = st.selectbox(
            "Select Your Career Goal",
            [
                "Software Developer",
                "Python Developer",
                "Java Developer",
                "Full Stack Developer",
                "Frontend Developer",
                "Backend Developer",
                "Data Analyst",
                "Data Scientist"
                "AI/ML Engineer",  
                "Cloud Engineer",
                "DevOps Engineer"
                "Cybersecurity Analyst",  
                "Testing Engineer",
                "Mobile App Developer",
                "UI/UX Designer",
                "Business Analyst",
                "Database Administrator"
            ]
        )

        courses = {

            "Software Developer":[
            ("Python Programming","Coursera"),
            ("Java Programming","Udemy"),
            ("Data Structures & Algorithms","Coursera"),
            ("DBMS","NPTEL"),
            ("Operating System","NPTEL"),
            ("Computer Networks","Cisco Networking Academy"),
            ("Git & GitHub","GitHub Skills"),
            ("System Design Basics","Udemy")
            ],

            "Python Developer":[
            ("Python for Everybody","Coursera"),
            ("Advanced Python","Udemy"),
            ("Flask Web Development","Udemy"),
            ("Django Framework","Coursera"),
            ("REST API Development","Udemy"),
            ("SQL Bootcamp","Udemy"),
            ("Git & GitHub","GitHub Skills")
            ],

            "Java Developer":[
            ("Core Java","Oracle Academy"),
            ("Advanced Java","Udemy"),
            ("Spring Boot","Udemy"),
            ("Hibernate","Udemy"),
            ("SQL","Coursera"),
            ("Microservices with Spring Boot","Udemy"),
            ("Git & GitHub","GitHub Skills")
            ],

            "Full Stack Developer":[
            ("HTML5 & CSS3","freeCodeCamp"),
            ("JavaScript","Coursera"),
            ("React JS","Meta"),
            ("Node.js & Express","Udemy"),
            ("MongoDB","MongoDB University"),
            ("Git & GitHub","GitHub Skills"),
            ("Full Stack MERN","Coursera")
            ],

            "Frontend Developer":[
            ("HTML5","freeCodeCamp"),
            ("CSS3","freeCodeCamp"),
            ("JavaScript","Coursera"),
            ("Bootstrap","Udemy"),
            ("React JS","Meta"),
            ("Responsive Web Design","freeCodeCamp")
            ],

            "Backend Developer":[
            ("Python","Coursera"),
            ("Java Spring Boot","Udemy"),
            ("Node.js","Udemy"),
            ("REST APIs","Coursera"),
            ("SQL","Coursera"),
            ("MongoDB","MongoDB University")
            ],

            "Data Analyst":[
            ("Python for Data Analysis","Coursera"),
            ("SQL","Coursera"),
            ("Excel","Microsoft Learn"),
            ("Power BI","Microsoft Learn"),
            ("Tableau","Coursera"),
            ("Statistics","Coursera"),
            ("Pandas & NumPy","Coursera")
            ],

            "Data Scientist":[
            ("Python","Coursera"),
            ("Machine Learning","Andrew Ng"),
            ("Deep Learning","DeepLearning.AI"),
            ("Statistics","Coursera"),
            ("Pandas","Coursera"),
            ("TensorFlow","Google"),
            ("Scikit-Learn","Coursera")
            ],

            "AI/ML Engineer":[
            ("Python","Coursera"),
            ("Machine Learning","Andrew Ng"),
            ("Deep Learning","DeepLearning.AI"),
            ("TensorFlow","Google"),
            ("PyTorch","Udemy"),
            ("Computer Vision","Coursera"),
            ("NLP","Coursera")
            ],

            "Cloud Engineer":[
            ("AWS Cloud Practitioner","AWS Skill Builder"),
            ("AWS Solutions Architect","AWS"),
            ("Microsoft Azure Fundamentals","Microsoft Learn"),
            ("Google Cloud Fundamentals","Google Cloud"),
            ("Docker","Udemy"),
            ("Kubernetes","Linux Foundation"),
            ("Terraform","HashiCorp")
            ],

            "DevOps Engineer":[
            ("Linux","Cisco"),
            ("Docker","Udemy"),
            ("Kubernetes","Linux Foundation"),
            ("Jenkins","Udemy"),
            ("Git & GitHub","GitHub Skills"),
            ("Terraform","HashiCorp"),
            ("AWS DevOps","AWS")
            ],

            "Cybersecurity Analyst":[
            ("Ethical Hacking","EC-Council"),
            ("Network Security","Cisco"),
            ("Linux","Cisco"),
            ("Python for Security","Udemy"),
            ("Cryptography","Coursera"),
            ("CompTIA Security+","CompTIA")
            ],

            "Testing Engineer":[
            ("Manual Testing","Udemy"),
            ("Selenium Automation","Udemy"),
            ("Java for Testers","Coursera"),
            ("API Testing with Postman","Udemy"),
            ("SQL","Coursera"),
            ("JMeter","Udemy")
            ],

            "Mobile App Developer":[
            ("Android Development","Google"),
            ("Kotlin","Udemy"),
            ("Flutter","Google"),
            ("Dart","Udemy"),
            ("Firebase","Google")
            ],

            "UI/UX Designer":[
            ("Figma","Coursera"),
            ("UI Design","Google UX"),
            ("UX Research","Coursera"),
            ("Adobe XD","Udemy"),
            ("Wireframing","Coursera")
            ],

            "Business Analyst":[
            ("Excel","Microsoft"),
            ("Power BI","Microsoft"),
            ("SQL","Coursera"),
            ("Business Analytics","Coursera"),
            ("Agile Fundamentals","Udemy")
            ],

            "Database Administrator":[
            ("SQL","Coursera"),
            ("Oracle Database","Oracle"),
            ("MySQL","Udemy"),
            ("PostgreSQL","Udemy"),
            ("Database Security","Coursera")
            ]

            }

        st.subheader("🎯 Recommended Courses")
        recommended_courses = []
        for course, platform in courses[career]:
            st.success(course)
            st.write("🏢 Platform:", platform)
            st.divider()

            recommended_courses.append(
            f"{course} ({platform})"
            )

# Save for PDF
        st.session_state.recommended_courses = recommended_courses


 #---------------------Report--------------------

    elif feature == "📄 Download Report":

        st.title("📄 Graduate Report")

        if st.button("Generate Report"):

            pdf = generate_graduate_report()

            with open(pdf, "rb") as file:

                st.download_button(
                    "⬇ Download Graduate Report",
                    file,
                    file_name="Graduate_Report.pdf",
                    mime="application/pdf"
                )