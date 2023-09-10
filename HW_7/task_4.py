days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
number_in_week = {i + 1: days_of_week[i] for i in range(len(days_of_week))}
day_in_week = {days_of_week[i]: i + 1 for i in range(len(days_of_week))}

print(number_in_week)
print(day_in_week)