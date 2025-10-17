# subagents/__init__.py

from .question_generator import question_generator
from .resource_finder import resource_finder
from .current_affairs_agent import current_affairs_agent
from .revision_agent import revision_agent
from .assessment_agent import assessment_agent
from .study_plan_agent import study_plan_agent

# Optional: expose all agents for easy import
__all__ = [
    "question_generator",
    "resource_finder",
    "current_affairs_agent",
    "revision_agent", 
    "assessment_agent",
    "study_plan_agent"
]
