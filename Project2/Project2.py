#  File: Project2.py
#  Description: 

#
#  Date Created: 4/29 08:45PM
#  Date Last Modified: 5/6 05:30PM

class Room:

    def __init__(self,name,north,east,south,west,up,down,contents):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.contents = contents #lists of items

    def displayRoom(self):

        print(format("Room name:","12s") + str(self.name))
        
        if self.north != None:
            print(format("   Room to the north:","23s") + self.north)
        if self.east != None:
            print(format("   Room to the east:","23s") + self.east)
        if self.south != None:
            print(format("   Room to the south:","23s") + self.south)
        if self.west != None:
            print(format("   Room to the west:","23s") + self.west)
        if self.up != None:
            print(format("   Room above:","23s") + self.up)
        if self.down != None:
            print(format("   Room below:","23s") + self.down)
            
        if self.contents != []:
            print(format("   Room contents:","23s") + str(self.contents))
            
        else:
            print(format("   Room contents:","23s") + "[]")
            
            
        print()     

def createRoom(roomData):
    
    if len(roomData) == 7: #no contents
        templist = []
        roomData.append(templist)

    elif len(roomData) == 8: #one item
        templist = [roomData[7]]
        roomData.remove(roomData[7])
        roomData.append(templist)

    else: #multiple items
        templist = []
        for i in range(7,len(roomData)):
            templist.append(roomData[i])
            
        for i in range(len(roomData)-1,6,-1):
            roomData.remove(roomData[i])
            
        roomData.append(templist)
            
    newRoom = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6],roomData[7])

    return newRoom

def look():
    
        print("You are currently in the",current.name)
        print("Contents of the room:")

        if current.contents != []:
            for i in range(0,len(current.contents)):
                print("    " + str(current.contents[i]))
        else:
            print("    " + "None")
            

def getRoom(name):

    for i in range(0, len(floorPlan)):
        if name == floorPlan[i].name:
            return floorPlan[i]
        else:
            continue
        
def move(direction):

    newRoom = current

     
    if direction == "north":
        
        newRoom = getRoom(current.north)
        
        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
        else:
            print("You are now in the " + newRoom.name)


    elif direction == "east":
        
        newRoom = getRoom(current.east)

        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
            
        else:
            print("You are now in the " + newRoom.name)

    elif direction == "south":
        newRoom = getRoom(current.south)
        
        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
            
        else:
            print("You are now in the " + newRoom.name)
        
    elif direction == "west":
        newRoom = getRoom(current.west)
        

        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
            
        else:
            print("You are now in the " + newRoom.name)

    elif direction == "up":
        newRoom = getRoom(current.up)
        

        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
            
        else:
            print("You are now in the " + newRoom.name)

    elif direction == "down":
        newRoom = getRoom(current.down)

        if newRoom == None:
            print("You can't move in that direction.")
            newRoom = current
            
        else:
            print("You are now in the " + newRoom.name)

    return newRoom

def pickup(item):

    if item in current.contents:
        inventory.append(item)
        current.contents.remove(item) 
        print("You now have the " + item)
        
    else:
        print("That item is not in this room.")

def drop(item):

    if item in inventory:
        current.contents.append(item)
        inventory.remove(item) 
        print("You have dropped the " + item)
        
    else:
        print("You don't have that item.")

def listInventory():

    if len(inventory) == 0:
        print("You are currently carrying:")
        print("    " + "nothing" )

    else:
        print("You are currently carrying:")
        for i in range (0, len(inventory)):
            print("    " + inventory[i])
    

def displayAllRooms():

    for i in range (0, len(floorPlan)):
        floorPlan[i].displayRoom()
        
        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable

    floorPlan = []
    nameFile = open("ProjectData.txt","r")
    
    line = nameFile.readline() #get line
    while line != "":

        fileLine = line.replace("\n","")
        roomList = [eval(x) for x in fileLine.split(",")]
        newRoom = createRoom(roomList)
        floorPlan.append(newRoom)

        line = nameFile.readline()
    

    nameFile.close()

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()

    displayAllRooms()

    current = floorPlan[0] 

    global inventory # global variable, list of the items the player is carrying

    inventory = []

    look()
    print()

    command = input("Enter a command: ")
    
    while command != "exit":

        if command == "help":
            print(format("look:","13s")+"display the name of the current room and its contents")
            print(format("north:","13s") + "move north")
            print(format("east:","13s") + "move east")
            print(format("south:","13s") + "move south")
            print(format("west:","13s") + "move west")
            print(format("up:","13s") + "move up")
            print(format("down:","13s") + "move down")
            print(format("inventory:","13s") + "list what items you're currently carrying")
            print(format("get <item>:","13s") + "pick up an item currently in the room")
            print(format("drop <item>:","13s") + "drop an item you're currently carrying")
            print(format("help:","13s") + "print this list")
            print(format("exit:","13s") + "quit the game")
            print()

            command = input("Enter a command: ")
            
        elif command == "north":
            current = move("north")
            print()
            command = input("Enter a command: ")

        elif command == "east":
            current = move("east")
            print()
            command = input("Enter a command: ")

        elif command == "south":
            current = move("south")
            print()
            command = input("Enter a command: ")

        elif command == "west":
            current = move("west")
            print()
            command = input("Enter a command: ")

        elif command == "up":
            current = move("up")
            print()
            command = input("Enter a command: ")

        elif command == "down":
            current = move("down")
            print()
            command = input("Enter a command: ")

        elif command == "look":
            look()
            print()
            command = input("Enter a command: ")

        elif command == "inventory":
            listInventory()
            print()
            command = input("Enter a command: ")

        elif "get" in command :
            splitCommand = command.split()
            item = splitCommand[len(splitCommand)-1]
            pickup(item)

            print()
            command = input("Enter a command: ")

        elif "drop" in command :
            splitCommand = command.split()
            item = splitCommand[len(splitCommand)-1]
            drop(item)
            
            print()
            command = input("Enter a command: ")

        else:
            print("I don't recognize that command.")
            print("Type in help to see what commands are available.")

            print()
            command = input("Enter a command: ")
            
      
            
    print("Quitting game.")
        

main()
