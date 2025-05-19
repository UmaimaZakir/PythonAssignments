
import streamlit as st

# Page Setup
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title
st.markdown("<h2 style='text-align:center; color:purple;'>🔐 Password Strength Checker</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Check how strong your password is and get tips to improve it!</p>", unsafe_allow_html=True)
st.write("---")

# Guidelines
with st.expander("📘 Password Tips (Click to expand)"):
    st.markdown("""
    A strong password should:
    - ✅ Be at least **8 characters**
    - ✅ Have both **uppercase and lowercase letters**
    - ✅ Include at least one **digit (0-9)**
    - ✅ Contain a **special character** like `!@#$%`
    """)

# Input field
password = st.text_input("🔑 Enter your password", type="password", help="We don't store your password.")

# Function to evaluate password
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Must be at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("🔸 Add at least one uppercase letter (A-Z).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("🔸 Add at least one lowercase letter (a-z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("🔸 Include at least one digit (0-9).")

    if any(c in "!@#$%^&*()_+-=~[]{}|:;<>?,./" for c in password):
        score += 1
    else:
        feedback.append("🔸 Add a special character (!@#$...).")

    return score, feedback

# Show results
if password:
    score, feedback = check_password_strength(password)

    st.markdown("### 🔎 Password Strength Analysis")

    strength_level = {
        5: ("✅ Very Strong", "green"),
        4: ("🟢 Strong", "lightgreen"),
        3: ("🟡 Moderate", "orange"),
        2: ("🔴 Weak", "red"),
        1: ("❌ Very Weak", "darkred"),
        0: ("❌ Extremely Weak", "maroon")
    }

    label, color = strength_level.get(score, ("Unknown", "gray"))

    st.markdown(
        f"""
        <div style='background-color:{color}; padding:12px; border-radius:10px; color:white; text-align:center; font-weight:bold;'>
            {label}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(score / 5)

    if feedback:
        st.markdown("#### 🛠️ Suggestions to Improve:")
        for f in feedback:
            st.write(f)
    else:
        st.success("🎉 Your password meets all the strong criteria!")

