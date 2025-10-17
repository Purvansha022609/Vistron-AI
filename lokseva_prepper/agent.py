# lokseva_prepper/agent.py

from google.adk import Agent

# -------------------------------
# Sub-agents for UPSC Preparation
# -------------------------------

question_generator = Agent(
    name="UPSC_QuestionGenerator",
    model="gemini-2.0-flash",
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

resource_finder = Agent(
    name="UPSC_ResourceFinder",
    model="gemini-2.0-flash",  # No tools used
    description="Suggests essential books, resources, and online links for a given UPSC subject.",
    instruction="""
        You are a UPSC resource expert. The coordinator will give you a subject.
        Suggest 3-4 essential resources including NCERTs, standard reference books, and key current affairs sources.
        For each resource, provide:
        - Title/Book/Article/Video
        - Author/Source/Channel
        - Purpose (Prelims/Mains, Conceptual Clarity)
        - URL if available
    """
)

current_affairs_agent = Agent(
    name="UPSC_CurrentAffairs",
    model="gemini-2.0-flash",
    description="Provides concise current affairs updates and analysis for UPSC preparation.",
    instruction="""
        You are a UPSC Current Affairs expert. The coordinator will give you:
        - Target Stage (Prelims/Mains)
        - Timeframe (e.g., last month, last 6 months)
        - Subject (Optional)

        Return:
        - Key events
        - Relevance to UPSC
        - Links or references if possible
    """
)

revision_agent = Agent(
    name="UPSC_RevisionNotes",
    model="gemini-2.0-flash",
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

assessment_agent = Agent(
    name="UPSC_SelfAssessment",
    model="gemini-2.0-flash",
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

study_plan_agent = Agent(
    name="UPSC_StudyPlanner",
    model="gemini-2.0-flash",
    description="Generates micro-study schedules for UPSC aspirants based on time availability and subjects.",
    instruction="""
        You are a UPSC study planner expert. The coordinator will give you:
        - Subjects to cover
        - Total preparation days
        - Daily study hours

        Return:
        - Daily/Weekly timetable
        - Subject-wise priority
        - Revision slots
    """
)

# -------------------------------
# Coordinator Agent
# -------------------------------
coordinator_agent = Agent(
    name="LoksevaUPSC_Coordinator",
    model="gemini-2.0-flash",
    description="""
        You are the Lokseva UPSC Study Coordinator. Your main role is to delegate tasks to specialized sub-agents.
        Do not perform the tasks yourself. Use the following sub-agents:

        - UPSC_QuestionGenerator: Creates practice questions.
        - UPSC_ResourceFinder: Recommends books, websites, and videos.
        - UPSC_CurrentAffairs: Provides current events updates.
        - UPSC_RevisionNotes: Generates concise study notes.
        - UPSC_SelfAssessment: Creates self-assessment tests.
        - UPSC_StudyPlanner: Generates study timetables.

        Task:
        1. Understand user's goal (study plan, resources, questions).
        2. Identify and delegate to the right sub-agent(s).
        3. Combine results and present a comprehensive response.
    """,
    sub_agents=[
        question_generator,
        resource_finder,
        current_affairs_agent,
        revision_agent,
        assessment_agent,
        study_plan_agent
    ]
)

# -------------------------------
# Set the root agent
# -------------------------------
root_agent = coordinator_agent
