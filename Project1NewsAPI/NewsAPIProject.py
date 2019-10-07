import requests
from tkinter import *

def getinfo():
    myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6b01c9faa902470ea4b65e0aa70768d5")
    entry = authorEnter.get()
    datajson = myrequest.json() #turns myrequests (which is in binary) into a json file
    ofile = open("NewsAPI.html","a")
    for i in range(len(datajson["articles"])): #loops through al articles in JSON
        if entry == (datajson["articles"][i]["author"]):
            ofile.write("<h4>" + "<u>" + datajson["articles"][i]["author"] + "</u>" + "</h4>")
            ofile.write("<p>" + "Publications by this author:" + "</p>")
            print(datajson["articles"][i]["url"])
            ofile.write("<a href=" + datajson["articles"][i]["url"])
            ofile.write("<p>" + "_____________________________________________________________________________" + "<br>" + "<br>" + "</p>")
            
'''
        else:
            ofile = open("NewsAPI.html","a")
            ofile.write("<h7>" + "This author has not written anything yet" + "<h7>")
    '''
ofile = open("NewsAPI.html","w")
ofile.write("<h1>" + "Nuntium" + "</h1>")
ofile.write("<h2>" + "Search Through the Latest News with Nuntium!" + "</h2>")
ofile.write("<p>" + "_____________________________________________________________________________" + "</p>")
ofile.close()


window1 = Tk()

authorEnter = Entry(window1)
authorEnter.config()
authorEnter.grid(column = 0, row = 1)

submit1 = Button(window1, text = "Submit", command = getinfo)
submit1.config()
submit1.grid(column = 0, row = 2)

authorTitle = Label(window1, text = "Search for an author's publications")
authorTitle.grid(column = 0, row = 0)

    



