class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        str_len = ""
        strs = []

        while i < len(s):
            if s[i] != "#":
                str_len += s[i]
                i +=1
            else:
                i+=1
                int_len = int(str_len)
                str_len = ""
                string = ""
                for j in range(i, i + int_len):
                    string += s[j]
                strs.append(string)
                i += int_len
        
        return  strs
