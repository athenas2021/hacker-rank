class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def __init__(self, firstname, lastname, idNumber, scores):
        self.firstName = firstname
        self.lastName = lastname
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        total = 0
        for x in scores:
            total += x
        media = (total/len(scores))
        letra = '' 

        if media >= 90 and media <= 100:
            letra = 'O'
        elif media >= 80 and media < 90:
            letra = 'E'
        elif media >= 70 and media < 80:
            letra = 'A'
        elif media >= 55 and media < 70:
            letra = 'P'
        elif media >= 40 and media < 55:
            letra = 'D'
        elif media < 40:
            letra = 'T'
        
        return letra
    

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
print(f'scores-> {scores}')
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())