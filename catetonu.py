def label_encode(data):
    mapping = {}
    encoded_data = []
    for column in zip(*data):
        unique_values = sorted(set(column))
        for i, value in enumerate(unique_values):
            mapping[value] = i
        encoded_column = [mapping[value] for value in column]
        encoded_data.append(encoded_column)
    return list(zip(*encoded_data)), mapping
def enter_input():
    data = []
    num_columns = int(input("enter num of columns: "))
    for i in range(num_columns):
        column_data = input(f"enter values of column {i+1}: ").strip().split()
        data.append(column_data)
    return data
data = enter_input()
encoded_data, mapping = label_encode(data)
print("encoded data:")
for row in encoded_data:
    print(row)
print("mapping:")
print(mapping)
