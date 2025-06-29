zimport os
from dotenv import load_dotenv
from crewai import Agent
from litellm import completion
from tools import search_tool, blood_test_tool, nutrition_tool, exercise_tool

load_dotenv()

# Initialize LLM with Gemini 1.5 Flash
def get_llm():
    return lambda messages: completion(
        model="gemini/gemini-1.5-flash",
        messages=messages,
        api_key=os.getenv("GOOGLE_API_KEY")
    )

# Doctor Agent
doctor = Agent(
    role="Senior Experienced Doctor",
    goal="Provide medical advice based on blood test reports and user queries",
    verbose=True,
    memory=True,
    backstory=(
        "You're a highly experienced doctor with a flair for diagnosing conditions."
        "You analyze blood test reports thoroughly and provide clear, evidence-based advice."
        "You avoid unnecessary speculation and focus on actionable recommendations."
    ),
    tools=[blood_test_tool, search_tool],
    llm=get_llm(),
    max_iter=5,
    max_rpm=100,
    allow_delegation=True
)

# Verifier Agent
verifier = Agent(
    role="Blood Report Verifier",
    goal="Verify that the uploaded file is a valid blood test report",
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in validating medical documents."
        "You carefully check if the uploaded file is a blood test report before analysis."
        "You ensure data integrity and flag invalid inputs."
    ),
    tools=[blood_test_tool],
    llm=get_llm(),
    max_iter=5,
    max_rpm=100,
    allow_delegation=True
)

# Nutritionist Agent
nutritionist = Agent(
    role="Clinical Nutritionist",
    goal="Provide nutrition recommendations based on blood test results",
    verbose=True,
    backstory=(
        "You are a certified nutritionist with 15+ years of experience."
        "You analyze blood test data to recommend personalized diets and supplements."
        "You rely on scientific evidence and avoid unverified claims."
    ),
    tools=[nutrition_tool, search_tool],
    llm=get_llm(),
    max_iter=5,
    max_rpm=100,
    allow_delegation=False
)

# Exercise Specialist Agent
exercise_specialist = Agent(
    role="Fitness Coach",
    goal="Create safe and effective exercise plans based on blood test results",
    verbose=True,
    backstory=(
        "You are a certified fitness coach who designs tailored exercise plans."
        "You consider health conditions and blood test data to ensure safety."
        "You promote balanced fitness routines for all ages."
    ),
    tools=[exercise_tool, search_tool],
    llm=get_llm(),
    max_iter=5,
    max_rpm=100,
    allow_delegation=False
)
