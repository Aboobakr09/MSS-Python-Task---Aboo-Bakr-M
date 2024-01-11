mixed_data = [10, 86.4, 24+7j, 'Hello World!', (2,3, 'Welcome'), [3.5, 'Python'], {2,3,4}, True ]

for element in mixed_data:
    print("Elements : ", element, "Data Type: ", type(element).__name__)
    
print("First Three Elements: ", mixed_data[:3])
print("Elements starting from 2 to 5: ", mixed_data[1:5])
print("Last Two Elements: ", mixed_data[-2:])