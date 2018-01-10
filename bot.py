import os
import telebot
import schedule
import time

bot_token = '532637906:AAHf9kCQIzYs83f84s5WhEo5jFtjFh95jp0'
#bot_token =  os.environ['BOT_API_TOKEN']

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['bot', 'help','info'])
def send_welcome(message):
    bot.reply_to(message, """
    *In order to get your questions answered, please use the commands below:*

    /tokenprice - Get token price
    /tokensale - Info on how to invest in token sale
    /ICOdate - Get ICO dates
    /airdrop - Get airdrop information
    /bounty - Get bounty campaign information
    /whatisSp8de - Info about Sp8de project
    /whatisCardano - Info about Cardano blockchain
    /whySp8de - Main reasons why it's worth investing in this token sale before it hits the exchanges
    /minimuminvestment - Minimum investment amount
    /claim - Info about airdrop and how to get involved in bounty
    /jackpots - Info about jackpots, how many jackpots there will be, which amount in which phases, and how much in total
    /roadmap - Info about the roadmap
    /realwebsite - What is the real website (ico.sp8de.com)
    /investnow - Where to invest (ico.sp8de.com)
    /erc20 - Is it an ERC20 token? Yes.
    /tokeninfo - Info about name and type of coin
    """,parse_mode='Markdown')

@bot.message_handler(commands=['tokenprice'])
def send_welcome(message):
    bot.reply_to(message, "1 ETH = 98888 SPX")

@bot.message_handler(commands=['tokensale'])
def send_welcome(message):
    bot.reply_to(message, """*The only place to invest in the token sale is here:*
    https://ico.sp8de.com/. Join the Pre-Sale to have the most chances of winning the token jackpot!""", parse_mode='Markdown')


@bot.message_handler(commands=['erc20'])
def send_welcome(message):
    bot.reply_to(message, """Yes, Sp8de will begin as an ERC20 token""", parse_mode='Markdown')

@bot.message_handler(commands=['ICOdate','icodate'])
def send_welcome(message):
    bot.reply_to(message, """Yes, Sp8de will begin as an ERC20 token""", parse_mode='Markdown')

@bot.message_handler(commands=['airdrop'])
def send_welcome(message):
    bot.reply_to(message, """The airdrop tokens will be automatically given at the end of the ICO - welcome to the community! We invite you to join our bounty program here: https://bitcointalk.org/index.php?topic=2718430.new
""", parse_mode='Markdown')


@bot.message_handler(commands=['bounty'])
def send_welcome(message):
    bot.reply_to(message, """To join and/or learn more regarding our bounty program,
    check out our bitcointalk announcement here: https://bitcointalk.org/index.php?topic=2718430.new""", parse_mode='Markdown')

@bot.message_handler(commands=['whatisSp8de'])
def send_welcome(message):
    bot.reply_to(message, """Sp8de is a new-generation blockchain gaming platform, based on the Cardano blockchain – a project that builds the unique entropy-injecting Proof-of-Stake protocol Ouroboros, which allows for the development and operation of distributed casino applications by eliminating completely all of the problems of traditional and online gambling environments. Sp8de provenly trumps all other blockchain casino projects as it allows players to bet as small amount of bet as they want, to know the result of their bet the very moment of the conclusion of the game, and all this, while being confident that neither the casino nor other players can manipulate in any way the outcome of the dice roll.""", parse_mode='Markdown')


@bot.message_handler(commands=['tokeninfo'])
def send_welcome(message):
    bot.reply_to(message, """SPX will be an ERC20 Token.""", parse_mode='Markdown')


@bot.message_handler(commands=['whatiscardano','whatisCardano'])
def send_welcome(message):
    bot.reply_to(message, """Cardano is a new-generation blockchain protocol developed by IOHK, to which Sp8de will connect its own blockchain.""", parse_mode='Markdown')

@bot.message_handler(commands=['whySp8de'])
def send_welcome(message):
    bot.reply_to(message, """As the first project built on Cardano, it will allow for provable randomness. It will also be the first ICO to have a gambling aspect incorporated into the sale. You can find more information in the summarized whitepaper: https://sp8de.com/fast_deck.pdf""", parse_mode='Markdown')


@bot.message_handler(commands=['minimuminvestment'])
def send_welcome(message):
    bot.reply_to(message, """Minimum investment is 20$ USD - About 1750 tokens""", parse_mode='Markdown')

@bot.message_handler(commands=['claim'])
def send_welcome(message):
    bot.reply_to(message, """Your airdrop tokens will be sent at the end of the token sale. Thank you for joining our community""", parse_mode='Markdown')

@bot.message_handler(commands=['investnow'])
def send_welcome(message):
    bot.reply_to(message, """The only place to invest is at https://ico.sp8de.com/""", parse_mode='Markdown')


@bot.message_handler(commands=['realwebsite'])
def send_welcome(message):
    bot.reply_to(message, """The only real website is https://sp8de.com/ for information & https://ico.sp8de.com/ for token sale""", parse_mode='Markdown')

@bot.message_handler(commands=['roadmap'])
def send_welcome(message):
    bot.reply_to(message, """To find out about our roadmap, visit our website https://sp8de.com/ or check out our whitepaper here:""", parse_mode='Markdown')

@bot.message_handler(commands=['jackpots'])
def send_welcome(message):
    bot.reply_to(message, """You get a chance to win in all of the jackpot rounds that still have not occured. Therefore, the sooner you invest, the higher the chance of winning the jackpots.

You get a chance to win in all of the jackpot rounds that still have not occured. Therefore, the sooner you invest, the higher the chance of winning the jackpots.
Cumulative Jackpots (If you invest in pre-sale, you get chances at each jackpot)
Jackpot Round 1 - 288,888,888 tokens 
Jackpot Round 2 - 388,888,888 tokens
Jackpot Round 3 - 888,888,888 tokens
Jackpot Round 4 - 1,888,888,888 tokens

            """, parse_mode='Markdown')

bot.polling()
