import os
import telebot
import schedule
import time

#bot_token = '528330714:AAHm5nYJkhLBWuq32zWfNgl-yzSBI1MSc4A'
bot_token =  os.environ['BOT_API_TOKEN']

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
    /smartcontract - Gives Smart Contract Address
    """,parse_mode='Markdown')

@bot.message_handler(commands=['tokenprice'])
def send_welcome(message):
    bot.reply_to(message, """SP8DE adopts the “classic” ICO structure in that we place substantial value in “early birds” - those contributors who are not afraid to be the first ones to invest. Therefore, the earlier one invests the more tokens he or she will receive for the same amount of money. 
    We propose the following discount schedule: 
    
Pre-ICO: 1 ETH = 98888 SPX (Roughly 40% discount)
ICO Phases:
Sale I:   1 ETH = 88888 SPX (Roughly 34% discount)
Sale II:   1 ETH = 78888 SPX (Roughly 25% discount)
Sale III:  1 ETH = 68888 SPX (Roughly 15% discount)
Sale IV:  1 ETH = 58888 SPX (the ultimate price of tokens - 0% discount)


Link to forum thread: https://forum.sp8de.com/index.php?threads/spx-token-price-information.1/""")

@bot.message_handler(commands=['tokensale'])
def send_welcome(message):
    bot.reply_to(message, """The only place to invest in the ICO is here: https://ico.sp8de.com/. Please, pay extra attention to the site you are using: beware of scammers. 
    The best place to explore the terms of the sale is our website: https://sp8de.com/, the best place to ask questions about it is our Bitcointalk thread on the following link: https://bitcointalk.org/index.php?topic=2659341.20.
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/spx-token-sale-information.2/
""", parse_mode='Markdown')


@bot.message_handler(commands=['erc20'])
def send_welcome(message):
    bot.reply_to(message, """Yes, Sp8de will begin as an ERC20 token. All the tokens, airdropped, purchased or won during the Jackpot Phases will be converted 1:1 into the tokens generated on the Cardano blockchain. Same procedure will convert all the tokens on exchange wallets.
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/spx-ico-token-information.3/""", parse_mode='Markdown')

@bot.message_handler(commands=['ICOdate','icodate'])
def send_welcome(message):
    bot.reply_to(message, """The Pre-ICO will last from January 8, 2018 until February 1, 2018. The ICO will begin on February 8, 2018 and will last until March 11, 2018. Every round of the token sale will be followed by a Jackpot round. 
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/sp8de-ico-date.4/""", parse_mode='Markdown')

@bot.message_handler(commands=['airdrop'])
def send_welcome(message):
    bot.reply_to(message, """The airdrop tokens will be automatically given at the end of the ICO - welcome to the community! 
    The only place where you can join our airdrop program is: https://www.airdropx.com/sp8de/. Beware of scammers, do not follow any other links! The airdrop tokens will be distributed at the end of the ICO. 
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/sp8de-airdrop.5/
""", parse_mode='Markdown')


@bot.message_handler(commands=['bounty'])
def send_welcome(message):
    bot.reply_to(message, """To join and/or learn more regarding our Sp8de Bounty Program, check out our Bitcointalk Bounty Thread here: https://bitcointalk.org/index.php?topic=2718430.new .

Link to forum thread: https://forum.sp8de.com/index.php?threads/sp8de-bounty-program.6/""", parse_mode='Markdown')

@bot.message_handler(commands=['whatisSp8de'])
def send_welcome(message):
    bot.reply_to(message, """SP8DE is the blockchain-based platform for decentralized gaming applications that is set to become the new industry standard of fairness. Sp8de is the platform that is set to give an answer for every single issue that is known in the on-chain gaming space. 
Built on top of Cardano, a Proof-of-Stake blockchain protocol, Sp8de will allow for the creation of distributed randomness that is fair by-design. Scalable and transparent, Sp8de will be entirely decentralized in every aspect of its design. Furthermore, Sp8de is a platform: anyone with a worthy idea can implement it as a decentralized application (DApp) and broadcast it through the Sp8de ecosystem.

Link to forum thread: https://forum.sp8de.com/index.php?threads/what-is-sp8de.7/""", parse_mode='Markdown')


@bot.message_handler(commands=['tokeninfo'])
def send_welcome(message):
    bot.reply_to(message, """SPX will be an ERC20 Token. There are 8,888,888,888 of which 3,655,555,558.4 (41.125%) will be distributed in the form of token sale and 3,455,555,552 (38.875%) will be given as a jackpot to those who have participated in the “token sale” rounds. The remaining 20% of the tokens will remain with the team (part of them will be given to those participating in the Sp8de Bounty Program and in the form of an Airdrop).
    
Pre-Sale (Pre-ICO): January 8 - February 1: 888,888,888 SPX
Sale I: February 8 - February 14: 388,888,888 SPX
Jackpot I: February 15: 288,888,888 SPX
Sale II: February 16 - February 22: 585,858,585 SPX
Jackpot II: February 23: 388,888,888 SPX
Sale III: February 24 - March 2: 886,868,686 SPX
Jackpot III: March 3: 888,888,888 SPX
Sale IV: March 4 - March 10: 905,050,511 SPX
Jackpot IV: March 11: 1,888,888,888 SPX

Link to forum thread: https://forum.sp8de.com/index.php?threads/spx-token-general-information.8/""", parse_mode='Markdown')


@bot.message_handler(commands=['whatiscardano','whatisCardano'])
def send_welcome(message):
    bot.reply_to(message, """Cardano is the new-generation Proof-of-Stake (POS) based blockchain developed by IOHK foundation. The Cardano project itself is a monumental work that embraced the best practices and most far reaching innovations in the area of cryptocurrencies packed into a single state-of-art system. It is being developed and maintained by a large team comprised solely of PhDs in the field of programming and cryptography, and experienced engineers. Ouroboros is the actual blockchain protocol underpinning Cardano: it is POS and it is provably secure. 
Achieving this security property in the adversary setting for a POS protocol requires a procedure for generating a ‘good quality’ on-chain randomness: Ouroboros is designed to solve this issue. ‘Good quality’ in this context means that no participant of the protocol can induce a significant bias on the outcome of the miner selection procedure, thus, on the process generating randomness. 
Sp8de enhances this procedure further by allowing the outputs of randomness to be generated at arbitrary frequencies. This feature is a prerequisite for allowing actual gaming applications run on top of our protocol. An important note is that this enhanced efficiency does not come at the expense of security: in our design, the actual random number generating process utilizes both, the Cardano blockchain and the Sp8de transactions. 

Link to forum thread: https://forum.sp8de.com/index.php?threads/what-is-cardano.9/""", parse_mode='Markdown')

@bot.message_handler(commands=['whySp8de'])
def send_welcome(message):
    bot.reply_to(message, """By purchasing Sp8de tokens, one becomes a part of the constantly growing ecosystem, which is set to grow as the word about the first provably fair gaming marketplace is being spread. So, firstly, there is a huge market out there waiting for the solution that Sp8de offers. 
Secondly, we have adopted a deflationary economic model for the token distribution: there is just 8,888,888,888 SPX tokens - not a single extra one will ever be created, so any increase in popularity of our platform will always be reflected positively in the price of the token. 
Finally, by entering our pre-sale, one gets the chance of participating in multiple jackpot rounds. Technically, these are the advanced airdrops that each will make one random token-holder rich in an instant. 

Link to forum thread: https://forum.sp8de.com/index.php?threads/why-sp8de.10/""", parse_mode='Markdown')


@bot.message_handler(commands=['minimuminvestment'])
def send_welcome(message):
    bot.reply_to(message, """Minimum investment is $20 - currently about 1750 tokens. We are not greedy: anyone participating early is entitled to all the discounts and benefits that are available only to large investors in the regular ICO setup. 
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/what-is-the-minimum-investment-to-participate-in-the-sp8de-ico.11/""", parse_mode='Markdown')

@bot.message_handler(commands=['claim'])
def send_welcome(message):
    bot.reply_to(message, """Please stop writing "claim" as it is not necessary.

Your Airdrop tokens will be sent at the end of the token sale (March 11, 2018). Thank you for joining the Sp8de community!

Link to forum thread: https://forum.sp8de.com/index.php?threads/when-do-i-receive-spx-tokens-from-the-airdrop.12/""", parse_mode='Markdown')

@bot.message_handler(commands=['investnow'])
def send_welcome(message):
    bot.reply_to(message, """The only place to invest is at https://ico.sp8de.com/.
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/how-do-i-participate-in-the-sp8de-ico.13/""", parse_mode='Markdown')


@bot.message_handler(commands=['realwebsite'])
def send_welcome(message):
    bot.reply_to(message, """The only real website is https://sp8de.com/ for information & https://ico.sp8de.com/ for token sale.
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/what-is-the-official-sp8de-website.14/
""", parse_mode='Markdown')

@bot.message_handler(commands=['roadmap'])
def send_welcome(message):
    bot.reply_to(message, """To find out about our roadmap, visit our website https://sp8de.com/ or check out the Sp8de Whitepaper here: https://sp8de.com/sp8de_white_paper.pdf (on page 25).
    
Link to forum thread: https://forum.sp8de.com/index.php?threads/the-sp8de-project-roadmap.15/""", parse_mode='Markdown')
    
@bot.message_handler(commands=['smartcontract'])
def send_welcome(message):
    bot.reply_to(message, """The smart contract address of SP8DE Pre-Sale Token (DSPX) ERC20 Token Tracker is: 
https://etherscan.io/token/0x30dda19c0b94a88ed8784868ec1e9375d9f0e27c
The Ethereum BlockChain Explorer, API and Analytics Platform

Link to forum thread: https://forum.sp8de.com/index.php?threads/the-smart-contract-address-of-sp8de-pre-sale-token-dspx-erc20.17/""", parse_mode='Markdown')

@bot.message_handler(commands=['jackpots'])
def send_welcome(message):
    bot.reply_to(message, """The Sp8de ICO is unique. By participating in the Pre-Sale and the Sale rounds you are automatically signed up for the Jackpot rounds where you will receive free SPX. The Jackpots are simple. If you have bought SPX during the Pre-Sale and the Sale 1 rounds you will receive SPX during ALL 4 Jackpots. However, if you participated in Sale 2 you get to receive SPX only from Jackpots 2, 3, and 4. Therefore, contributing to the token sale earlier gives you the opportunity to receive more tokens later. 
    
The amount of tokens given away during the Jackpots and their dates are as follows:
Jackpot Round 1 - 288,888,888 (10 x 28,888,888) SPX
Jackpot Round 2 - 388,888,888 (28 x 13,888,888) SPX
Jackpot Round 3 - 888,888,888 (100 x 8,888,888) SPX
Jackpot Round 4 - 1,888,888,888 (888 x 2,127,127) SPX
If you want to know more about the Jackpots go through the Whitepaper  https://sp8de.com/sp8de_white_paper.pdf on pages 18 to 23.

Link to forum thread: https://forum.sp8de.com/index.php?threads/sp8de-jackpots.16/""", parse_mode='Markdown')

bot.polling()
#end
