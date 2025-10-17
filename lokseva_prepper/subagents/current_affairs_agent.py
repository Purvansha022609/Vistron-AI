# In your agent.py or assessment_agent.py file

from google.adk import Agent

assessment_agent = Agent(
    name="UPSC_SelfAssessment",
    model="gemini-2.0-flash", # <-- Use a stable, supported model
    description="Creates self-assessment tests and answer keys for UPSC aspirants.",
    instruction="""
        You are a UPSC self-assessment specialist. The coordinator will give you:
        - Subject
        - Topic
        - Target Stage (Prelims/Mains)
        
        Return:
        - 5-10 MCQs for Prelims with correct answers
        - 1-2 descriptive questions for Mains with answer hints
        - Provide explanation for each answer
    """
)