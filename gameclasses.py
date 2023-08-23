
class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions
    
    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nNombre minimum de questions = 1")
            print("Ainsi, le nombre de questions a été mis à 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nNombre maximum de questions = 10")
            print("Ainsi, le nombre de questions a été mis à 10")
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\nVeuillez convertir %d en binaire: " %(base10))
        while True:
            try:
                answer = int(userResult, base = 2)
                if answer == base10:
                    print("Bonne réponse")
                    score = score + 1
                    break
                else:
                    print("Mauvaise réponse. La bonne réponse était {:b}.".format(base10))
                    break
            except:
                print("Vous n'avez pas entrez un nombre binaire. Recommencez!")
                userResult = input("\nVeuillez convertir %d en binaire: " %(base10))
        return score
        
class MathGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:' + ', 2:' - ', 3:'*', 4:'**'}
        for i in range(self.noOfQuestions):
            for index in range(0, 5):
                numberList[index] = randint(1, 9)
            #refer to explanation below
            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == '**':
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1, 4)]
                questionString = str(numberList[0])
                for index in range(0, 4):
                    questionString = questionString + symbolList[index] +str(numberList[index+1])
                result = eval(questionString)
                questionString = questionString.replace("**", "^")
                userResult = input("\nVeuillez calculer %s: "%(questionString))
                while True:
                    try:
                        answer = int(userResult)
                        if answer == result:
                            print("Bonne réponse!")
                            score = score + 1
                            break
                        else:
                            print("Mauvaise réponse. La bonne réponse était {:d}.".format(result))
                            break
                    except:
                        print("Vous n'avez pas entrez un nombre binaire. Recommencez!")
                        userResult = input("\nVeuillez calculer %s: "%(questionString))
        return score