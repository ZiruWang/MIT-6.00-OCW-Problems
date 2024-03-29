from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,'and',key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
        

def subStringMatchExact(target,key):
    index1 = ();
    start = 0;
    while(find(target,key,start) != -1):
        index1 = index1 + (find(target,key,start),);
        start = find(target,key,start) + 1;

    return index1

# For the matches of 'atg', they use both ''+ 'atg' and 'atg' + ''. 

##def constrainedMatchPair(firstMatch,secondMatch,length):
##    index1 = ();
##    for n in range(0,len(firstMatch)):
##        flag = 0;
##        m = 0;
##        while(flag != 1 and m < len(secondMatch)):
##            if firstMatch[n] + length + 1 == secondMatch[m]:
##                flag = 1;
##                index1 = index1 + (firstMatch[n],);
##            m += 1;
##
##    return index1


def constrainedMatchPair(firstMatch,secondMatch,length):
    index1 = ();
    for n in range(0,len(firstMatch)):
        for m in range(0,len(secondMatch)):
            if firstMatch[n] + length + 1 == secondMatch[m]:
                index1 = index1 + (firstMatch[n],);
                break

    return index1

target = target1;
key = key12;
     
print subStringMatchOneSub(key,target)
    







                



