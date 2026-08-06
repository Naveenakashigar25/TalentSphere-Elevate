import streamlit as st
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
import PyPDF2
if "assessment" not in st.session_state:
    st.session_state.assessment = ""
# ==========================
# PROFESSIONAL MODULE REPORT
# ==========================
def generate_professional_report():

    filename = "Professional_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>TalentSphere Elevate</b>", styles["Title"]))
    story.append(Paragraph("<b>PROFESSIONAL MODULE REPORT</b>", styles["Heading1"]))

# Professional Profile
    story.append(Paragraph("<b> Professional Profile</b>", styles["Heading2"]))

    story.append(Paragraph(f"Name : {st.session_state.get('prof_name','')}", styles["Normal"]))
    story.append(Paragraph(f"Current Company : {st.session_state.get('prof_company','')}", styles["Normal"]))
    story.append(Paragraph(f"Current Role : {st.session_state.get('prof_role','')}", styles["Normal"]))
    story.append(Paragraph(f"Experience : {st.session_state.get('prof_experience',0)} Years", styles["Normal"]))
    story.append(Paragraph(f"Skills : {', '.join(st.session_state.get('prof_skills',[]))}", styles["Normal"]))
    story.append(Paragraph(f"Career Goal : {st.session_state.get('prof_goal','')}", styles["Normal"]))
    story.append(Paragraph(f"Preferred Role : {st.session_state.get('prof_preferred_role','')}", styles["Normal"]))


# Skill Assessment
    story.append(Paragraph("<b>Professional Skill Assessment</b>", styles["Heading2"]))

    story.append(Paragraph(f"Python: {st.session_state.get('python_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"Java: {st.session_state.get('java_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"SQL: {st.session_state.get('sql_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"Cloud Computing: {st.session_state.get('cloud_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"Data Structures: {st.session_state.get('dsa_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"Backend Development: {st.session_state.get('backend_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"System Design: {st.session_state.get('system_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"DevOps: {st.session_state.get('devops_score', 0)}/10", styles["Normal"]))
    story.append(Paragraph(f"Leadership: {st.session_state.get('leadership_score', 0)}/10", styles["Normal"]))



# Promotion Readiness
    story.append(Paragraph("<b>Promotion Readiness</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Promotion Readiness Score : {st.session_state.get('promotion_score', 0):.0f}%",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Experience : {st.session_state.get('experience', 0)} Years",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Technical Skills : {st.session_state.get('technical', 0)}/100",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Leadership Skills : {st.session_state.get('leadership', 0)}/100",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Communication Skills : {st.session_state.get('communication', 0)}/100",
        styles["Normal"]
    ))

    story.append(Paragraph(
       f"Certifications : {st.session_state.get('certifications', 0)}",
       styles["Normal"]
    ))

    story.append(Paragraph(
        f"Recommendation : {st.session_state.get('promotion_recommendation', 'Not Available')}",
        styles["Normal"]
    ))


# Salary Benchmark
    story.append(Paragraph("<b>Salary Benchmark</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Job Role : {st.session_state.get('job_role','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Experience : {st.session_state.get('salary_experience',0)} Years",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Primary Skill : {st.session_state.get('primary_skill','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Estimated Salary : ₹{st.session_state.get('salary',0):,} per year",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Recommendation : {st.session_state.get('salary_recommendation','Not Available')}",
        styles["Normal"]
    ))
#---------------industry trends-------------
    story.append(Paragraph("<b>Industry Trends</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Technology : {st.session_state.get('industry_technology','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Market Demand : {st.session_state.get('industry_demand','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Expected Growth : {st.session_state.get('industry_growth','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Average Salary : {st.session_state.get('industry_salary','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph("<b>Trending Skills</b>", styles["Heading3"]))

    skills = st.session_state.get("industry_skills", [])

    for skill in skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    

# -------------------Certification Suggestions-------------------
    

    story.append(Paragraph(
        f"Career Domain : {st.session_state.get('certification_domain', 'Not Available')}",
        styles["Normal"]
    ))


    story.append(Paragraph(
        "<b>Recommended Certifications</b>",
        styles["Heading3"]
    ))


    certifications = st.session_state.get("certifications", [])

    if certifications:
        for cert in certifications:
            story.append(
                Paragraph(f"• {cert}", styles["Normal"])
            )
    else:
        story.append(
            Paragraph("No certifications available", styles["Normal"])
        )


    story.append(Paragraph("<b>Benefits</b>",styles["Heading3"]
    ))


    benefits = st.session_state.get("certification_benefits", [])

    for benefit in benefits:
        story.append(Paragraph(f"• {benefit}", styles["Normal"])
    )



#------------------------------- Leadership Evaluation------------------------
    story.append(
        Paragraph(
        "<b>Leadership Evaluation</b>",
        styles["Heading2"]
    ))


    story.append(
        Paragraph(
        f"Leadership Score : {st.session_state.get('leadership_score','Not Available')}/100",
        styles["Normal"]
    ))



    story.append(
        Paragraph(
        "<b>Recommendations</b>",
        styles["Heading3"]
    ))


    leadership_recommendations = st.session_state.get(
        "leadership_recommendations",
        []
    )


    for recommendation in leadership_recommendations:
        story.append(
        Paragraph(
            f"• {recommendation}",
            styles["Normal"]
        ))


# -------------------AI Growth Analysis-----------------------------
    story.append(
        Paragraph(
        "<b>Advanced Job Matching</b>",
        styles["Heading2"]
    ))


    story.append(
        Paragraph(
        f"Primary Skill : {st.session_state.get('job_skill','Not Available')}",
        styles["Normal"]
    ))


    story.append(
        Paragraph(
        f"Experience : {st.session_state.get('job_experience','Not Available')} Years",
        styles["Normal"]
    ))


    story.append(
        Paragraph(
        "<b>Recommended Job Roles</b>",
        styles["Heading3"]
    ))


    jobs = st.session_state.get("matched_jobs", [])

    for job in jobs:
        story.append(
            Paragraph(
                f"• {job}",
                styles["Normal"]
        ))


    story.append(
        Paragraph(
        "<b>Career Advice</b>",
        styles["Heading3"]
    ))


    story.append(
        Paragraph(
        st.session_state.get(
            "job_career_advice",
            "Not Available"
        ),
        styles["Normal"]
    ))


#----------------90-Day Action Plan-----------------------
    

    story.append(
    Paragraph(
        "<b>90-Day Action Plan</b>",
        styles["Heading2"]
    ))
    
    story.append(
    Paragraph(
        f"Career Goal : {st.session_state.get('action_goal','Not Available')}",
        styles["Normal"]
    )
)
    story.append(
    Paragraph(
        f"Experience : {st.session_state.get('action_experience','Not Available')} Years",
        styles["Normal"]
    ))


    story.append(
    Paragraph(
        "<b>Month 1 : Build Strong Foundations</b>",
        styles["Heading3"]
    ))

    for item in st.session_state.get("month1_plan", []):
        story.append(
        Paragraph(f"• {item}", styles["Normal"])
    )


    story.append(
    Paragraph(
        "<b>Month 2 : Apply Your Knowledge</b>",
        styles["Heading3"]
    ))

    for item in st.session_state.get("month2_plan", []):
        story.append(
        Paragraph(f"• {item}", styles["Normal"])
    )


    story.append(
    Paragraph(
        "<b>Month 3 : Career Growth</b>",
        styles["Heading3"]
    ))

    for item in st.session_state.get("month3_plan", []):
        story.append(
        Paragraph(f"• {item}", styles["Normal"])
    )


    story.append(
    Paragraph(
        "<b>Goal-Specific Recommendations</b>",
        styles["Heading3"]
    ))

    for item in st.session_state.get("goal_recommendations", []):
        story.append(
        Paragraph(f"• {item}", styles["Normal"])
    )


    story.append(
    Paragraph(
        "<b>Expected Outcome After 90 Days</b>",
        styles["Heading3"]
    ))

    for item in st.session_state.get("action_outcomes", []):
        story.append(
        Paragraph(f"• {item}", styles["Normal"])
    )

    doc.build(story)
    return filename

# ======================================================
# PROFESSIONAL DASHBOARD
# ======================================================

def professional_dashboard():

    st.title("🎓 Professional Dashboard")


    # ======================================================
    # SIDEBAR
    # ======================================================

    feature = st.sidebar.selectbox(

        "Select Feature",

        [

            "🏠 Home",

            "👤 Professional Profile",

            "Professional Skill Assessment",

            "Promotion Readiness",

            "Salary Benchmark",

            "Industry Trends",

            "Certification Suggestions",

            "Leadership Evaluation",

            "Advanced Job Matching",

            "90-Day Action Plan",

            "Report"

        ]

    )

    # ======================================================
    # HOME
    # ======================================================

    if feature=="🏠 Home":

        st.subheader("Working Professional Module")

        st.write(
            """
Welcome to the Working Professional Dashboard.

This module helps professionals

✅ Assess Technical Skills

✅ Analyze Promotion Readiness

✅ Explore Career Transition

✅ Benchmark Salary

✅ Learn Trending Skills

✅ Get Certification Suggestions

✅ Find Better Job Opportunities

✅ Receive AI Career Roadmap

            """
        )
        # ======================================================
# PROFESSIONAL PROFILE
# ======================================================

    elif feature == "👤 Professional Profile":

        st.header("👤 Professional Profile")

        st.write("Please enter your professional information.")

        name = st.text_input("Full Name")

        email = st.text_input("Email Address")

        phone = st.text_input("Phone Number")

        company = st.text_input("Current Company")

        role = st.text_input("Current Role")

        experience = st.slider(
            "Total Experience (Years)",
            0,
            30,
            2
        )

        qualification = st.selectbox(
            "Highest Qualification",
            [
                "Diploma",
                "B.E",
                "B.Tech",
                "M.Tech",
                "MBA",
                "MCA",
                "PhD",
                "Other"
            ]
        )

        industry = st.selectbox(
            "Industry",
            [
                "Information Technology",
                "Software",
                "Banking",
                "Healthcare",
                "Education",
                "Manufacturing",
                "Telecommunication",
                "Other"
            ]
        )

        skills = st.multiselect(
            "Technical Skills",
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
                "Node.js",
                "Django",
                "AWS",
                "Azure",
                "Docker",
                "Kubernetes",
                "Git",
                "GitHub",
                "Machine Learning",
                "Power BI",
                "DevOps",
                "System Design"
            ]
        )

        leadership = st.radio(
            "Leadership Experience",
            [
                "Yes",
                "No"
            ]
        )

        certifications = st.text_area(
            "Certifications"
        )

        current_salary = st.number_input(
            "Current Salary (LPA)",
            0.0,
            100.0,
            6.0
        )

        career_goal = st.selectbox(
            "Career Goal",
            [
                "Senior Software Engineer",
                "Technical Lead",
                "Cloud Engineer",
                "Engineering Manager",
                "Backend Architect",
                "DevOps Engineer",
                "AI Engineer",
                "Data Scientist"
            ]
        )

        preferred_role = st.selectbox(
            "Preferred Job Role",
            [
                "Senior Backend Engineer",
                "Cloud Engineer",
                "Engineering Lead",
                "Backend Architect",
                "DevOps Engineer",
                "AI Engineer",
                "Technical Manager"
            ]
        )

        if st.button("Save Profile"):

        # Save in Session State
            st.session_state.prof_name = name
            st.session_state.prof_email = email
            st.session_state.prof_phone = phone
            st.session_state.prof_company = company
            st.session_state.prof_role = role
            st.session_state.prof_experience = experience
            st.session_state.prof_qualification = qualification
            st.session_state.prof_industry = industry
            st.session_state.prof_skills = skills
            st.session_state.prof_leadership = leadership
            st.session_state.prof_certifications = certifications
            st.session_state.prof_salary = current_salary
            st.session_state.prof_goal = career_goal
            st.session_state.prof_preferred_role = preferred_role

            st.success("✅ Professional Profile Saved Successfully!")

            st.subheader("Profile Summary")

            st.write("**Name:**", name)
            st.write("**Company:**", company)
            st.write("**Current Role:**", role)
            st.write("**Experience:**", experience, "Years")
            st.write("**Industry:**", industry)
            st.write("**Skills:**", ", ".join(skills))
            st.write("**Career Goal:**", career_goal)
            st.write("**Preferred Role:**", preferred_role)
    
#---------------------------professional assessment--------------------------


    elif feature == "Professional Skill Assessment":
        
        st.header("📊 Professional Skill Assessment")
#----------------------------------------------------------
        st.subheader("Select an Assessment")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🐍 Python Assessment"):
                st.session_state.assessment = "Python"

        with col2:
            if st.button("☕ Java Assessment"):
                st.session_state.assessment = "Java"

        with col3:
            if st.button("🗄 SQL Assessment"):
                st.session_state.assessment = "SQL"

        col4, col5, col6 = st.columns(3)

        with col4:
            if st.button("☁ Cloud Computing"):
                st.session_state.assessment = "Cloud"

        with col5:
            if st.button("📚 Data Structures"):
                st.session_state.assessment = "DSA"

        with col6:
            if st.button("⚙ Backend Development"):
                st.session_state.assessment = "Backend"

        col7, col8, col9 = st.columns(3)

        with col7:
            if st.button("🌐 System Design"):
                st.session_state.assessment = "System"

        with col8:
            if st.button("🚀 DevOps"):
                st.session_state.assessment = "DevOps"
# -------------------------------
# PYTHON ASSESSMENT
# -------------------------------
        if st.session_state.assessment == "Python":

            st.subheader("🐍 Python Assessment")

            score = 0

            q1 = st.radio(
                "1. Which keyword is used to define a function in Python?",
                ["func", "define", "def", "function"],
                key="python_q1"
            )

            q2 = st.radio(
                "2. Which data type stores True or False values?",
                ["Integer", "Boolean", "String", "Float"],
                key="python_q2"
            )

            q3 = st.radio(
                "3. Which function is used to display output?",
                ["show()", "print()", "echo()", "display()"],
                key="python_q3"
            )

            q4 = st.radio(
                "4. Which symbol is used for single-line comments in Python?",
                ["//", "#", "--", "/* */"],
                key="python_q4"
            )

            q5 = st.radio(
                "5. Which loop continues until the condition becomes False?",
                ["for", "while", "if", "switch"],
                key="python_q5"
            )

            if st.button("Submit Python Assessment"):

                if q1 == "def":
                    score += 2

                if q2 == "Boolean":
                    score += 2

                if q3 == "print()":
                    score += 2

                if q4 == "#":
                    score += 2

                if q5 == "while":
                    score += 2
                              
            # Save the score
                st.session_state.python_score = score

                st.success(f"Python Assessment Score : {score}/10")
                

                st.progress(score / 10)

                if score == 10:
                    st.success("Excellent! You have strong Python fundamentals.")

                elif score >= 6:
                    st.info("Good! Continue practicing Python concepts.")

                else:
                    st.warning("You need to improve your Python fundamentals.")
         
# -------------------------------
# JAVA ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "Java":

            st.subheader("☕ Java Assessment")

            score = 0

            q1 = st.radio(
                "1. Java is a ______ programming language.",
                [
                    "Procedural",
                    "Object-Oriented",
                    "Assembly",
                    "Machine"
                ],
                key="java_q1"
            ) 

            q2 = st.radio(
                "2. Which keyword is used to create an object?",
                [
                    "create",
                    "new",
                    "class",
                    "object"
                ],
                key="java_q2"
            )

            q3 = st.radio(
                "3. Which method is the entry point of every Java program?",
                [
                    "start()",
                    "run()",
                    "main()",
                    "execute()"
                ],
                key="java_q3"
            )

            q4 = st.radio(
                "4. Which of the following is NOT an OOP concept?",
                [
                    "Inheritance",
                    "Encapsulation",
                    "Compilation",
                    "Polymorphism"
                ],
                key="java_q4"
            )

            q5 = st.radio(
                "5. Which symbol is used to end a statement in Java?",
                [
                    ":",
                    ";",
                    ",",
                    "."
                ],
                key="java_q5"
            )

            if st.button("Submit Java Assessment"):

                if q1 == "Object-Oriented":
                    score += 2

                if q2 == "new":
                    score += 2

                if q3 == "main()":
                    score += 2

                if q4 == "Compilation":
                    score += 2

                if q5 == ";":
                    score += 2
                st.session_state.java_score = score
                st.success(f"Java Assessment Score : {score}/10")

                st.progress(score / 10)

            if score == 10:
                st.success("Excellent! You have strong Java programming skills.")

            elif score >= 6:
                st.info("Good! Continue practicing Java concepts and OOP.")

            else:
                st.warning("Improve your Java fundamentals and object-oriented programming concepts.")

# -------------------------------
# SQL ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "SQL":

            st.subheader("🗄 SQL Assessment")

            score = 0

            q1 = st.radio(
                "1. Which SQL statement is used to retrieve data from a database?",
                [
                    "SELECT",
                    "INSERT",
                    "UPDATE",
                    "DELETE"
                ],
                key="sql_q1"
            )

            q2 = st.radio(
                "2. Which clause is used to filter records?",
                [
                    "ORDER BY",
                    "GROUP BY",
                    "WHERE",
                    "HAVING"
                ],
                key="sql_q2"
            )

            q3 = st.radio(
                "3. Which SQL command is used to add a new record?",
                [
                    "INSERT",
                    "ADD",
                    "UPDATE",
                    "CREATE"
                ],
                key="sql_q3"
            )

            q4 = st.radio(
                "4. Which SQL function returns the total number of rows?",
                [
                    "SUM()",
                    "COUNT()",
                    "AVG()",
                    "MAX()"
                ],
                key="sql_q4"
            )

            q5 = st.radio(
                "5. Which JOIN returns matching rows from both tables?",
                [
                    "LEFT JOIN",
                    "RIGHT JOIN",
                    "INNER JOIN",
                    "FULL JOIN"
                ],
                key="sql_q5"
            )

            if st.button("Submit SQL Assessment"):

                if q1 == "SELECT":
                    score += 2

                if q2 == "WHERE":
                    score += 2

                if q3 == "INSERT":
                    score += 2

                if q4 == "COUNT()":
                    score += 2

                if q5 == "INNER JOIN":
                    score += 2
            st.session_state.sql_score = score
            st.success(f"SQL Assessment Score : {score}/10")

            st.progress(score / 10)

            if score == 10:
                st.success("Excellent! You have strong SQL and database skills.")

            elif score >= 6:
                st.info("Good! Continue practicing SQL queries and database concepts.")

            else:
                st.warning("Improve your SQL fundamentals, joins, and database concepts.")

# -------------------------------
# CLOUD COMPUTING ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "Cloud":

            st.subheader("☁ Cloud Computing Assessment")

            score = 0

            q1 = st.radio(
                "1. Which of the following is a cloud service provider?",
                [
                    "AWS",
                    "Oracle",
                    "MySQL",
                    "Python"
                ],
                key="cloud_q1"
            )

            q2 = st.radio(
                "2. Which AWS service provides virtual machines?",
                [
                    "S3",
                    "EC2",
                    "Lambda",
                    "RDS"
                ],
                key="cloud_q2"
            )

            q3 = st.radio(
                "3. Which cloud model is used only within an organization?",
                [
                    "Public Cloud",
                    "Private Cloud",
                    "Hybrid Cloud",
                    "Community Cloud"
                ],
                key="cloud_q3"
            )

            q4 = st.radio(
                "4. Which service is mainly used for object storage?",
                [
                    "EC2",
                    "S3",
                    "Lambda",
                    "IAM"
                ],
                key="cloud_q4"
            )

            q5 = st.radio(
                "5. What does SaaS stand for?",
                [
                    "Software as a Service",
                    "Storage as a Service",
                    "System as a Service",
                    "Security as a Service"
                ],
                key="cloud_q5"
            )

            if st.button("Submit Cloud Assessment"):

                if q1 == "AWS":
                    score += 2

                if q2 == "EC2":
                    score += 2

                if q3 == "Private Cloud":
                    score += 2

                if q4 == "S3":
                    score += 2

                if q5 == "Software as a Service":
                    score += 2
                
                st.session_state.cloud_score = score
                st.success(f"Cloud Computing Score : {score}/10")

                st.progress(score / 10)

                if score == 10:
                    st.success("Excellent! You have strong Cloud Computing knowledge.")

                elif score >= 6:
                    st.info("Good! Improve your AWS services and cloud architecture concepts.")

                else:
                    st.warning("Learn cloud fundamentals, deployment models, and AWS services.")
        

        # -------------------------------
# DATA STRUCTURES & ALGORITHMS ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "DSA":

            st.subheader("📚 Data Structures & Algorithms Assessment")

            score = 0

            q1 = st.radio(
                "1. Which data structure follows the LIFO principle?",
                [
                    "Queue",
                    "Stack",
                    "Linked List",
                    "Tree"
                ],
                key="dsa_q1"
            )

            q2 = st.radio(
                "2. Which data structure follows the FIFO principle?",
                [
                    "Stack",
                    "Queue",
                    "Tree",
                    "Graph"
                ],
                key="dsa_q2"
            )

            q3 = st.radio(
                "3. What is the time complexity of Binary Search?",
                [
                    "O(n)",
                    "O(log n)",
                    "O(n²)",
                    "O(1)"
                ],
                key="dsa_q3"
            )

            q4 = st.radio(
                "4. Which traversal visits the Root node first?",
                [
                    "Inorder",
                    "Postorder",
                    "Preorder",
                    "Level Order"
                ],
                key="dsa_q4"
            )

            q5 = st.radio(
                "5. Which sorting algorithm has the best average time complexity?",
                [
                    "Bubble Sort",
                    "Selection Sort",
                    "Merge Sort",
                    "Insertion Sort"
                ],
                key="dsa_q5"
            )

            if st.button("Submit DSA Assessment"):

                if q1 == "Stack":
                    score += 2

                if q2 == "Queue":
                    score += 2

                if q3 == "O(log n)":
                    score += 2

                if q4 == "Preorder":
                    score += 2

                if q5 == "Merge Sort":
                    score += 2
                     
                st.session_state.dsa_score = score

                st.success(f"DSA Assessment Score : {score}/10")

                st.progress(score / 10)

                if score == 10:
                    st.success("Excellent! Your Data Structures and Algorithms skills are outstanding.")

                elif score >= 6:
                    st.info("Good! Continue practicing DSA problems on coding platforms.")

                else:
                    st.warning("Strengthen your understanding of DSA concepts and practice coding regularly.")
        

        # -------------------------------
# BACKEND DEVELOPMENT ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "Backend":

            st.subheader("⚙ Backend Development Assessment")

            score = 0

            q1 = st.radio(
                "1. Which Python framework is commonly used for building REST APIs?",
                [
                    "Streamlit",
                    "FastAPI",
                    "Tkinter",
                    "Pygame"
                ],
                key="backend_q1"
            )

            q2 = st.radio(
                "2. Which HTTP method is used to retrieve data from a server?",
                [
                    "POST",
                    "PUT",
                    "GET",
                    "DELETE"
                ],
                key="backend_q2"
            )

            q3 = st.radio(
                "3. Which HTTP method is mainly used to create a new resource?",
                [
                    "GET",
                    "POST",
                    "DELETE",
                    "PATCH"
                ],
                key="backend_q3"
            )

            q4 = st.radio(
                "4. Which authentication method is commonly used in REST APIs?",
                [
                    "JWT",
                    "HTML",
                    "CSS",
                    "Bootstrap"
                ],
                key="backend_q4"
            )

            q5 = st.radio(
                "5. Which database is commonly used with FastAPI?",
                [
                    "PostgreSQL",
                    "MS Paint",
                    "PowerPoint",
                    "Photoshop"
                ],
                key="backend_q5"
            )

            if st.button("Submit Backend Assessment"):

                if q1 == "FastAPI":
                    score += 2

                if q2 == "GET":
                    score += 2

                if q3 == "POST":
                    score += 2

                if q4 == "JWT":
                    score += 2

                if q5 == "PostgreSQL":
                    score += 2

            st.session_state.backend_score = score

            st.success(f"Backend Development Score : {score}/10")

            st.progress(score / 10)

            if score == 10:
                st.success("Excellent! You have strong Backend Development knowledge.")

            elif score >= 6:
                st.info("Good! Continue improving your API development and database skills.")

            else:
                st.warning("Strengthen your understanding of FastAPI, REST APIs, authentication, and databases.")

            st.subheader("Recommendations")

            if score < 10:
                st.write("• Learn REST API concepts.")
                st.write("• Practice FastAPI projects.")
                st.write("• Understand CRUD operations.")
                st.write("• Learn JWT Authentication.")
                st.write("• Practice PostgreSQL and SQL queries.")


# -------------------------------
# SYSTEM DESIGN ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "System":

            st.subheader("🌐 System Design Assessment")

            score = 0

            q1 = st.radio(
                "1. What is the main purpose of a Load Balancer?",
                [
                    "Store Data",
                    "Distribute incoming traffic across multiple servers",
                    "Increase Internet Speed",
                    "Encrypt Data"
                ],
                key="system_q1"
            )

            q2 = st.radio(
                "2. Which component stores frequently accessed data to improve performance?",
                [
                    "Firewall",
                    "Cache",
                    "Router",
                    "Switch"
                ],
                key="system_q2"
            )

            q3 = st.radio(
                "3. In Microservices Architecture, an application is divided into:",
                [
                    "One Large Module",
                    "Independent Small Services",
                    "Only Databases",
                    "One API"
                ],
                key="system_q3"
            )

            q4 = st.radio(
                "4. Which database is generally preferred for structured relational data?",
                [
                    "PostgreSQL",
                    "MongoDB",
                    "Redis",
                    "Firebase"
                ],
                key="system_q4"
            )

            q5 = st.radio(
                "5. What is Scalability in System Design?",
                [
                    "Making the application colorful",
                    "Ability of a system to handle increasing users or workload",
                    "Reducing code size",
                    "Removing unnecessary files"
                ],
                key="system_q5"
            )

            if st.button("Submit System Design Assessment"):

                if q1 == "Distribute incoming traffic across multiple servers":
                    score += 2

                if q2 == "Cache":
                    score += 2

                if q3 == "Independent Small Services":
                    score += 2

                if q4 == "PostgreSQL":
                    score += 2

                if q5 == "Ability of a system to handle increasing users or workload":
                    score += 2
                
                st.session_state.system_score = score
                st.success(f"System Design Score : {score}/10")

                st.progress(score / 10)

                if score == 10:
                    st.success("Excellent! You have a strong understanding of System Design concepts.")

                elif score >= 6:
                    st.info("Good! Continue learning distributed systems, scalability, and architecture.")

                else:
                    st.warning("Improve your knowledge of caching, load balancing, scalability, and microservices.")

                st.subheader("Recommendations")

                if score < 10:
                    st.write("• Learn Load Balancing concepts.")
                    st.write("• Understand Caching techniques (Redis).")
                    st.write("• Study Microservices Architecture.")
                    st.write("• Learn Database Scaling.")
                    st.write("• Practice designing scalable applications.")


# -------------------------------
# DEVOPS ASSESSMENT
# -------------------------------

        if st.session_state.assessment == "DevOps":

            st.subheader("🚀 DevOps Assessment")

            score = 0

            q1 = st.radio(
                "1. What is the primary purpose of Docker?",
                [
                    "Database Management",
                    "Containerization",
                    "Programming Language",
                    "Operating System"
                ],
                key="devops_q1"
            )

            q2 = st.radio(
                "2. Which tool is commonly used for Continuous Integration (CI)?",
                [
                    "Jenkins",
                    "Photoshop",
                    "Excel",
                    "PowerPoint"
                ],
                key="devops_q2"
            )

            q3 = st.radio(
                "3. Which version control system is widely used in software development?",
                [
                    "Git",
                    "Docker",
                    "Kubernetes",
                    "Linux"
                ],
                key="devops_q3"
            )

            q4 = st.radio(
                "4. Which tool is used to manage containerized applications?",
                [
                    "Kubernetes",
                    "MySQL",
                    "FastAPI",
                    "VS Code"
                ],
                key="devops_q4"
            )

            q5 = st.radio(
                "5. What does CI/CD stand for?",
                [
                    "Continuous Integration / Continuous Deployment",
                    "Computer Integration / Computer Deployment",
                    "Continuous Installation / Continuous Delivery",
                    "Code Integration / Code Distribution"
                ],
                key="devops_q5"
            )

            if st.button("Submit DevOps Assessment"):

                if q1 == "Containerization":
                    score += 2

                if q2 == "Jenkins":
                    score += 2

                if q3 == "Git":
                    score += 2

                if q4 == "Kubernetes":
                    score += 2

                if q5 == "Continuous Integration / Continuous Deployment":
                    score += 2
                
                st.session_state.devops_score = score
                st.success(f"DevOps Assessment Score : {score}/10")

                st.progress(score / 10)

                if score == 10:
                    st.success("Excellent! You have strong DevOps knowledge.")

                elif score >= 6:
                    st.info("Good! Continue learning CI/CD pipelines, Docker, and Kubernetes.")

                else:
                    st.warning("Improve your understanding of DevOps tools and practices.")

                st.subheader("Recommendations")

                if score < 10:
                    st.write("• Learn Git and GitHub version control.")
                    st.write("• Practice Docker containerization.")
                    st.write("• Understand Kubernetes orchestration.")
                    st.write("• Build CI/CD pipelines using Jenkins or GitHub Actions.")
                    st.write("• Learn Linux commands and shell scripting.")


                    st.subheader("📊 Professional Skill Assessment Scores")

                    python = st.session_state.get("python_score", 0)
                    java = st.session_state.get("java_score", 0)
                    sql = st.session_state.get("sql_score", 0)
                    cloud = st.session_state.get("cloud_score", 0)
                    dsa = st.session_state.get("dsa_score", 0)
                    backend = st.session_state.get("backend_score", 0)
                    system = st.session_state.get("system_score", 0)
                    devops = st.session_state.get("devops_score", 0)
                    leadership = st.session_state.get("leadership_score", 0)

                    st.write(f"🐍 Python : **{python}/10**")
                    st.progress(python / 10)

                    st.write(f"☕ Java : **{java}/10**")
                    st.progress(java / 10)

                    st.write(f"🗄 SQL : **{sql}/10**")
                    st.progress(sql / 10)

                    st.write(f"☁ Cloud Computing : **{cloud}/10**")
                    st.progress(cloud / 10)

                    st.write(f"📚 Data Structures : **{dsa}/10**")
                    st.progress(dsa / 10)

                    st.write(f"⚙ Backend Development : **{backend}/10**")
                    st.progress(backend / 10)

                    st.write(f"🌐 System Design : **{system}/10**")
                    st.progress(system / 10)

                    st.write(f"🚀 DevOps : **{devops}/10**")
                    st.progress(devops / 10)

                    st.write(f"👨‍💼 Leadership : **{leadership}/10**")
                    st.progress(leadership / 10)
    #----------------Promotion rediness---------------------

    elif feature == "Promotion Readiness":

        st.header("📈 Promotion Readiness")

        st.write("Evaluate your readiness for the next level in your career.")

        experience = st.slider(
            "Years of Experience",
            0, 20, 2
        )

        technical = st.slider(
            "Technical Skills",
            0, 100, 70
        )

        leadership = st.slider(
            "Leadership Skills",
            0, 100, 60
        )

        communication = st.slider(
            "Communication Skills",
            0, 100, 75
        )
    
        certifications = st.slider(
            "Number of Certifications",
            0, 10, 2
        )

        if st.button("Analyze Promotion Readiness"):

            score = (
                technical * 0.35 +
                leadership * 0.25 +
                communication * 0.20 +
                experience * 2 +
                certifications * 2
            )

            if score > 100:
                score = 100

        # Save values
            st.session_state.promotion_score = score
            st.session_state.experience = experience
            st.session_state.technical = technical
            st.session_state.leadership = leadership
            st.session_state.communication = communication
            st.session_state.certifications = certifications

            st.subheader("Promotion Readiness Score")

            st.metric("Score", f"{int(score)}%")
            st.progress(score / 100)

            st.write(f"Experience : {experience} Years")
            st.write(f"Technical Skills : {technical}/100")
            st.write(f"Leadership Skills : {leadership}/100")
            st.write(f"Communication Skills : {communication}/100")
            st.write(f"Certifications : {certifications}")

        # Recommendation
            if score >= 85:

                recommendation = "Excellent! You are highly ready for a promotion."
                st.success(recommendation)

            elif score >= 70:

                recommendation = "Good! Improve a few areas to increase your promotion chances."
                st.info(recommendation)

            else:
 
                recommendation = "You need to improve your skills before aiming for a promotion."
                st.warning(recommendation)

        # Save recommendation
            st.session_state.promotion_recommendation = recommendation

            st.subheader("Recommendations")

            if technical < 80:
                st.write("• Improve technical expertise.")

            if leadership < 80:
                st.write("• Take leadership responsibilities.")

            if communication < 80:
                st.write("• Improve communication and presentation skills.")

            if certifications < 3:
                st.write("• Complete professional certifications.")

            if experience < 3:
                st.write("• Gain more project experience.")

#--------------------Salary Benchmark-----------------------------------

    

    elif feature == "Salary Benchmark":

        st.header("💰 Salary Benchmark")

        st.write("Estimate your salary based on your role, experience, and skills.")

        role = st.selectbox(
            "Select Job Role",
            [
                "Software Engineer",
                "Backend Developer",
                "Frontend Developer",
                "Full Stack Developer",
                "Data Analyst",
                "Data Scientist",
                "DevOps Engineer",
                "Cloud Engineer",
                "QA Engineer",
                "Cyber Security Engineer"
            ]
        )

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            2
        )

        location = st.selectbox(
            "Location",
            [
                "Bangalore",
                "Hyderabad",
                "Chennai",
                "Pune",
                "Mumbai",
                "Delhi"
            ]
        )

        skill = st.selectbox(
            "Primary Skill",
            [
                "Python",
                "Java",
                "SQL",
                "Cloud",
                "DevOps",
                "AI/ML",
                "React",
                "FastAPI"
            ]
        )

        if st.button("Estimate Salary"):

            salary = 0

            if experience <= 1:
                salary = 300000

            elif experience <= 2:
                salary = 500000

            elif experience <= 5:
                salary = 900000

            elif experience <= 8:
                salary = 1500000
 
            else:
                salary = 2200000
            
            # Save Salary Benchmark details
            st.session_state.salary = salary
            st.session_state.job_role = role
            st.session_state.salary_experience = experience
            st.session_state.primary_skill = skill

            st.subheader("Estimated Annual Salary")
 
            st.metric(
                "Salary",
                f"₹{salary:,} per year"
            )

            st.progress(min(salary / 2500000, 1.0))
 
            st.subheader("Career Insights")

            st.write(f"**Role:** {role}")
            st.write(f"**Location:** {location}")
            st.write(f"**Primary Skill:** {skill}")

            st.subheader("Recommendations")

            recommendation = ""

            if skill == "Python":
                recommendation = (
                    "• Learn FastAPI and Django.\n"
                    "• Improve DSA and System Design."
                )

            elif skill == "Java":
                recommendation = (
                "• Learn Spring Boot and Microservices.\n"
                "• Practice Java interview questions."
            )

            elif skill == "Cloud":
                recommendation = (
                "• Complete AWS or Azure certifications.\n"
                "• Learn Docker and Kubernetes."
            )

            elif skill == "DevOps":
                recommendation = (
                "• Master Jenkins and CI/CD pipelines.\n"
                "• Learn Terraform and Kubernetes."
            )

            elif skill == "AI/ML":
                recommendation = (
                "• Learn Deep Learning and Generative AI.\n"
                "• Build real-world AI projects."
            )

            st.session_state.salary_recommendation = recommendation
            st.write(recommendation)

#----------------------Industry Trends-------------------------

    
    elif feature == "Industry Trends":

        st.header("📈 Industry Trends")

        st.write(
            "Explore current technology trends, market demand, "
            "future growth opportunities, salary ranges, and required skills."
        )

        technology_data = {

            "Artificial Intelligence": {
                "demand": "Very High 🔥",
                "growth": "35%",
                "salary": "₹12 LPA - ₹35 LPA",
                "skills": [
                    "Machine Learning",
                    "Deep Learning",
                    "Generative AI",
                    "Natural Language Processing",
                    "Computer Vision"
                ]
            },

            "Cloud Computing": {
                "demand": "High ☁️",
                "growth": "28%",
                "salary": "₹8 LPA - ₹25 LPA",
                "skills": [
                    "AWS",
                    "Microsoft Azure",
                    "Google Cloud",
                    "Docker",
                    "Kubernetes"
                ]
            },

            "Cyber Security": {
                "demand": "Very High 🔒",
                "growth": "32%",
                "salary": "₹8 LPA - ₹30 LPA",
                "skills": [
                    "Ethical Hacking",
                    "Network Security",
                    "Penetration Testing",
                    "SOC Analysis",
                    "Incident Response"
                ]
            },

            "Data Science": {
                "demand": "High 📊",
                "growth": "30%",
                "salary": "₹9 LPA - ₹28 LPA",
                "skills": [
                    "Python",
                    "SQL",
                    "Power BI",
                    "Tableau",
                    "Machine Learning"
                ]
            },

            "DevOps": {
                "demand": "High 🚀",
                "growth": "26%",
                "salary": "₹10 LPA - ₹30 LPA",
                "skills": [
                    "Docker",
                    "Kubernetes",
                    "Jenkins",
                    "Git",
                    "Terraform"
                ]
            },

            "Full Stack Development": {
                "demand": "High 💻",
                "growth": "25%",
                "salary": "₹7 LPA - ₹24 LPA",
                "skills": [
                    "React",
                    "Node.js",
                    "FastAPI",
                    "MongoDB",
                    "PostgreSQL"
                ]
            },

            "Mobile App Development": {
                "demand": "Medium 📱",
                "growth": "20%",
                "salary": "₹6 LPA - ₹18 LPA",
                "skills": [
                    "Flutter",
                    "Kotlin",
                    "Swift",
                    "Firebase",
                    "Android Studio"
                ]
            },

            "Internet of Things (IoT)": {
                "demand": "High 🌐",
                "growth": "24%",
                "salary": "₹6 LPA - ₹20 LPA",
                "skills": [
                    "Arduino",
                    "Raspberry Pi",
                    "MQTT",
                    "Embedded C",
                    "Sensor Integration"
                ]
            }
        }


        technology = st.selectbox(
            "Select Technology",
            list(technology_data.keys())
        )


        if st.button("Show Industry Trends"):

            data = technology_data[technology]
            st.session_state["industry_technology"] = technology
            st.session_state["industry_demand"] = data["demand"]
            st.session_state["industry_growth"] = data["growth"]
            st.session_state["industry_salary"] = data["salary"]
            st.session_state["industry_skills"] = data["skills"]
            

            st.subheader(f"📊 {technology} Industry Analysis")


            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Market Demand",
                    data["demand"]
                )

            with col2:
                st.metric(
                    "Expected Growth",
                    data["growth"]
                )

            with col3:
                st.metric(
                    "Average Salary",
                    data["salary"]
                )


            st.divider()


            st.subheader("🚀 Trending Skills")
 
            for skill in data["skills"]:
                st.write("✅", skill)


            st.divider()


            st.subheader("💡 Career Recommendation")

            st.success(
                f"""
                To build a successful career in {technology},
                focus on learning the required skills, completing
                practical projects, earning certifications, and
                continuously improving your technical knowledge.
                """
            )


            st.subheader("📌 Learning Roadmap")

            st.write("""
            **Step 1:** Learn fundamentals and basic concepts  
        
            **Step 2:** Practice tools and technologies
        
            **Step 3:** Build real-world projects
        
            **Step 4:** Complete certifications
        
            **Step 5:** Apply skills through internships and jobs
            """)

#-------------------Certification Suggestions----------------------


    elif feature == "Certification Suggestions":

        st.header("🎓 Certification Suggestions")

        st.write("Select your career domain to view recommended certifications.")

        domain = st.selectbox(
            "Select Your Domain",
            [
                "Software Development",
                "Cloud Computing",
                "DevOps",
                "Data Science",
                "Artificial Intelligence",
                "Cyber Security",
                "Backend Development",
                "Full Stack Development",
                "Project Management",
                "Leadership & Management"
            ]
        )

        if st.button("Show Recommendations"):

            certifications = []


            if domain == "Software Development":

                certifications = [
                    "Oracle Certified Professional (Java)",
                    "Python Programming Professional",
                    "Advanced Data Structures & Algorithms"
                ]


            elif domain == "Cloud Computing":

                certifications = [
                    "AWS Certified Solutions Architect",
                    "Microsoft Azure Administrator",
                    "Google Associate Cloud Engineer"
                ]


            elif domain == "DevOps":

                certifications = [
                    "Docker Certified Associate",
                    "Certified Kubernetes Administrator (CKA)",
                    "Jenkins Professional"
                ]


            elif domain == "Data Science":

                certifications = [
                    "IBM Data Science Professional",
                    "Advanced Machine Learning",
                    "Data Analytics Professional"
                ]


            elif domain == "Artificial Intelligence":

                certifications = [
                    "AI Engineer Certification",
                    "Generative AI Professional",
                    "Deep Learning Specialization"
                ]


            elif domain == "Cyber Security":

                certifications = [
                    "Certified Ethical Hacker (CEH)",
                    "CompTIA Security+",
                    "CISSP"
                ]


            elif domain == "Backend Development":

                certifications = [
                    "FastAPI Professional",
                    "Spring Boot Certification",
                    "REST API Development"
                ]


            elif domain == "Full Stack Development":

                certifications = [
                    "MERN Stack Certification",
                    "React Professional",
                    "Full Stack Web Development"
                ]


            elif domain == "Project Management":

                certifications = [
                    "PMP (Project Management Professional)",
                    "PRINCE2 Foundation",
                    "Scrum Master Certification"
                ]


            elif domain == "Leadership & Management":

                certifications = [
                    "Agile Leadership",
                    "Strategic Leadership",
                    "Business Communication & Leadership"
                ]


    # SAVE DATA FOR REPORT
            st.session_state["certification_domain"] = domain
            st.session_state["certifications"] = certifications


            benefits = [
                "Improve technical and professional skills",
                "Increase promotion opportunities",
                "Enhance leadership capabilities",
                "Stay updated with industry trends",
                "Strengthen your professional profile"
            ]

            st.session_state["certification_benefits"] = benefits


    # DISPLAY OUTPUT
            st.subheader(f"Recommended Certifications for {domain}")

            for cert in certifications:
                st.write("✅", cert)


            st.write("---")

            st.subheader("Benefits")

            for benefit in benefits:
                st.write("✅", benefit)


#----------------Leadership Evaluation-------------------------------

    

    elif feature == "Leadership Evaluation":

        st.header("👨‍💼 Leadership Evaluation")

        st.write("Evaluate your leadership skills.")

        q1 = st.radio(
            "1. How do you handle team conflicts?",
            [
                "Ignore them",
                "Listen to everyone and find a solution",
                "Let others solve it",
                "Take one person's side"
            ]
        )

        q2 = st.radio(
            "2. How do you motivate your team?",
            [
                "Give clear guidance and appreciation",
                "Do nothing",
                "Only assign work",
                "Criticize mistakes"
            ]
        )

        q3 = st.radio(
            "3. How confident are you in making decisions?",
            [
                "Very Confident",
                "Somewhat Confident",
                "Not Confident"
            ]
        )

        q4 = st.radio(
            "4. How do you manage project deadlines?",
            [
                "Plan and prioritize tasks",
                "Work at the last minute",
                "Depend on others",
                "Ignore deadlines"
            ]
        )

        q5 = st.radio(
            "5. How do you respond to workplace changes?",
            [
                "Adapt quickly",
                "Need some time",
                "Avoid changes"
            ]
        )

        if st.button("Evaluate Leadership"):
  
            score = 0

            if q1 == "Listen to everyone and find a solution":
                score += 20

            if q2 == "Give clear guidance and appreciation":
                score += 20

            if q3 == "Very Confident":
                score += 20
            elif q3 == "Somewhat Confident":
                score += 10

            if q4 == "Plan and prioritize tasks":
                score += 20

            if q5 == "Adapt quickly":
                score += 20
            elif q5 == "Need some time":
                score += 10

                # Create recommendations list
            recommendations = []

            if score >= 80:

                recommendations = [
                "Continue improving strategic leadership skills.",
                "Mentor and guide team members.",
                "Develop advanced decision-making skills.",
                "Improve strategic planning abilities."
            ]

            elif score >= 60:

                recommendations = [
                "Improve communication and presentation skills.",
                "Take ownership of projects.",
                "Practice conflict resolution.",
                "Enhance decision-making abilities.",
                "Learn Agile and team management techniques."
            ]

            else:

                recommendations = [
                "Develop teamwork and collaboration skills.",
                "Improve confidence in decision-making.",
                "Practice leadership activities.",
                "Improve communication skills."
            ]


    # Save for PDF report
            st.session_state["leadership_score"] = score
            st.session_state["leadership_recommendations"] = recommendations


            st.subheader("Leadership Evaluation Result")

            st.metric(
               "Leadership Score",
               f"{score}/100"
            )

            st.subheader("Recommendations")

            for item in recommendations:
                st.write("•", item)


#-----------------------Advanced Job Matching--------------------------
  

    elif feature == "Advanced Job Matching":

        st.header("🔍 Advanced Job Matching")

        st.write("Find job roles that match your skills and experience.")

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            2
        )

        skill = st.selectbox(
            "Primary Skill",
            [
                "Python",
                "Java",
                "SQL",
                "Cloud Computing",
                "Data Science",
                "Artificial Intelligence",
                "Cyber Security",
                "DevOps",
                "Backend Development",
                "Full Stack Development"
            ]
        )

        if st.button("Find Matching Jobs"):

            matched_jobs = []


            if skill == "Python":

                matched_jobs = [
                    "Python Developer",
                    "Backend Developer",
                    "Automation Engineer"
                ]

            elif skill == "Java":

                matched_jobs = [
                    "Java Developer",
                    "Software Engineer",
                    "Spring Boot Developer"
                ]

            elif skill == "SQL":

                matched_jobs = [
                    "Database Administrator",
                    "SQL Developer",
                    "Data Analyst"
                ]

            elif skill == "Cloud Computing":

                matched_jobs = [
                    "Cloud Engineer",
                    "Cloud Solutions Architect",
                    "Cloud Administrator"
                ]

            elif skill == "Data Science":

                matched_jobs = [
                    "Data Scientist",
                    "Data Analyst",
                    "Machine Learning Engineer"
                ]

            elif skill == "Artificial Intelligence":

                matched_jobs = [
                    "AI Engineer",
                    "Machine Learning Engineer",
                    "NLP Engineer"
                ]

            elif skill == "Cyber Security":

                matched_jobs = [
                    "Security Analyst",
                    "Cyber Security Engineer",
                    "SOC Analyst"
                ]

            elif skill == "DevOps":

                matched_jobs = [
                    "DevOps Engineer",
                    "Site Reliability Engineer",
                    "Platform Engineer"
                ]

            elif skill == "Backend Development":

                matched_jobs = [
                    "Backend Developer",
                    "API Developer",
                    "Software Engineer"
                ]

            elif skill == "Full Stack Development":

                matched_jobs = [
                    "Full Stack Developer",
                    "Web Application Developer",
                    "Software Engineer"
                ]


    # Career Advice
            if experience < 2:

                career_advice = (
                    "Focus on strengthening technical skills, "
                    "building projects, and gaining hands-on experience."
                )

            elif experience <= 5:

                career_advice = (
                    "Develop expertise in your domain, earn certifications, "
                    "and improve leadership skills."
                )

            else:

                career_advice = (
                    "Aim for senior roles, mentor others, contribute to "
                    "architecture decisions, and enhance strategic leadership skills."
                )


    # Save data for PDF Report
            st.session_state["job_skill"] = skill
            st.session_state["job_experience"] = experience
            st.session_state["matched_jobs"] = matched_jobs
            st.session_state["job_career_advice"] = career_advice


    # Display Results
            st.subheader("Recommended Job Roles")

            for job in matched_jobs:
                st.write("✅", job)


            st.write("---")

            st.subheader("Career Advice")

            st.info(career_advice)

#--------------------------90-Day Action Plan-----------------------


    elif feature == "90-Day Action Plan":

        st.header("📅 90-Day Action Plan")

        st.write("Generate a personalized 3-month career growth plan.")
        
        goal = st.selectbox( 
            "Select Your Career Goal", 
            [ 
                "Get a Promotion", 
                "Switch Company", 
                "Become a Team Lead", 
                "Become a Full Stack Developer", 
                "Become a Cloud Engineer", 
                "Become a Data Scientist", 
                "Become an AI Engineer", 
                "Become a DevOps Engineer" 
                ] 
            )

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            2
        )

        if st.button("Generate Action Plan"):
 
            st.success("Your Personalized 90-Day Action Plan")

        # ---------------- Month 1 ----------------

          
            month1 = [
                "Improve technical concepts.",
                "Practice coding for 1 hour daily.",
                "Complete one online certification.",
                "Read industry articles every week.",
                "Update LinkedIn profile."
            ]

            month2 = [
                "Build two real-world projects.",
                "Improve communication skills.",
                "Practice system design.",
                "Solve coding interview questions.",
                "Participate in mock interviews."
            ]

            month3 = [
                "Update resume.",
                "Apply for suitable job roles.",
                "Attend technical interviews.",
                "Network with professionals.",
                "Review progress and set new goals."
            ]


            goal_recommendations = []


            if goal == "Get a Promotion":

                goal_recommendations = [
                    "Improve leadership skills.",
                    "Take ownership of projects.",
                    "Mentor junior team members.",
                    "Learn project management."
                ]

            elif goal == "Switch Company":

                goal_recommendations = [
                    "Update your resume.",
                    "Strengthen DSA and System Design.",
                    "Apply to multiple companies.",
                    "Practice HR and technical interviews."
                ]

            elif goal == "Become a Team Lead":

                goal_recommendations = [
                    "Improve communication.",
                    "Learn Agile and Scrum.",
                    "Develop conflict resolution skills.",
                    "Practice decision-making."
                ]

            elif goal == "Become a Full Stack Developer":

                goal_recommendations = [
                    "Learn React and FastAPI.",
                    "Build full-stack projects.",
                    "Learn PostgreSQL.",
                    "Deploy applications online."
                ]

            elif goal == "Become a Cloud Engineer":

                goal_recommendations = [
                    "Learn AWS or Azure.",
                    "Practice Docker and Kubernetes.",
                    "Build cloud projects.",
                    "Complete cloud certifications."
                ]

            elif goal == "Become a Data Scientist":

                goal_recommendations = [
                    "Learn Python and SQL.",
                    "Practice Machine Learning.",
                    "Build data analysis projects.",
                    "Learn Power BI or Tableau."
                ]

            elif goal == "Become an AI Engineer":

                goal_recommendations = [
                    "Learn Deep Learning.",
                    "Practice Generative AI.",
                    "Build AI applications.",
                    "Study Large Language Models (LLMs)."
                ]

            elif goal == "Become a DevOps Engineer":

                goal_recommendations = [
                    "Learn Docker and Kubernetes.",
                    "Practice CI/CD pipelines.",
                    "Learn Terraform.",
                    "Complete DevOps certifications."
                ]

            st.write("---")

            st.subheader("📅 Month 1 : Build Strong Foundations")

            for item in month1:
                st.write("✅", item)


            st.write("---")

            st.subheader("📅 Month 2 : Apply Your Knowledge")

            for item in month2:
                st.write("✅", item)


            st.write("---")

            st.subheader("📅 Month 3 : Career Growth")

            for item in month3:
                st.write("✅", item)


            st.write("---")

            st.subheader("🎯 Goal-Specific Recommendations")

            for item in goal_recommendations:
                st.write("•", item)


            st.write("---")

            st.subheader("🏆 Expected Outcome After 90 Days")

            outcomes = [
                "Stronger technical skills",
                "Improved confidence",
                "Better interview preparation",
                "Updated professional profile",
                "Increased career opportunities"
            ]

            for item in outcomes:
                st.write("✅", item)
# Store data for PDF Report

            st.session_state["action_goal"] = goal
            st.session_state["action_experience"] = experience
            st.session_state["month1_plan"] = month1
            st.session_state["month2_plan"] = month2
            st.session_state["month3_plan"] = month3
            st.session_state["goal_recommendations"] = goal_recommendations

            st.session_state["action_outcomes"] = [
                "Stronger technical skills",
                "Improved confidence",
                "Better interview preparation",
                "Updated professional profile",
                "Increased career opportunities"
            ]              


#-----------------Report--------------------------
    elif feature == "Report":

        st.title("📄 Professionals Report")

        if st.button("Generate Report"):

            pdf = generate_professional_report()

            with open(pdf, "rb") as file:

                st.download_button(
                    "⬇ Download Professional Report",
                    file,
                    file_name="Professional_Report.pdf",
                    mime="application/pdf"
                )