class car:
    car1=[["mer","A5","125","AV"],["Odi","Q8","140","Av"],["BMW","x10","160","Av"]]
class company(car):
    # constructor used to welecome 
    def __init__(self):
        for i in range(5):
            print("*",end=" ")
        print("welecome",end=" ")
        for i in range(5):
            print("*",end=" ")
        print()
    
    # function to add a car in the list  
    def addcar(self):
        self.car=input("Enter car name: ")
        self.model=input("Enter car model: ")
        self.rate=input("Enter the rate: ")
        self.status=input("Enter the status: ")
        self.car1.append([self.car,self.model,self.rate,self.status])

        
    # function to remove the car in list
    def removecar(self):
        self.car=input("Enter car name: ")
        self.model=input("Enter car model: ")
        for i in range(len(self.car1)):
            if(self.car1[i][0]==self.car and self.car1[i][1]==self.model):
                del self.car1[i]
        print(self.car1)
    
    # function to show the list of car
    def showthelist(self):
        print("Car\tModel\tRate\tStatus")
        for i in range(len(self.car1)):
            print(f"{self.car1[i][0]}\t{self.car1[i][1]}\t{self.car1[i][2]}\t{self.car1[i][3]}")

class user(company):
    # funtion to rent the car
    def carrent(self):
        self.car=input("Enter car name: ")
        self.model=input("Enter car model: ")
        flag=0
        rate=0
        for i in range(len(self.car1)):
            if self.car1[i][0]==self.car and self.car1[i][1]==self.model:
                if self.car1[i][3]=="Av":
                    self.car1[i][3]="Ren"
                    rate=int(self.car1[i][2])
                    flag=1
                    print("Succesfully rented")
                else:
                    print("Car is Already book")
        if flag==1:
            self.name=input("Enter the name: ")
            self.starting=input("Enter the starting point: ")
            self.destination=input("Enter the destination: ")
            self.Distance=int(input("Enter the total distance: "))
            self.getrecipt(self.car,self.model,self.name,self.starting,self.destination,self.Distance,rate)
    
    # funtion to return the car
    def returncar(self):
        self.car=input("Enter car name: ")
        self.model=input("Enter car model: ")
        for i in range(len(self.car1)):
            if self.car1[i][0]==self.car and self.car1[i][1]==self.model:
                if self.car1[i][3]=="Ren":
                    self.car1[i][3]="Av"
                    print("Succesfully return")
    
    # funtion for user
    def getuser(self):
        ch='y'
        while(ch=='y'):
            opt1=int(input("1: Car rent\t2: Return car\t3: Exit\n"))
            if(opt1==1):
                self.carrent()
            elif(opt1==2):
                self.returncar()
            else:
                break
    
    # funtion for company
    def getcomp(self):
        ch='y'
        while(ch=='y'):
            opt2=int(input("1: Add car\t2: Remove car\t3: Show the list\t4: Exit\n"))
            if(opt2==1):
                self.addcar()
            elif(opt2==2):
                self.removecar()
            elif(opt2==3):
                self.showthelist()
            else:
                break
    # funtion to get a recipt
    def getrecipt(self,car,model,name,starting,destination,Distance,rate):
        with open("Bill","a") as f:
            data=f"\n\nNEW RECORD\nCar Name:-{car}\nCar Model:-{model}\nName:-{name}\nSarting point:-{starting}\nDestination:-{destination}\nDistance:-{Distance}\nTotal Price:-{rate*Distance}"
            f.write(data)
            print(data)
    
    
        
    
c1=user()
ch='y'

while(ch=='y'):
    opt=int(input("1: user\t2: company\t3: Exit\n"))
    if(opt==1):
        c1.getuser()
    elif(opt==2):
        c1.getcomp()
    else:
        break

