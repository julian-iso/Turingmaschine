import tkinter as tk

global band
band = []

global table
table = [[]]

global bandIndex 
bandIndex = 0

global tableIndex
tableIndex = 0

global tableLength
tableLength = 0

global state
state = 1

global pointer
pointer = 0

def fillBand(length):
    global band
    for i in range(0, length):  
        band.append("#")  

fillBand(50)
   
class GUI(tk.Frame):
   
   def __init__(self, parent):
      super(GUI, self).__init__(parent)
      self.parent = parent
      parent.title("Turing")
      parent.geometry("600x475")
      parent.configure(bg="#36393F")


      #StartButton
      bandLeft = tk.Button(parent,fg="black", bg="#43B581",font= 50, text = "Start", command=self.start)
      bandLeft.place(x = 50, y = 125, width = 250, height = 50)

      #Pointer
      self.pointer = tk.Label(parent, bg="#F04747", font=50, text="V")
      self.pointer.place(x =50-bandIndex, y =0, width=50 , height = 25) #index angezeigter Feld - links rechts 

      #Second Pointer
      self.secondPointer = tk.Label(parent, bg="#F04747", font=50, text="Ʌ")
      self.secondPointer.place(x =50, y =75, width=50 , height = 25) 

      #state Pointer
      self.statePointer = tk.Label(parent, bg="#FAA61A", font=50, text="V")
      self.statePointer.place(x =100, y =200, width=50 , height = 25) 
      
      #Band
      bandLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136",font= 50, text = "<", command=self.bandBack)
      bandLeft.place(x = 0, y = 25, width = 50, height = 50)

      self.arr = []
      for i in range (10):
         element = tk.Entry(parent)
         element.place(x=i*50 + 50, y=25, width=50, height=50)
         self.arr.append(element)
      
      bandRight = tk.Button(parent,fg="#ffffff", bg="#2F3136",font= 50, text = ">", command=self.bandForward)
      bandRight.place(x = 550, y = 25, width = 50, height = 50)


      #Table
      self.table = []

      th = ["Q", "L", "S", "B", "Q'"]
      for j in range(5):
         element = tk.Label(self.parent, text=th[j])
         element.place(x=50, y=j*50 + 225 , width=50, height=50)
         element.config(bg="#7289D9", font= 60) ##FAA61A orange #7289D9

      self.addCol = tk.Button(parent, bg="#7289D9", font= 50, text = "Add", command=self.add)
      self.addCol.place(x = 300, y = 125, width = 250, height = 50)
      self.add()
      
      tableLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text="<", command=self.tableLeft)
      tableLeft.place(x = 0, y = 225, width = 50, height = 250)
      
      tableRight = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text=">", command=self.tableRight)
      tableRight.place(x = 550, y = 225, width = 50, height = 250)

      self.update()

   def update(self): 
      global band, bandIndex
      for i in range(10):
         self.arr[i].delete(0, tk.END)
         self.arr[i].insert(0, band[i + bandIndex])
      if (50 - 50 * bandIndex >= 0 and 50 - 50 * bandIndex <= 550):
         self.pointer.place(x = 50 - 50 * bandIndex, y =0, width=50 , height = 25) #index angezeigter Feld - links rechts 
         self.secondPointer.place(x = 50 - 50 * bandIndex, y =75, width=50 , height = 25)

   def start(self):
      print("start")
      run()

   def add(self):
      global tableLength
      tableLength += 1
      if (tableLength < 10):
         tableElement = []
         for j in range(5):
            element = tk.Entry(self.parent)
            element.place(x=tableLength*50 + 50, y=j*50 + 225 , width=50, height=50)
            tableElement.append(element)
         self.table.append(element)

   def bandForward(self):
      global bandIndex
      self.mapBand()
      bandIndex += 1
      self.update()

   def bandBack(self):
      global bandIndex
      self.mapBand()
      bandIndex -= 1
      self.update()

   #deprecated
   def tableLeft(self):
      print()

   #deprecated
   def tableRight(self):
      global table, tableIndex
      self.mapTable()
      for x in range(10 if tableIndex >= 10 else tableIndex + 1):
         for y in range(5):
            self.table[x][y].delete()
            self.table[x][y].insert(0, table[x - tableIndex][y])

   #deprecated
   def mapTable(self):
      global table, tableLength
      table = []
      for x in range(tableLength + 1):
         arr = []
         for y in range(5):
            a = self.table[x][y].get()
            print(a)
            arr.append(a)
         table.append(arr)


   def mapBand(self):
      global band, bandIndex
      for i in range(10):
         value = self.arr[i].get()
         band[bandIndex + i] =  value if len(value) > 0 else "#"
         





#Backend
def appendLeft(self):
    global band, pointer
    self.band.insert(0, "#")  # das band wird links um eine stelle erweitert
    self.pointer += 1

def appendRight():
    global band
    band.append("#")  # das band wird rehts um eine stelle erweitert

def nextStep():
    global table, state, pointer, band
    for column in table:  # gehe jede spalte durch
        if column[0] == state:  # wenn der aktuelle zustand stimmt
            if column[1] == band[pointer]:  # wenn man das richtige liest
                band[pointer] = column[2]  # ersetzte mit dem schreibe element
                move = 1 if column[3] == "R" else -1
                pointer += move  # ändere den Pointer entsprechend der richtung
                if move == 1 and pointer >= len(band):
                    appendRight()
                elif move == -1 and pointer < 0:
                    appendLeft()
                state = column[4]  # setzte den neuen state
                return True
    return False



root = tk.Tk()
GUI(root)
root.mainloop()

   
def run():     
   nextStep()
   root.after(1000, func=run)