import sys
class Student:
    count=100
    def __init__(self,x,y,z):
        print('Constructor called')
        self.name = x
        self.rollno = y
        self.marks = z


    def dispaly(self):
        #del self.marks
        print('Student name:{}\n' \
              'Roll no:{}\n' \
              'Marks:{}'.format(self.name,self.rollno,self.marks))


print("---------1")
s1 = Student('A',10,90)

#s1 = Student('A',10,901)
print("---------2")
s2 = Student('B',10,90)
#del s2.marks
print("---------1")
print(s1.dispaly())
print(s2.dispaly())

print("---------Static Variable")
print(Student.count)
print(s1.count)
print("---------")
print("---------dict")
print(Student.__dict__)
print("----------===========")
print(Student.dispaly(s1))