import math
def VFloatFromSEM(s, e, m):
    print("m is " + str(m))
    print("s is " + str(s))
    print("e is " + str(e))
    v = str((s*-2 + 1) * m * (2**e))
    return v

def binToDec(bin):
    dec = 0
    bits = len(bin)
    for i in range(bits):
        dec += (2**(bits - i - 1) * int(bin[i:i+1]))
    return dec

def decToBin(dec):
    bin = ""
    while (dec > 0):
       # print(str(dec))
        bin = str(dec % 2) + bin
        dec = dec//2
    return bin

#
# def fracCutZeros(frac):
#     bit = 0
#     index = len(frac) - 1
#     while (not bit and index > 0):
#         bit = int(frac[index])
#         index -= 1
#     return frac[: index + 2]

# def intLog(int, base):
#     log = 0
#     while (int > 1):
#         int = int//base
#         log += 1
#     return log

# def getIntFromFloatString(string):
#     int_str = ""
#     i = 0
#     while (string[i] != '.' and i < len(string)):
#         int_str += string[i]

#     return int(int_str)

print ("mode selection")
print ("A: SEM to decimal point value")
print ("B: binary representation to fraction + decimal value")
print ("C: binary to decimal")
print ("D: decimal to binary")
print ("E: floating point in decimal to binary representation")

mode = input()
if (mode == "A"):
    print("S?")
    s = int(input())
    print("E?")
    e = int(input())
    print("M?")
    m = float(input())
    print(VFloatFromSEM(s, e, m))
#this was hard
if (mode == "B"):
    print("binary representation?")
    bin = input()
    print("bits for exp?")
    expBits = int(input())
    bias = 2**(expBits - 1) - 1
    print("bias is " + str(bias))
    exp = bin[1: expBits+1]
    frac = bin[expBits + 1:]
    print("exp is " + exp)
    print("frac is " + frac)
    s = int(bin[0])
    e = binToDec(exp) - bias
    #but i did it
    m = 1 + binToDec(frac)/(2**(len(bin) - expBits - 1))
    print(VFloatFromSEM(s, e, m))

if (mode == "C"):
    print("binary?")
    bin = input()
    print(str(binToDec(bin)))
if (mode == "D"):
    print ("decimal?")
    dec = int(input())
    print("decimal is " + str(dec))
    print(decToBin(dec))

#doing this a mildly stupid way for now. 
#i hate it i hate doing it theres definitely a more efficient way but like
#i have math hw and i got kind of wild abt finishing this and
if (mode == "E"):
    print ("decimal?")
    dec = float(input())
    s = "0"
    if (dec < 0.0):
        s = "1"
        dec = abs(dec)
    if (dec == 0.0):
        print("it's just a bunch of 0s")
    else: 
        print ("how many bits total?")
        total = int(input())
        print ("how many bits for exp?")
        expBits = int(input())
        bias = 2**(expBits - 1) - 1
        fracBits = total - expBits - 1
        e = math.floor(math.log2(dec))
        if (e < (1-bias)):
            e = 1 - bias
            f = dec/(2**(e - total))
        if (e > (bias * 2)):
            print("this is out of range, but can be represented as infinity")
        else:
            f = dec/(2**(e - fracBits)) - (2** fracBits)
        if (f - int(f) == 0.5):
            print("danger: rule to round to even totally ignored, you have to do this by hand at least for now")
        fracNoZeros = decToBin(round(f))
        zeros = ""
        for i in range(fracBits- len(fracNoZeros)):
            zeros += "0"
        frac = zeros + fracNoZeros
        expNoZeros = decToBin(e + bias)
        zeros = ""
        for i in range(expBits - len(expNoZeros)):
            zeros += "0"
        exp = zeros + expNoZeros
        print("e is: " + str(e))
        print("f is: " + str(f))
        print("s is: " + s)
        print("exp is " + exp)
        print("frac is: " + frac)
        print("the whole thing is " + s + exp + frac)
        
        




