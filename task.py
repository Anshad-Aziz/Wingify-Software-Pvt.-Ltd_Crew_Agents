from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import blood_test_tool, nutrition_tool, exercise_tool, search_tool

# Verification Task
verification = Task(
    description="Verify that the uploaded file at {file_path} is a valid blood test report. If not, indicate potential issues.",
    expected_output="A confirmation that the file is a valid blood test report or a description of any issues.",
    agent=verifier,
    tools=[blood_test_tool],
    async_execution=False
)

# Main Analysis Task
help_patients = Task(
    description="Analyze the blood test report at {file_path} and respond to the user's query: {query}. Provide a detailed summary with medical insights.",
    expected_output="A detailed analysis of the blood test report, addressing the user's query with medical insights and recommendations.",
    agent=doctor,
    tools=[blood_test_tool, search_tool],
    async_execution=False
)

# Nutrition Analysis Task
nutrition_analysis = Task(
    description="Analyze the blood test report at {file_path} and provide personalized nutrition recommendations based on the data.",
    expected_output="Personalized nutrition recommendations including foods and supplements, based on blood test data.",
    agent=nutritionist,
    tools=[nutrition_tool, search_tool],
    async_execution=False
)

# Exercise Planning Task
exercise_planning = Task(
    description="Create a safe and effective exercise plan based on the blood test report at {file_path}, considering the user's health status.",
    expected_output="A tailored exercise plan with specific activities and precautions based on blood test data.",
    agent=exercise_specialist,
    tools=[exercise_tool, search_tool],
    async_execution=False
)