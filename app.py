import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API Key from your .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Configure wide layout
st.set_page_config(page_title="AI Content Generation Studio")

# --- RICH PINK THEME CSS ---
girly_theme_css = """
<style>
/* Force the rich pink background over all Streamlit components */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainBlockContainer"] {
    background: #E58AA7 !important;
    background-image: linear-gradient(rgba(229, 138, 167, 0.85), rgba(229, 138, 167, 0.85)), 
                      url('https://images.unsplash.com/photo-1526047932273-341f2a7631f9?q=80&w=1000') !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
}

/* Force Text to be Bright White for visibility against the pink */
h1, h2, h3, h4, h5, h6, .stSubheader, p, span, label, [data-testid="stWidgetLabel"] p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
}

/* Sidebar Panel Styling */
section[data-testid="stSidebar"] {
    background-color: #C16A87 !important;
    border-right: 1px solid #B05B77;
}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
    color: #FFFFFF !important;
}

/* --- FORCE EVERYTHING INSIDE INPUTS/TEXTAREAS TO BE PINK --- */
div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"], 
.stTextInput>div>div, .stTextArea>div>div, .stSelectbox>div>div,
textarea, input, select, div[role="textbox"] {
    background-color: #E2829F !important; /* Pinkish shade */
    background: #E2829F !important;
    border: 2px solid #C45F7F !important; /* Darker pink border outline */
    border-radius: 25px !important; /* Pill capsule shaped */
    color: #FFFFFF !important;
}

/* REMOVE BLACK CORNERS: Force base widget blocks to have transparent or pink backgrounds */
div[data-testid="stTextArea"], div[data-testid="stTextInput"], div[data-testid="stSelectbox"] {
    background-color: transparent !important;
    background: transparent !important;
    border: none !important;
}

/* Target focused state of text areas to prevent dark corners */
textarea:focus, input:focus, div[data-baseweb="textarea"] > div:focus-within, div[data-baseweb="input"] > div:focus-within {
    background-color: #E2829F !important;
    background: #E2829F !important;
    border-color: #C45F7F !important;
    box-shadow: none !important;
}

/* Force text style inside all input types */
input, textarea, select, .stTextInput input, .stTextArea textarea {
    color: #FFFFFF !important;
    font-weight: 500 !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
}

/* Ensure placeholder text inside inputs is light pink/white */
input::placeholder, textarea::placeholder, div[data-placeholder] {
    color: rgba(255, 255, 255, 0.8) !important;
}

/* --- FIX DROPDOWN MENU OPEN STATE --- */
/* Completely clear out the black background container */
div[data-baseweb="popover"], 
ul[role="listbox"], 
ul[data-baseweb="menu"],
[data-testid="stSelectboxVirtualDropdownContainer"] div,
[data-baseweb="popover"] > div {
    background-color: #E2829F !important;
    background: #E2829F !important;
    border: 2px solid #C45F7F !important;
}

/* Style individual list items inside dropdown menu */
li[role="option"], 
[data-baseweb="popover"] li,
ul[data-baseweb="menu"] li,
div[data-baseweb="select"] + div li {
    color: #FFFFFF !important;
    background-color: #E2829F !important;
    background: #E2829F !important;
}

/* Handle hover effect on dropdown choices */
li[role="option"]:hover, 
[data-baseweb="popover"] li:hover,
ul[data-baseweb="menu"] li:hover,
div[data-baseweb="select"] + div li:hover {
    background-color: #C45F7F !important; /* Darker pink highlight */
    background: #C45F7F !important;
    color: #FFFFFF !important;
}

/* --- THE BUTTONS --- */
/* Solid pink capsule with white text */
.stButton>button, div.stButton > button, [data-testid="stBaseButton-secondary"] {
    background-color: #C45F7F !important; /* Solid pink background */
    color: #FFFFFF !important; /* White text */
    border-radius: 25px !important; /* Capsule/rounded look */
    border: 2px solid #C45F7F !important;
    font-weight: 700 !important;
    padding: 12px 30px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
    transition: all 0.2s ease-in-out !important;
}

/* Button Hover State */
.stButton>button:hover, div.stButton > button:hover {
    background-color: #E2829F !important;
    border-color: #E2829F !important;
    color: #FFFFFF !important;
    transform: scale(1.03) !important;
}

/* Navigation Tabs */
div[data-testid="stTabBar"] {
    background-color: rgba(255, 255, 255, 0.2) !important;
    padding: 6px !important;
    border-radius: 8px !important;
}
button[data-baseweb="tab"] {
    color: #FFFFFF !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #FFFFFF !important;
    color: #E58AA7 !important;
    border-radius: 6px !important;
    font-weight: bold !important;
}

/* Fix the dropdown select box and its arrow container to match the first image */
div[data-baseweb="select"] {
    border-radius: 25px !important;
}

/* Hide any inner borders or background patches around the arrow */
div[data-baseweb="select"] > div {
    background-color: transparent !important;
    border: none !important;
}

/* Ensure the arrow icon area matches perfectly */
div[data-baseweb="select"] svg {
    fill: #FFFFFF !important; /* Makes the arrow clean white */
}
</style>
"""

# Apply the theme styling
st.markdown(girly_theme_css, unsafe_allow_html=True)

# Main Headings
st.title("🌸 AI Content Generation Studio")
st.caption("InnoViast AI Internship - Week 2 Assignment")

# --- SIDEBAR CONTROLS ---
st.sidebar.markdown("## 🎀 Customization Panel")
tone = st.sidebar.selectbox("Select Writing Tone", ["Professional", "Casual & Cute", "Enthusiastic ", "Persuasive", "Informative"])
length = st.sidebar.select_slider("Target Content Length", options=["Short", "Medium", "Long"], value="Medium")
audience = st.sidebar.text_input("Target Audience", placeholder="e.g., College students, Tech recruiters")

# --- MAIN CONTENT AREA ---
st.subheader("📋 Choose Your Content Template")

prompt_payload = {}

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📝 Blog Post", "📱 Caption", "💼 LinkedIn Post", "📧 Email", "🏷️ Product Description", "📣 Ad Copy"])

with tab1:
    st.write("### 📝 Blog Post Draftsman")
    blog_title = st.text_input("Blog Post Topic")
    keywords = st.text_input("Keywords (comma-separated)")
    if st.button("Generate Blog Post", key="btn_blog"):
        prompt_payload = {"template_name": "Blog Post", "specific_inputs": f"Topic: {blog_title}. Keywords: {keywords}."}

with tab2:
    st.write("### 📱 Social Media Caption")
    platform = st.selectbox("Platform", ["Instagram", "Pinterest", "TikTok", "Facebook"])
    context = st.text_area("What is your visual post about?")
    if st.button("Generate Caption Layout", key="btn_caption"):
        prompt_payload = {"template_name": f"{platform} Caption", "specific_inputs": f"Context: {context}. Include matching emojis and hashtags."}

with tab3:
    st.write("### 💼 Professional LinkedIn Post")
    hook = st.text_input("Your Hook / Opening Statement")
    lessons = st.text_area("Core professional takeaways")
    if st.button("Generate LinkedIn Post", key="btn_linkedin"):
        prompt_payload = {"template_name": "LinkedIn Post", "specific_inputs": f"Hook: {hook}. Takeaways: {lessons}."}

with tab4:
    st.write("### 📧 Strategic Email Writer")
    purpose = st.text_input("Objective of your email")
    key_points = st.text_area("Important notes to include")
    if st.button("Draft Email", key="btn_email"):
        prompt_payload = {"template_name": "Email Template", "specific_inputs": f"Objective: {purpose}. Details: {key_points}."}

with tab5:
    st.write("### 🏷️ Product Descriptions")
    prod_name = st.text_input("Product/Service Name")
    features = st.text_area("Key highlights & features")
    if st.button("Write Product Copy", key="btn_prod"):
        prompt_payload = {"template_name": "Product Description", "specific_inputs": f"Product: {prod_name}. Features: {features}."}

with tab6:
    st.write("### 📣 Marketing Ad Variations")
    campaign = st.text_input("What are we promoting?")
    cta = st.text_input("Call to Action (e.g., Book your event now)")
    if st.button("Create Ad Copy Variations", key="btn_ad"):
        prompt_payload = {"template_name": "Ad Copy Set", "specific_inputs": f"Promotion: {campaign}. CTA: {cta}."}

# --- GENERATION LOGIC ---
if prompt_payload:
    system_instruction = (
        "You are an expert AI copywriter. Generate clean, high-quality content. "
        "Strictly respect the selected Tone, Length, and Target Audience parameters. Structure the output clearly using standard Markdown."
    )
    
    user_prompt = f"""
    Generate an elite {prompt_payload['template_name']}.
    Specific details: {prompt_payload['specific_inputs']}
    Tone: {tone}
    Length: {length}
    Audience: {audience if audience else "General audience"}
    """
    
    with st.spinner("Processing content strategy generation..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7,
                )
            )
            st.success("✨ Content Studio Generation Ready:")
            st.markdown(response.text)
            st.divider()
            st.download_button(
                label="📥 Download Output Markdown (.md)",
                data=response.text,
                file_name=f"{prompt_payload['template_name'].lower().replace(' ', '_')}_output.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"Execution Error: {e}") 