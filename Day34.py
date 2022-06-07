
#Small program that populates a list() from user input() and stops populating when a negative number is entered
#It then calculates several parameters, such as max(), min(), statistics.mean() and sum().
import statistics
enter_value = 0

lst=[]

while True:
    
    enter_value < 1 or enter_value > 10
    
    enter_value = int(input("Enter number:"))
    
    lst.append(enter_value)

    if enter_value < 0:
        break

print("You entered a negative number, program STOPS here!")

lst = lst[:-1]

sum_lst=sum(lst)

print("Final list to work with: ",lst)

print("Maximum:", max(lst))

print("Minimum:", min(lst))

print("Mean:", statistics.mean(lst))

print("Sum:",sum_lst)
