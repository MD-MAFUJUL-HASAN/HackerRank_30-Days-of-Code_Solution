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
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        total = 0

        for testScore in self.testScores:
            total += testScore

        average = total / len(self.testScores)

        if 90 <= average <= 100:
            return "O"
        if 80 <= average < 90:
            return "E"
        if 70 <= average < 80:
            return "A"
        if 55 <= average < 70:
            return "P"
        if 40 <= average < 55:
            return "D"
        return "T"


line = input().split()
