# 🚀 AI Workspace Pro

> A Production-Ready Multi-Agent AI Workspace powered by OpenRouter, MCP (Model Context Protocol), and Streamlit.

AI Workspace Pro is an intelligent multi-agent platform that routes user requests to specialized AI agents capable of code review, research, GitHub exploration, resume analysis, and filesystem interaction through MCP servers.

Built with a modular architecture, the application demonstrates modern AI engineering practices including agent orchestration, tool calling, memory management, latency optimization, and cloud deployment.

---

## ✨ Features

### 🤖 Multi-Agent Architecture

- General Assistant
- Code Reviewer
- Research Expert
- Resume Expert
- GitHub Expert
- Document Expert (Foundation Ready)

---

### 🧠 OpenRouter Integration

- Supports multiple LLMs
- Configurable model selection
- Tool Calling support
- Async API requests
- Optimized response latency

---

### 🔧 Model Context Protocol (MCP)

Integrated MCP Servers

- 📂 Filesystem Server
- 🐙 GitHub Server

Capabilities

- Read project files
- Explore repositories
- Execute MCP tools
- Dynamic tool loading

---

### 🧩 Intelligent Routing

Automatically routes user queries to the most suitable AI agent.

Examples

- Resume Review → Resume Expert
- GitHub Questions → GitHub Expert
- Research Tasks → Research Expert
- Programming → Code Reviewer

---

### 💬 Conversation Memory

- Per-agent memory
- Session-aware conversations
- Memory optimization
- Automatic history trimming

---

### ⚡ Performance Optimizations

- Persistent MCP connections
- Reduced token usage
- Token Manager
- Memory Manager
- Lower response latency
- Optimized OpenRouter requests

---

### 📊 Activity Timeline

Visual timeline displaying

- Selected Agent
- Connected MCP Servers
- Provider Used
- Tool Execution
- Response Generation

---

### 🛠 Tool Execution History

Displays

- Executed Tools
- Arguments
- Tool Results

Useful for debugging and transparency.

---

### 🎨 Modern Streamlit UI

- Responsive layout
- Sidebar controls
- Chat interface
- Activity timeline
- Tool history
- Dashboard metrics

---

## 🏗 Architecture

```
User
        │
        ▼
 Streamlit UI
        │
        ▼
 Agent Manager
        │
        ▼
 Keyword Router
        │
        ▼
 Selected Agent
        │
        ▼
 OpenRouter Provider
        │
        ▼
 MCP Tool Executor
        │
        ▼
 GitHub / Filesystem
```

---

## 📂 Project Structure

```
multi_mcp_agent_router_pro/

│
├── agents/
│ ├── base.py
│ ├── researcher.py
│ ├── code_reviewer.py
│ ├── resume_expert.py
│ └── registry.py
│
├── core/
│ ├── agent_manager.py
│ ├── context.py
│ └── models.py
│
├── providers/
│ ├── base.py
│ ├── factory.py
│ └── openrouter.py
│
├── routers/
│ └── keyword_router.py
│
├── services/
│ ├── activity_tracker.py
│ ├── logger.py
│ ├── mcp_manager.py
│ ├── memory.py
│ ├── token_manager.py
│ ├── tool_executor.py
│ └── url_reader.py
│
├── ui/
│ ├── sidebar.py
│ ├── chat.py
│ ├── activity.py
│ ├── tool_history.py
│ └── styles.py
│
├── app.py
├── Dockerfile
├── railway.json
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python 3.12+

### AI

- OpenRouter API
- DeepSeek Chat V3
- Qwen (Supported)

### Agent Framework

- Custom Multi-Agent Router

### Protocol

- Model Context Protocol (MCP)

### Tools

- GitHub MCP
- Filesystem MCP

### Deployment

- Railway
- Docker

### Utilities

- Requests
- BeautifulSoup
- Pydantic
- AsyncIO

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/abhiguthikonda/Multi-MCP-Agent-Router.git

cd Multi-MCP-Agent-Router
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment

Create

```
.env
```

Example

```env
OPENROUTER_API_KEY=your_api_key

GITHUB_TOKEN=your_token
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 🐳 Docker

Build

```bash
docker build -t ai-workspace-pro .
```

Run

```bash
docker run -p 8501:8501 ai-workspace-pro
```

---

## 🚀 Railway Deployment

This project supports one-click Railway deployment.

Required Environment Variables

```
OPENROUTER_API_KEY

GITHUB_TOKEN
```

---

## 📈 Performance Improvements

Implemented

- Persistent MCP Sessions
- Token Manager
- Memory Manager
- Conversation History Limiting
- Optimized OpenRouter Calls
- Reduced Token Consumption

---

## 🔮 Roadmap

### Version 1.1

- Drag & Drop Upload
- PDF Analysis
- DOCX Analysis
- CSV Analysis
- Workspace Manager
- Website Reader
- Image Understanding

---

### Version 1.2

- Streaming Responses
- Authentication
- Cloud Storage
- Database Integration
- Vector Search
- Advanced Context Builder

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Abhi Guthikonda**

Computer Science Engineering Student

AI • Backend • Cloud • Multi-Agent Systems

GitHub

https://github.com/abhiguthikonda