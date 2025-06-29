# Blood Test Report Analyzer

A FastAPI-based application that uses CrewAI to analyze blood test reports with a humorous, non-scientific twist. The project includes multiple agents (Doctor, Verifier, Nutritionist, Exercise Specialist) that provide exaggerated medical advice, nutrition recommendations, and extreme exercise plans based on uploaded PDF reports and user queries.

## Bugs Found and Fixes

The original code contained several bugs that prevented it from running correctly. Below is a summary of the issues and how they were resolved:

1. **Undefined `llm` in `agents.py`**:
   - **Issue**: The `llm` variable was undefined, causing a `NameError`.
   - **Fix**: Imported `ChatOpenAI` from `langchain_openai` and initialized it with an API key from `.env`.

2. **Undefined `PDFLoader` in `tools.py`**:
   - **Issue**: `PDFLoader` was not imported, causing a `NameError`.
   - **Fix**: Used `PDFPlumberLoader` from `langchain_community.document_loaders` and added error handling.

3. **Unused Agents and Tasks**:
   - **Issue**: Only the `doctor` agent and `help_patients` task were used, leaving other agents and tasks as dead code.
   - **Fix**: Updated `main.py` to include all agents (`doctor`, `verifier`, `nutritionist`, `exercise_specialist`) and tasks (`verification`, `help_patients`, `nutrition_analysis`, `exercise_planning`).

4. **Incorrect Task-Agent Assignments**:
   - **Issue**: Tasks like `nutrition_analysis` were assigned to the `doctor` instead of the appropriate agent.
   - **Fix**: Assigned tasks to their respective agents and added corresponding tools (`NutritionTool`, `ExerciseTool`).

5. **Missing `requirements.txt`**:
   - **Issue**: No `requirements.txt` was provided, and `README.md` had a typo (`requirement.txt`).
   - **Fix**: Created `requirements.txt` with necessary dependencies and corrected the typo.

6. **Incorrect Import in `tools.py`**:
   - **Issue**: `from crewai_tools import tools` was invalid.
   - **Fix**: Removed the incorrect import, keeping only `SerperDevTool`.

7. **Improper Tool Signature**:
   - **Issue**: `read_data_tool` lacked the `@tool` decorator and used an async signature.
   - **Fix**: Added `@tool` decorator and made the method synchronous.

8. **Hardcoded File Path**:
   - **Issue**: `read_data_tool` used a hardcoded `data/sample.pdf` path.
   - **Fix**: Passed dynamic `file_path` from `main.py` to tasks and tools.

9. **Silent File Cleanup Errors**:
   - **Issue**: File cleanup errors were silently ignored.
   - **Fix**: Added logging for cleanup errors.

## Setup Instructions

### Prerequisites
- Python 3.10+
- A valid OpenAI API key (for LLM)
- A valid Serper API key (for search tool)

### Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd blood-test-report-analyzer
