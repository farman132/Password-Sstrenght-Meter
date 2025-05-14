import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Checker")
st.write("Check how strong your password is and get tips to improve it.")

password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Your password must be at least 8 characters long.")

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase (A-Z) and lowercase (a-z) letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("🔴 Include at least one number (0-9).")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%^&*).")

    if score == 4:
        strength = "🟢 Strong"
        feedback.append("✅ Great! Your password is strong and secure.")
    elif score == 3:
        strength = "🟡 Moderate"
        feedback.append("⚠️ Your password is moderate. Try adding missing elements.")
    else:
        strength = "🔴 Weak"
        feedback.append("❌ Your password is weak. Please improve it using the above suggestions.")

    return strength, feedback

if password:
    strength, feedback = check_password_strength(password)
    st.markdown(f"### Password Strength: {strength}")
    st.markdown("### 💡 Feedback:")
    for point in feedback:
        st.write(point)
else:
    st.info("🟡 Please enter your password to get started.")


