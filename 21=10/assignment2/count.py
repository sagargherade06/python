def frequency_count(s):
    frequency={}
    for char in s:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
samplestring='ogool.com'
frequency=frequency_count(samplestring)
print(frequency)