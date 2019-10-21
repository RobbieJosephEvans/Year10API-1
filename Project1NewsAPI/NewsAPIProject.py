import requests
from tkinter import *
from PIL import ImageTk, Image

def getinfo():
    #myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6b01c9faa902470ea4b65e0aa70768d5") <-- not needed, just wastes time
    global datajson
    entry = variable.get()
    #datajson = myrequest.json() #turns myrequests (which is in binary) into a json file
    ofile = open("NewsAPI.html","a")
    '''
        if entry == "Unknown Author":
        ofile.write("<h4>" + "<u>" + "Unknown Author" + "</u>" + "</h4>")
        ofile.write("<p>" + "Publication:" + "</p>")
        print("Unknown Author")
        ofile.write("<a href='" + datajson["articles"][i]["url"] + "' target='_blank'>Link to page</a>")
        ofile.write("<p>" + "_____________________________________________________________________________" + "<br>" + "<br>" + "</p>")
'''
    
    for i in range(len(datajson["articles"])): #loops through al articles in JSON
        if entry == (datajson["articles"][i]["author"]):
            title = datajson["articles"][i]["title"]
            ofile = open("NewsAPI.html","w")
            ofile.write("<h1>" + "Nuntium" + "</h1>")
            ofile.write("<h2>" + "Search Through the Latest News with Nuntium!" + "</h2>")
            ofile.write("<p>" + "_____________________________________________________________________________" + "</p>")
            ofile.write("<h4>" + "<u>" + datajson["articles"][i]["author"] + "</u>" + "</h4>")
            ofile.write("<p>" + "Publications by this author:" + "</p>")
            print(datajson["articles"][i]["url"])
            ofile.write("<h5>" + datajson["articles"][i]["title"] + "<h5>")
            ofile.write("<a href='" + datajson["articles"][i]["url"] + "' target='_blank'>Link to site</a>")
            ofile.write("<p>" + "_____________________________________________________________________________" + "<br>" + "<br>" + "</p>")
        elif entry == "Unknown Author: " + datajson["articles"][i]["title"]:
            ofile = open("NewsAPI.html","w")
            ofile.write("<h1>" + "Nuntium" + "</h1>")
            ofile.write("<h2>" + "Search Through the Latest News with Nuntium!" + "</h2>")
            ofile.write("<p>" + "_____________________________________________________________________________" + "</p>")
          #  ofile.close()
            ofile.write("<h4>" + "<u>" + "Unknown Author" + "</u>" + "</h4>")
            ofile.write("<p>" + "Publications by this author:" + "</p>")
            ofile.write("<h5>" + datajson["articles"][i]["title"] + "<h5>")
            print("worked")
            ofile.write("<a href='" + datajson["articles"][i]["url"] + "' target='_blank'>Link to page</a>")
            ofile.write("<p>" + "_____________________________________________________________________________" + "<br>" + "<br>" + "</p>")

'''
        listauthor = ["1","2","3","4","5"]
        stringlist = str(listauthor)
        if entry == "Unknown Author "+ stringlist[i]:
            ofile.write("<h4>" + "<u>" + "Unknown Author" + "</u>" + "</h4>")
            ofile.write("<p>" + "Publication:" + "</p>")
            print(entry)
            ofile.write("<a href='" + datajson["articles"][i]["url"] + "' target='_blank'>Link to page</a>")
            ofile.write("<p>" + "_____________________________________________________________________________" + "<br>" + "<br>" + "</p>")
    '''
            
'''
        else:
            ofile = open("NewsAPI.html","a")
            ofile.write("<h7>" + "This author has not written anything yet" + "<h7>")
    '''

#def goback():
    

def opennew():
    window2 = Tk()
    titleInfoAuthor = Label(window2, text = "Nuntium")
    titleInfoAuthor.configure(font=("Times New Roman", 16, "bold"))
    titleInfoAuthor.grid(column = 0, row = 0)

    infoAuthorQuestion = Label(window2, text = 'What do we do? How does "Search by Author" work?')
    infoAuthorQuestion.configure(font=("Times New Roman", 16, "bold"))
    infoAuthorQuestion.grid(column = 0, row = 1)
    
    infoAboutAuthor = Label(window2, text = "Nuntium searches through the latest Wall Street Journal news. " +
    "Every day, most recent publications, ranging from sports to politics, change. " +
    "Use the drop-down" +
    " to browse through all of the authors who have published today, and select one to view their articles. If the author is unknown, " +
    "the title of the article will be displayed", wraplength=500, justify=LEFT)
    infoAboutAuthor.configure(font=("Times New Roman", 14))
    infoAboutAuthor.grid(column = 0, row = 2)

    terminateInfoAuthor = Button(window2, text = "Back", command = window2.destroy)
    terminateInfoAuthor.grid(column = 0, row = 3)

    
#____________________________________________________________________________________

def getauthor(*args):
    print(variable.get())

   


window1 = Tk()

myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6b01c9faa902470ea4b65e0aa70768d5")
datajson = myrequest.json()

x = " "

spaceframe = Frame(window1,height=10)
spaceframe.grid(column = 0, row = 4)
frame = Frame(window1,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.grid(column = 0, row = 4)
spaceframe = Frame(window1,height=10)
spaceframe.grid(column = 0, row = 4)


pageTitle = Label(window1, text = x*15 + "Search Through the Latest News with Nuntium!" + x*15)
pageTitle.configure(font=("Times New Roman", 16, "bold"))
pageTitle.grid(column = 0, row = 0)

authorTitle = Label(spaceframe, text = "Search for publication by author")
authorTitle.configure(font=("Times New Roman", 14))
authorTitle.grid(column = 0, row = 1)

authorInfo = Button(spaceframe, text = "ⓘ", command = opennew)
authorInfo.grid(column = 1, row = 1)

myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6b01c9faa902470ea4b65e0aa70768d5")

datajson = myrequest.json()

#___________________________________________________________________________
OPTIONS = ["Authors Today:"]


for i in range(len(datajson["articles"])):
    numberofnulls = 0
    if datajson["articles"][i]["author"] is None:
        if len(datajson["articles"][i]["title"]) > 10:
            OPTIONS.append("Unknown Author: " + datajson["articles"][i]["title"][0:25] + "...")
    else:
        OPTIONS.append(datajson["articles"][i]["author"])

'''
        nullauthor = numberofnulls+1
        for s in range(nullauthor):
            global c
            c = str(s+1)
            global unknownAuthor1
            unknownAuthor1 = ("Unknown Author " + c)
            OPTIONS.append("Unknown Author " + c)
'''

  

variable = StringVar(authorInfo)
variable.set(OPTIONS[0]) # default value


w = OptionMenu(spaceframe, variable, *OPTIONS, command = getauthor)
w.config(font=("Times New Roman", 14))
w.grid(column = 0, row = 2)


submit1 = Button(spaceframe, text = "Submit", command = getinfo)
submit1.place(anchor=CENTER)
submit1.configure(font=("Times New Roman", 14))
submit1.grid(column = 0, row = 3)


#_______________________________________________________________________________

newline = Label(window1, text = "")
newline.configure(font=("Times New Roman", 16, "bold"))
newline.grid(column = 0, row = 5)


spaceframe = Frame(window1,height=10)
spaceframe.grid(column = 0, row = 6)
frame = Frame(window1,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.grid(column = 0, row = 6)
spaceframe = Frame(window1,height=10)
spaceframe.grid(column = 0, row = 6)

keywordTitle = Label(spaceframe, text = "Search for publication by keyword")
keywordTitle.configure(font=("Times New Roman", 14))
keywordTitle.grid(column = 0, row = 7)

keywordDrop = Entry(spaceframe)
keywordDrop.configure(font=("Times New Roman", 14))
keywordDrop.grid(column = 0, row = 8)

submit2 = Button(spaceframe, text = "Submit", command = getinfo)
submit2.configure(font=("Times New Roman", 14))
submit2.grid(column = 0, row = 9)


#__________________________________________________________________________________



#def click():
 #   entered_text = entry.get()

newsImage1 = ImageTk.PhotoImage(Image.open("newsImage1.png"))
newsImage = Label(window1, image = newsImage1)
newsImage.grid(column = 0, row = 7)


window1.mainloop()
