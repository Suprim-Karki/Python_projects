''' Temperature Converter '''

def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

temp=input("Enter temperature in fareenheit to convert into celsius: ")
print(convert(temp))