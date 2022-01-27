from bs4 import BeautifulSoup
import urllib.request
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import itertools
import mysql.connector
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

#start the database//change according to your own credentials
def database_connect(hst,usr,passwrd,dtbs):
    global db
    db = mysql.connector.connect(
        host=hst,
        user=usr,
        passwd=passwrd,
        database=dtbs


    )

def split(word):
    return [char for char in word]
mycursor = db.cursor(buffered=True)
#create the tables if non existant//should create a way to check if they exist//however at the time I was not taking the translation of this code into another database in mind
#mycursor.execute('CREATE TABLE Coinnnnnn (name VARCHAR(50) PRIMARY KEY, price float, dailyRate float, weeklyRate float,marketCap BIGINT,dailyVolume float, circulatingSupply float, date VARCHAR(50), time VARCHAR(50))')
#mycursor.execute('CREATE TABLE Coinbbbb (name VARCHAR(50), coinID int PRIMARY KEY AUTO_INCREMENT, price float, dailyRate float, weeklyRate float,marketCap BIGINT,dailyVolume BIGINT, circulatingSupply BIGINT, date VARCHAR(50), time VARCHAR(50))')
mycursor.execute("DESCRIBE Coin")
opts = Options()
opts.add_argument(" --headless")
#enter the desired url//due to the nature of coinmarketcap and the way it was created dynamically this scraper might not work with other services
item = str('https://coinmarketcap.com/homepage-v21/')
#initialize the virtual browser
driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.get(item)
#zoom out in order to load all of the content
driver.execute_script("document.body.style.zoom='5%'")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
#main scraper
def main_scraper():
    global driver
    #get the html off the website
    page = driver.execute_script('return document.body.innerHTML')
    #list of words not desired when I scrape the information out
    nonoWords=('#','Name','Price','24h %','7d %','Market Cap','Volume(24h)','Circulating Supply', 'Last 7 Days','')

    rowdy=[]
    counter=0
    soup = BeautifulSoup(''.join(driver.page_source), 'html.parser')
    shenanigans=dict()
    itemss=0
    #iterate through every single "tr" element inside the html//this is where these are all coins are stored
    for x in soup.find_all('tr'):
        #print(len(x))
        #print(x[0])

        #print(type(x))
        #print(x.text)
        lists=list()
        for y in x:
            lists.append(y.text)
        #print(lists)
        for y in lists:
            #make sure the line that is being iterated through doesnt contain any of the illegal characters which we dont want
            if y.strip() not in nonoWords:
                #print(y)
                try:

                    int(y)+int(y)
                    rowdy=[]

                    counter=0
                except:
                    #a bunch of counter checks in order to see where in the data we currently are and taking steps in order to format it appropiately
                    if counter==0:
                        for q in y:
                            if q.isdigit():
                                digit=str(q)
                                print(q)
                                break

                        print(y.split(q)[0],'go home')
                        counter+=1
                        rowdy.append(y.split(q)[0])
                    elif counter in range(1,4):
                        #take every single string and what ever the number is replace any rouge characters with nothing so that we can convert it into a int type variable instead of a string

                        rowdy.append(y.replace('%','').replace('%','').replace('$','').replace(',',''))
                        counter+=1
                    elif counter==4:
                    #    print('what? \n',y)
                    #    print('gmc',y.split('$')[2])
                        rowdy.append(y.split('$')[2].replace(',',''))
                        counter+=1
                        theSplit=0
                    elif counter in range(5,8):
                        print(y,'radish')

                        for k in y.split(','):
                            print(k,'carrots')

                            if len(k.replace('$',''))>3 and theSplit==0:
                            #    print(k.split()[isdigit()],k.split(),'apples')
                                theSplit=''.join(split(k)[:3])
                                print(theSplit,'cucumbers')
                                #                            theSplit=''.join(split(k)[:3])

                                #    print(y.split(theSplit)[0],theSplit,'cucumbers',y.split(theSplit)[1])
                                rowdy.append(y.split(theSplit)[0].replace('$','').replace(',','').strip()+theSplit)
                                rowdy.append(y.split(theSplit)[1].split(' ')[0].replace('$','').replace(',','').strip())
                                #after all of this the data will be properly formated and printed out in a neatly matter ready to be inserted into our database
                                print(rowdy)
                        print(rowdy,'cavendish')
                        #print('cavish',len(rowdy))
                        counter+=1
                        if counter==7:
                            try:
                                print(rowdy[0],'Corn')
                                #insert the data into a table inside of sql by using the integrated %s method instead of the insecure string formatting
                                mycursor.execute('INSERT INTO Coinnnnnn(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply,date,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (rowdy[0],rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6],datetime.today().strftime('%Y-%m-%d'),datetime.today().strftime('%H:%M:%S')))
                                #mycursor.execute('INSERT INTO Coinbbbb(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply,date, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (rowdy[0],rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6],datetime.today().strftime('%Y-%m-%d'),datetime.today().strftime('%H:%M:%S')))
                                #mycursor.execute('INSERT INTO Coinb(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply) VALUES (%s,%s,%s,%s,%s,%s,%s)', (rowdy[0],rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6]))
                                #commit the changes
                                db.commit()
                            except:
                                #in some conditions the previous statement will throw an error and instead of saying insert we should say update/set
                                print(rowdy[0],'Corn')
                                mycursor.execute('UPDATE Coinnnnnn SET price=%s,dailyRate=%s,weeklyRate=%s,marketCap=%s,dailyVolume=%s,circulatingSupply=%s,date=%s,time=%s WHERE name=%s ', (rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6],datetime.today().strftime('%Y-%m-%d'),datetime.today().strftime('%H:%M:%S'),rowdy[0]))
                                #mycursor.execute('INSERT INTO Coinbbbb(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply,date,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (rowdy[0],rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6],datetime.today().strftime('%Y-%m-%d'),datetime.today().strftime('%H:%M:%S')))
                                db.commit()


                    #    dropti


                        #mycursor.execute("INSERT INTO Coin")
                #    print(counter,'counter')
    #mycursor.execute('INSERT INTO Coinnnnn(name,price,dailyRate,weeklyRate,marketCap,dailyVolume,circulatingSupply) VALUES (%s,%s,%s,%s,%s,%s,%s)', (rowdy[0],rowdy[1],rowdy[2],rowdy[3],rowdy[4],rowdy[5],rowdy[6]))

    for x in mycursor:
        print(x)
                        #print(y)
    #print(rowdy)
                #    print(y)

if __name__=="__main__":
    while True:
        database_connect('localhost','Gohsot','AscaxAnya!1313','cryptoBase')
        main_scraper()
        time.sleep(2)
