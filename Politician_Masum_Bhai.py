"""Conditional Flow Control"""
fool = 3
clever = 3
if fool != clever:
    fool = "Clever"
    print("Yeah boy,Masum Bhai is " + fool)
elif (0 < 1) and not (0 > 1):
    print("This is universal truth")
    print("So,the else block would never run")
else:
    clever = "fool"
    print("OMG,You are very very much", clever)

speech = """Vote casting
Once an self proclaimed dictator Masum Bhai, ordered his cadets to attract voters by asking voters age
if age < 18: Take some candy and implore your parents to vote Masum Bhai
elif (age >= 18 and age <= 25): If you vote Masum Bhai,he will give all of you(who votes Masum Bhai) special permit for adult site,wink wink
elif(age <25 and age <= 30): if you vote Masum Bhai,he will arrange blind marriage ceremony where any adult can choose his bride on the spot,wink wink wink
elif (age <30 and age <=35): if you vote Masum Bhai,he will urge govt. to decree 'every week day will be officially sex day for couples' wink,wink,wink
elif (age <35 and age <=45): if you vote Masum Bhai,he will reduce the price of play station (game tool) for your kids and implore to govt. to ensure parental access to their kids smart phone.(in mind,he'm against this but what to do...)
elif (age <45 and age <= 60): if you vote Masum Bhai,he will prolong the govt. job service duration and increase pension money,wink wink
else: Kakku,you don't have to go vote center,your vote will already be given by our agent.Stay home and rest ha..ha
"""
print(speech)
age = int(input("So what's your age?\n"))
if age < 18:
    print("Take some candy and implore your parents to vote Masum Bhai")
elif (age >= 18 and age <= 25):
    print("If you vote Masum Bhai,he will give all of you(who votes Masum Bhai) special permit for adult site,wink wink")
elif(age <25 and age <= 30):
    print("if you vote Masum Bhai,he will arrange blind marriage ceremony where any adult can choose his groom on the spot,wink wink wink")
elif (age <30 and age <=35):
    print("if you vote Masum Bhai,he will urge govt. to decree 'every week day will be officially sex day for couples' wink,wink,wink")
elif (age <35 and age <=45):
    print("if you vote Masum Bhai,he will reduce the price of play station (game tool) for your kids and implore to govt. to ensure parental access to their kids smart phone.(in mind,he'm against this but what to do...)")
elif (age <45 and age <= 60):
    print("if you vote Masum Bhai,he will prolong the govt. job service duration and increase pension money,wink wink")
else:
    print("Kakku,you don't have to go vote center,your vote will already be given by our agent.Stay home and rest ha..ha")