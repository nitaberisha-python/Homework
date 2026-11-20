print("===== CLASS VOTE =====")

candidates = ["Python", "SQL", "Excel", "Power BI"]

votes = ["Python", "SQL", "Python", "Excel", "SQL", "Java", "Python",
         "Power BI", "SQL", "", "Python", "Excel", "SQL", "SQL", "Python", "SQL"]

results = {}

for candidate in candidates:
    results[candidate] = 0

invalid_votes = 0

for vote in votes:
    if vote in results:
        results[vote] = results[vote] + 1
    else:
        invalid_votes = invalid_votes + 1

winner = ""
highest_votes = 0

for name, number in results.items():
    if number > highest_votes:
        highest_votes = number
        winner = name

valid_votes = len(votes) - invalid_votes
winner_percent = highest_votes / valid_votes * 100

for name, number in results.items():
    print(f"{name}: {'#' * number} ({number})")

print("----------------------")
print(f"Total Votes: {len(votes)}")
print(f"Valid Votes: {valid_votes}")
print(f"Invalid Votes: {invalid_votes}")
print(f"Winner: {winner} with {highest_votes} votes ({winner_percent:.1f}%)")
print("======================")