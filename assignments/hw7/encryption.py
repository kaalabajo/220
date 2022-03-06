def encode(my_msg, my_key):
    code = ""
    for letter in my_msg:
        num = ord(letter)
        code = code + chr(num + my_key)
    return code



def encode_better(code,key):

    track_code = []
    track_key = []
    for letter in code:
        track_code.append(ord(letter) - 65)
    for letter in key:
        track_key.append(ord(letter) - 65)
    #print(track_code,track_key)
    # make a new list to keep track of the number versions
    nums = []
    for i in range(len(code)):
        looped = int(track_code[i]) + int(track_key[i % len(key)])
        nums.append(looped%58)

    # ciphered is a blank string that will add all our letters
    ciphered = ''
    for i in nums:
        ciphered = ciphered + chr(i+65)
    return ciphered