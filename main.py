import  secrets, string

#Random Password that will be generated for users
password=""

#Generating random number between 8 and 16 for password strength
min_value=8
max_value=16

#Generating random size for the password
Password_Size=min_value + secrets.randbelow(max_value - min_value + 1)

#List of choices to be choosen randomly from
choices = ['ascii_uppercase','ascii_lowercase','punctuation','digits']

#Flags to check the existence of uppercase, lowercase & special characters and digits
ExistsUpperCase=0
ExistsLowerCase=0
ExistsDigit=0
ExistsSpecial=0

#Looping on the randomly generated password size
i=0
while i <Password_Size:
    choice = secrets.choice(choices)
    if choice=='punctuation':
        password+=secrets.choice(string.punctuation)
        ExistsSpecial=1
    elif choice=='digits':
        password+=secrets.choice(string.digits)
        ExistsDigit=1
    elif choice=='ascii_uppercase':
        password+=secrets.choice(string.ascii_uppercase)
        ExistsUpperCase=1
    elif choice=='ascii_lowercase':
        password+=secrets.choice(string.ascii_lowercase)
        ExistsLowerCase=1
    i+=1

#Adding missed conditions if needed
if ExistsUpperCase==0 or ExistsDigit==0 or ExistsSpecial==0 or ExistsLowerCase==0:
    if ExistsDigit == 0:
        password += secrets.choice(string.digits)
    elif ExistsUpperCase == 0:
        password += secrets.choice(string.ascii_uppercase)
    elif ExistsLowerCase == 0:
        password += secrets.choice(string.ascii_lowercase)
    elif ExistsSpecial == 0:
        password += secrets.choice(string.punctuation)

#-------------------- Output --------------------
print("Random password size is", Password_Size)
print("Random password is", password)
