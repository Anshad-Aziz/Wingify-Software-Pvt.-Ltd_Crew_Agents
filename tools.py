import os
import logging
import pdfplumber
from dotenv import load_dotenv
from litellm import completion
from crewai_tools import SerperDevTool

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# Search Tool
search_tool = SerperDevTool()

# Blood Test Report Tool
class BloodTestReportTool:
    name = "BloodTestReportTool"
    description = "Extracts text from a blood test report PDF and analyzes it with an LLM."

    def run(self, path: str, query: str = "Summarize the blood test report"):
        try:
            logger.debug(f"Processing file: {path}, query: {query}")
            # Extract text from PDF
            with pdfplumber.open(path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
            logger.debug(f"Extracted text: {text[:100]}...")
            # Call LLM
            prompt = f"{query}: {text}"
            response = completion(
                model="gemini/gemini-1.5-flash",
                messages=[{"role": "user", "content": prompt}],
                api_key=os.getenv("GOOGLE_API_KEY")
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error in BloodTestReportTool: {str(e)}")
            return f"Error in BloodTestReportTool: {str(e)}"

# Nutrition Tool
class NutritionTool:
    name = "NutritionTool"
    description = "Analyzes blood test data and provides nutrition recommendations."

    def run(self, blood_report_data: str):
        try:
            logger.debug(f"Analyzing nutrition for data: {blood_report_data[:100]}...")
            prompt = (
                f"Based on the following blood test data, provide personalized nutrition recommendations "
                f"including specific foods and supplements. Focus on any abnormal values and their dietary implications:\n{blood_report_data}"
            )
            response = completion(
                model="gemini/gemini-1.5-flash",
                messages=[{"role": "user", "content": prompt}],
                api_key=os.getenv("GOOGLE_API_KEY")
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error in NutritionTool: {str(e)}")
            return f"Error in NutritionTool: {str(e)}"

# Exercise Tool
class ExerciseTool:
    name = "ExerciseTool"
    description = "Creates an exercise plan based on blood test data."

    def run(self, blood_report_data: str):
        try:
            logger.debug(f"Creating exercise plan for data: {blood_report_data[:100]}...")
            prompt = (
                f"Based on the following blood test data, create a safe and effective exercise plan "
                f"tailored to the user's health status. Consider any abnormal values:\n{blood_report_data}"
            )
            response = completion(
                model="gemini/gemini-1.5-flash",
                messages=[{"role": "user", "content": prompt}],
                api_key=os.getenv("GOOGLE_API_KEY")
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error in ExerciseTool: {str(e)}")
            return f"Error in ExerciseTool: {str(e)}"

# Instantiate tools
blood_test_tool = BloodTestReportTool()
nutrition_tool = NutritionTool()
exercise_tool = ExerciseTool()