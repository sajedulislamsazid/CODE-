class student:
   def __init__(self, name, current_class, grade):
       self.name = name  
       self.current_class = current_class
       self.grade = grade
       self.attendance = 0

    def __repr__(self) -> str:
        return f'student name: {self.name}, current class: {self.current_class}, grade: {self.grade}'           


class teacher: 
    def __init__(self, name, subject,id):
        self.name = name
        self.subject = subject      
        self.id = id(self)
        self.students = []          
               
 






sneha = student('Sneha', 10, 'A')  
print(sneha.name)       
print(sneha.current_class)
print(sneha.grade)      
print(sneha)