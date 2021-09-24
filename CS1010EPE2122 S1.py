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
            

            
                
                
                
    
