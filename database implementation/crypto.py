import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='Gohsot',
    passwd='AscaxAnya!1313',
    database='cryptoBase'


)
import time
from datetime import datetime,timedelta,date
from matplotlib import pyplot as plt

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

#mycursor.execute('CREATE TABLE Coin (name VARCHAR(50), coinID int PRIMARY KEY AUTO_INCREMENT, price int, dailyRate int, weeklyRate int,marketCap int,dailyVolume int, circulatingSupply int)')
#mycursor.execute('INSERT INTO Coin(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply) VALUES (%s,%s,%s,%s,%s,%s,%s)', ('rowdy[0]',5,45,45,45,465,465))
#mycursor.execute("SELECT * FROM Coinbbbb")
mycursor = db.cursor()
def multi_drop_out(coins,type):
    price=list()
    Multi_prices=list()
    Hours=list()

    if type == '24h':
        currDay=datetime.today().strftime('%Y-%m-%d')
        yestDay=datetime.today().strftime('%Y %m %d')

        print(yestDay)
        yestDay=datetime.today().strftime('%Y %m ')+(str(int(datetime.today().strftime('%Y %m %d').split(' ')[2])-1))
        print(yestDay)
        patch=[]
        for x in coins:
            for y in x:
                patch.append(y)

        coinsUsed=[]
        for y in patch:

                #print(y)
                print('coins',y)
        #        input()
                mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date="%s" AND name="%s"'%(currDay,y))
                print(mycursor)
                #patch.remove(y)
                count=0
                secondaryHours=[]
                for z in mycursor:
                    print(y)
                    currX=str(z[0].split(':')[0])+':'+str(z[0].split(':')[1])
                    print(currX,'Corn')
                    #for l in x[0].split(':')[:1]:
                    if  currX not in Hours:
                        Hours.append(currX)
                        print(z)

                        print(z[1])
                        if y == 'Ethereum':
                            input()
                    #    input()
                        print(y)
                    #    input()
                        price.append(z[1])
                        print(Hours,price,y[1],currX,'x')
                        count+=1
                        secondaryHours.append(currX)

                    elif y not in coinsUsed and currX in Hours and currX not in secondaryHours:
                        count+=1
                        print(currX,'NO ME IMPORTA QUIEN SEA ELLLLLLLLLLLLLLLLLLLLL \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',secondaryHours)
                        #input()
                        secondaryHours.append(currX)
                        #print(currX,'\n\n\n\n\n\n\n\n\n\n')
                        print(Hours)
                    #    input()
                        price.append(z[1])
                        """
                    elif y in coinsUsed and y =='Ethereum':
                        print('A')
                        input()
                    elif currX not in Hours and y =='Ethereum':
                        print('A')
                        input()
                    elif currX  in secondaryHours and y =='Ethereum':
                        print('C')
                        input()
                        """
                coinsUsed.append(y)

                print(count)
            #    input()
                Multi_prices.append(price)
                price=[]
        plotPoints=dict()
    #    loui=list()
        #for x in Hours:
    #        loui.append(x)
        #print(Hours,price)
        print(Hours)
        print(Multi_prices,"hold up")
        plotPoints['Hours']=Hours
        plotPoints['price']=Multi_prices
    #    plt.clf()
        print('YO EXCUSEME THO WHATS???????')
        print(plotPoints,'apio')
        #print(plotPoints['hours'],)
        #plt.plot(plotPoints['Hours'],plotPoints['price'])
        #plt.show()
        return plotPoints
    elif type == '7d':
        currDay=datetime.today().strftime('%Y-%m-%d')
        currDay=[int(x) for x in currDay.split('-')]
        currDayRange=date(int(currDay[0]),int(currDay[1]),int(currDay[2]))
        yestDay=datetime.today().strftime('%Y %m %d')
        yestDate=[int(why) for why in yestDay.split(' ')]
#        yestDay=timedelta(7)-date(yestDate[0],yestDate[1],yestDate[2])
        print(yestDay)
        yestDay=datetime.today().strftime('%Y %m ')+(str(int(datetime.today().strftime('%Y %m %d').split(' ')[2])-7))
        print(yestDay)
        dateRange=date(int(yestDay.split(' ')[0]),int(yestDay.split(' ')[1]),int(yestDay.split(' ')[2]))
        print(dateRange)
        dayList=[]
        for dt in daterange(dateRange,currDayRange):
            dayList.append(''.join(dt.strftime("%Y %m %d").split(' ')[0]+'-'+dt.strftime("%Y %m %d").split(' ')[1]+'-'+dt.strftime("%Y %m %d").split(' ')[2]))
        print(dayList)
        #mycursor.execute('SELECT date FROM Coinbbbb WHERE name="%s" OR date="%s" AND name="%s"'%(coin,yestDay,coin))
        #for x in mycursor:
        #    print(x)
        #Hours=set()
        mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date IN %s AND name="%s" OR date="%s" AND name="%s"'%(tuple(dayList),coin,yestDay,coin))
        #print(mycursor)
        for x in mycursor:
            print(x)
            currX=str(x[0].split(':')[0])+':'+str(x[0].split(':')[1])
            #for l in x[0].split(':')[:1]:
            if  currX not in Hours:
                Hours.append(currX)
                price.append(x[1])
    #    mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date="%s" AND name="%s" OR date="%s" AND name="%s"'%(currDay,coin,yestDay,coin))
    #    for x in mycursor:
    #        print(x)
    #        if float(x[0]) not in price:
    #            price.append(float(x[0]))
        plotPoints=dict()
    #    loui=list()
        #for x in Hours:
    #        loui.append(x)
        print(Hours,price)
        plotPoints['Hours']=Hours
        plotPoints['price']=price
    #    plt.clf()
        print('YO EXCUSEME THO WHATS???????')
        print(plotPoints,'apio')
        #print(plotPoints['hours'],)
        #plt.plot(plotPoints['Hours'],plotPoints['price'])
        #plt.show()
        return plotPoints
def drop_out(coin,type):
    price=list()
    Hours=list()
    print('fuckingwhat')
    if type == '24h':
        currDay=datetime.today().strftime('%Y-%m-%d')
        yestDay=datetime.today().strftime('%Y %m %d')

        print(yestDay)
        yestDay=datetime.today().strftime('%Y %m ')+(str(int(datetime.today().strftime('%Y %m %d').split(' ')[2])-1))
        print(yestDay)
        #Hours=set()
        print('bust down for the gang')
        mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date="%s" AND name="%s" OR date="%s" AND name="%s"'%(currDay,coin,yestDay,coin))
        print(mycursor)
        for x in mycursor:
            print(x)
            currX=str(x[0].split(':')[0])+':'+str(x[0].split(':')[1])
            print(currX,'Corn')

            #for l in x[0].split(':')[:1]:
            if  currX not in Hours:
                Hours.append(currX)
                price.append(x[1])
                print(Hours,price,x[1],currX,'x')
        plotPoints=dict()
    #    loui=list()
        #for x in Hours:
    #        loui.append(x)
        print(Hours,price)
        plotPoints['Hours']=Hours
        plotPoints['price']=price
    #    plt.clf()
        print('YO EXCUSEME THO WHATS???????')
        print(plotPoints,'apio')
        #print(plotPoints['hours'],)
        #plt.plot(plotPoints['Hours'],plotPoints['price'])
        #plt.show()
        return plotPoints
    elif type == '7d':
        currDay=datetime.today().strftime('%Y-%m-%d')
        currDay=[int(x) for x in currDay.split('-')]
        currDayRange=date(int(currDay[0]),int(currDay[1]),int(currDay[2]))
        yestDay=datetime.today().strftime('%Y %m %d')
        yestDate=[int(why) for why in yestDay.split(' ')]
#        yestDay=timedelta(7)-date(yestDate[0],yestDate[1],yestDate[2])
        print(yestDay)
        yestDay=datetime.today().strftime('%Y %m ')+(str(int(datetime.today().strftime('%Y %m %d').split(' ')[2])-7))
        print(yestDay)
        dateRange=date(int(yestDay.split(' ')[0]),int(yestDay.split(' ')[1]),int(yestDay.split(' ')[2]))
        print(dateRange)
        dayList=[]
        for dt in daterange(dateRange,currDayRange):
            dayList.append(''.join(dt.strftime("%Y %m %d").split(' ')[0]+'-'+dt.strftime("%Y %m %d").split(' ')[1]+'-'+dt.strftime("%Y %m %d").split(' ')[2]))
        print(dayList)
        #mycursor.execute('SELECT date FROM Coinbbbb WHERE name="%s" OR date="%s" AND name="%s"'%(coin,yestDay,coin))
        #for x in mycursor:
        #    print(x)
        #Hours=set()
        mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date IN %s AND name="%s" OR date="%s" AND name="%s"'%(tuple(dayList),coin,yestDay,coin))
        #print(mycursor)
        for x in mycursor:
            print(x)
            currX=str(x[0].split(':')[0])+':'+str(x[0].split(':')[1])
            #for l in x[0].split(':')[:1]:
            if  currX not in Hours:
                Hours.append(currX)
                price.append(x[1])
    #    mycursor.execute('SELECT time,price FROM Coinbbbb WHERE date="%s" AND name="%s" OR date="%s" AND name="%s"'%(currDay,coin,yestDay,coin))
    #    for x in mycursor:
    #        print(x)
    #        if float(x[0]) not in price:
    #            price.append(float(x[0]))
        plotPoints=dict()
    #    loui=list()
        #for x in Hours:
    #        loui.append(x)
        print(Hours,price)
        plotPoints['Hours']=Hours
        plotPoints['price']=price
    #    plt.clf()
        print('YO EXCUSEME THO WHATS???????')
        print(plotPoints,'apio')
        #print(plotPoints['hours'],)
        #plt.plot(plotPoints['Hours'],plotPoints['price'])
        #plt.show()
        return plotPoints
        #bitch=mycursor.execute('SELECT * FROM Coinbbbb WHERE date="%s" AND name="%s" OR date="%s" AND name="%s"'%(currDay,coin,yestDay,coin))
        #return plt.plot(Hours,price)
        #plt.show()
    #    for x in bitch:
        #    print(x)
#drop_out('Bitcoin','24h')
#mycursor.execute('SELECT * FROM Coinbbbb WHERE date="%s" AND name="Bitcoin"'%(currDay))










#mycursor.execute("DESCRIBE Coin")
while False:

    mycursor.execute("SELECT * FROM Coinnnnnn")
    for x in mycursor:
        print(x,'f')
    time.sleep(3)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    mycursor.execute("SELECT * FROM Coinbbbb")
    for x in mycursor:
        for y in x:
            print(y)
        #print(x,'f')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(3)
    #clear()
