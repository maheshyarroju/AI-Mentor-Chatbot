# 🤖 AI Mentor – Domain-Specific AI Learning Assistant

AI Mentor is an AI-powered intelligent tutoring system designed to provide **focused, module-specific learning guidance** using Generative AI.

Unlike general-purpose chatbots, MentorAI ensures that responses are **strictly restricted to the selected domain**, improving accuracy, reducing hallucinations, and enhancing learning efficiency.

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