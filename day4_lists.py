#lists in python 
candidate_skills=["python","java ","communication","sql" ]
print(candidate_skills )
print("Total skills : ",len(candidate_skills ))
print("First skill: ",candidate_skills[0])
print("Last skill: ",candidate_skills[-1])

#check skills 
required_skills=["python","sql","machine learning"]

print("---skill match---")
for skill in required_skills:
    if skill in candidate_skills:
        print(skill,"found")
    else:
        print(skill,"missing")
