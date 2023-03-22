import discord

# question : answer
FAQs = {
    "q1": "a1",
    "q2": "a2",
    "q3": "a3"
}

#bot token here
TOKEN = "xxx"

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"started")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for question, answer in FAQs.items():
        if question.lower() in message.content.lower():
            await message.channel.send(answer)

bot.run(TOKEN)
