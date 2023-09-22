""" 
https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode.
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
"""

def encode(strs):
    res = ""
    for s in strs:
        res += f'{len(s)}#{s}'
    return res

def decode(s):
    i = 0
    out = []

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        l = int(s[i:j])
        word = s[j+1 : j + 1 + l]
        out.append(word)
        i = j + 1 + l
    return out


if __name__ == '__main__':
    strs = ['lint', 'code', 'love', 'you']
    # strs = ["we", "say", ":", "yes"]
    print(encode(strs))
    print(decode(encode(strs)))