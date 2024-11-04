class Student:
    university="Queen Mary" # class variable - see below
    
    def __init__(self, name, surname): # constructor
        self.name=name # self.name is an attribute, name is the parameter
        self.surname=surname 
        self._printaccount=0.0

    def __str__(self):
        s="Name: " + self.name+ " "+ self.surname+"\n"
        s+="Print credit: " + str(self._printaccount)
        return s
        
    def buyPrintCredit(self, amount): # method with a parameter
        self._printaccount+=amount
        
    def canPrint(self): # method that returns a value.
        return self._printaccount>0


class BScStudent(Student): # inherit from Student
    """ A type of student who may like beer """
    def __init__(self, name, surname, likesbeer=True): # constructor
        Student.__init__(self, name, surname) # call constructor of the parent class
        self.likesbeer=likesbeer


    def __str__(self):
        # override parent method
        s="Name: " + self.name+ " "+ self.surname+"\n"
        s+="Print credit: " + str(self._printaccount) +"\n"
        if self.likesbeer:
            s+="Likes beer"
        else:
            s+="Does not like beer"
        return s


    def havePint(self):
        if self.likesbeer:
            print("Cheers mate!")
        else:
            print("No thanks")
            

class PhDStudent(Student): # inherit from Student
    """ A type of student who must publish or perish """
    def __init__(self, name, surname, haspublished=False):
        Student.__init__(self, name, surname) # call constructor of the parent class
        self.haspublished=haspublished

    def __str__(self):
        # override parent method
        s=Student.__str__(self) # this is quicker
        if self.haspublished:
            s+="\nHas published - is safe"
        else:
            s+="\nWill perish"
        return s
        
    def publish(self):
        self.haspublished=True
        
    def checkStatus(self):
        if self.haspublished:
            print("Has published")
        else:
            print("Has perished")


