# 📧 Gmail AI Cleaner

A Gmail automation tool built with Python, Gmail API, and Streamlit.

Automatically classifies emails into:

* 🚫 Spam
* 📰 Newsletter
* ✅ Important

and applies Gmail labels automatically.

---

## 🚀 Features

### 📬 Gmail Integration

* Gmail API integration
* OAuth2 authentication
* Secure access to personal Gmail account

### 🏷 Auto Labeling

Automatically creates and manages:

* AI-Spam
* AI-Newsletter
* AI-Important

### 🧠 Email Classification

Rule-based classification engine:

* Spam detection
* Newsletter detection
* Important email detection

### 🌐 Streamlit Dashboard

Interactive web dashboard:

* Scan Gmail mailbox
* View classification results
* Search emails
* Filter by category
* Email statistics
* Pie chart visualization

---

## 📸 Dashboard

> Create a folder named `screenshots` and save your dashboard screenshot as:

```text
screenshots/dashboard.png
```

Then uncomment the line below:

```markdown
![Dashboard](screenshots/dashboard.png)
```

<!--
![Dashboard](screenshots/dashboard.png)
-->

---

## 🛠 Tech Stack

* Python
* Gmail API
* Google OAuth2
* Streamlit
* Pandas
* Plotly

---

## 📂 Project Structure

```text
gmail-ai-cleaner/

├── app.py
├── gmail_cleaner.py
├── spam_rules.py
├── label_helper.py
├── requirements.txt
├── README.md
└── screenshots/
    └── dashboard.png
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/chunchiech/gmail-ai-cleaner.git

cd gmail-ai-cleaner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Gmail API Setup

1. Create a Google Cloud Project
2. Enable Gmail API
3. Create OAuth Desktop Application
4. Download `credentials.json`
5. Place `credentials.json` in the project root directory

Example:

```text
gmail-ai-cleaner/
├── credentials.json
├── app.py
└── ...
```

---

## ▶️ Run Application

Launch Streamlit dashboard:

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## 📊 Example Output

```text
Spam: 2
Newsletter: 2
Important: 16
```

Labels created automatically:

```text
AI-Spam
AI-Newsletter
AI-Important
```

---

## 🔒 Security

The following files should NEVER be committed:

```text
credentials.json
token.json
.env
```

Example `.gitignore`:

```gitignore
credentials.json
token.json
.env
venv/
__pycache__/
```

---

## 🗺 Roadmap

### Version 1.0

* [x] Gmail API Integration
* [x] OAuth Authentication
* [x] Email Classification
* [x] Gmail Labels
* [x] Streamlit Dashboard

### Version 2.0

* [ ] One-click Spam Cleanup
* [ ] Newsletter Archive
* [ ] Processed Email Tracking
* [ ] Advanced Rules Engine

### Version 3.0

* [ ] AI Classification
* [ ] Email Summarization
* [ ] Daily Digest Report

### Version 4.0

* [ ] Docker Deployment
* [ ] GitHub Actions Automation
* [ ] Streamlit Cloud Deployment
* [ ] Multi-Account Support

---

## 🤝 Contributing

Pull requests and suggestions are welcome.

Feel free to open issues for feature requests or bug reports.

---

## 📄 License

MIT License

---

Built with ❤️ using Python, Gmail API, and Streamlit.

