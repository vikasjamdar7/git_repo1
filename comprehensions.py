def list_comprehension(l):
    l = [x**3 for x in l]
    return l
def dict_comprehension(l):
    d = {str(x):x**3 for x in l}
    return d

def two_forloops():
    l= [i for x in [[1,2,3],[4,5,6]] for i in x]
    return l

if __name__=="__main__":
    l=eval(input("Enter list:"))
    o=list_comprehension(l)
    print("cubes by list_comprehension==",o)
    o=dict_comprehension(l)
    print("cubes by list_comprehension==", o)

    result = two_forloops()
    print("list comphrension using two for loops==",result)


