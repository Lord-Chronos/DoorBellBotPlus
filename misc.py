from discord.ext import tasks, commands
from tictactoe import print_board
import fileinput

class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        # bot.bg_task = bot.loop.create_task(Miscellaneous.my_background_task())

    @commands.command(name='dontdead')
    async def dont_dead(self, ctx):
        await ctx.send('Open inside.')

    @commands.command(name='misc')
    async def misc_function(self, ctx):
        await ctx.send('Well done, you\'ve called a misc function.')

    @commands.command(name='tictactoe')
    async def play_tic_tac_toe(self, ctx):
        board = print_board()
        await ctx.send(board)

    @commands.command(name='setring')
    async def set_ring(self, ctx,arg, arg2):
        ftimeread = open("SwanData.txt", "r")
        ftimewrite = open("SwanData.txt", "w")
        found = False
        lineNum = 0
        listOfLines = []
        for line in ftimeread:
            listOfLines.append(line)

            values = line.split()
            for v in values:
                if v == arg:
                    found = True
                    listOfLines[lineNum] = str(values[0] +" " +arg2)
            lineNum += 1
        if found:
            ftimewrite.writelines(listOfLines)
            ftimewrite.close()
            await ctx.send("Found and renamed")

        else:
            await ctx.send("Time not found :(")



def setup(bot):
    bot.add_cog(Miscellaneous(bot))
