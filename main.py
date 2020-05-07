import random
import configparser
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Sets the bot call command prefix
bot = commands.Bot(command_prefix='!')

# Get Discord Bot Token from the config file
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['aoebot']['discord_token']
GUILD = config['aoebot']['discord_channel']


# Initilise the Discord Client
load_dotenv()
client = discord.Client()


# Returns a randomly selected civilisation
@bot.command(name='civ', help='Randomly selects a civilisation')
async def civ(ctx):
    civlist = [
        'Britons',
        'Byzantines',
        'Celts',
        'Chinese',
        'Franks',
        'Goths',
        'Japanese',
        'Mongols',
        'Persians',
        'Saracens',
        'Teutons',
        'Turks',
        'Vikings',
        'Aztecs',
        'Huns',
        'Korens',
        'Mayans',
        'Spanish',
        'Incas',
        'Indians',
        'Italians',
        'Magyars',
        'Slavs',
        'Berbers',
        'Ethiopians',
        'Malians',
        'Portuguese',
        'Burmese',
        'Khmer',
        'Vietnamese'
    ]
    response = random.choice(civlist)
    await ctx.send(response)


# Returns a randomly selected location map
@bot.command(name='map', help='Randomly selects a multiplier location')
async def civ(ctx):
    location = [
        'Acropolis',
        'Arabia',
        'Arena',
        'Baltic',
        'Black Forest',
        'Budapest',
        'Cenotes',
        'City of Lakes',
        'Coastal',
        'Continental',
        'Crater Lake',
        'Ctr Monsoon',
        'Ctr Pyramid Descent',
        'Ctr Random',
        'Ctr Spiral',
        'Fortress',
        'Ghost Lake',
        'Gold Rush',
        'Golden Pit',
        'Hamburger'
        'Hideout',
        'Highland',
        'Hill Fort',
        'Islands',
        'Kilimanjaro',
        'Lombardia',
        'Mediterranean',
        'MegaRandom',
        'Migration',
        'Mongolia',
        'Mountain Pass',
        'Nile Delta',
        'Nomad',
        'Oasis',
        'Rivers',
        'Salt Marsh',
        'Scandinavia',
        'Serengeti',
        'Socotra',
        'Steppe',
        'Team Islands',
        'Valley',
        'Yucatan'
    ]
    response = random.choice(location)
    await ctx.send(response)


# Returns a randomly selected location map
@bot.command(name='3', help='Randomly selects a multiplier location from the trusty three')
async def civ(ctx):
    location = [
        'Black Forest',
        'Islands',
        'Team Islands'
    ]
    response = random.choice(location)
    await ctx.send(response)


# Returns a randomly selected dad joke
@bot.command(name='mitch', help='Randomly selects a great joke for Mitch')
async def civ(ctx):
    joke = [
            'I\'ll call you later. Don\'t call me later, call me Dad!',
            'How do celebrities stay cool? They have many fans.',
            'What\'s Forrest Gump\'s Facebook password? 1forest1.',
            'What do you call it when Batman skips church? Christian Bale.',
            'What time did the man go to the dentist? Tooth hurt-y.',
            'Did you hear about the man who fell into an upholstery machine? He\'s fully recovered.',
            'Why didn\'t the melons get married? Because they cantaloupe.',
            'What kind of egg did the evil chicken lay? A deviled egg.',
            'Why did the coach go to the bank? To get his quarter back.',
            'Why does Snoop Dogg always carry an umbrella? Fo\' Drizzle.',
            'What did the fisherman say to the magician? Pick a cod, any cod.',
            'What do you call a fake noodle? An impasta.',
            'Which is faster, hot or cold? Hot, because you can catch a cold.',
            'How do you organize a space party? You planet.',
            'Did you know that milk is the fastest liquid on earth? It\'s pasteurized before you even see it.',
            'Why are skeletons so calm? Because nothing gets under their skin.',
            'What did one ocean say to the other ocean? Nothing, they just waved.',
            'What does a baby computer call his father? Data.',
            'Did you hear about the power outlet who got into a fight with a power cord? He thought he could socket to him.',
            'Why are elevator jokes so good? They work on so many levels.',
            'Why can\'t a leopard hide? Because he\'s always spotted.',
            'How do moths swim? Using the butterfly stroke.',
            'How many tickles does it take to make an octopus laugh? 10 tickles.',
            'Do you know the story about the chicken that crossed the border? Me neither, I couldn\'t follow it.',
            'I made a pencil with two erasers. It was pointless.',
            'How do you make a Kleenex dance? Put a little boogie in it!',
            'What do you get from a pampered cow? Spoiled milk!',
            'What do you call an illegally parked frog? Toad.',
            'Where do baby cats learn to swim? The kitty pool.',
            'Why are spiders so smart? They can find everything on the web.',
            'How can a leopard change his spots? By moving.'
            ]
    response = random.choice(joke)
    await ctx.send(response)


# Returns a dice roll based on the number of dice and the sides each die has
@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(TOKEN)



