# Adds the duration time to the start time and returns the result with optional day.
def add_time(start, duration, day=None):

    # Define constants
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    DAYS_IN_WEEK = 7
    
    # Split the start time into hours, minutes, and AM/PM
    time, am_pm = start.split()
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    
    # Split the duration into hours and minutes
    duration_hours, duration_minutes = duration.split(':')
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)

    # List of weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_lower = ("monday", "tuesday", "wednesday", "friday", "saturday", "sunday")
    current_day = 0

    # If a specific day is provided, find its index in the weekdays_lower list
    if day is not None:
        day = day.lower()
        current_day = weekdays_lower.index(day)

    # Convert hours to 24-hour format
    if am_pm == "PM":
        hours += 12
    
    # Calculate the total duration in minutes
    total_minutes = minutes + duration_minutes

    # Calculate any extra hours that result from adding the minutes
    extra_hours = total_minutes // MINUTES_IN_HOUR

    # Calculate the final minutes after adding the duration
    result_minutes = total_minutes % MINUTES_IN_HOUR

    # Calculate the total hours after adding the duration and extra hours
    total_hours = hours + duration_hours + extra_hours

    # Calculate the final hours after accounting for multiple days and convert back to 12-hour format
    result_hours = (total_hours % HOURS_IN_DAY) % (HOURS_IN_DAY // 2)

    # Determine whether it's AM or PM for the final time
    if (total_hours % HOURS_IN_DAY) <= 11:
        am_pm = "AM"
    else:
        am_pm = "PM"

    # Format the hours as a string, and set 12:00 as 12, not 0
    if result_hours == 0:
        result_hours = 12
    result_hours = str(result_hours)

    # Calculate the number of days that have passed
    result_days = total_hours // HOURS_IN_DAY

    # Format minutes with leading zero if needed
    if result_minutes < 10:
        result_minutes = '0' + str(result_minutes)
    else:
        result_minutes = str(result_minutes)
    
    # Construct the final result string with hours, minutes, and AM/PM
    result = result_hours + ':' + result_minutes + ' ' + am_pm

    # If a specific day was provided, calculate the resulting day of the week and add the information to the final result string
    if day is not None:
        day = weekdays[(result_days + current_day) % DAYS_IN_WEEK]
        result += ", " + day

    # Add information about how many days have passed, if applicable, to the final result string.
    if result_days == 1:
        result += " (next day)"
    elif result_days > 1:
        result += f" ({str(result_days)} days later)"
        #result += " (" + str(result_days) + " days later)"

    # Return the final result string
    return result

# Test cases
print(add_time("8:16 PM", "466:02")) # 6:18 AM (20 days later)
print(add_time("3:00 PM", "3:10")) # 6:10 PM
print(add_time("11:43 AM", "00:20")) # 12:03 PM
print(add_time("11:43 PM", "24:20", "tueSday")) # 12:03 AM, Thursday (2 days later)
print(add_time("11:30 AM", "2:32", "Monday")) # 2:02 PM, Monday
print(add_time("11:00 PM", "1:30")) # 12:30 AM (next day)
print(add_time("11:30 AM", "00:30")) # 12:00 PM