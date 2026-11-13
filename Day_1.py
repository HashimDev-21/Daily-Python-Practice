### INTRODUCTION --------------------------------

first_name=input("Enter your First Name:")
print("Length of your First Name:", len(first_name), "characters")
last_name=input("Enter your Last Name:")
print("Length of your Last Name:", len(last_name), "characters")
country=input("Enter your Country:")
print("Length of your Country:", len(country), "characters")
state=input("Enter your state:")
print("Length of your state:", len(state), "characters")
district=input("Enter your district:")
print("Length of your district:", len(district), "characters")
age=int(input("Enter your age:"))

print("Here is your detailed Introduction")
print("-" * 25)
print(f"Greetings {first_name} {last_name}. Your current age is {age}. You currently stay in {district}, which is located in {state}, {country}.")
res=input("Was that correct?:")
if res=="Y" or res=="y":
    print("Lovely! Have a good day.")
else:
    print("Apologies! Let's try that again by pressing `cls` and re-running the program.")