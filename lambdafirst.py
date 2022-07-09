max = lambda a,b : a if(a > b) else b

print(max(4,7))
print(max(8,4))

def sortByPattern(pat, str):
    priority = list(pat)

    myDict = {priority[i] : i for i in range(len(priority))}

    str = list(str)

    str.sort(key=lambda ele : myDict[ele])

    str.reverse()

    new_str = ''.join(str)
    return new_str

if __name__ =='__main__':
    pat = 'asbcklfdmegnot'
    str = 'eksge'
    new_str = sortByPattern(pat, str)
    print(new_str)