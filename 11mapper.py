# Case 1 - Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("part.txt", "r") as input:
  with open("output11mapped.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("    ")
      if (len(datalist) == 6) : 
        date, time,store, department, cost, paymentType = datalist

        # output intermediate key-value pairs
        output.write(store + "\t" + cost + "\n")

        # display to console (not required - just for the user)
        print(store + "\t" + cost + "\n")
