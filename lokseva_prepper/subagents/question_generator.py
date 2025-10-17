from google.adk import Agent

question_generator = Agent(
    name="UPSC_QuestionGenerator",
    model="gemini-2.0-flash-exp",
    description="Generates UPSC-style questions and evaluation criteria for a given subject and topic.",
    instruction="""
        You are a UPSC question specialist. The coordinator will give you:
        - target_stage (Prelims or Mains)
        - subject
        - topic
        
        If target_stage is 'Prelims', return 3-5 MCQs in UPSC format with correct answer and explanation.
        If target_stage is 'Mains', return 1-2 descriptive questions with suggested word limit and model answer structure.
    """
)