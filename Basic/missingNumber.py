'''
Arr=[]
N=int(input("Enter number for elements:"))
newArr=[x+1 for x in range(N)]
print(Arr)
'''
def missing_number(array, n):
    expected_sum=(n*(n+1))//2
    actual_sum=sum(array)
    
    missing = expected_sum - actual_sum
    
    return missing

arr_input=input("Enter elements for arrary incuding spaces:") 
Arr=list(map(int, arr_input.split()))
N=int(input("Enter expected element number: "))

print("The missing number is: ", missing_number(Arr, N))
