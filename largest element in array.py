#Problem Statement: Given an array, we have to find the largest element in the array.


def LargestElement(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>arr[0] :
            max=arr[i]
    return max

if __name__=='__main__':
    arr=[10,8,21,5,3,0]
    n=len(arr)
    ele=LargestElement(arr,n)
    print(f"The largest element of the array is {ele}")
