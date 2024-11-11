# --- Lambda Functions ---
# Lambda functions Python mein chhote, anonymous functions hain jo 'lambda' keyword se bante hain.
# Ye short operations ke liye use kiye jaate hain, jahan ek poora function define karna zaroori nahi hota.
# Syntax: lambda arguments: expression

# Ek lambda function banate hain jo kisi number ka square calculate karega
f = lambda x:x * x   # Lambda function jo number ko square karega

# Lambda function ko 10 argument ke saath call karte hain
result = f(10)

# f(10) ka result print karte hain, jo ki 100 hai
print(f(10))  # Output: 100
print(result)  # Output: 100


# --- Cube Calculation Regular Function aur Lambda ke Saath ---

# Ek regular function jo kisi number ka cube calculate karega
def cube(n):
    return n ** 3  # Function jo n ka cube return karega

# Cube function ko argument 3 ke saath call karte hain
print(cube(3))  # Output: 27

# Lambda function jo kisi number ka cube calculate karega
c = lambda x: x ** 3  # Lambda function jo cube calculation karega

# Lambda function ko argument 3 ke saath call karte hain
print(c(3))  # Output: 27


# --- Do Numbers ka Sum Regular Function aur Lambda ke Saath ---

# Ek regular function jo do numbers ko add karega
def add(x, y):
    return x + y  # x aur y ko add karta hai aur result return karta hai

# Add function ko 5 aur 6 arguments ke saath call karte hain
print(add(5, 6))  # Output: 11

# Lambda function jo do numbers ka sum karega
s = lambda x, y: x + y  # Lambda addition ke liye

# Lambda function ko 5 aur 6 arguments ke saath call karte hain
print(s(5, 6))  # Output: 11


# --- Conditional Logic in Lambda ---
# Hum lambda functions mein condition bhi use kar sakte hain.
# Yahan lambda 'YES' return karega agar number even hai, nahi toh 'NO'

# Lambda function jo check karega agar number even hai ya odd
y = lambda x: 'YES' if x % 2 == 0 else 'NO'  # Agar even hai toh 'YES', odd hai toh 'NO' return karega

# Lambda function ko ek odd number ke saath test karte hain
print(y(5))  # Output: 'NO' (kyunki 5 odd hai)


# --- Filter Function ---
# Filter function ek iterable (jaise list) ke har element par ek function apply karta hai aur sirf wahi elements return karta hai jo True hote hain.
# Syntax: filter(function, iterable)

# Ek list of numbers define karte hain
lst = [6, 7, 8, 9]

# Filter function ko lambda ke saath use karte hain taaki even numbers list mein se mil sakein
# Lambda function tabhi True return karega jab number even ho
answer = list(filter(lambda x: x % 2 == 0, lst))

# Filtered result ko print karte hain, jismein sirf even numbers hone chahiye
print(answer)  # Output: [6, 8]

# Filtered result ke har even number ko loop ke saath print karte hain
for i in answer:
    print(i)  # Output karega 6 aur fir 8


# --- Filter Function aur Lambda ka Use Odd Numbers Filter Karne ke Liye ---

# Phir se list define karte hain (ye step redundant hai agar list mein koi change na hua ho)
lst = [6, 7, 8, 9]

# Filter function ko use karte hain odd numbers dhoondhne ke liye list mein
# Lambda function tabhi True return karega jab number odd ho
answer = list(filter(lambda x: x % 2 != 0, lst))

# Filtered result ko print karte hain, jismein sirf odd numbers hone chahiye
print(answer)  # Output: [7, 9]


# --- Map Function ---
# Map function ek function ko ek iterable ke har element par apply karta hai aur ek naye list mein result ko store karta hai.
# Syntax: map(function, iterable)

# Ek list define karte hain
lst2 = [23, 4, 5, 6, 7]

# Map function use karte hain, jisme lambda function har element mein 2 add karega
resultMap = list(map(lambda x: x + 2, lst2))

# Map function ka result print karte hain
print(resultMap)  # Output: [25, 6, 7, 8, 9]


# --- Reduce Function ---
# Reduce function iterable mein se elements ko combine (reduce) karta hai ek single output mein.
# Yeh 'functools' module se import karna padta hai kyunki yeh Python mein default nahi hota.

# Functools module se reduce function import karte hain
from functools import reduce

# Reduce function use karte hain jisme lambda function har element ko multiply karega
resultReduce = reduce(lambda a, b: a * b, lst2)

# Reduce function ka result print karte hain
print(resultReduce)  # Output: 19320 (product of all elements in lst2)
