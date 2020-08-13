from bot_conn_data import client_id, initial_channels, irctoken, nick, prefix
from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=irctoken,
            client_id=client_id,
            nick=nick,
            prefix=prefix,
            initial_channels=initial_channels)

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(f'{message.channel}:{message.author.name}:{message.content}')
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='090')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()

if __name__ == "__main__":
    bot.run()
