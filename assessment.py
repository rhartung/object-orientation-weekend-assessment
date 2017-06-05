"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   -Polymorphism! (Woo!)
    Methods and attributes defined in the parent class can easily be called
    and redefined in each child class without needing to use conditionals
    and without creating 'spaghetti code'.

   -Encapsulation! (Yay!)
    Instantiating an object of a particular class gives that object access
    to each method and attribute defined within its subclass and
    superclass.

   -Abstraction! (Ermahgherd!)
    Classes allow for the creation of an overarching 'abstract' class whose
    methods and attributes apply to each child that subclasses the abstract
    class.  Using polymorphism, each method and attribute from the abstract class
    can then be altered to fit the needs of each subclass.

2. What is a class?
    When creating an object in Python, the object's class defines what type of
    object has been created, and what methods and attributes that object has
    by default.  For example, 'String', 'List', and 'Dictionary' are all classes.
    When instantiating an object of the string class, that object will, by
    default, have access to all string methods.

3. What is an instance attribute?
    An instance attribute is defined only upon instantiation of an object that
    belongs to a particular class.  An whereas a 'class attribute' will
    apply uniformly to each object belonging to a class, an instance attribute
    may vary among objects belonging to the same class depending on user input.

4. What is a method?
    A method is a function that is defined within a class.  Each object belonging
    to that class will have access to that method, but objects outside of that
    class will not be able to use another class' methods.

5. What is an instance in object orientation?
    In object orientation, an instance is one object that belongs to the class
    specified upon creation of that object.  For example, the following syntax -
    my_string = "Hi there!" - would instantiate an instance of the string class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute applies uniformly to any object that belongs to that class.
   An instance attribute is assigned to an object upon instantiation and may
   be different from object to object depending upon user input at the time of
   instantiation.  For example, if you were creating a class called 'Mammals',
   you could assign an attribute to the whole class called 'warm_blooded' and
   set the value to the boolean value True because all Mammals are warm blooded.
   However, if you wanted to assign a color attribute to every instance of the
   Mammals class, you would use an instance attribute to be determined upon
   instantiation of the object becasuse not all Mammals are the same color.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student's names and addresses"""

    def __init__(self, first_name, last_name, address):
        """Init student w/ first name, last name, and address attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions include a question and a correct answer."""

    def __init__(self, question, correct_answer):
        """Init question and correct answer"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Asks user a question and evaluates if user's answer is correct"""

        user_answer = raw_input(self.question)

        if user_answer == self.correct_answer:
            return True

        else:
            return False


class Exam(object):
    """Exam will contain objects of the Questions class"""

    def __init__(self, exam_name, questions_list=[]):
        """Init exam with exam name and list of questions as attributes.

        questions must come from Question class.
        """

        self.exam_name = exam_name
        self.questions_list = questions_list

    def add_question(self, question):
        """Adds questions to exam's questions_list."""

        self.questions_list.append(question)

    def administer(self):
        """Administers exam with all questions from questions_list.

        Method will evaluate all answers to True or False, then return how many
        questions student answered correctly.
        """

        correct_responses = []

        for question in self.questions_list:
            answer = question.ask_and_evaluate()

            if answer:
                correct_responses.append(answer)

        num_correct = float(len(correct_responses))

        user_grade = (num_correct / len(self.questions_list)) * 100.0

        return user_grade


class StudentExam(object):
    """Stores a student, an exam, and the student's score for that exam.

    Student should be object of Student class, exam an object of Exam class.
    """

    def __init__(self, student, exam):
        """Initializes student exam with input of student and exam.

        self.score defaults to 0 until student takes test.
        """

        self.student = student
        self.exam = exam
        self.score = 0

    def take_test(self):
        """Administers exam and assigns score to self.score."""

        self.score += self.exam.administer()

        print "Hi {}, your final score is {}" .format(self.student.first_name, self.score)


def example():
    """Example exam using classes defined above"""

    alberta_capital = Question("What is the capital of Alberta? ", "Edmonton")
    best_cat = Question("Who is the best cat in the world? ", "Roscoe")
    best_food = Question("What is the best food ever? ", "Pizza")

    robyn = Student("Robyn", "Lundin", "18 10th St. Unit 934")

    an_exam = Exam("Really random exam")

    an_exam.add_question(alberta_capital)
    an_exam.add_question(best_cat)
    an_exam.add_question(best_food)

    this_exam = StudentExam(robyn, an_exam)

    this_exam.take_test()


class Quiz(Exam):
    """Quiz is a subclass of Exam: returns score 1 if pass, 0 if fail"""

    def administer(self):
        """calls on administer method from superclass - scores student 1 or 0"""

        user_grade = super(Quiz, self).administer()

        if user_grade > 50:
            return 1

        else:
            return 0


class StudentQuiz(StudentExam):
    """Stores a student, a quiz, and the student's score for that quiz.

    Student should be object of Student class, exam an object of Quiz class.
    """

    def take_test(self):
        """Administers exam and assigns score to self.score."""

        super(StudentQuiz, self).take_test()



















