with open("E:\Aboobakr (E)\MSS\product_descriptions.txt", 'r') as product_descriptions:
    with open("E:\Aboobakr (E)\MSS\ formatted_descriptions.txt", 'w') as formatted_descriptions:
        for line in product_descriptions:
            formatted_descriptions.write(line.title())
            
#Opens the Product Description txt to read the content. -> Line 1
#Opens the Formatted Description txt to write content. --> Line 2
#Using for loop, every line in the product description is read and is written in the formatted description. -> Line 3
#Using the title() method, the first letter in each word becomes capitalize. -> Line 4

#By using With Function, the files closes automatically and file.closed() is not necessary.
#First Text capitalization can be done by using strip().capitalize() method also.
