
file = open('Input.txt')
content_list = file.readlines()

increased = 0;
for index, elem in enumerate(content_list):
    if index > 0:
        prev_el = int(content_list[index - 1])
        curr_el = int(elem)
        if curr_el > prev_el:
            increased += 1;
            incr = True;
        else:
            incr = False;
        print(index, prev_el, curr_el, increased, incr)

print("Total depths increased: " + str(increased))
