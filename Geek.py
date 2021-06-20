# -*- coding: utf-8 -*-
# modificateurs d'accès: public, protected, private
class Student: 
     
     
     _name = None
     _roll = None
     _branch = None
     
     
     def __init__(self, name, roll, branch):   
          self._name = name 
          self._roll = roll 
          self._branch = branch 
     
     
     def _displayRollAndBranch(self): 
  
          
          print("Roll: ", self._roll) 
          print("Branch: ", self._branch) 

class Geek(Student): 
  
       
       def __init__(self, name, roll, branch):  
                Student.__init__(self, name, roll, branch)  
          
       
       def displayDetails(self): 
                    
                 
                print("Name: ", self._name)  
                    
                 
                self._displayRollAndBranch()


obj = Geek("R2J", 1706256, "Information Technology")  
  
obj.displayDetails()  


## modificateur d'accès privé
class Geek: 
     
     
     __name = None
     __roll = None
     __branch = None
  
     
     def __init__(self, name, roll, branch):   
          self.__name = name 
          self.__roll = roll 
          self.__branch = branch 
  
     
     def __displayDetails(self): 
            
           
           print("Name: ", self.__name) 
           print("Roll: ", self.__roll) 
           print("Branch: ", self.__branch) 
     
     
     def accessPrivateFunction(self):  
             
           
           self.__displayDetails()   
  
obj = Geek("R2J", 1706257, "Information Technology") 
  
obj.accessPrivateFunction()
#end modificateur d'accès privé 