#calculates the pay rate for someone while adding a certain percentage if they did ot
h = float(hrs)
pay= input("Enter Rate:")
p= float(pay)
if h <=40:
    print("Pay:", h*p)
else:
    print("Pay:", p*40+(h-40)*1.5*p)

#numbers the data, totals it, and gives you the average of a set of numbers
num = 0
tot = 0
    while True:
        sval= input("Enter a number: " )
        if sval == "done":
            break
        try:
            fval= float(sval)
        except:
            print("Ivalid Input")
            continue
        fval= float(sval)
        print(fval)
        num = num +1
        tot= tot+fval
    print("ALL DONE")
    print(tot, num, tot/num)
#calculated the lergest and smallest in data and does error is not applicable
#this lets you collect data from file and find the average.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n=float(num)
        if largest is None or largest< n:
            largest=n
        elif smallest is None or smallest>n:
            smallest = n
    except:
        print("Invalid input")
        continue
print("Maximum", largest)
print("Minimum", smallest)


#creating a file and slicing information from it
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count= count+1
        t= line.find("0")
        num= float(line[t:])
        tot= tot+num
average= tot/count
print("Average sum confidence", average)

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print lst                          # print the list


#how to get specific parts from line in files
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": continue

    words = line.split()
    if words[0] !="From": continue

    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")


#how to open a file put in dictionary and find out the word
#that is used the most in the file and the number of times its used
name=input("Enter file here:")
handle= open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1

bigcount=None
bigword= None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword= word
        bigcount= count
print(bigword, bigcount)

#how to retrieve file start from after a certain word to find the count
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst=list()

for line in handle:
    if not line.startswith("From:"):
        continue
    line=line.split()
    lst.append(line[1])

counts=dict()
for word in lst:
    counts[word]= counts.get(word, 0)+1

bigcount=None
bigword= None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword= word
        bigcount= count
print(bigword, bigcount)

#turns lists into tuples than sorts them in reverse
#sorts by keys
c= {"a":10, "b":1, "c":22}
tmp= list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp= sorted(tmp, reverse=True)
print(tmp)

#code to retrieve timees from a piece of text and see which part was seen the most
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for key, val in sorted(counts.items()):
    print (key, val)
