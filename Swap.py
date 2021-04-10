#Swapping the first element to last element and Last element to First Element

def swap(l1):
  l1[0],l1[-1] = l1[-1], l1[0]
  return l1
List = [10, 20, 30, 40, 50]
print(swap(List))


