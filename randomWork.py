# return kth distinct string in a list of strings
def kth_distinct_string(lst,k):
    # make a frequency table
    freq ={}
    for str in lst:
        if str not in freq:
            freq[str]=1
        else:
            freq[str]+=1
    
    # as we iter trhough dict decrease k every time we find distinct until we hit 0 and return key
    '''
        for key,value in freq.items():
        if k == 0 and value == 1:
            return key
        elif value==1:
            k-=1
        return 'none'
    '''
    #BECAUSE DICTIONARY DOES NOT GUARANTEE AN ORDER OF ACCESS,INSTEAD we can iter through the list again and check their dict values from there
    #this guarantees we are checking the correct k index
    for str in lst:
        if freq[str]==1 and k==0:
            return str
        elif freq[str]==1:
            k-=1
    return 'none'

        

print(kth_distinct_string(['d','db','a','c'],2))
print(kth_distinct_string(['d','d','db','db'],3))
print(kth_distinct_string(['d','d','db','db'],1))
print(kth_distinct_string(['d','d','db','db'],2))

