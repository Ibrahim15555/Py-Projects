name = "Abdallah Ibrahim"  
age = 30           
ai_course = True    


print("Name:", name)
print("Age in 5 years:", age + 5)
print("Is enrolled in CS 335 course?", ai_course)



topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference"]


topics.append("Computer Vision")
topics.append("Reinforcement Learning")


for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")






    student = {"name": "Abdallah", "score": 95}


if student["score"] >= 95:
    grade = "A+"
elif student["score"] >= 90:
    grade = "A"
elif student["score"] >= 80:
    grade = "B"
else:
    grade = "C or below"

print(f"{student['name']} received a grade of {grade}.")




def greet_student(name):
    return f"Welcome to Abdallah, {name}!"


print(greet_student("Abdallah Ibrahim"))


def square_number(num):
    """Returns the square of the input number"""
    return num ** 2


print(square_number(5))  
print(square_number(10)) 
print(square_number(-3)) 
