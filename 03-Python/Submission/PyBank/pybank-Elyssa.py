import csv

filepath = "C://Users//Elyssalex//Desktop//SMU//SMU-Data-12-2021-homework//03-Python//Submission//PyBank//budget_data.csv"

totalMonths = 0
totalProfit = 0

changes = []
changeMonths = []
prevProfit = 0

with open(filepath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
       
        totalMonths += 1
        totalProfit += int(row[1])

        # if not first row, then get change
        if totalMonths > 1:
            change = int(row[1]) - prevProfit
            changes.append(change)
            changeMonths.append(row[0])

        # update previous profit
        prevProfit = int(row[1])

        print(row)


print("Months = " + str(totalMonths))
print(totalProfit)
avg_change = sum(changes) / len(changes)
avg_change_curr = "{:,.2f}".format(avg_change)
print(avg_change_curr)

#formats with commas and rounded to nearest hundredths
max_change = max(changes)
max_change_curr = "{:,.2f}".format(max_change)

min_change = min(changes)
min_change_curr = "{:,.2f}".format(min_change)

print(max_change_curr)
print(min_change_curr)

maxMonth_index = changes.index(max_change)
maxMonth = changeMonths[maxMonth_index]

minMonth_index = changes.index(min_change)
minMonth = changeMonths[minMonth_index]
print(maxMonth)
print(minMonth)
print()

# create summary
summary = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average  Change: ${avg_change_curr}
Greatest Increase in Profits: {maxMonth} (${max_change_curr})
Greatest Decrease in Profits: {minMonth} (${min_change_curr})
        """

print(summary)

# write analysis to file
with open("analysis-Elyssa.txt", "w") as file:
    file.write(summary)