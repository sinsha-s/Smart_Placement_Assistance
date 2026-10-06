print("==== SMART PLACEMENT ASSISTANT ====")
print("1. Analyze Student")
print("2. Exit")
choice = int(input("Enter your choice:"))
if choice == 1:
    name = input("Enter your name: ")
    aptitude = int(input("Enter aptitude score: "))
    coding = int(input("Enter coding score: "))
    communication = int(input("Enter communication score: "))
average = (aptitude+coding+communication) / 3
print("\n----REPORT----")
print("Name: ", name)
print("Average score: ",round(average, 2))
if average >= 90:
    print("Skill level: Outstanding")
elif average>= 80:
    print("Skill level: Advanced")
elif average>= 60:
    print("Skill level: Intermediate")
else:
    print("Skill level: Beginner")
if average>=80:
    print("Placement Status: Excellent")
elif average>=60:
    print("Placement Status: Good")
else:
    print("Placement Status: Needs Improvement ")


print("\n==== CAREER RECOMMENDATION ====")
if coding>=80:
    print("Software Developer")
if aptitude>=80:
    print("Data Analyst")
if communication>=80:
    print("Technical Support")
print("\n==== SUITABLE COMPANIES ====")
if average >=90:
    print("Intel")
    print("Google")
    print("Microsoft")
elif average >=80:
    print("TCS")
    print("Infosys")
    print("Wipro")
else:
    print("Focus on skill development and internships")
print("\n==== INTERNSHIPS READINESS ====")
if average >=85:
    print("Internship Ready: YES")
elif average >= 70:
    print("Internship Ready: ALMOST")
else:
    print("Internship Ready: NEED PREPERATION")
print("\n==== INTERVIEW READINESS")
if communication >= 85 and coding>=80:
    print("Interview Ready: YES")
elif communication >=70:
    print("Interview Ready: ALMOST")
else:
    print("Interview Ready: NEEDS PRACTICE")
print("\n==== FINAL RESULT ====")
if average >=85 and communication >= 80 and coding >=80:
    print("Overall Assessment: PLACEMENT READY")
elif average >= 70:
    print("Overall Assessment: PREPARING FOR PLACEMENTS")
else:
    print("Overall Assessment: NEEDS MORE TRAINING")
print("\n==== IMPROVEMENT AREAS ====")
if coding < 80:
    print("Improve Coding Skills")
if aptitude < 80:
    print("Improve Aptitude Skills")
if communication < 80:
    print("Improve Communication Skills")
elif choice == 2:
    print("Thank you for using Smart Placement Assistant!")
else:
    print("Invalid Choice")



