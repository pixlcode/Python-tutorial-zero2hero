# Calculates days, hours, minutes, seconds based on number of seconds
seconds = int(input("Enter seconds: "))
minutes = 0
hours = 0
days = 0
if seconds <= 59:
    print( days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
elif seconds >= 60 and seconds <= 3599:
    minutes = int(seconds / 60)
    seconds = seconds - 60 * minutes
    print( days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
elif seconds >= 3600 and seconds <= 86399:
    minutes = int(seconds / 60)
    seconds = seconds - 60 * minutes
    hours = int(minutes / 60)
    minutes = minutes - hours * 60
    print( days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
elif seconds >= 86400:
    minutes = int(seconds / 60)
    seconds = seconds - 60 * minutes
    hours = int(minutes / 60)
    minutes = minutes - 60 * hours
    days = int(hours/24)
    hours = hours - days * 24
    print( days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
    
    
    
