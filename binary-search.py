pos = -1
def search(lst,n):
    l = 0
    u = len(lst) - 1

    while l <= u:
        mid = (l+u) //2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        elif lst[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return False

lst = [10,20,30,40,60,70,80,90]
n =  75


if search(lst,n):
    print('the element found at: ', pos+1)
else:
    print('the value is missing from the list')