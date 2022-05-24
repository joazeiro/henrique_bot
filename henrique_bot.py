import discord
import random

TOKEN = 'OTc1MTM1NDg5NzE3ODM3OTI0.GiW4t4.P2XrbR7RasO0HiyamjbQgMA-qXhMVmOJGULKbw'

client = discord.Client()

@client.event
async def on_ready():
    print('Connected to discord as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    list_champs = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bardo", "Blitz", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ez", "Fiddle", "Fiora", "Fizz", "Galio", "GP", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimer", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan", "Jax", "Jayce", "Jhin", "Jinx", "Kai'sa", "Kalista 2021 kkkkk", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'zix", "Kindred", "Kled", "Kog", "Le Blanc AD Suporte", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master", "MF", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Noc", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'sai", "Rell", "Renata", "Renek", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir KKKKKKKK", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TK", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Trynda", "TF", "Twitch SNEAKY SNEAKY", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vlad", "Voli", "WW", "Wukong", "Xayah", "Geladeira Brastemp", "Xin", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
    list_messages = ["MEEEEH", "Você é prata, cala a boca", "Vou fatiar os caras", "Meu time só me afunda", "Seu ruim", "Dá uma mamada aqui", "É O PIJAS", "Ainda", "Você é podre mlk", "CARALHO DUDA"]

    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'bot_commands':
        if user_message.lower() == '!luiz':
            random_champ = list_champs[random.randint(0, len(list_champs) + 1)]
            response = f'Aí {username}, virei mono {random_champ} agora, que boneco roubado'
            await message.channel.send(response)
            return

        if user_message.lower() == "!henrique":
            random_message = list_messages[random.randint(0, len(list_messages) + 1)]
            response2 = f'{random_message}'
            await message.channel.send(response2)
            return
        

client.run(TOKEN)
