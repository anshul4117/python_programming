# seconds to hours, minutes

seconds =  int(input("Enter time in seconds : "))

# initializing no of hours and minutes
minutes = 0
hours = 0


# calculate hours
if(seconds >= 3600):
    hours = seconds // 3600 #storing quotient as hours
    seconds = seconds % 60 #storing reminder as seconds

# calculate minutes
if(seconds >= 60):
    minutes = seconds // 60 #storing quotient as minutes
    seconds = seconds % 60 #storing reminder as seconds

