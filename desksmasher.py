from codes import *
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

channelDS = client.get_channel('YOUR COMMANDS CHANNEL HERE')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


#--------------------COMMANDS----------------------------

@client.event
async def on_message(message) :
    channelDS = client.get_channel(1314127566025785396)
    if message.content.startswith('ds!help'):
        embedHelp = discord.Embed(
            title=(f':ocean: Welcome, {message.author}!'),
            description=(f'**I am DeskSmasher!**\nMy commands are:\n* ds!help\n* ds!ping')
        )
        embedHelp.set_author(name="DeskSmasher: your ultimate headache! ✅")
        embedHelp.set_image(url="https://i.ytimg.com/vi/LpeBFiXJ1js/maxresdefault.jpg")
        await channelDS.send(embed=embedHelp)


    if message.content.startswith('ds!ping'):
        latency = client.latency
        await channelDS.send(f':ping_pong: **My latency is** {latency}**!**')

    if message.content.startswith('ds!profile'):
        user = message.author
        userIcon = user.display_avatar
        userprofileEmbed = discord.Embed(
            title=(f':wave: {user}s profile'),
            description=(f'**Mention:** {user.mention}\n**Joined at:** {user.joined_at}\n**ID:** {user.id}'),
        )
        userprofileEmbed.set_author(name="DeskSmasher: your ultimate headache! ✅")
        userprofileEmbed.set_image(url= userIcon)

        await channelDS.send(embed=userprofileEmbed)


    if message.content.startswith('ds!uwu'):
        for i in range(30):
            await channelDS.send('uwu')



#--------------------EVENTS----------------------------

@client.event
async def on_member_join(member):
    channel = client.get_channel(1314308224555683902)
    embed = discord.Embed(
        title=(f'New member!'),
        description=(f'Everybody welcome {member.mention}!\nThis server is powered by **DeskSmasher** :sunglasses:')
    )
    await channel.send(embed=embed)





client.run(DESKSMASH_BOT_TOKEN) # PUT THIS UNDER EVERYTHING
