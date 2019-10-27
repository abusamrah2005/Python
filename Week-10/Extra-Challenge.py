# Week-10 Extra Challenge


try:

    number_array = list()
    number = input(" Enter the number of elements you want: ")

    print (' Number of items selected {} elements ' .format(number))
    for i in range(int(number)):
        n = input(" Enter Values in Your array : " )
        number_array.append(int(n))

except ValueError as err:
     print(" Enter Numbers Onle")
else:
    print (' ARRAY Elements: ', *number_array)



