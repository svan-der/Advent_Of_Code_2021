import filecmp

file = open('input.txt')
content_list = file.readlines()

unique = set(content_list)
print(unique) # only options: 'forward', 'up', 'down'

horizontal_position = 0;
depth = 0;
for line in content_list:
    chunk = line.split(' ')
    if chunk[0] == "forward":
        horizontal_position = horizontal_position + int(chunk[1]);

    elif chunk[0] == "down":
        depth = depth + int(chunk[1]);

    elif chunk[0] == "up":
        depth = depth - int(chunk[1]);

print("This is depth: " + str(depth));
print("This is horizontal position: " + str(horizontal_position));
print("Final outcome is: ", str(horizontal_position * depth));

#--- Part Two --- #

horizontal_position = 0
aim = 0
depth = 0
total = 0
for line in content_list:
    chunk = line.split(' ')
    if chunk[0] == "forward":
        horizontal_position = horizontal_position + int(chunk[1]);
        total = (int(chunk[1]) * aim);
        depth = depth + total;

    elif chunk[0] == "down":
        aim = aim + int(chunk[1]);

    elif chunk[0] == "up":
        aim = aim - int(chunk[1]);

print("This is depth: " + str(depth));
print("This is horizontal position: " + str(horizontal_position));
print("New final outcome is: ", str(horizontal_position * depth));
