s = "babad"

length = len(s)
max_str = ""

for i in range(length):
    for j in range(length - i):
        start_pos = i
        end_pos = i + j + 1

        s1 = s[start_pos: end_pos]
        if s1 == s1[::-1]:
            if len(s1) > len(max_str):
                max_str = s1
print(max_str)