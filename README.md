# Project: LangChain Ollama Chat Example

Simple demonstration of streaming a chat response using `ChatOllama` and a `ChatPromptTemplate`.

## Requirements

- Python 3.10+ (recommended 3.11+)
- Windows (development tested)
- `pip`

Recommended packages (example):
- `langchain-ollama`
- `langchain-core`

Place required packages in `requirements.txt` or install directly.

## Installation

1. Create and activate a virtual environment (Windows):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
## Run
   ```bash
      python main.py
   ```
  
# Activate virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1

# Simple freeze: write all installed packages to `requirements.txt`
pip freeze > `requirements.txt`

# Freeze only packages installed in the active environment (exclude global)
pip freeze --local > `requirements.txt`

# (Alternative) Use pip-tools for a deterministic file:
pip install pip-tools
# create `requirements.in` with top-level deps, then:
pip-compile --output-file=`requirements.txt` `requirements.in`