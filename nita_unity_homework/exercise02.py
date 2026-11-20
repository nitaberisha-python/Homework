print("===== WEEKLY STEPS =====")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [8200, 12500, 6400, 10100, 11800, 15300, 4700]

goal = 10000
goal_days = []

total_steps = 0
current_streak = 0
best_streak = 0
goal_count = 0

for i in range(len(steps)):
    total_steps = total_steps + steps[i]

    if steps[i] >= goal:
        print(f"{days[i]}: {steps[i]} steps - Goal reached")
        goal_days.append(days[i])

        goal_count = goal_count + 1
        current_streak = current_streak + 1

        if current_streak > best_streak:
            best_streak = current_streak
    else:
        print(f"{days[i]}: {steps[i]} steps - Missed")
        current_streak = 0

average_steps = total_steps / len(steps)

best_steps = max(steps)
best_index = steps.index(best_steps)
best_day = days[best_index]

worst_steps = min(steps)
worst_index = steps.index(worst_steps)
worst_day = days[worst_index]

if average_steps >= 10000:
    status = "Very Active"
elif average_steps >= 7500:
    status = "Active"
else:
    status = "Needs More Walking"

print("------------------------")
print(f"Total Steps: {total_steps}")
print(f"Average Steps: {average_steps:.2f}")
print(f"Best Day: {best_day} ({best_steps})")
print(f"Worst Day: {worst_day} ({worst_steps})")
print(f"Goal Days: {goal_days}")
print(f"Goal Reached: {goal_count}/7 days")
print(f"Longest Streak: {best_streak} days")
print(f"Status: {status}")
print("========================")