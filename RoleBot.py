import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#When emoting a certain emote, gain that role.
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="deep rock")
        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "6️⃣":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "7️⃣":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "8️⃣":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "9️⃣":
            role = discord.utils.get(guild.roles, name="valorant")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            member = payload.member
            print("Done")
            print(member)
            if member is not None:
                await member.add_roles(role)
                print("Await Done")

#Why is this not working?
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="deep rock")
        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "6️⃣":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "7️⃣":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "8️⃣":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "9️⃣":
            role = discord.utils.get(guild.roles, name="valorant")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            # member = payload.user_id
            print(member)
            print("Done")
            if member is not None:
                await member.remove_roles(role)
                print("Await Done")

client.run(os.environ.get('DISCORD_TOKEN'))