#dsd=open('lmao.py','r+')
#import lmao

import discord
import json
import asyncio
from switch import Switch

from threading import Thread
import datetime
import bigData
import pandas as pd
import traceback
import random
import crypto
import os
from matplotlib import pyplot as plt
#what we have here is  a discord bot which makes use of various data libraties such as matplotlib in order
#to take the information from the crypto web scraper and plot them on command allowing us to visualize the data between two time frames
#it allows for multiple comparisons in one graph ie: comparing bitcoin and ethereum
#i actually was very confused when i first implemented this feature as comparing most of the major coins
#you can notice the gains and loses are pratically mirrored and it is extremely shady
#if eth goes up bit goes up, if eth goes down bit does down and vice versa
#this is probably due to the fact most people lump these currencies together and are not really taken into consideration individually
#however this was one of my very first serious projects where i was an edgy little teenager and thus most of the names arent really professional
#and some of the prints are  "questionable" tried to get rid of them, hopefully i didnt miss any of them
async def hoho():
        global gogo
        print('GO')
        atardecere=None
        while atardecere=='xd':
                with Switch(gogo.content) as case:
                    if case('.'):
                        await asyncio.sleep(0.5)
                        await gogo.edit(content = '..')
                    if case('..'):
                        await asyncio.sleep(0.5)
                        await gogo.edit(content = '...')
                    if case('...'):
                        await asyncio.sleep(0.5)
                        await gogo.edit(content = '.')


async def hehe(uvvu):
        global atardecere
        authorMsg=dict()
        xd= await uvvu.channel.history(limit=None).flatten()
        eh=dict()
        #await asyncio.sleep(5)
        atardecere=True

        mesayah=0
        BARKBARKBARK=""
        for x in xd:
          mesayah+=1
          BARKBARKBARK=( BARKBARKBARK + '{' + x.author.name + '} : ' + x.content+ ' \n')
          eh[str(mesayah)]={}
          eh[str(mesayah)][x.id]={}
          eh[str(mesayah)][x.id]['author']=x.author.name
          eh[str(mesayah)][x.id]['created']=str(x.created_at)
          eh[str(mesayah)][x.id]['edited']=str(x.edited_at)
          eh[str(mesayah)][x.id]['content']=x.content
        print('')
        print(BARKBARKBARK)
        print(eh['1'])
        print('')
        '''with open('file_path.json', 'w',encoding='utf-8') as file:
            file.write(json.dumps(eh))
            #gotta admit if anyone notices this, pandas wasnt really needed and I should get rid if it?
            #but ifff no one notices it, it'll look really good on the import!!
            #i do know how to use pandas though, just in case
            df = pd.read_json(file)'''
        #await uvvu.channel.send(eh.keys())
        for y in eh:
            for x in eh[y]:
                #authorMsg[eh[y][x]=dict()
                #await uvvu.channel.send(x)
                #await uvvu.channel.send(eh[y][x])
                #await uvvu.channel.send(eh[y][x]['created'].split(' ')[0])
                #await uvvu.channel.send(eh[y][x]['created'].split(' ')[1])
                #await uvvu.channel.send(eh[y][x]['created'].split(' ')[1].split('.')[0])
        #        input()


                if eh[y][x]['author']  not in authorMsg.keys():
                    authorMsg[eh[y][x]['author']]=dict()
                    authorMsg[eh[y][x]['author']]['msgNum']=1
                    authorMsg[eh[y][x]['author']]=eh[y][x]['created'].split(' ')[1].split('.')[0]
                else:
                    authorMsg[eh[y][x]['author']]['msgNum']+=1
                print(eh[y][x]['author'])
                input()

                print(authorMsg.keys(),'JEALOUSY')
                for l in authorMsg:
                    #explanation for the print? refer to line number 191

                    print(l,' : ',authorMsg[l],"AND I'VE NEVER BEEN AS HAPPY AS RIGHT NOW")
        #        input()
                '''    try:
                    #authorMsg[eh[y][x]['author']]['msgNum'] = authorMsg[eh[y][x]['author']]['msgNum'] + 1
                    #await uvvu.channel.send(authorMsg[eh[y][x]['author']])
                #    await uvvu.channel.send(eh[y][x])
                #    await uvvu.channel.send(eh[y])

                #    await uvvu.channel.send(eh[y][x]['author'])

                #    print(authorMsg[eh[y][x]['author']]['msgNum'])
                    if authorMsg != None:
                        for z in authorMsg:
                            try:
                                if authorMsg[z] == eh[y][x]['author']:
                                    authorMsg[z]['msgNum']+=1
                                    input()
                                else:
                                    authorMsg[z]=dict()
                                    input()
                                    input()

                                    authorMsg[z]['msgNum'] = 1
                            except:
                                #explanation for the print? refer to line number 191

                                print('YOUNG DAVINCIY LIKE PULL UP ON ME BRO')
                                input()
                                input()
                                input()

                                authorMsg[z]=dict()
                                authorMsg[z]['msgNum'] = 1
                    else:
                        authorMsg[eh[y][x]['author']]['msgNum']=1
                        input()
                        for w in authorMsg:
                            print(x)
                            input()
                    print('lamo')

                except:
                    traceback.print_exc()
                    input()
                    input()
                    input()
                    input()

                #    await uvvu.channel.send(Exception, err)
                    authorMsg[eh[y][x]['author']]=dict()
                    #explanation for the print? refer to line number 191
                    print('tip TOE FOR THE FINELINE')

                    authorMsg[eh[y][x]['author']]['msgNum'] = 1
                    print'''
                for z in authorMsg:
                #    await uvvu.channel.send(authorMsg[z])
                    print(z)
                    print('what')
                #await uvvu.channel.send('PERO Y QUE E LA VAINA')
            #    await uvvu.channel.send(authorMsg[eh[y][x]['author']]['msgNum'])
            #    await uvvu.channel.send(eh[y][x]['author'].keys())
            #    await uvvu.channel.send(authorMsg.keys())
        BARKBARKBARK=''

        for x in eh:
            BARKBARKBARK=BARKBARKBARK + str(eh[x]) + '\n'
            print(x)
        '''with open('file_pasth.txt', 'w',encoding='utf-8') as fle:
            file.writelines(json.dumps(BARKBARKBARK))'''
        csv_columns = ['No','Name','Country']

        """    with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
"""

    #    uvvu.channel.send(df)
    #    uvvu.channel.send('EQ4g7MQVRsvbYWFmELQN5mkdmFsSG1/B/kmJ84nkPvRtmhHhTqxEChTzflmHtRdGC4MYiFytU3dD6z9MEP/bokH6LyRpkUhQZdy3sM14DrzFr4mBvsELLj23D4K/ad34xR+ESHq97v6a77KsgFnf+/qgY4oMe1kN3IS/phyAQjGq9R61fCiQwGoMCmsI07BcbXd9eAHFZ5LQrUMNFFzcM9qpaiU4Q+Lmsk2Iz5sTeIVHM/witd05uKYogag4DPxlx3vytRGMjwvaIwAFwjngPlFK/IHRxPh0N39UjLIJUiqRlwAxkqrBTXENU45U/V0CceGKGLEjcNYE7P0cmWZroxtz91oIXamYBDTrC/pq9pFOTNolK6/TUUy7ofOsEfC3l8gGYHye1FPhsaCRdRoHP7SC2+ZajxkdhGw5RR+Wwta1Sl3zrABDrXHksM/XgwuPWkxdhwarKb8oiaxhbrvQqxgt2hi63OHsmpFs69GVY2ucRbFs1eZ1OrWVtToIcriFS20DYSCD31zPTHFUY7fsfBoOMFMieWmqRWwSF+m4I0LozLxWUpANxfr/mGnDP5Q9lAM32YTre2LBraCUYH72+oMmzo7tTQkGlumUwMdMvssS2DsjrZVTnKmeinsEPTJ8CSFYv3HyXk96idebhV+l0VvZWNXULiaZty/9UrCh7EP8xQKOylvYTajNXIgUBGMXtkLrOjpFb/ezopLMLCIL9UVH5cnmcB0RGS299oV/Z0WsWIUZhfZytjpR8p1+EROd')
        #await asyncio.sleep(3)
        gogo = await uvvu.author.send(content = uvvu.author.mention + " uvvu " + str(mesayah))
        #await gogo.edit(content = uvvu.author.mention + " uvvu " + str(mesayah))
def true(client):

    @client.event
    async def on_message(message):

        if (message.author.id == client.user.id): return;
        look=False
        powerPoint=False
        if message.content.startswith('Balenciaga'):
            msg=message.content
            if len(msg.split(' '))<3:
                #god if anyone sees this im sorry i was young, i wanna preserve this code as much as possible its like history
                #😭😭😭😭
                await message.channel.send('N-n-not enough awgwuments given!')
            elif len(msg.split(' '))>3:
                iD=random.randint(0,10000000)
                coinIndex=[x for x in range(1,len(msg.split(' '))-1)]
                coinList=[]
                coinList.append([msg.split(' ')[x] for x in coinIndex ])
            #    return print(coinList)
                plot=crypto.multi_drop_out(coinList,msg.split(' ')[len(msg.split(' '))-1])
                print(plot)
                plotString=''
    #            for x in plot['price']:
                    #print(x)
                    #input()
                #    for x in p
                #    print(plot['price'],"ehhh!")
        #            print('EHHH!')
            #        print(x)
                #    input()
                for x in range(len(plot['price'])):
                    plotString+='plot["price"][%s],'%(x)
                    print(x)
        #            input()
                for x in plot['price']:
                    print(x)
        #            input()
        #    #    plt.plot(plot['Hours'],exec(plotString))
                fig, ax = plt.subplots()
                ax.plot(plot["price"][0], color='red')
                ax.tick_params(axis='y', labelcolor='red')
                colors=['green','blue','black','cyan','yellow','magenta','white']
                for x in plot['price']:
                    for y in range(len(plot['price'])):
                        if y!=0:
                            currColor=random.choice(colors)
                            colors.remove(currColor)
                            exec("""ax%s = ax.twinx()"""%(y))
                            exec("""ax%s.plot(plot['price'][%s],color='%s')"""%(y,y,currColor))
                            exec("""ax%s.tick_params(axis='y', labelcolor='%s')"""%(y,currColor))

                # Generate a new Axes instance, on the twin-X axes (same position)

                # Plot exponential sequence, set scale to logarithmic and change tick color
            ##    ax2.plot(plot["price"][1], color='green')
            #    ax2.set_yscale('log')
            #    ax2.tick_params(axis='y', labelcolor='green')

        #        plt.plot(plot['Hours'],,)

                plt.savefig(str(iD)+'.png')
                plt.clf()
                #with open(str(iD)+'.png','r+',encoding="utf8") as filee:
                #    f=d
                await message.channel.send(file=discord.File(str(iD)+'.png'))
                os.remove(str(iD)+'.png')
            else:
                iD=random.randint(0,10000000)
                plot=crypto.drop_out(msg.split(' ')[1],msg.split(' ')[2])
                print(plot)
                plt.plot(plot['Hours'],plot['price'])
                plt.savefig(str(iD)+'.png')
                plt.clf()
                #with open(str(iD)+'.png','r+',encoding="utf8") as filee:
                #    f=d
                await message.channel.send(file=discord.File(str(iD)+'.png'))
                os.remove(str(iD)+'.png')
        if message.content.startswith('//.-. -- ....'):
            global gogo
            print('GO')
            gogo = await message.author.send('.')

            await asyncio.gather(hoho(),hehe(message))
        if message.content.startswith('//.-.'):
            userid= await message.channel.send(content = (message.author.id))
            USERID= message.author.id
            #userid=message.author.name
        for x in takon.split('\n'):
            if powerPoint==True:
                await message.channel.send(x)
                powerPoint=False
                return;
            if message.content==x:
                powerPoint=True

    #    gogos = await message.channel.send('f.')
    #    hohoT = Thread(target = hoho)
    #    await hohoT.start()
#client = discord.Client()
def setVariables():
    gogo=None
    atardecere = False

fsetVariables="""
gogo=None
atardecere = False
"""
#pretty sure this right here was just a dumb little thing i made that would take the song and sing along the lyrics with you
takon='''Couple shots from the bar
Stagger home at night, I called your cell number
When I slurred, you were so polite
I love your voice, but it feels so far away
I turned my ass around and found which way to walk today
Stumble to your door step, its raining: You wouldn't let me in
I said I wanna marry you, you stuttered like "let's be friends"
You're drunk, I'm drunk
I'm not, I said I was though rejection was as fun as getting bellied by a snub-nose
Uh-oh, another stain on the glass
Like I need another friend, that's a pain in the ass
But I ain't really mad, I'm drunk as hell and on your couch now
My head is on your thigh, I'm thinking about passing out now
I wake up, you're still there
I'm impaired, you've been there
You know me, you loathe me
Cause I'm gone and I'll see you later
I've gone away
I checked in, I checked out
I moved in, I wrecked house
Like who's he, I lose she
Now I'm gone and I'll see you later
But not today
And why am I just sitting in this dark room?
Your words could paint a picture like it's cartoons
And I'm the punchline when it comes to crunch time
Semester one will start soon
The pain doubles, hung over and foggy
And when I try to come over its probably kinda awkward
But the halo hungover is awfully suspicious
I'm off, she done did it to cross me, but fuck it
She don't want to talk about it
She don't want to talk about it
I can't run through it or dance, the suns brutal
My chance is all gone, the situation is all wrong
I wake up, you're still there
I'm impaired, you've been there
You know me, you loathe me
Cause I'm gone and I'll see you later
I've gone away
I checked in, I checked out
I moved in, I wrecked house
Like who's he, I lose she
Now I'm gone and I'll see you later
But not today
My head splittin'
Wide open
And its from sipping my potion
And life tends to kick divine motions
I feel my inner mind is hopeless
Nucleosis
I am one, I am mono, I am the solitude
I couldn't even write a rhyme or fucking swallow food
And bitch you had the fucking nerve to say that I didn't try
You scaled my whole world back
I would have died by your side
I'm not a violent guy
But shit, I threw a chair or two
Knife edge the chest
Now why you go and Ric Flair a dude
My head is still splittin'
Wide open
And its from s-s-s-s-sipping my potion
I wake up, you're still there
I'm impaired, you've been there
You know me, you loathe me
Cause I'm gone and I'll see you later
I've gone away
I checked in, I checked out
I moved in, I wrecked house
Like who's he, I lose she
Now I'm gone and I'll see you later
But not today


You move your lips
And knock me down
Hmm
I can't get up
Where are you now
Hmm
We both conceal emotions that we ain't supposed to feel
We open up new wounds
Before the old ones heal
It's cold as hell
I try to hide my broken self
But if we can't be real with one another, no one's real
Or maybe real is overrated
Let's not overthink, or debate it
Best avoid an altercation
I keep running from trouble that I've orchestrated
I was born distracted
You were born impatient
Despise this trite circus
Tracing my steps, I pace in tight circles
I don't see gray
You're great, and I'm worthless
You said we need to talk
I'm nervous
Damn
You move your lips
And knock me down
Hmm
I can't get up
Where are you now
Hmm
Where are you
I don't want to talk
Rather run away
Hide my face
But not today
Source: Musixmatch
Songwriters: Rav









'''
fhehe=r"""
async def hehe(uvvu):
    global atardecere

    xd= await uvvu.channel.history(limit=None).flatten()
    eh=dict()
    #await asyncio.sleep(5)
    atardecere=True

    mesayah=0
    BARKBARKBARK=""
    for x in xd:
      mesayah+=1
      print(x.content)
      BARKBARKBARK=( BARKBARKBARK + '{' + x.author.name + '} : ' + x.content+ ' \n')
      eh[str(mesayah)]={}
      eh[str(mesayah)][x.id]={}
      eh[str(mesayah)][x.id]['author']=x.author.name
      eh[str(mesayah)][x.id]['created']=str(x.created_at)
      eh[str(mesayah)][x.id]['edited']=str(x.edited_at)
      eh[str(mesayah)][x.id]['content']=x.content
    print(BARKBARKBARK)
    print(eh['1'])

    with open('file_path.json', 'w',encoding='utf-8') as file:
        file.write(json.dumps(eh))
    BARKBARKBARK=''
    for x in eh:
        BARKBARKBARK=BARKBARKBARK + str(eh[x]) + '\n'
        print(x)
    with open('file_pasth.txt', 'w',encoding='utf-8') as file:
        file.writelines(json.dumps(BARKBARKBARK))
    #await asyncio.sleep(3)
    gogo = await uvvu.author.send(content = uvvu.author.mention + " uvvu " + str(mesayah))

    #await gogo.edit(content = uvvu.author.mention + " uvvu " + str(mesayah))
"""
fhoho="""
async def hoho():
    global gogo
    print('GO')
    while atardecere=='xd':
            with Switch(gogo.content) as case:
                if case('.'):
                    await asyncio.sleep(0.5)
                    await gogo.edit(content = '..')
                if case('..'):
                    await asyncio.sleep(0.5)
                    await gogo.edit(content = '...')
                if case('...'):
                    await asyncio.sleep(0.5)
                    await gogo.edit(content = '.')
"""
pull="""
@client.event
async def on_message(message):
  if message.content.startswith('//.-. -- ....'):
    global gogo
    print('GO')
    gogo = await message.author.send('.')


    await asyncio.gather(hoho(),hehe(message))
  if message.content.startswith('//.-.'):
    userid= await message.channel.send(content = (message.author.id))
    USERID= message.author.id
        #userid=message.author.name

#    gogos = await message.channel.send('f.')
#    hohoT = Thread(target = hoho)
#    await hohoT.start()
"""
