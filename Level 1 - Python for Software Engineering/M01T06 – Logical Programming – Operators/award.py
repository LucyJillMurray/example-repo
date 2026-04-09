swim_time  = int(input("Enter your swimming time: ")) 
cycle_time = int(input("Enter your cycling time: ")) 
run_time   = int(input("Enter your running time: "))

total_time = swim_time + cycle_time + run_time
print(f"Total time taken for the triathlon: {total_time} minutes")

award_type = ""
if total_time <= 100:
    award_type = "Provincial colours"
elif total_time > 100 and total_time <= 105:
    award_type = "Provincial half colours"
elif total_time > 105 and total_time <= 110:
    award_type = "Provincial scroll"
else:
    award_type = "No award"


print(f"Award: {award_type}")