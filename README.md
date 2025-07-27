# TRacer: UDS CAN Trace Analyzer

TRacer is an offline diagnostic CAN trace analyzer tool built with Streamlit and powered by a local LLM (Mistral 7B Instruct via Ollama). It explains .asc and .txt UDS CAN traces with color-coded diagnostic services, and PDF export support.

---

## 📌 Prerequisites

Before using TRacer, make sure your system meets the following requirements:

### 1. Python Environment
- Python 3.10 or later
- pip package manager

### 2. Ollama (Required to run the Mistral LLM locally)

#### 🔧 Steps to Install Ollama:

##### Windows:
- Install via Winget:
  winget install Ollama.Ollama
- Or download the installer from: https://ollama.com

##### Linux/macOS:
  curl -fsSL https://ollama.com/install.sh | sh

### 3. Pull the Mistral 7B Model
  ollama pull mistral:7b-instruct

Ensure Ollama is running before starting the tool:
  ollama serve

---

## 🛠 Folder Structure

\TRacer\
├── venv\                  # Python virtual environment
├── scripts\
│   ├── app.py             # Main Streamlit app
│   ├── utils.py           # Helper functions (PDF, etc.)
│   └── install.bat        # First-time setup script
├── TRacer.bat             # Launches the tool (activates venv + runs app)
├── req.txt                # Python dependencies

---

## 🚀 First-Time Setup

### 1. Clone or Download TRacer

Place the project in:
TRacer\

### 2. Install Dependencies

Run the following from the scripts/ folder:
  install.bat

This script will:
- Create a virtual environment (venv)
- Install all required Python libraries from req.txt

---

## ✅ How to Use

### 1. Launch the Tool

From the root folder (TRacer\), run:
  TRacer.bat

This will:
- Activate the virtual environment
- Launch the Streamlit app in your default browser

### 2. Upload a Trace File

Supported formats:
- .asc
- .txt

### 3. Analyze Trace

- Click "Start Analyzing"
- The tool will process the trace and use Mistral 7B to provide service-level breakdowns and explanations

### 4. Export as PDF

- After processing, click "Export to PDF"
- Choose filename and destination to save the output

---

## 💡 Notes

- Ollama must be running before launching TRacer.
- Works entirely offline once the model is downloaded.
- Processing time depends on trace length and system performance.

---

## 📞 Support

For issues, bugs, or suggestions, please open an issue on the project repository or contact the developer directly.
