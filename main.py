name = "adam"


csv = "age, 33, 123 , 11111, adam"
split_csv = csv.split(",")

testing_csv = []
for i in split_csv:
    if i == "age":
        testing_csv.append(i)

print(testing_csv)

print("---------------")

fname = " bill"
print(fname.strip())

learn = "####fod "
print(learn.strip("#"))
print(learn.find("fod"))


print('adam' in name)