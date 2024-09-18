total=int(input("What are the total points?"))
achieved=int(input("How many points did they get?"))
percentage=(achieved/total)*100

if percentage >=0 and percentage <= 50:
    print("Grade: F")
elif percentage >=51 and percentage <= 60:
    print("Grade: D")
elif percentage >=61 and percentage <= 75:
    print("Grade: C")
elif percentage >=76 and percentage <= 88:
    print("Grade: B")
elif percentage >=89 and percentage <= 100:
    print("Grade: A")
