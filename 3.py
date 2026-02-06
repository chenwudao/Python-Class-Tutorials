def function(s):
    for i in range(len(s)):
        count=0
        for j in range(i):
            if s[i]==s[j]:
                count+=1
                if count==1:
                    return s[i]
    return None

e = "abccaz"
print(function(e))