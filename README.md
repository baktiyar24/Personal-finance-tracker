# 💰 Personal Finance Tracker

A personal finance management application built with **Python and FastAPI**.

This is my first independent Python development project. It started as a simple command-line application and is gradually evolving into a fully functional REST API.

The main purpose of this project is not only to build a useful application, but also to gain practical experience in backend development, software architecture, and problem-solving.

## 👨‍💻 About Me

Hi! I'm a second-year **Information Systems student at Kazakh-British Technical University (KBTU)** in Kazakhstan.

I'm an aspiring software developer currently focusing on **Python Backend Development**, with a long-term goal of becoming a **Full-Stack Developer**.

I'm passionate about understanding how applications work behind the scenes, improving my problem-solving skills, and applying what I learn to real projects.

I'm currently exploring Python, REST APIs, FastAPI, databases, and algorithms.

I believe the best way to become a better developer is to build projects, experiment, make mistakes, and learn from them.

This repository represents one of my first steps into software development.

**My goal is to grow into a developer capable of building reliable, scalable, and meaningful applications.**

## 🚀 Features

### Finance Management
- Add income and expenses
- Calculate the current balance in KZT
- Track transaction history
- Prevent expenses that exceed the available balance
- Validate user input
- Save and load transactions using JSON

### REST API
- Retrieve the current balance
- Retrieve transaction history
- Add income through HTTP requests
- Validate incoming JSON using Pydantic
- Explore and test endpoints with Swagger UI

### Available API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/balance` | Get current balance |
| GET | `/transactions` | Get transaction history |
| POST | `/income` | Add income and save the transaction |

## 🛠️ Tech Stack

**Language**
- Python 3

**Backend**
- FastAPI
- Pydantic
- Uvicorn

**Data Storage**
- JSON (currently)
- PostgreSQL (planned)

**Development Tools**
- Git & GitHub
- Visual Studio Code
- Swagger UI

## 📂 Project Structure

```text
Personal-finance-tracker/
├── api_practice/
│   └── app.py
├── main.py
├── transactions.py
├── storage.py
├── .gitignore
└── README.md
```

The application currently separates responsibilities across different modules:

- `main.py` — command-line interface and user interaction
- `transactions.py` — business logic for income, expenses, and balance calculations
- `storage.py` — transaction storage and retrieval
- `api_practice/app.py` — FastAPI application and HTTP endpoints

Transaction data is stored locally in `transactions.json`.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/baktiyar24/Personal-finance-tracker.git
cd Personal-finance-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install "fastapi[standard]"
```

### 4. Run the console application

```bash
python main.py
```

### 5. Run the FastAPI server

```bash
python -m uvicorn api_practice.app:app --reload
```

Open the interactive API documentation:

**http://127.0.0.1:8000/docs**

## 🗺️ Development Roadmap

- [x] **v0.1** — Basic income, expense, and balance management
- [x] **v0.2** — Refactor the application into reusable functions and modules
- [x] **v0.3** — Transaction history and persistent JSON storage
- [x] **v0.4** — Introduction to FastAPI, GET endpoints, and Pydantic validation
- [x] **v0.5** — Implement `POST /income` with persistent storage
- [ ] **v0.6** — Implement `POST /expense` and HTTP error handling
- [ ] **v0.7** — PostgreSQL integration and database models
- [ ] **v0.8** — Automated testing and improved project architecture
- [ ] **v0.9** — User authentication and authorization
- [ ] **v1.0** — Docker, deployment, and production-ready improvements
- [ ] **Future** — Build a frontend and evolve the project into a full-stack application

## 📚 What I'm Learning

Through this project, I'm developing my understanding of:

- Python programming and modular application design
- Business logic and input validation
- HTTP methods, requests, responses, and status codes
- REST API development with FastAPI
- Data validation with Pydantic
- File handling and JSON serialization
- Git and version control
- Debugging and problem-solving

Each new feature is an opportunity to understand not just **how to write code**, but also **why it works**.

## 📌 Project Status

**Under active development — learning project.**

The current version provides a working command-line finance tracker and an early FastAPI backend.

The project is being developed incrementally as I continue learning Python backend engineering.

Future updates will focus on expense management through the API, database integration, testing, authentication, and deployment.

---

*Built with curiosity, consistency, and a willingness to keep learning.* 🚀