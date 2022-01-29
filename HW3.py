# Your name: Reshad Alam
# Your student id: 91578522
# Your email: reshad@umich.edu
# List who you have worked with on this homework: N/A


# import the random module for use in this program
import random

# Create the class Magic_8_Ball

    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's answer_list (instance variable) to the passed list of possible answers
    # it sets this object's question_list (instance variable) to an empty list
    # it sets this object's answer_history_list (instance variable) to an empty list

class Magic_8_Ball:

    def __init__(self, input, answer_list, question_list, answer_history_list):
        self.input = input
        self.answer_list = answer_list
        self.question_list = []
        self.answer_history_list = []


    # create the __str__ method
    # It should return a string with all the answers
    # in answer_list separated by commas
    # For example : "Yes, No, Not clear"

    def __str__(self):
        return f", {self.answer_list}"


    # create the shake_8_ball method
    # it randomly picks an answer from the answer_list
    # it adds that index to the end of the answer_history_list
    # it returns the answer at the picked index

    def shake_8_ball(self):
        pickAnswer = random.randint(0, len(self.answer_list) - 1)
        self.answer_history_list.append(pickAnswer)
        return self.answer_list[pickAnswer]


    # create the check_question method that takes a question
    # it checks if the question is in the question_list and if so returns
    #         "I've already answered that question”
    # Otherwise it adds the question to the question_list and
    # returns the answer from shake_8_ball

    def check_question(self, question):
        if (question in self.question_list):
            return "I've already answered that question"
        else:
            self.question_list.append(question)
            answer = self.shake_8_ball()
            return answer

    # create the print_question_history method
    # prints "[answer index] question - answer" for each of the indices in the answer_history_list
    # from the first to the last with each on a separate line.  If there are no items in the
    # answer_history_list it prints "None yet"
    # it does not return anything!

    def print_question_history(self):
        if (self.answer_history_list == []):
            print("None yet")
        else:
            for index in range(len(self.answer_history_list)):
                print("[", str(self.answer_history_list[index]), "] ",
                self.question_list[index], " - ", self.answer_list[self.answer_history_list[index]])

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #   a number, n. Ex: 200
    # it generates a random response n times by calling shake_8_ball
    # It prints the counts for each answer and
    # prints the most frequently occurring answer (Do not use a dictionary in this solution):
    #   Yes: 36
    #   No: 36
    #   Ask again: 48
    #   Maybe: 38
    #   Not clear: 47
    #   The most frequent answer after 200 was Not clear

def main():

    # You are welcome to replace the answer_list with your desired answers
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8_Ball(answer_list)

    # get the first question or quit
    getQuestion = input

        # print question - answer

        # get the next question or quit 
    
    while getQuestion != "quit":
        check_question = input
        print(getQuestion, " - ", answer_list)
        break

def test():

    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8_Ball(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_question_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.check_question("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.check_question("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.check_question("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.check_question("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_question_history()
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    # print("Testing most_frequent method with 200 responses")
    # bot2.most_frequent(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 