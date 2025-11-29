#pcode

# * 1. build class 
# 2. make parameters: answer(int), 
# 3. make a function called guess that pulls user input as parameter user_guess
# 4. return function above with a string with an if / else method
# 5. creat guessing game test file


class GuessingGame():
    answer = 7

    def __init__(self, answer):
        self.answer = answer

    def guess(user_guess): # example of an *instance method*
        if user_guess == answer:
            return "Correct"
        elif user_guess > answer:
            return "High"
        else:
            return "Low"

    def solved(self, item):
        if user_guess == "Correct":
            return True
        else:
            return False

GuessingGame.guess(5) 
