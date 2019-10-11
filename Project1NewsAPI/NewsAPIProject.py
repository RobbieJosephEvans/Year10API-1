import requests
from tkinter import *
#from PIL import ImageTk, Image

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
            ofile.write("<a href='" + datajson["articles"][i]["url"] + "' target='_blank'>Link to page</a>")
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

authorEnter = Entry(spaceframe)
authorEnter.configure(font=("Times New Roman", 14))
authorEnter.grid(column = 0, row = 2)

submit1 = Button(spaceframe, text = "Submit", command = getinfo)
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

keywordEnter = Entry(spaceframe)
keywordEnter.configure(font=("Times New Roman", 14))
keywordEnter.grid(column = 0, row = 8)

submit2 = Button(spaceframe, text = "Submit", command = getinfo)
submit2.configure(font=("Times New Roman", 14))
submit2.grid(column = 0, row = 9)


#__________________________________________________________________________________

myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6b01c9faa902470ea4b65e0aa70768d5")
datajson = myrequest.json()

OPTIONS = ["Scroll through authors"]




for i in range(len(datajson["articles"])):
    if datajson["articles"][i]["author"] is None:
        OPTIONS.append("Unknown Author")
    else:
        OPTIONS.append(datajson["articles"][i]["author"])
  

variable = StringVar(window1)
variable.set(OPTIONS[0]) # default value


w = OptionMenu(window1, variable, *OPTIONS)
w.config(font=("Times New Roman", 14))
w.grid(column = 0, row = 10)

#def click():
 #   entered_text = entry.get()

'''
path = Image.open("newsImage1.png")
newsImage1 = ImageTk.PhotoImage(path)
newsImage = tk.Label(root, image = newsImage1)
newsImage.pack(side = "bottom", fill = "both", expand = "yes")
'''

window1.mainloop()
