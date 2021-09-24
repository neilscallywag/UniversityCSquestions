'''
Part 1 Run-length Decoding (15 + 15 = 30 marks)
Run-length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same
data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the
original run. This technique is extremely useful especially in data compression.
Assuming we have a string with ASCII characters. Each run of consecutive data item is represented as that item with its
count. Here is an example of RLE.
‘AAAAAAAAAHHHEEM’ → ‘A9H3E2M1’
You can see that the string with 15 characters on the left is converted to a string with 8 characters only.
However, we want you to write a function to perform the reverse, namely, run-length decoding (RLD) as the following
example:
‘A9H3E2M1’ → ‘AAAAAAAAAAHHHEEM’
In this part, you can assume that the input is a string with even number of characters. Each ASCII character is followed
by its count in an integer between 1 to 9. So, you will not have an input like ‘B11C2’.
Task 1 Iterative Run-length Decoding (15 marks)
Write an iterative version of the function RLD_I(s) to decode a string s mentioned above. In this task, you cannot use
any recursion.

'''
def RLD_I(s):
    char = []
    numbers = []
    token=''
    for x in s:
        if x.isalpha():
            char.append(x)
        elif x.isdigit():
            numbers.append(int(x))
    for index in range(len(char)):
        token+= numbers[index]*char[index]
    return token
        
print(RLD_I('H3e2l3o1W1o3r4l2d1'))

'''
Remember Alice in Wonderland? She drank a potion and made her shrink. The magic potion can change her height!

Now, these magic potions are available for everyone! And not only by shrinking, it can also make you grow taller!
However, because of the limitation of our current “technology”, we only have two types of potions now:
● Potion A: Make someone to grow 1 cm taller
● Potion B: Make someone’s height shrink by half, but this potion is only effective if the height is an even number
in cm.
Let’s have an example, if Alice is 4 cm tall now, and she wants to change her height to 3 cm, we can either
● Drink one Potion B (4 cm  2 cm) then one Potion A (2 cm  3 cm), or
● Drink two Potions A (4 cm  6 cm) then one Potion B (6 cm  3 cm).
The first choice needs two potions and the second choice needs three potions.
However, the potions are still new, we tried not to take as many as possible because we are afraid if there is any side
effect. So in the above example, the optimal way to take the potions is the first choice (Potion B then Potion A).
Task 1 Magic Potion Treatment (25 marks)
Given the initial and final heights as two integers h1 and h2 in cm respectively, write a function
magicPotionTreatment(h1,h2) to return the string of the potion process with the minimal number of potions
that change the height from h1 to h2
'''

#This is an already optimised solution 
def magicPotionTreatment(h1,h2):
    def potionA(height):
        height +=1
        return height
    def potionB(height):
        if height % 2==0:
            height /=2
            return height
        else:
            return None
    string = ''
    count = 0
    while h1 != h2:
        if h1 < h2:
            h1 = potionA(h1)
            count +=1
        string += "A"*count
        if h1 > h2:
            if h1%2 == 0:
                h1 = potionB(h1)
                string += "B"
            else:
                h1 = potionA(h1)
                string +='A'
            
    return string

if magicPotionTreatment(134217729,3) == "ABABABABABABABABABABABABABABABABABABABABABABABABABAB":
    print(True)
else:
    print(False)
            

            
                
                
                
    
