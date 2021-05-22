from .Ticket-System import Ticket-System


async def setup(bot):
    cog = Ticket-System(bot)
    bot.add_cog(cog)
    await cog.initialize()
