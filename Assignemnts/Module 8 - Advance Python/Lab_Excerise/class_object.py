class Member:

 
    def student(self, id, name):
        self.id = id
        self.name = name

   
    def display(self):
        print("ID is:", self.id)
        print("Name is:", self.name)



M1 = Member()


M1.student(1, "danish")


M1.display()