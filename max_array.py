def max_array(a, index):
    if(index == 0):
        return a[index]
    
    else:
        return max(a[index], max_array(a, index-1))
        
print(max_array(a, 6))
