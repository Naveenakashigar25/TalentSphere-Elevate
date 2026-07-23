import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os
import matplotlib.pyplot as plt
from reportlab.platypus import Image
def create_performance_chart():

    labels = [
        "Science",
        "Commerce",
        "Arts",
        "Aptitude",
        "Communication"
    ]

    scores = [
        st.session_state.get("science_score",0),
        st.session_state.get("commerce_score",0),
        st.session_state.get("arts_score",0),
        st.session_state.get("aptitude_score",0),
        st.session_state.get("communication_score",0)
    ]

    plt.figure(figsize=(8,4))

    plt.bar(labels, scores)

    plt.ylim(0,100)

    plt.ylabel("Percentage")

    plt.title("Assessment Scores")

    for i, value in enumerate(scores):
        plt.text(i, value + 2, f"{value:.0f}%", ha="center")

    plt.savefig("assessment_graph.png")

    plt.close()

    return "assessment_graph.png"

def generate_highschool_report():

    filename = "TalentSphere_HighSchool_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # ---------------- Title ----------------

    story.append(Paragraph("<b>TalentSphere Elevate</b>", styles["Title"]))
    story.append(Paragraph("High School Student Assessment Report", styles["Heading1"]))
    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    # ---------------- Personal Information ----------------

    story.append(Paragraph("<b>PERSONAL INFORMATION</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Name : {st.session_state.get('name','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Email : {st.session_state.get('email','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Date of Birth : {st.session_state.get('dob','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Phone Number : {st.session_state.get('phone','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------- Career Quiz ----------------

    story.append(Paragraph("<b>CAREER QUIZ ASSESSMENT</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Science Score : {st.session_state.get('science_score',0)}%",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Commerce Score : {st.session_state.get('commerce_score',0)}%",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Arts Score : {st.session_state.get('arts_score',0)}%",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"Recommended Stream : {st.session_state.get('recommended_stream','Not Available')}",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------- Aptitude ----------------

    story.append(Paragraph("<b>APTITUDE ASSESSMENT</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Aptitude Score : {st.session_state.get('aptitude_score',0)}%",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------- Communication ----------------

    story.append(Paragraph("<b>COMMUNICATION SKILL ASSESSMENT</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Communication Score : {st.session_state.get('communication_score',0)}%",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>Performance Graph</b>", styles["Heading2"]))

    chart = create_performance_chart()

    story.append(Image(chart, width=420, height=260))

    doc.build(story)
    return filename

def highschool_dashboard():



    st.title("🎓 High School Dashboard")



    feature = st.sidebar.selectbox(

        "Select Feature",

        [
            "Home",

            "👤 Personal Information",

            "Career Guidance",

            "Career Quiz Assessment",

            "Aptitude Practice",

            "Communication Skills",

            "AI Mentor Chatbot",

            "Download Report"

        ]

    )
   

    # ------------------------------------

    # HOME

    # ------------------------------------



    if feature == "Home":



        st.header("Welcome")



        st.write("""

TalentSphere Elevate helps High School students choosethe right career path and improve their skills.
""")


     #------------------------------------
    #personal information
    #------------------------------------

    elif feature == "👤 Personal Information":

        st.title("👤 Personal Information")

        name = st.text_input(
            "Full Name",
            value=st.session_state.get("name", "")
        )

        email = st.text_input(
            "Email",
            value=st.session_state.get("email", "")
        )

        dob = st.date_input(
            "Date of Birth",
            value=datetime.date(2008, 1, 1),     
            min_value=datetime.date(1990, 1, 1),  
            max_value=datetime.date.today() 
        )

        phone = st.text_input(
            "Phone Number",
            value=st.session_state.get("phone", "")
        )

        if st.button("Save Information"):

            st.session_state.name = name
            st.session_state.email = email
            st.session_state.dob = str(dob)
            st.session_state.phone = phone

            st.success("✅ Personal Information Saved Successfully")
    # ------------------------------------

    # CAREER GUIDANCE

    # ------------------------------------



    elif feature == "Career Guidance":



        st.header("Career Guidance")



        stream = st.selectbox(

            "Select Your Stream",

            [

                "Science",

                "Commerce",

                "Arts"

            ]

        )



        if stream == "Science":



            st.subheader("Science Career Options")



            st.write("""

✔ Engineering



✔ Medicine



✔ Pharmacy



✔ Biotechnology



✔ B.Sc



✔ AI & Data Science



✔ Cyber Security

""")



        elif stream == "Commerce":



            st.subheader("Commerce Career Options")



            st.write("""

✔ B.Com



✔ CA



✔ CS



✔ CMA



✔ Banking



✔ Finance



✔ Digital Marketing

""")



        else:



            st.subheader("Arts Career Options")



            st.write("""

✔ BA



✔ Journalism



✔ Law



✔ Fashion Designing



✔ Psychology



✔ Hotel Management



✔ Civil Services

""")
            
    #-------------------------------------
    #Career Quiz Assessment
    #-------------------------------------
    elif feature == "Career Quiz Assessment":

        st.title("Career Quiz Assessment")
        st.write("Choose a stream to test your aptitude.")

        if "selected_quiz" not in st.session_state:
            st.session_state.selected_quiz = None

        if "science_score" not in st.session_state:
            st.session_state.science_score = None

        if "commerce_score" not in st.session_state:
            st.session_state.commerce_score = None

        if "arts_score" not in st.session_state:
            st.session_state.arts_score = None

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🔬 Science Quiz"):
                st.session_state.selected_quiz = "Science"

        with col2:
            if st.button("💼 Commerce Quiz"):
                st.session_state.selected_quiz = "Commerce"

        with col3:
            if st.button("🎨 Arts Quiz"):
                st.session_state.selected_quiz = "Arts"

        st.divider()

    # ---------------- SCIENCE ---------------- #

        if st.session_state.selected_quiz == "Science":

            st.subheader("🔬 Science Quiz")

            score = 0

            if st.radio("1. Red Planet?", ["Earth","Mars","Venus","Jupiter"]) == "Mars":
                score += 1

            if st.radio("2. SI unit of Force?", ["Newton","Joule","Watt","Volt"]) == "Newton":
                score += 1

            if st.radio("3. Water Formula?", ["CO2","H2O","O2","NaCl"]) == "H2O":
                score += 1

            if st.radio("4. Which organ pumps blood?", ["Heart","Brain","Kidney","Liver"]) == "Heart":
                score += 1

            if st.radio("5. 12 × 15 = ?", ["150","180","200","220"]) == "180":
                score += 1
            
            if st.radio("6. Which is the largest planet in our Solar System?",["Earth", "Mars", "Jupiter", "Saturn"])== "Jupiter":
                score += 1

            if st.radio("7. What is the square root of 225?", ["12", "15", "18", "20"])== "15":
                score += 1

            if st.radio("8. Which vitamin is produced when our skin is exposed to sunlight?",["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"])== "Vitamin D":
                score += 1

            if st.radio("9. Which branch of science studies living organisms?",["Physics", "Chemistry", "Biology", "Astronomy"])== "Biology":
                score += 1

            if st.radio( "10. What is the SI unit of Energy?",["Newton", "Joule", "Watt", "Volt"])== "Joule":
                score += 1

            if st.radio("11. Which blood group is called the universal donor?",["A+", "B+", "AB+", "O-"])== "O-":
                score += 1

            if st.radio("12. Speed = Distance ÷ ?",["Area", "Time", "Mass", "Volume"])== "Time":
                score += 1

            if st.radio("13. Which force keeps planets moving around the Sun?",["Magnetic Force", "Electric Force", "Gravity", "Friction"])== "Gravity":
                score += 1

            if st.radio( "14. What is 25 × 8?",["180", "190", "200", "220"])== "200":
                score += 1
        
            if st.radio("15. Which instrument measures electric current?",["Voltmeter", "Ammeter", "Thermometer", "Barometer"])== "Ammeter":
                score += 1

            if st.radio("16. Which part of the plant prepares food?",["Root", "Stem", "Leaf", "Flower"])== "Leaf":
                score += 1

            if st.radio("17. Which gas is essential for human respiration?",["Nitrogen", "Hydrogen", "Carbon Dioxide", "Oxygen"])== "Oxygen":
                score += 1

            if st.radio("18. Which engineering branch mainly develops software applications?",["Mechanical", "Civil", "Computer Science", "Chemical"])== "Computer Science":
                score += 1

            if st.radio("19. Which scientist proposed the three laws of motion?",["Albert Einstein", "Isaac Newton", "Galileo", "Nikola Tesla"])== "Isaac Newton":
                score += 1

            if st.radio("20. If a student enjoys Mathematics, Physics, and solving logical problems, which stream is generally the most suitable?",["Science", "Commerce", "Arts", "Any stream"])== "Science":
                score += 1
            if st.button("Submit Science Quiz"):

                st.session_state.science_score = score

                st.success(f"Science Score : {score}/20")

                percentage = (score / 20) * 100
                st.session_state.Science_score = percentage

                if "Science_score" in st.session_state:
                    st.success(
                        f"🎯 Science Score: {st.session_state.Science_score:.0f}%"
                    )
                    st.progress(st.session_state.Science_score / 100)

    # ---------------- COMMERCE ---------------- #

        elif st.session_state.selected_quiz == "Commerce":

            st.subheader("💼 Commerce Quiz")

            score = 0

            if st.radio(
                "1. Profit = ?",
                [
                    "Selling Price - Cost Price",
                    "Cost Price - Selling Price",
                    "SP + CP",
                    "None"
                ]
            ) == "Selling Price - Cost Price":
                score += 1

            if st.radio(
                "2. GST stands for?",
                [
                    "Goods and Service Tax",
                    "Government Sales Tax",
                    "General Sales Tax",
                    "None"
                ]
            ) == "Goods and Service Tax":
                score += 1

            if st.radio(
                "3. Central Bank of India?",
                [
                    "RBI",
                    "SBI",
                    "ICICI",
                    "PNB"
                ]
            ) == "RBI":
                score += 1

            if st.radio(
                "4. IPO stands for?",
                [
                    "Initial Public Offering",
                    "Indian Public Office",
                    "Internal Public Office",
                    "None"
                ]
            ) == "Initial Public Offering":
                score += 1

            if st.radio(
                "5. Which profession prepares financial statements?",
                [
                    "Doctor",
                    "Engineer",
                    "Chartered Accountant",
                    "Teacher"
                ]
            ) == "Chartered Accountant":
                score += 1

            if st.radio(
                "6. Which account records cash transactions?", 
                [
                    "Cash Book", 
                    "Journal",
                    "Ledger", 
                    "Invoice"
                ]
            )== "Cash Book":
                score += 1

            if st.radio(
                "7. Main objective of business?",
                [
                    "Profit", 
                    "Loss", 
                    "Donation", 
                    "Entertainment"
                ]
            )== "Profit":
                score += 1

            if st.radio(
                "8. Which tax is paid on income?", 
                [
                    "Income Tax", 
                    "GST", 
                    "Road Tax", 
                    "Property Tax"
                ]
            )== "Income Tax":
                score += 1

            if st.radio(
                "9. What is a Balance Sheet?", 
                [
                    "Assets & Liabilities Statement", 
                    "Sales Report", 
                    "Attendance Sheet", 
                    "Invoice"
                ]
            )== "Assets & Liabilities Statement":
                score += 1

            if st.radio(
                "10. SEBI regulates?", 
                [
                    "Stock Market", 
                    "Schools", 
                    "Hospitals", 
                    "Railways"
                ]
            )== "Stock Market":
                score += 1

            if st.radio(
                "11. Marketing helps to?", 
                [
                    "Sell Products", 
                    "Build Roads", 
                    "Treat Patients", 
                    "Teach Students"
                ]
            )== "Sell Products":
                score += 1

            if st.radio(
                "12. Sole Proprietorship has?",
                [
                    "One Owner", 
                    "Two Owners", 
                    "Many Owners", 
                    "Government"
                ]
            )== "One Owner":
                score += 1

            if st.radio(
                "13. Budget means?",
                [
                    "Financial Plan", 
                    "Loan", 
                    "Profit", 
                    "Tax"
                ]
            )== "Financial Plan":
                score += 1

            if st.radio(
                "14. Which is a digital payment method?",
                [
                    "UPI", 
                    "Bluetooth", 
                    "USB", 
                    "Wi-Fi"
                ]
            )== "UPI":
                score += 1

            if st.radio(
                "15. Entrepreneurship means?", 
                [
                    "Starting a Business", 
                    "Teaching", 
                    "Farming", 
                    "Driving"
                ]
            )== "Starting a Business":
                score += 1

            if st.radio(
                "16. Invoice is issued after?", 
                [
                    "Sale", 
                    "Purchase", 
                    "Meeting", 
                    "Interview"
                ]
            )== "Sale":
                score += 1

            if st.radio(
                "17. Which bank gives education loans?", 
                [
                    "Commercial Bank", 
                    "Post Office", 
                    "School", 
                    "Hospital"
                ]
            )== "Commercial Bank":
                score += 1

            if st.radio(
                "18. Which document records daily transactions?", 
                [
                    "Journal", 
                    "Balance Sheet", 
                    "Invoice", 
                    "Ledger"
                ]
            )== "Journal":
                score += 1

            if st.radio(
                "19. Cost Price means?", 
                [
                    "Buying Price", 
                    "Selling Price", 
                    "Discount", 
                    "Tax"
                ]
            )== "Buying Price":
                score += 1

            if st.radio(
                "20. Which sector includes banking?", 
                [
                    "Service Sector", 
                    "Agriculture", 
                    "Manufacturing", 
                    "Transport"
                ]
                )== "Service Sector":
                    score += 1

            if st.button("Submit Commerce Quiz"):

                st.session_state.commerce_score = score

                st.success(f"Commerce Score : {score}/20")
                percentage = (score / 20) * 100
                st.session_state.Commerce_score = percentage

                if "Commerce_score" in st.session_state:
                    st.success(
                        f"🎯 Commerce Score: {st.session_state.Commerce_score:.0f}%"
                    )
                    st.progress(st.session_state.Commerce_score / 100)



    # ---------------- ARTS ---------------- #

        elif st.session_state.selected_quiz == "Arts":

            st.subheader("🎨 Arts Quiz")

            score = 0

            if st.radio(
                "1. National Anthem written by?",
                [
                    "Rabindranath Tagore",
                    "Gandhi",
                    "Nehru",
                    "Tilak"
                ]
            ) == "Rabindranath Tagore":
                score += 1

            if st.radio(
                "2. Capital of Karnataka?",
                [
                    "Bengaluru",
                    "Mysuru",
                    "Hubballi",
                    "Belagavi"
                ]
            ) == "Bengaluru":
                score += 1

            if st.radio(
                "3. Largest Continent?",
                [
                    "Asia",
                    "Europe",
                    "Africa",
                    "Australia"
                ]
            ) == "Asia":
                score += 1

            if st.radio(
                "4. Psychology studies?",
                [
                    "Human Mind",
                    "Plants",
                    "Animals",
                    "Computers"
                ]
            ) == "Human Mind":
                score += 1

            if st.radio(
                "5. Democracy means?",
                [
                    "Rule by People",
                    "Rule by King",
                    "Rule by Army",
                    "Rule by Queen"
                ]
            ) == "Rule by People":
                score += 1

            if st.radio(
                "6. Who built the Taj Mahal?", 
                [
                    "Shah Jahan", 
                    "Akbar", 
                    "Aurangzeb", 
                    "Babur"
                ]
            )== "Shah Jahan":
                score += 1

            if st.radio(
                "7. Which is the longest river in India?", 
                [
                    "Ganga", 
                    "Godavari", 
                    "Krishna", 
                    "Kaveri"
                ]
            )== "Ganga":
                score += 1

            if st.radio(
                "8. First President of India?", 
                [
                    "Dr. Rajendra Prasad", 
                    "Dr. APJ Abdul Kalam", 
                    "Jawaharlal Nehru", 
                    "Sardar Patel"
                ]
            )== "Dr. Rajendra Prasad":
                score += 1

            if st.radio(
                "9. Which state is known as the Land of Five Rivers?", 
                [
                    "Punjab", 
                    "Kerala", 
                    "Tamil Nadu", 
                    "Odisha"
                ]
            )== "Punjab":
                score += 1

            if st.radio(
                "10. Journalism is related to?", 
                [
                    "News Reporting",
                      "Medicine", 
                      "Engineering", 
                      "Banking"
                ]
            )== "News Reporting":
                score += 1

            if st.radio(
                "11. Which organization conducts UPSC exams?", 
                [
                    "UPSC", 
                    "SSC", 
                    "IBPS", 
                    "AICTE"
                ]
            )== "UPSC":
                score += 1

            if st.radio(
                "12. Mahatma Gandhi launched?", 
                [
                    "Dandi March", 
                    "Green Revolution", 
                    "Operation Flood", 
                    "White Revolution"
                ]
            )== "Dandi March":
                score += 1

            if st.radio(
                "13. UNESCO stands for?", 
                [
                    "United Nations Educational, Scientific and Cultural Organization", 
                    "United National Education Society", 
                    "Universal Education Council", 
                    "None"
                ]
            )== "United Nations Educational, Scientific and Cultural Organization":
                score += 1

            if st.radio(
                "14. Which language has the highest number of native speakers?", 
                [
                    "Mandarin Chinese", 
                    "English", 
                    "Hindi", 
                    "Spanish"
                ]
            )== "Mandarin Chinese":
                score += 1

            if st.radio(
                "15. Constitution of India came into effect on?", 
                [
                    "26 January 1950", 
                    "15 August 1947", 
                    "2 October 1948", 
                    "26 November 1949"
                ]
            )== "26 January 1950":
                score += 1

            if st.radio(
                "16. Which field studies human society?",
                [
                    "Sociology", 
                    "Physics", 
                    "Chemistry", 
                    "Biology"
                ]
            )== "Sociology":
                score += 1

            if st.radio(
                "17. Which is the largest democracy in the world?", 
                [
                    "India", 
                    "USA", 
                    "Japan", 
                    "Australia"
                ]
            )== "India":
                score += 1

            if st.radio(
                "18. Which freedom fighter is known as Netaji?", 
                [
                    "Subhas Chandra Bose", 
                    "Bhagat Singh", 
                    "Gandhi", 
                    "Nehru"
                ]
            )== "Subhas Chandra Bose":
                score += 1

            if st.radio(
                "19. Which country gifted the Statue of Liberty to the USA?", 
                [
                    "France", 
                    "India", 
                    "UK", 
                    "Germany"
                ]
            )== "France":
                score += 1

            if st.radio(
                "20. Which subject helps us understand maps and landforms?", 
                [
                    "Geography", 
                    "History", 
                    "Economics", 
                    "Political Science"
                ]
            )== "Geography":
                score += 1
            if st.button("Submit Arts Quiz"):

                st.session_state.arts_score = score

                st.success(f"Arts Score : {score}/20")
                percentage = (score / 20) * 100
                st.session_state.arts_score = percentage

                if "arts_score" in st.session_state:
                    st.success(
                        f"🎯 arts Score: {st.session_state.arts_score:.0f}%"
                    )
                    st.progress(st.session_state.arts_score / 100)

        st.divider()

        st.subheader("📊 Quiz Progress")

        st.write(f"🔬 Science : {st.session_state.science_score if st.session_state.science_score is not None else 'Not Attempted'}")

        st.write(f"💼 Commerce : {st.session_state.commerce_score if st.session_state.commerce_score is not None else 'Not Attempted'}")

        st.write(f"🎨 Arts : {st.session_state.arts_score if st.session_state.arts_score is not None else 'Not Attempted'}")

        if (
            st.session_state.science_score is not None and
            st.session_state.commerce_score is not None and
            st.session_state.arts_score is not None
        ):

            if st.button("🏆 Recommend Stream"):

                scores = {
                    "Science": st.session_state.science_score,
                    "Commerce": st.session_state.commerce_score,
                    "Arts": st.session_state.arts_score
                }

                recommended = max(scores, key=scores.get)

                st.success(f"🎯 Recommended Stream: {recommended}")

                if recommended == "Science":
                    st.write("💻 Careers: Software Engineer, Doctor, AI Engineer, Data Scientist")

                elif recommended == "Commerce":
                    st.write("💼 Careers: CA, Banker, Financial Analyst, Entrepreneur")

                else:
                    st.write("🎨 Careers: Lawyer, Journalist, Psychologist, Civil Services")
                    
                    st.session_state.recommended_stream = recommended_Stream
    # ------------------------------------

    # APTITUDE

    # ------------------------------------

    elif feature == "Aptitude Practice":



        st.header("Aptitude Practice")



        score = 0



        q1 = st.radio(

            "1. 15 + 27 = ?",

            ["40","42","43","45"],

            key="q1"

        )



        q2 = st.radio(

            "2. Which number is divisible by 5?",

            ["22","41","55","67"],

            key="q2"

        )



        q3 = st.radio(

            "3. Next Number: 2,4,6,8,?",

            ["9","10","12","14"],

            key="q3"

        )



        q4 = st.radio(

            "4. Which is the largest?",

            ["12","19","17","16"],

            key="q4"

        )



        q5 = st.radio(

            "5. Square of 12?",

            ["124","140","144","154"],

            key="q5"

        )

        q6 = st.radio(
            "6. 25 × 4 = ?", 
            ["75", "80", "90", "100"],
            key="q6"
        )
        q7 = st.radio(
            "7. Half of 200 is?", 
            ["50", "100", "150", "120"], 
            key="q7"
        )
        q8 = st.radio(
            "8. Which is a prime number?", 
            ["15", "21", "17", "27"], 
            key="q8"
        )

        q9 = st.radio(
            "9. 9² = ?", 
            ["72", "81", "91", "99"], 
            key="q9"
        )

        q10 = st.radio(
            "10. Which is the smallest number?", 
            ["18", "12", "25", "20"], 
            key="q10"
        )

        q11 = st.radio(
            "11. Next number: 5, 10, 15, 20, ?", 
            ["24", "25", "30", "35"], 
            key="q11"
        )

        q12 = st.radio(
            "12. 120 ÷ 10 = ?", 
            ["10", "11", "12", "13"], 
            key="q12"
        )

        q13 = st.radio(
            "13. If today is Monday, after 3 days it will be?", 
            ["Tuesday", "Thursday", "Friday", "Sunday"], 
            key="q13"
        )

        q14 = st.radio(
            "14. Which shape has 4 equal sides?", 
            ["Triangle", "Rectangle", "Square", "Circle"], 
            key="q14"
        )

        q15 = st.radio(
            "15. Which planet is called the Red Planet?", 
            ["Earth", "Mars", "Venus", "Jupiter"], 
            key="q15"
        )

        q16 = st.radio(
            "16. 18 + 19 = ?", 
            ["36", "37", "38", "39"], 
            key="q16"
        )

        q17 = st.radio(
            "17. Which is an even number?", 
            ["15", "21", "28", "33"], 
            key="q17"
        )

        q18 = st.radio(
            "18. Opposite of 'Success'?", 
            ["Victory", "Failure", "Achievement", "Progress"], 
            key="q18"
        )

        q19 = st.radio(
            "19. Complete the series: A, C, E, G, ?", 
            ["H", "I", "J", "K"], 
            key="q19"
        )

        q20 = st.radio(
            "20. Which is the largest ocean?", 
            ["Indian", "Atlantic", "Pacific", "Arctic"], 
            key="q20"
        )

        q21 = st.radio(
            "21. 45 + 35 = ?", 
            ["70", "75", "80", "85"], 
            key="q21"
        )

        q22 = st.radio(
            "22. 56 ÷ 8 = ?", 
            ["6", "7", "8", "9"], 
            key="q22"
        )

        q23 = st.radio(
            "23. Cube of 4 is?", 
            ["16", "32", "64", "48"], 
            key="q23"
        )

        q24 = st.radio(
            "24. Which is a programming language?", 
            ["Python", "Chrome", "Google", "Windows"], 
            key="q24"
        )

        q25 = st.radio(
            "25. Which animal is known as the King of the Jungle?", 
            ["Tiger", "Elephant", "Lion", "Leopard"], 
            key="q25"
        )

        q26 = st.radio(
            "26. 14 × 6 = ?", 
            ["72", "84", "92", "96"], 
            key="q26"
        )

        q27 = st.radio(
            "27. Which is the national bird of India?", 
            ["Peacock", "Parrot", "Sparrow", "Crow"], 
            key="q27"
        )

        q28 = st.radio(
            "28. Find the odd one out.", 
            ["Apple", "Mango", "Potato", "Banana"], 
            key="q28"
        )

        q29 = st.radio(
            "29. Which number comes next? 3, 6, 9, 12, ?", 
            ["13", "14", "15", "16"], 
            key="q29"
        )

        q30 = st.radio(
            "30. Which gas do plants absorb?", 
            ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 
            key="q30"
        )

        if st.button("Submit Test"):



            if q1=="42":

                score+=1



            if q2=="55":

                score+=1



            if q3=="10":

                score+=1



            if q4=="19":

                score+=1



            if q5=="144":

                score+=1

            
            if q6=="100":

                score+=1
         
            if q7=="100":

                score+=1
            if q8=="17":

                score+=1
            if q9=="81":

                score+=1
            if q10=="12":

                score+=1
            if q11=="25":

                score+=1
            if q12=="12":

                score+=1
            if q13=="Thursday":

                score+=1
            if q14=="Square":

                score+=1
            if q15=="Mars":

                score+=1
            if q16=="37":

                score+=1
            if q17=="28":

                score+=1
            if q18=="Failure":

                score+=1
            if q19=="I":

                score+=1
            if q20=="Pacific":

                score+=1
            if q21=="80":

                score+=1
            if q22=="7":

                score+=1
            if q23=="64":

                score+=1
            if q24=="Python":

                score+=1
            if q25=="Lion":

                score+=1
            if q26=="84":

                score+=1
            if q27=="Peacock":

                score+=1
            if q28=="Potato":

                score+=1
            if q29=="15":

                score+=1
            if q30=="Carbon Dioxide":

                score+=1
            st.success(f"Your Score : {score}/30")
            percentage = (score / 30) * 100
            st.session_state.aptitude_score = percentage

            if "aptitude_score" in st.session_state:
                st.success(
                    f"🎯 aptitude Score: {st.session_state.aptitude_score:.0f}%"
                )
                st.progress(st.session_state.aptitude_score / 100)



    # ------------------------------------

    # COMMUNICATION

    # ------------------------------------



    elif feature == "Communication Skills":

        st.header("Communication Skills")

        st.write("### Tips")

        st.write("✔ Speak confidently")
        st.write("✔ Maintain eye contact")
        st.write("✔ Read newspapers")
        st.write("✔ Improve vocabulary")
        st.write("✔ Practice public speaking")

        st.divider()

        if "show_comm" not in st.session_state:
            st.session_state.show_comm = False

        if st.button(
            "📝 Take Communication Skill Assessment",
            key="comm_btn"
        ):
            st.session_state.show_comm = True

        if st.session_state.show_comm:

            st.subheader("Communication Assessment")

            score=0
            if st.radio("1. What is the most important part of effective communication?",["Listening", "Talking", "Writing", "Reading"])== "Listening":
                score += 1

            if st.radio("2. While speaking to someone, you should:",["Maintain eye contact", "Look at your phone", "Walk away", "Ignore them"])== "Maintain eye contact":
                score += 1

            if st.radio("3. Which of the following is a good communication skill?",["Interrupting others", "Listening carefully", "Speaking loudly always", "Ignoring questions"])== "Listening carefully":
                score += 1

            if st.radio("4. What should you do if you don't understand a question?",["Guess randomly", "Ask politely for clarification", "Stay silent", "Change the topic"])== "Ask politely for clarification":
                score += 1

            if st.radio("5. Which greeting is appropriate in a job interview?",["Good Morning", "Hey", "What's up?", "Hi Dude"])== "Good Morning":
                score += 1

            if st.radio("6. Which word is the most polite?",["Please", "Move", "Come", "Now"])== "Please":
                score += 1

            if st.radio("7. When someone is speaking, you should:",["Interrupt", "Listen patiently", "Look away", "Talk to someone else"])== "Listen patiently":
                score += 1

            if st.radio("8. Which sentence is grammatically correct?",["She goes to school.", "She go to school.", "She going school.", "She gone school."])== "She goes to school.":
                score += 1

            if st.radio("9. Which of these is a positive body language?",["Smiling", "Crossing arms angrily", "Looking down", "Rolling eyes"])== "Smiling":
                score += 1

            if st.radio("10. Which quality improves communication the most?",["Confidence", "Fear", "Anger", "Silence"])== "Confidence":
                score += 1

            if st.radio("11. What should you do before answering a question?",["Think carefully", "Answer immediately without thinking", "Ignore it", "Change the topic"])== "Think carefully":
                score += 1

            if st.radio("12. Which is an example of non-verbal communication?",["Eye contact", "Speaking", "Writing", "Reading"])== "Eye contact":
                score += 1

            if st.radio("13. Which word shows appreciation?",["Thank you", "Move", "No", "Stop"])== "Thank you":
                score += 1

            if st.radio("14. During a presentation, you should:",["Speak clearly", "Mumble", "Read everything without looking up", "Speak very fast"])== "Speak clearly":
                score += 1

            if st.radio("15. Which of these is a communication barrier?",["Noise", "Active listening", "Confidence", "Clear pronunciation"])== "Noise":
                score += 1

            if st.radio("16. Good communication helps in:",["Building relationships", "Creating misunderstandings", "Avoiding teamwork", "Increasing conflicts"])== "Building relationships":
                score += 1

            if st.radio("17. Which is the best way to answer in an interview?",["Be honest and confident", "Guess answers", "Stay silent", "Avoid eye contact"])== "Be honest and confident":
                score += 1

            if st.radio("18. What is the purpose of communication?",["Share ideas and information", "Create confusion", "Waste time", "Avoid people"])== "Share ideas and information":
                score += 1

            if st.radio("19. Which tone is best while talking to teachers or interviewers?",["Polite", "Rude", "Angry", "Very loud"])== "Polite":
                score += 1

            if st.radio("20. Which communication skill is most important for future careers?",["Listening and speaking effectively", "Arguing with everyone", "Ignoring feedback", "Talking continuously"])== "Listening and speaking effectively":
                score += 1

            
            
    # Convert score to percentage
                if st.button("Submit Communication Assessment"):
                    percentage = (score / 20) * 100
                    st.session_state.communication_score = percentage

                if "communication_score" in st.session_state:
                    st.success(
                        f"🎯 Communication Score: {st.session_state.communication_score:.0f}%"
                    )
                    st.progress(st.session_state.communication_score / 100)
                

                    if percentage >= 90:
                        st.balloons()
                        st.success("🌟 Excellent Communication Skills")
                        st.write("✔ Confident speaker")
                        st.write("✔ Active listener")
                        st.write("✔ Professional communication")
                        st.write("✔ Strong vocabulary")

                    elif percentage >= 75:
                        st.success("😊 Very Good Communication Skills")
                        st.write("✔ Good speaking ability")
                        st.write("✔ Good listening skills")
                        st.write("✔ Continue practicing vocabulary")

                    elif percentage >= 60:
                        st.info("🙂 Good Communication Skills")
                        st.write("✔ Basic communication is good")
                        st.write("✔ Improve confidence")
                        st.write("✔ Practice speaking English daily")

                    elif percentage >= 40:
                        st.warning("⚠ Average Communication Skills")
                        st.write("✔ Improve grammar")
                        st.write("✔ Practice public speaking")
                        st.write("✔ Improve pronunciation")

                    else:
                        st.error("❌ Needs Improvement")
                        st.write("✔ Read English newspapers")
                        st.write("✔ Watch English educational videos")
                        st.write("✔ Practice speaking for 15 minutes daily")
                        st.write("✔ Participate in group discussions")

    # ------------------------------------

    # AI CHATBOT

    # ------------------------------------
    elif feature == "AI Mentor Chatbot":
        st.header("AI Mentor Chatbot")
        question = st.text_input("Ask your question")



        if st.button("Ask AI"):

            if "science" in question.lower():

                st.success("Science is suitable if you enjoy Maths, Physics, Biology or Chemistry.")


            elif "commerce" in question.lower():

                st.success("Commerce is suitable if you are interested in Business, Accounts and Finance.")


            elif "arts" in question.lower():

                st.success("Arts offers careers in Law, Journalism, Psychology, Civil Services and Design.")

            elif "engineer" in question.lower():
                st.success("Choose PCM, prepare for JEE/CET and join an Engineering college.")
            
            elif "doctor" in question.lower():
                st.success("To become a Doctor: Choose PCB, prepare for NEET and complete MBBS.")
            elif "hello" in question.lower() or "hi" in question.lower():
                st.success("Hello! 👋 How can I help you today?")
            else:

                st.info("Explore your interests, strengths and career goals before choosing a stream.")               

    #----------------------------------
    # Report
    # ---------------------------------

    elif feature == "Download Report":

        st.title("Student Assessment Report")

        if st.button("Generate Report"):

            pdf = generate_highschool_report()

            with open(pdf, "rb") as file:

                st.download_button(
                    "⬇ Download PDF Report",
                    data=file,
                    file_name="TalentSphere_HighSchool_Report.pdf",
                    mime="application/pdf"
                )