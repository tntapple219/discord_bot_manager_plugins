import discord
from discord.ext import commands
import json
import os

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.path = os.path.dirname(__file__)
        self.config_path = os.path.join(self.path, 'info.json')
        
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.info = json.load(f)
        else:
            self.info = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[PingCommand] 插件已就緒")

    @commands.command(name="ping", help="顯示機器人的延遲")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"目前延遲: **{latency}ms**",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(PingCommand(bot))
