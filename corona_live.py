from bs4 import BeautifulSoup #must have pip install bs4
import requests #must have pip install requests
import time
from tkinter import * #must have pip install tkinter
from tkinter import messagebox as tkMessageBox

html_text= requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(html_text,"html.parser")


def dis_corona_world():# funcution for filter data from http for display
    global st,nu
    try:
        par = soup.find_all('div',id="maincounter-wrap")
    except:
        return "some error with source"
    st =[]
    nu=[]
    for ind,i in enumerate(par):
        st.append(i.find('h1').text)
        nu.append(i.find('span').text)
        #print(st[ind],nu[ind])
    return st,nu

def dis():
    root = Tk()
    root.title("Corona data display")
    
    canvas = Canvas(root,height=350,width=600,bg = '#263D42')
    canvas.pack()

    frame = Frame(root,bg='white')
    frame.place(relwidth= 0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    t=[]
    def data(): # display data from above function
        Label(frame,text="Statistics of Corona - LIVE",font=('Helvetica',20),anchor='n',bg='grey').pack(fill='both')
        for i in range(len(st)):
            t.append((st[i],nu[i]))
        for i in range(len(st)):
            Label(frame,text=t[i],font=('bold',20),padx=20,pady=10, anchor='w',bg='white').pack(fill='both')
    
    data() # refresh button function 
    def helloCallBack():
       tkMessageBox.showinfo( "Request refresh", "Refresh Data")
       for widget in frame.winfo_children():
            widget.destroy()
       dis_corona_world()
       data()

    B = Button(root, text ="Refresh",fg='blue', command = helloCallBack)
    B.place(x=295, y=270)
    root.mainloop()


if __name__ == '__main__':
    dis_corona_world()
    dis()
    time.sleep(1)
    #time_wait =10
    #print(f'Wating for {time_wait} seconds...')
    #time.sleep(time_wait*6)


