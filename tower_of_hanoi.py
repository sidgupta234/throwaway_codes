# a = 0
def hanoi(disks, src="A", temp="B", dest="C"):
    # global a
    # a+=1
    # print(a)
    if disks==1:
        print("move 1 from {} to {}".format(src, dest))
        return
    
    else:
        hanoi(disks-1, src="A", temp="C", dest="B")
        print("move from {} to {}".format(src, dest))
        hanoi(disks-1, src="B", temp="A", dest="C")
        return
    
hanoi(8)
