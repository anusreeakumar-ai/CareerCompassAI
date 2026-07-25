from flask import Flask, render_template, request,redirect
import os
import requests
import sqlite3
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
API_KEY = "YOUR_API_KEY"
PROJECT_ID = "YOUR_PROJECT_ID"
DEPLOYMENT_URL = "YOUR_DEPLOYMENT_ENDPOINT"
@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        name="Anusree",
        career="AI Engineer"
    )
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    name = request.form['name']
    education = request.form['education']
    skills = request.form['skills'].lower()
    interest = request.form['interest'].lower()

    if "python" in skills and "ai" in interest:
        career = "AI Engineer"
        missing = "Machine Learning, TensorFlow, Deep Learning"

    elif "java" in skills:
        career = "Software Developer"
        missing = "Spring Boot, Microservices"

    elif "design" in interest:
        career = "UI/UX Designer"
        missing = "Figma, Adobe XD"

    elif "marketing" in interest:
        career = "Digital Marketing Specialist"
        missing = "SEO, Google Ads"

    else:
        career = "Data Analyst"
        missing = "Excel, Power BI, SQL"

    return render_template(
        "result.html",
        name=name,
        education=education,
        career=career,
        missing=missing
    )
@app.route("/interview", methods=["GET", "POST"])
def interview():

    questions = []

    if request.method == "POST":

        career = request.form["career"]

        if career == "AI Engineer":

            questions = [

                "What is Machine Learning?",

                "Difference between AI and ML?",

                "Explain Neural Networks.",

                "What is TensorFlow?",

                "What is Overfitting?"

            ]

        elif career == "Software Developer":

            questions = [

                "Explain OOP Concepts.",

                "What is Polymorphism?",

                "Difference between Stack and Queue?",

                "What is Git?",

                "Explain REST API."

            ]

        elif career == "Data Scientist":

            questions = [

                "Explain Data Cleaning.",

                "What is Pandas?",

                "Difference between Regression and Classification?",

                "Explain Cross Validation.",

                "What is Feature Engineering?"

            ]

        elif career == "Web Developer":

            questions = [

                "Difference between HTML and HTML5?",

                "Explain CSS Flexbox.",

                "What is JavaScript?",

                "Explain DOM.",

                "Difference between GET and POST."

            ]

        elif career == "Cyber Security Analyst":

            questions = [

                "What is SQL Injection?",

                "Explain Firewall.",

                "What is Encryption?",

                "Difference between Virus and Malware?",

                "Explain Phishing."

            ]

        elif career == "Cloud Engineer":

            questions = [

                "What is Cloud Computing?",

                "Difference between IaaS and PaaS?",

                "What is Docker?",

                "Explain Kubernetes.",

                "What is Virtualization?"

            ]

        else:

            questions = [

                "Tell me about yourself.",

                "Why should we hire you?",

                "Describe one challenging project.",

                "Where do you see yourself in 5 years?",

                "What are your strengths?"

            ]

    return render_template(
        "interview.html",
        questions=questions
    )
@app.route("/recommendation")
def recommendation():

    name = "Student"

    career = "AI Engineer"

    match = 94

    skills = [

        "Python",

        "Machine Learning",

        "Deep Learning",

        "TensorFlow",

        "Git",

        "Cloud Computing"

    ]

    courses = [

        "IBM SkillsBuild - Artificial Intelligence",

        "Python for Data Science",

        "Machine Learning with Python",

        "Google AI Essentials",

        "AWS Cloud Practitioner"

    ]

    roadmap = [

        "Complete Python Basics",

        "Learn Data Structures",

        "Study Machine Learning",

        "Practice TensorFlow",

        "Build AI Projects",

        "Deploy Projects",

        "Apply for AI Internships"

    ]

    salary = "₹6 LPA - ₹12 LPA"

    tips = [

        "Practice coding daily.",

        "Build at least 5 AI projects.",

        "Create a GitHub portfolio.",

        "Learn system design basics.",

        "Prepare HR interview questions."

    ]

    return render_template(

        "recommendation.html",

        name=name,

        career=career,

        match=match,

        skills=skills,

        courses=courses,

        roadmap=roadmap,

        salary=salary,

        tips=tips

    )
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("database.db", timeout=10)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users
                (name,email,password,age,gender,college,degree,branch,year,cgpa,company,skills,interests,workmode,goal)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                request.form["name"],
                request.form["email"],
                request.form["password"],
                request.form["age"],
                request.form["gender"],
                request.form["college"],
                request.form["degree"],
                request.form["branch"],
                request.form["year"],
                request.form["cgpa"],
                request.form["company"],
                request.form["skills"],
                request.form["interests"],
                request.form["workmode"],
                request.form["goal"]
            ))

            conn.commit()

        finally:
            conn.close()

        return redirect("/dashboard")

    return render_template("register.html")

@app.route("/result")
def result():

    return render_template(
        "result.html",
        name="Anusree",
        career="AI Engineer",
        match=94,
        workmode="Hybrid",
        salary="₹8 LPA - ₹15 LPA",

        skills=[
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Git",
            "Cloud Computing"
        ],

        courses=[
            "IBM SkillsBuild AI Fundamentals",
            "Google AI Essentials",
            "Machine Learning with Python",
            "AWS Cloud Practitioner"
        ],

        roadmap=[
            "Complete Python",
            "Learn Data Structures",
            "Study Machine Learning",
            "Build AI Projects",
            "Create GitHub Portfolio",
            "Apply for Internships"
        ],

        tips=[
            "Practice coding daily",
            "Revise Python fundamentals",
            "Build real-world projects",
            "Prepare HR questions",
            "Practice mock interviews"
        ],
          missing="Machine Learning, TensorFlow, Git, Cloud Computing"
    )
        
    
@app.route("/resume", methods=["GET", "POST"])
def resume():

    if request.method == "POST":

        file = request.files["resume"]

        if file:

            filename = secure_filename(file.filename)

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

            file.save(filepath)

            score = 85

            strengths = [
                "Good Resume Format",
                "Projects Included",
                "Skills Mentioned",
                "Education Complete"
            ]

            suggestions = [
                "Add GitHub Profile",
                "Improve Summary",
                "Add Certifications",
                "Include Internship Experience"
            ]

            ats = "ATS Friendly (85%)"

            return render_template(
                "resume.html",
                score=score,
                strengths=strengths,
                suggestions=suggestions,
                ats=ats,
                filename=filename
            )

    return render_template("resume.html")
@app.route("/roadmap")
def roadmap():

    career = "AI Engineer"

    return render_template(
        "roadmap.html",
        career=career
    )
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)