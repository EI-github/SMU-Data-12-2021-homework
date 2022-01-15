import csv

csvpath = "Resources/election_data.csv"

totalVotes = 0
candidates = set()
candidates2 = []

candidate_dict = {
    "Li": 0,
    "O'Tooley": 0,
    "Khan": 0,
    "Correy": 0
}

candidate_dict2 = {}

with open(csvpath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        # print(row)

        totalVotes += 1

        # UNIQUE LIST OF CANDIDATES
        candidates.add(row[2])

        if row[2] not in candidates2:
            candidates2.append(row[2])

        # Two ways to add votes to dictionary
        # candidate_dict[row[2]] += 1

        # easier logic
        if row[2] == "Li":
            candidate_dict["Li"] += 1
        elif row[2] == "Khan":
            candidate_dict["Khan"] += 1
        elif row[2] == "O'Tooley":
            candidate_dict["O'Tooley"] += 1
        else:
            candidate_dict["Correy"] += 1

        # if candidate exists, add 1 to value
        if row[2] in candidate_dict2.keys():
            candidate_dict2[row[2]] += 1
        else:
            candidate_dict2[row[2]] = 1 # init in dict with one vote (since row voted for this dude)

print(totalVotes)
print(candidates)
print(candidates2)

print(candidate_dict)
print(candidate_dict2)
print()

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
max_cand = max(candidate_dict2, key=candidate_dict2.get)
max_votes = candidate_dict2[max_cand]

results = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------\n"""

for dude in candidate_dict2.keys():
    perc = 100*(candidate_dict2[dude] / totalVotes)
    results += f"{dude}: {round(perc, 2)}% ({candidate_dict2[dude]})\n"


results += f"""-------------------------
Winner: {max_cand}
-------------------------
"""

print(results)

# writes to file
with open("analysis/analysis.txt", "w") as file:
    file.write(results)
