candidate={
"Name": "Akshita",
"age": 20,
"college": "IITM",
"Branch":"Btech cse",
"Cgpa" : 8.5,
"skills": ["python","Sql","communication"],
"Goal": "top 0.5 founder",
}

#profile of candidate
print("===candidate profile===")
for key,value in candidate.items(): 
    print(key,":",value)

#skill check 
print("\n===Cgpa check===")
required=["python","machine learning"]
for skill in required:
    if skill in candidate["skills"]:
        print(skill,"found")
    else :
        print(skill,"missing")


#check cgpa 
print("\n===candidate Cgpa")
if candidate ["Cgpa"]>=7.5:
    print("Cgpa good")
else :
    print("cgpa bad")
            
