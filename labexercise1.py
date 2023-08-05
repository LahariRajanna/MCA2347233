intro = "Hi I'm Lahari, student of MCA-B with regno. 2347233. I've choosen Railways management as my domain. The distance from my home to college is 13.4 kms."
#word counting
def count_word(paragraph, target_word):
     words= paragraph.split()
     word_count = 0
     for word in words:
         word = word.strip(',.!?()[]{}"\ ')
         if word.lower() == target_word.lower():
             word_count += 1
     return word_count

paragraph= input("enter the paragraph from which you want to find the word count:") 
target_word= input("enter the word that you want to count:")
frequency=count_word (paragraph, target_word)
print(f"The word '{target_word}' appears {frequency} times in the paragraph.")

num=["0","1","2","3","4","5","6","7","8","9"]
s_word=intro.split(" ")
for i in s_word:
     for j in i:
         if j in num:
             if "." in i:
                 print (i," is float")
                 break
             else:
                 print(i, "is int")
                 break
         else:
             print(i," is string")
             break
     
def count_char(paragraph):
     alphabets= 0
     numerics= 0
     specials= 0
     
     for char in paragraph: 
         if char.isalpha(): 
             alphabets += 1
         elif char.isnumeric():
             numerics += 1 
         else:
             specials += 1
     return alphabets, numerics, specials

paragraph = "Hi I'm Lahari, student of MCA-B with regno. of 2347233. The distance from my home to college is 13.4 kms."
def count_char(paragraph):
     alphabets= 0
     numerics= 0
     specials= 0
     
     for char in paragraph: 
         if char.isalpha(): 
             alphabets += 1
         elif char.isnumeric():
             numerics += 1 
         else:
             specials += 1
     return alphabets, numerics, specials
alpha, num, schar= count_char(paragraph)
print(f"Alphabets: {alpha}") 
print(f"Numeric characters: {num}")
print(f"Special symbols: {schar}")

#sorting the set
def set_op():
     string_set= {"Bengaluru", "Mangaluru", "Mysuru"}
     print("Initial Set:", string_set)
     sorted_set =sorted(string_set, reverse=True) 
     print("Sorted Set (Descending Order):", sorted_set)
set_op()

#packing and unpacking of tuple
def tuple_op():
     #packing
     Cities= ("Bengaluru", "Mysuru", "Mangaluru")
     print("Original Tuple:", Cities)
     
     #unpacking
     BengaluruStation1, MysuruStation2, MangaluruStation3= Cities
     print("\nUnpacked Variables: ")
     print("City 1:", BengaluruStation1)
     print("City 2:", MysuruStation2)
     print("City 3:", MangaluruStation3)
tuple_op()

def set_operations_example():
    mixed_set = {1, "Bengaluru", 2.263, True, (1, 2)}
    print("Initial Set:", mixed_set)
    popped_element = mixed_set.pop()
    print("\nElement popped:", popped_element)
    print("Updated Set after pop:", mixed_set)
    mixed_set.clear()
    print("\nSet after clear:", mixed_set)
    mixed_set.add(42)
    mixed_set.add("Bengaluru")
    mixed_set.add("Managluru")
    mixed_set.add(False)
    mixed_set.add((3, 4))
    mixed_set.update(["Bengaluru","Managluru","Mysuru","Davengere"])  
    print("Set after adding elements:", mixed_set)
    mixed_set.discard("Managluru")
    print("\nSet after discarding 'Managluru':", mixed_set)
    del mixed_set
set_operations_example()

d_name=("R","a","i","l","w","a", "y")
count=0
for i in d_name:
     count=count+1
print("count of r", count)

#tuple slicing
def  slice_neg_index(domain_name): 
     print("Original Domain Name:", domain_name) 
     print("\n Positive Slicing:")
     print("1. Slicing from index 3 to 9:", domain_name[3:10])
     print("2. Slicing from index 0 to 7:", domain_name[:8])
     print("3. Slicing from index 5 to the end: ", domain_name [5:])
     print("4. Slicing from index 2 to 11 with step 2:", domain_name[2:12:2])
     print("\nNegative Slicing:")
     print("1. Slicing from the end -8 to the end -3:", domain_name [-8:-2])
     print("2. Slicing from the end -11 to the end -1 with step 2:",domain_name[-11:-1:2])
     print("\nNegative Indexing: ")
     print("Last character:", domain_name[-1])
     print("Second to last character:", domain_name [-2]) 
domain_name = "railways management"
slice_neg_index (domain_name)