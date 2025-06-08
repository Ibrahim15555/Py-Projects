name = "Abdallah Ibrahim"  
age = 30           
ai_course = True    
print(f"My name is {name}, I am {age} years old, and my enrollment status in the AI course is {ai_course}.")


topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference"]
topics.append("Computer Vision")
topics.append("Reinforcement Learning")
for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")

 Student = {"name": "Abdallah", "score": 97}  # Modified score to test different outputs

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

# Square number function
def square_number(num):
    return num ** 2


print(greet_student("Abdallah"))
print(square_number(5))   
print(square_number(10))  
