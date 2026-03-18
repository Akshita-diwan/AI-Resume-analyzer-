#resume analyzer- string operations 
candidate_name= input("enter your name : ")
candidate_skills=input("enteer your skills: ")
candidate_college=input("enter your college: ")

#string operations 

print("\n---formatted pattern---")
print("name: ",candidate_name.upper())
print("name length: ",len(candidate_name))
print("college: ",candidate_college.capitalize())
print("skills: ",candidate_skills.lower())

#skill check 
print("\n ---skills check---")
print("Python?", "python" in candidate_skills.lower())
print("Total skills length: ",len(candidate_skills))
