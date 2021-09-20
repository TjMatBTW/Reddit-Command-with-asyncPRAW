import discord
from discord.ext import commands
import asyncpraw

client = commands.Bot(command_prefix='!')

@client.command()
async def meme(ctx, subred="memes"):
    msg = await ctx.send('Getting the best meme from this category. Please wait...')
    await asyncio.sleep(5)
    await msg.delete()

    reddit = asyncpraw.Reddit(
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        password="PASSWORD",
        user_agent="USER_AGENT",
        username="USERNAME",
        )

    subreddit = await reddit.subreddit(subred)
    all_subs = []

    top = subreddit.top(limit=50)

    async for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(f'{ctx.author.mention}')
    await ctx.send(embed=em)


client.run('token')

# Made by TjMat#5830
