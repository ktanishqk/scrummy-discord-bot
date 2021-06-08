from discord.ext import commands
import discord
import discord.ext
from enum import Enum
from scrum_board import ScrumBoard

class Project:
    def __init__(self, name, project_manager, members, priority_tag):
        self.name = name
        self.project_manager = project_manager
        self.members = members
        self.priority_tag = priority_tag
        self.scrum_board = scrum_board
    def get_name(self):
        return self.name
    def set_project_manager(self, project_manager):
        self.project_manager = project_manager
    def get_project_manager(self):
        return self.project_manager
    def set_members(self, members):
        self.members = members
    def get_members(self):
        return self.members
    def set_priority_tag(self, priority_tag):
        self.priority_tag = priority_tag
    def get_priority_tag(self):
        return self.priority_tag
    def get_scrum_board(self):
        return scrum_board    