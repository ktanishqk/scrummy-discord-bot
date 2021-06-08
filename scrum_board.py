from discord.ext import commands
import discord
import discord.ext
from enum import Enum

class ProjectState(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    UNDER_REVIEW = auto()
    DONE = auto()

class ScrumBoard(project):
    project_state = ProjectState()