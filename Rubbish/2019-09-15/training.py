

set1 = {1,3,5,7,8}
print(set1)

set1.add (int(input("Add number Only : ")))
print(set1)
while True:
    try:
        set1.remove (int(input("Delete number : ")))
        print(set1)
        break
    except KeyError as err:
        print("Error value tru agin")
        print(set1)
        


















# my_dict = {"type":"bird", "skin cover":"feathers"}
# print(my_dict)
# type = my_dict["type"]
# print(type)
# print("-------")
# my_dict["skin cover"] = "Scales"
# print(my_dict)
# print("-------")

