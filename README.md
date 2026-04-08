# 🤖 AI Mentor – Domain-Specific AI Learning Assistant

AI Mentor is an AI-powered intelligent tutoring system designed to provide **focused, module-specific learning guidance** using Generative AI.

Unlike general-purpose chatbots, MentorAI ensures that responses are **strictly restricted to the selected domain**, improving accuracy, reducing hallucinations, and enhancing learning efficiency.

## 🌐 Live Demo

Experience the application live:

👉 https://ai-mentor-chatbot-agq9fd4oards7jvb7nyykc.streamlit.app/


## 🎥 Video Demo

Watch the full walkthrough of the project:

👉 https://drive.google.com/file/d/19fVjb3Wo3X89zKbg3oY20o53Z_8edFvm/view?usp=sharing

---

## 🚀 Key Features

- 🎯 Module-specific AI mentoring
- 🧠 Domain-restricted responses (No irrelevant answers)
- 💬 Interactive chat interface (ChatGPT-like)
- 📥 Download complete chat history
- ⚡ Fast and lightweight Streamlit UI
- 🔐 Secure API integration using environment variables

---

## 📚 Supported Modules

- Python  
- SQL  
- Power BI  
- Exploratory Data Analysis (EDA)  
- Machine Learning  
- Deep Learning  
- Generative AI  
- Agentic AI  

---

## 🧠 How It Works

1. User selects a learning module  
2. A dedicated AI mentor is assigned  
3. AI answers only domain-related queries  
4. Irrelevant questions are rejected with a fixed response  
5. Chat history is stored and downloadable  

---

## 🏗️ System Architecture

### Frontend
- Streamlit UI
- Interactive chat interface
- Sidebar controls

### Backend
- LangChain for orchestration
- Prompt templates for domain restriction
- Google Gemini LLM

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| UI | Streamlit |
| LLM Framework | LangChain |
| Model | Google gemini llm |
| Environment | python-dotenv |
| Language | Python |

---

## 🔐 Environment Setup

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_api_key

## 📂 Project Structure
```
AI-Chatbot-Mentor/ │ 
├── app.py 
├── .env 
├── requirements.txt 
├── README.md
```

## ▶️ Run Locally

- git clone https://github.com/your-username/MentorAI.git
- cd MentorAI
- pip install -r requirements.txt
- streamlit run app.py

## 📥 Chat Export Feature

Users can download the entire conversation:

- Includes both user & AI responses
- Stored in .txt format
- Useful for revision, notes, and documentation


## 🎯 Use Cases
- Self-learning and revision
- Interview preparation
- Concept clarification
- Guided AI-assisted learning

## 💡 Unique Value

MentorAI solves a key problem in GenAI systems:

- ❌ Generic Chatbots → Irrelevant Answers
- ✅ MentorAI → Controlled, Domain-Specific Responses

This makes it more reliable for education and structured learning.

## ⭐ Future Enhancements

- RAG-based knowledge integration
- Voice-based interaction
- Multi-language support
- Progress tracking dashboard