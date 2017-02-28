import SmsBot

#Logging in
query = SmsBot.sms("username","password") # username is usually Mobile Number .

print("Remember Message should be less than 139 characters ")
my_message=input("Enter Your Message")

if query.count()>=100 :
    print("Sorry You've Crossed The Daily Limit of 100 sms")
    quit()
query.send("recipient",my_message) # recipient = receiver's numebr

print(query.count())
query.Logout()