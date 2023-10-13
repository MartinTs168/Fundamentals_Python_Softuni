line = input().split()
while True:
    command_details = input().split()
    command = command_details[0]
    if command == "3:1":
        break
    elif command == "merge":
        start_index = int(command_details[1])
        end_index = int(command_details[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(line) - 1:
            end_index = len(line) - 1
        merged_elements = ''.join(line[start_index:end_index + 1])
        line[start_index:end_index + 1] = [merged_elements]
    elif command == "divide":
        index = int(command_details[1])
        partitions = int(command_details[2])
        divided_partition = []
        element = line[index]
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(element[current_element_index*partition_length:(current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index*partition_length:])
        line[index:index + 1] = divided_partition
print(' '.join(line))
