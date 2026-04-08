import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


from langchain_core.prompts import PromptTemplate

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Background */
body {
    background-color: #black ;
}

/* Title */
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #00F5FF;
    text-align: center;
}

/* Subtitle */
.sub-text {
    text-align: center;
    color: #AAAAAA;
    font-size: 18px;
}

/* Card style */
.card {
    background-color: #blue;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,255,255,0.2);
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    background-color: #00F5FF;
    color: black;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-weight: bold;
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD ENV ----------------
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Chatbot Mentor", page_icon="🤖")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "module" not in st.session_state:
    st.session_state.module = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- MODULES ----------------
MODULES = [
    "Python",
    "SQL",
    "Power BI",
    "EDA",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
    "Agentic AI"
]

REJECTION_MSG = (
    "Sorry, I don’t know about this question. "
    "Please ask something related to the selected module."
)

# ===================== HOME PAGE =====================
if st.session_state.page == "home":

    st.markdown('<div class="main-title">🤖 AI Mentor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Your Personal AI Learning Mentor powered by GenAI</div>', unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="card">
        📚 <b>What You Get:</b><br><br>
        ✔ Module-based learning<br>
        ✔ Domain-restricted answers<br>
        ✔ Smart AI explanations<br>
        ✔ Chat history download<br>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        🚀 <b>Technologies Used:</b><br><br>
        ✔ LangChain<br>
        ✔ Google Gemini LLMs<br>
        ✔ Streamlit UI<br>
        ✔ Prompt Engineering<br>
        </div>
        """, unsafe_allow_html=True)

    st.write("### 📌 Select Your Learning Module")

    selected_module = st.selectbox("Choose Module", [""] + MODULES)

    if selected_module and st.button("🚀 Start Learning"):
        st.session_state.module = selected_module
        st.session_state.page = "chat"
        st.session_state.chat = []
        st.rerun()

# ===================== CHAT PAGE =====================
if st.session_state.page == "chat":

    st.title(f"🎯 {st.session_state.module} AI Mentor")
    st.write(f"I am your dedicated mentor for **{st.session_state.module}**.")
    st.write("How can I help you today?")

    # ---------------- LLM ----------------
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )


    # ---------------- PROMPT ----------------
    prompt_template = PromptTemplate(
        input_variables=["question"],
        template=f"""
    You are a STRICT mentor for {st.session_state.module}.

    RULES:
    1. Answer ONLY if the question is DIRECTLY about {st.session_state.module}.
    2. Do NOT answer related, advanced, or subfields unless explicitly part of {st.session_state.module}.
    3. If the question is even slightly outside the module, reply EXACTLY:
    "{REJECTION_MSG}"

    Examples:
    - Allowed: Basic concepts of {st.session_state.module}
    - NOT Allowed: Deep Learning, Generative AI, Agentic AI, LLMs (unless module is those)

    Question: {{question}}
    """
    )

    # ---------------- SHOW CHAT HISTORY ----------------
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ---------------- CHAT INPUT (MUST BE TOP LEVEL) ----------------
    user_input = st.chat_input("Ask your question...")

    if user_input:
        # store user message
        st.session_state.chat.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        # format prompt
        formatted_prompt = prompt_template.format(question=user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = llm.invoke(formatted_prompt)
                st.markdown(response.content)

        st.session_state.chat.append(
            {"role": "assistant", "content": response.content}
        )

    # ---------------- DOWNLOAD CHAT ----------------
    if st.session_state.chat:
        chat_text = ""
        for msg in st.session_state.chat:
            role = "User" if msg["role"] == "user" else "AI"
            chat_text += f"{role}: {msg['content']}\n\n"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        st.download_button(
            label="📥 Download Chat History",
            data=chat_text,
            file_name=f"AI_Chatbot_Mentor_{timestamp}.txt",
            mime="text/plain"
        )

    # ---------------- BACK BUTTON ----------------
    if st.button("⬅ Back to Modules"):
        st.session_state.page = "home"
        st.session_state.chat = []
        st.rerun()