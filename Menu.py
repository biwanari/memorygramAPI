class Menu:

    def __init__(self):
        self.menuOption = []
        self.menuOptionName = []

    def addOptionAndName(self, parameterOption,parameterOptionname):
        """
        add option to list menu in terminal
        """
        self.menuOption.append(parameterOption)
        self.menuOptionName.append(parameterOptionname)
    
#    def generateMenu(self):
#        flag = True
#        while(flag):
#            for i,j in zip(menuOption,menuOptionName):
#                print(f"{i}) {j}")
    def generateMenu(self):
        flag = True
        
        while(flag):
            for i, j in enumerate(self.menuOptionName):
                print(f"{i}) {j}")
            print("\n")
            command = input("Digit command> ")    
            
            if command == "Q":
                flag = False
            else:
                print("Exception Command not found,  try another command or quit program")
                print("\n")


##all method and defines works!
#minstance = Menu()

#minstance.addOptionAndName("profile","profilehack")

#minstance.addOptionAndName("hashtag","hashtagGeoLocalization")

#minstance.addOptionAndName("quit","quit memorygram api || digit Q to exit")

#minstance.generateMenu()