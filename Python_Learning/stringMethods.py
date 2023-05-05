# 1 Indexing ===> variable[index of string] (Access Single Element)
# 2 Slicing ===> variable[Start:End] (Access Multiple Sequence Item)
# 3 Slicing ===> variable[Start:End:step] (Access Multiple Sequence Item and Steps)

test = "Hello World!"
print(test[3])
print(test[2:7])
print(test[1:8:2])

# 4 length ===> len(variable)

print(len(test))

#5 strip ,rstrip ,lstrip ===> variable.strip()
test2 = "   Say My Name   "
print(test2.strip())
print(test2.rstrip())
print(test2.lstrip())
print(len(test2))
print(len(test2.strip()))

#6 upper , lower ===> variable.upper()
#7 zfill ===> variable.zfill(num)
#8 title , capitalize ===> variable.title()

#---------------------------------------------------------------------------------------------------------

#9 split ===> listed Element var.split()
#10 center, rjust , ljust ===> add strings to var var.center(width , fill char)
#11 count ===> var.count(string , start , end)
print(test2.split())
print(test2.center(30 ,"$"))
print(test2.count("a"))

#12 swapcase ===> upper to lower and vise verse var.swapcase()
#13 startswith ,endswith ===> query   var.startswith(string ,start , end)

#--------------------------------------------------------------------------------------------------------------

#14 index ===> query for index var.index(substring , start , end)
print(test.index("W"))

# 15 splitlines ===> split lines into list var.splitlines()
print(test.splitlines())
