# In your revision_agent.py or agent.py file

from google.adk import Agent

revision_agent = Agent(
    name="UPSC_RevisionNotes",
    model="gemini-2.0-flash", # Changed model for stability
    description="Generates concise summaries, mnemonics, and revision notes for UPSC topics.",
    instruction="""
        You are a UPSC revision expert. The coordinator will give you:
        - Subject
        - Topic
        - Target Stage
        
        Return:
        - Short notes in bullet points
        - Important dates/facts/formulas
        - Quick mnemonics or memory aids
    """
)