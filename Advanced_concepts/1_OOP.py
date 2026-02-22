import datetime as dt
# creating a class
class employee:
    no_of_emp=0 #class variable
    raise_amount =1.04 #by 4 percent
    
    def __init__(self,first,last,pay,Batch):
        #instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.date=Batch
        self.email=first+'.'+last+str(Batch)+'@company.com'

        employee.no_of_emp+=1 #runs everytime there is an object created

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay,Batch=emp_str.split('-')
        return cls(first,last,pay,Batch)
    

    def printdetails(self):
        return '{}{}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=employee.raise_amount *self.pay
    

    #change class varaible using class method
    @classmethod
    def apply_raise_classmethod(cls,amount):
        cls.raise_amount=amount



    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

# creating an object
emp1=employee("Aayam","Tiwari",3000,80)
emp2=employee("Panam","Parmer",4000,79)
emp3=employee("Johnny","Silverhand",3500,77)



 # creating an object using class method
emp4=employee.from_string('Vincent-Silverhand-4500-80')




#accessing individual attribute
print(emp1.email)
# to display instance varaibles in the objects
print(emp1.__dict__)
#before raise
print(emp2.pay)
emp2.apply_raise() # applying raise to emp1
#after raise
print(emp2.pay)

print(employee.no_of_emp) # to access class variable

#to create object using class method
print(emp4.first)


#using static method
my_date=dt.date(2024,6,10)
print(employee.is_workday(my_date))
