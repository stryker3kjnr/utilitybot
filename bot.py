import discord
from discord.ext import commands
from utilitybot import Utilitybot
from discord.ext import *
import asyncio
import asyncpg
import dotenv
from utils.permissions import permissions
bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity= discord.Game(name="Vibing", type=3),
    case_insensitive=True,
    owner_id=388788632686690305
)