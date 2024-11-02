# return kth distinct string in a list of strings
def kth_distinct_string(lst,k):
    # make a frequency table
    freq ={}
    for str in lst:
        if str not in freq:
            freq[str]=1
        else:
            freq[str]+=1

