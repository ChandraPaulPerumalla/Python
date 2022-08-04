class Student:
    def __init__(self,student_id,age,marks):
        self.student_id = student_id
        self.__age = age
        self.marks = marks
        
    def check_qualification(self,age,marks):
        if age > 20 and marks >= 65:
            return true
        else:
            return false
    
    def set_age(self,age):
        if age > 20:
            self.__age = age
            return true
        else:
            return false
        
    def get_age(self):
        return self.__age
                   
    def set_marks(self):
        if marks >= 65:
            self.marks = marks
            return true
        else:
            return false
        
    def get_marks(self):
        return self.marks

s1 = Student(124,22,75)
print(s1.get_age())
print(s1.get_marks())
    