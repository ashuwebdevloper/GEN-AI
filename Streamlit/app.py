import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Ashish Kumar Tiwari | Portfolio",
    page_icon="🎓",
    layout="wide"
)

# 2. Custom CSS styling for a sharp layout
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .section-header {
        color: #1E3A8A;
        border-bottom: 2px solid #DBEAFE;
        padding-bottom: 0.3rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .project-card {
        background-color: #F8FAFC;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #3B82F6;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Layout (Contact & Links)
with st.sidebar:
    st.markdown("## 🌐 Professional Profiles")
    st.markdown("[💻 GitHub (ashuwebdevloper)](https://github.com/ashuwebdevloper)")
    st.markdown("[🚀 Google Developer Profile](https://g.dev/Ashish_Kumar_Tiwari)")
    st.markdown("[☁️ Google Cloud Skill Boost](https://www.cloudskillsboost.google)")
    
    st.markdown("---")
    st.markdown("## 💼 Work Experience")
    st.markdown("**Summer Intern**\n\n*BHEL Varanasi*")
    st.markdown("**Part-time Intern**\n\n*Nextute (3 Months)*")

# 4. Main Header Section
st.markdown('<p class="main-title">Ashish Kumar Tiwari</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Computer Science, Data Analytics & Electrical Engineering Student</p>', unsafe_allow_html=True)

# 5. Education Section
st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Indian Institute of Technology Patna (IITP)")
    st.markdown("**Bachelor of Science (Hons.) in Computer Science and Data Analytics (CSDA)**")

with col2:
    st.markdown("#### Schooling")
    st.markdown("* **Class 12:** B.P.S School Naubatpur, Chandauli")
    st.markdown("* **Class 10:** St. John’s School Katsila, Chandauli")

# 6. Technical Skills Section
st.markdown('<h2 class="section-header">🛠️ Technical Skills & Concepts</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("#### 💻 Languages & Frameworks")
    st.markdown("- **Languages:** Python, C, C++")
    st.markdown("- **ML/Data Science:** NumPy, Pandas, Scikit-learn, Matplotlib")
    st.markdown("- **Web Dev:** MERN Stack (MongoDB, Express, React, Node.js)")

with c2:
    st.markdown("#### 🔧 Tools & Tech")
    st.markdown("- SQL, MongoDB, Git")
    st.markdown("- Matlab, Simulink, PSPice, TinkerCad")
    st.markdown("- Docker, Vercel, Jupyter, VS Code, Google Colab")

with c3:
    st.markdown("#### 🧠 Core Concepts")
    st.markdown("- Machine Learning, Basic DSA, DBMS")
    st.markdown("- Computer Networks, Probability & Statistics, Linear Algebra")
    st.markdown("- Signals & Systems, Network Theorems")

# 7. Projects Section
st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)

# Project 1
st.markdown("""
<div class="project-card">
    <h4>🛒 E-Commerce Platform (ShopX) | <span style="color:#3B82F6;">MERN Stack, Git</span></h4>
    <p><strong>Timeline:</strong> June - July 2024</p>
    <ul>
        <li>Developed a fully functional cross-platform web application deployed via Vercel to connect nationwide manufacturers with local shopkeepers.</li>
        <li>Incorporated 3 distinct security-based login roles: Admin, User, and Seller.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Project 2
st.markdown("""
<div class="project-card">
    <h4>🛣️ Data-Driven Road Safety Platform | <span style="color:#3B82F6;">MERN Stack, ML, SQL, Drawio</span></h4>
    <p>Developed for public and government stakeholders to identify safety metrics. Includes a scalable financial planning interface built using interactive tech architecture.</p>
</div>
""", unsafe_allow_html=True)

# Project 3 (Electrical)
with st.expander("⚡ Engineering & Minor Hardware Projects (BIET Jhansi)"):
    st.write("Leveraged Matlab, Simulink, PSPice, and TinkerCad to implement:")
    st.markdown("- **Automatic Plant Watering System**")
    st.markdown("- **Digital Voltmeter Architecture**")
    st.markdown("- **Sun Ray Solar Detector**")
    st.markdown("- **200 W Solar Photovoltaic (PV) Module Analysis**")

# 8. Achievements & Extras
st.markdown('<h2 class="section-header">🏆 Achievements & Leadership</h2>', unsafe_allow_html=True)
col_a, col_b = st.columns(2)

with col_a:
    st.metric(label="JEE Rank (Percentile)", value="96K", delta="89.9 %tile")
    st.markdown("**Campus Ambassador:** Elixir, IIT Patna")

with col_b:
    st.markdown("🏆 **Semi-finalist:** Road Safety Hackathon organized by NHAI & HOIA (Certified)")
    st.markdown("🥇 **Gold & Silver Medals:** College events (Treasure Hunt & Espresso Ideas)")
    st.markdown("♟️ **Non-Technical:** Problem-Solving, Leadership, Teamwork, Communication, Chess")