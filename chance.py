
saved_list = []
counter = 0

for a in range(1, 26):
    for b in range(1, 26):
        for c in range(1, 26):
            if (a != b) and (a != c) and (b != c):
                if (a%3==0) or (b%3==0) or (c%3==0):
                    temp_list = [a, b, c]
                    temp_list.sort()
                    if temp_list not in saved_list:
                        saved_list.append(temp_list)
                        counter += 1

ofile = open('out_chance.txt', 'w')
ofile.write(str(saved_list))

print(saved_list)
print("counter = ", counter)