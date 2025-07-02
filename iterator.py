a=iter(range(9))
print(type(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#next in file wird zeil für zeil lesen 
file=open("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt", "r", encoding="UTF-8")
print(next(file), end="")
print(next(file), end="")
print(next(file), end="")
print(next(file), end="")



