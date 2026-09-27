# ECE Student Skill & Placement Readiness Analyzer
# Beginner Python Project

print("=" * 45)
print("   ECE PLACEMENT READINESS ANALYZER")
print("=" * 45)

name = input("\nEnter your name: ")

print("\nRate each skill from 1 to 10.")

python = int(input("Python programming: "))
c = int(input("C programming: "))
embedded = int(input("Embedded systems: "))
electronics = int(input("Electronics fundamentals: "))
communication = int(input("Communication skills: "))
aptitude = int(input("Aptitude: "))
projects = int(input("Project knowledge: "))

# Calculate average score
total = python + c + embedded + electronics
total += communication + aptitude + projects

score = total / 7

print("\n" + "=" * 45)
print("              YOUR RESULT")
print("=" * 45)

print("Student:", name)
print("Readiness Score:", round(score, 2), "/ 10")

# Find strongest skill
skills = {
    "Python": python,
    "C": c,
    "Embedded Systems": embedded,
    "Electronics": electronics,
    "Communication": communication,
    "Aptitude": aptitude,
    "Project Knowledge": projects
}

strongest_skill = max(skills, key=skills.get)

print("Strongest Skill:", strongest_skill)

# Give feedback
if score >= 8:
    print("Level: Excellent")
    print("Keep improving and start preparing for interviews!")

elif score >= 6:
    print("Level: Good")
    print("You have a good foundation. Focus on your weaker areas.")

elif score >= 4:
    print("Level: Developing")
    print("Practice regularly and build more projects.")

else:
    print("Level: Beginner")
    print("Start with fundamentals and practice every day.")

print("=" * 45)
print("Keep learning. Keep building. 🚀")