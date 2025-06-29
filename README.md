# 🩸 Blood Test Report Analyser

A FastAPI-based application that analyzes blood test report PDFs using CrewAI agents and the Gemini 1.5 Flash model via LiteLLM. The system processes uploaded PDFs, extracts text, and provides medical analysis, nutrition recommendations, and exercise plans.

---

## 🐞 Bugs Found and Fixes

| Issue | Fix |
|------|-----|
| `llm = llm` caused `NameError` in `agents.py` | Defined `llm` using `litellm.completion` with `gemini/gemini-1.5-flash` and `GOOGLE_API_KEY` |
| Invalid import `from crewai_tools import tools` in `tools.py` | Replaced with standalone classes: `BloodTestReportTool`, `NutritionTool`, `ExerciseTool` |
| `PDFLoader` undefined in `tools.py` | Replaced with `pdfplumber` for robust PDF text extraction |
| Incorrect tool reference like `BloodTestReportTool().read_data_tool` | Updated to use `blood_test_tool.run` and instantiated tools properly |
| All tasks assigned to doctor agent in `task.py` | Reassigned: verification → verifier, nutrition_analysis → nutritionist, exercise_planning → exercise_specialist |
| Only `help_patients` task executed in `main.py` | Included all tasks in `run_crew` |
| Invalid LiteLLM model names | Standardized to `gemini/gemini-1.5-flash` |
| `NutritionTool` and `ExerciseTool` returned static strings | Implemented LLM-based analysis using Gemini |
| Async tool methods not awaited | Converted to synchronous methods and used `kickoff_async` in `main.py` |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd blood-test-analyser-debug


### 1. Create a Virtual Environment

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On Unix or MacOS
source .venv/bin/activate

#installation
pip install -r requirements.txt

#Set Environment Variables
Create a .env file

#Run the API
uvicorn main:app --reload
