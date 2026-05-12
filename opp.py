import streamlit as st
import smtplib
from email.mime.text import MIMEText

# -----------------------------------------------------
# Mitradnya Publication - Email Setup
# -----------------------------------------------------
# (टीप: येथे तुम्हाला तुमचा खरा ईमेल आणि Gmail चा App Password टाकावा लागेल)
TEACHER_EMAIL = "your_email@gmail.com" 
EMAIL_PASSWORD = "your_app_password"   

def send_score_to_teacher(student_name, score):
    msg_content = f"Mitradnya Publication Alert!\n\nStudent Name: {student_name}\nTopic: Partnership Final Accounts\nScore: {score}/50"
    msg = MIMEText(msg_content)
    msg['Subject'] = f"New Quiz Result: {student_name} scored {score}/50"
    msg['From'] = TEACHER_EMAIL
    msg['To'] = TEACHER_EMAIL

    try:
        # Gmail सर्व्हरशी कनेक्ट करणे
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(TEACHER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(TEACHER_EMAIL, TEACHER_EMAIL, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False

# -----------------------------------------------------
# Website Interface
# -----------------------------------------------------
st.title("📚 Mitradnya Publication - Online Exam")
st.subheader("Topic: Partnership Final Accounts")

student_name = st.text_input("Enter Your Full Name:")

# उदाहरणासाठी येथे पहिले २ प्रश्न दिले आहेत (अशाच प्रकारे तुम्ही ५० प्रश्न जोडू शकता)
st.markdown("---")
ans1 = st.radio("1. The Indian Partnership Act was passed in the year:", ["Select", "1923", "1932", "1956", "2013"])
ans2 = st.radio("2. Registration of a Partnership Firm is compulsory in the state of:", ["Select", "Gujarat", "Maharashtra", "Delhi", "Goa"])

if st.button("Submit Exam"):
    if student_name == "":
        st.warning("Please enter your name first!")
    else:
        score = 0
        # उत्तरे तपासणे
        if ans1 == "1932": score += 1
        if ans2 == "Maharashtra": score += 1
        # (येथे बाकीच्या प्रश्नांचे लॉजिक येईल)

        st.success(f"Exam Submitted! Your Score is {score}/50")
        
        # शिक्षकाला ईमेल पाठवणे
        email_sent = send_score_to_teacher(student_name, score)
        if email_sent:
            st.info("Your result has been emailed to Mukesh Sir.")
        else:
            st.error("Error sending email report.")
