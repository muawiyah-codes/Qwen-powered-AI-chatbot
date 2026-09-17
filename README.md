# 🤖 Qwen Multi-Mode AI Chatbot

An interactive AI chatbot built with **Streamlit, LangChain, Groq, and Qwen**.
The chatbot provides real-time streaming responses, maintains conversation history, and allows users to interact with AI in four different personality modes.

## ✨ Features

* 🤖 **Qwen LLM** powered chatbot
* ⚡ Fast inference using **Groq**
* 💬 Real-time **streaming responses**
* 🧠 Maintains **conversation history** during the session
* 🎭 Four different AI personality modes:

  * 😠 Angry
  * 😂 Funny
  * 😢 Sad
  * 🙂 Friendly
* 🎨 Modern dark-themed UI with custom CSS
* 🌈 Dynamic gradients based on the selected personality
* 🔄 Automatically resets conversation when personality mode changes
* 🔐 Secure API key management using environment variables
* 🚀 Interactive web interface powered by **Streamlit**

---

## 🛠️ Tech Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| Python        | Core programming language              |
| Streamlit     | Web application interface              |
| LangChain     | LLM integration and message management |
| Groq          | Fast LLM inference                     |
| Qwen          | Large Language Model                   |
| python-dotenv | Environment variable management        |
| HTML/CSS      | Custom chatbot interface               |

---

## 🧠 How It Works

The application uses different **system prompts** to control the personality of the chatbot.

When a user selects a mode, the corresponding system prompt is sent to the Qwen model.

```text
User selects personality
        ↓
System Prompt Generated
        ↓
User enters message
        ↓
Conversation History
        ↓
LangChain
        ↓
Groq API
        ↓
Qwen Model
        ↓
Streaming Response
        ↓
Streamlit Chat Interface
```

The complete conversation history is stored using `st.session_state` and sent to the model with every new message, allowing the chatbot to maintain context during the conversation.

---

## 📂 Project Structure

```text
Qwen-Multi-Mode-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> **Important:** Never upload your `.env` file or API key to GitHub.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Qwen-Multi-Mode-AI-Chatbot.git
```

Move into the project directory:

```bash
cd Qwen-Multi-Mode-AI-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit langchain langchain-groq python-dotenv
```

Or, if `requirements.txt` is included:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The API key will automatically be loaded using `python-dotenv`.

### Add `.env` to `.gitignore`

```gitignore
.env
.venv/
__pycache__/
```

This prevents sensitive credentials from being uploaded to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open it in your browser and start chatting.

---

## 🎭 Available AI Modes

### 😠 Angry

Responds with an angry personality while still answering the user's questions.

### 😂 Funny

Provides helpful responses with a humorous and entertaining personality.

### 😢 Sad

Responds in a sad emotional style while continuing to provide useful information.

### 🙂 Friendly

Provides warm, friendly, and helpful responses for general conversations.

Switching between modes automatically starts a fresh conversation with the selected personality.

---

## 💬 Conversation Memory

The application maintains chat history using:

```python
st.session_state.messages
```

Messages are represented using LangChain's:

```python
SystemMessage
HumanMessage
AIMessage
```

The complete conversation is passed back to the model whenever a new message is submitted.

This enables contextual conversations such as:

```text
User: My name is Alex.

AI: Nice to meet you, Alex!

User: What is my name?

AI: Your name is Alex.
```

---

## ⚡ Response Streaming

Instead of waiting for the complete response, the chatbot uses:

```python
model.stream()
```

This allows the AI response to appear progressively in the interface, creating a more natural chatbot experience.

---

## 🎨 User Interface

The interface includes:

* Dark cinematic background
* Gradient chatbot bubbles
* Dynamic personality colors
* Custom avatars
* Responsive chat layout
* Google Fonts
* Animated streaming cursor
* Personality selector

Each personality mode has its own gradient color theme.

---

## 🚀 Future Improvements

Future versions of this project could include:

* 💾 Persistent chat history using a database
* 👤 User authentication
* 🗂️ Multiple chat sessions
* 📝 Rename and delete conversations
* 📄 PDF/document-based chatting
* 🔍 RAG integration
* 🎙️ Voice input
* 🔊 Text-to-speech responses
* 🖼️ Image input support
* 🌐 Deployment for public access

---

## 🔒 Security

API keys should never be hard-coded directly inside the Python source code.

Always store sensitive credentials inside `.env`:

```env
GROQ_API_KEY=your_api_key
```

and ensure `.env` is included in `.gitignore`.

---

## 👨‍💻 Author

**Muawiyah**

Data Science & AI Enthusiast

Interested in:

`Python` • `Machine Learning` • `Deep Learning` • `Generative AI` • `LangChain` • `LLMs`

---

## ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star**.

Contributions, suggestions, and feedback are welcome!

---

### Made with ❤️ using Streamlit, LangChain, Groq & Qwen
