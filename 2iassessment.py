
def my_list():
    my_list = []
    for i in range(10):
        my_list.append(int(input("Please enter a number between 1 and 100: ")))
        #remove the duplicates using a set
        my_list = list(set(my_list))
        #sort the list in descending order
        my_list.sort(reverse=True)
    return my_list

print(my_list())