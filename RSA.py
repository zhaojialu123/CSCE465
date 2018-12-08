import random
import math
# using Euclidean algorithm to do GCD
import time

def gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

# prime number checker
def isPrime(n):
    
    if n == 0 or n == 1: # 0 and 1 are not primes 
        return False
    if n == 2: # 2 is the smallest prime number 
        return True
    else:
        isprime = True
        for i in range(2, n):
            if n % i == 0:
                isprime = False
        return isprime


# prime generator
def prime_generator():
    primes = [i for i in range(2,1000) if isPrime(i)]
    n = random.choice(primes)
    return n

def eea(a,b):
	if b==0:return (1,0)
	(q,r) = (a//b,a%b)
	(s,t) = eea(b,r)
	return (t, s-(q*t) )

# Find the multiplicative inverse of x (mod y)
# see: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def generate_private(x,y):
	inv = eea(x,y)[0]
	if inv < 1: inv += y #we only want positive values
	return inv


def encrypt(plaintext, e, n):
    return math.fmod(pow(plaintext, e), n)
 
def decrypt(ciphertext, d, n):
    return math.fmod(pow(ciphertext, d), n)




# welcome to our RSA calculator
print("Welcome to RSA calculator!")

#  generate two primes number 
p = int(input("Please enter a prime number:\n(You can enter 0 to use prime generator to generate one)\n"))

if p == 0:
    p = prime_generator()
else:
    while isPrime(p) != True:
        p = int(input("The number you enetered is not prime number, please try again:\n(You can enter 0 to use prime generator to generate one)\n"))
        if p == 0:
            p = prime_generator()
print("p is:" , p)


q = int(input("Please enter another different prime number:\n(You can enter 0 to use prime generator to generate one)\n"))

if q == 0:
    q = prime_generator()

while q == p:
    q = int(input("The number you entered is same as the first one, please try again:\n(You can enter 0 to use prime generator to generate one)\n"))
while isPrime(q) != True:
    q = int(input("The number you enetered is not prime number, please try again:\n(You can enter 0 to use prime generator to generate one)\n"))

print("q is:" , q)

# generate public key
print("Generating public key now...")
n = p * q

phi = (p-1) * (q-1)

# small component e
e = 2

# e has to be comprime with phi
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
       e = e + 1

print("The public key is:", e)

# k is always 2
k = 2

# generate private key
print("Generating private key now...")

d = generate_private(e, phi);
print("The private key is:", d)

# encrypt message using private key 
plaintext = float(input("Please enter the message that you want to encrypt:"))
print("Encrypting message now...")


ciphertext = encrypt(plaintext, e, n)


print("The cipher text of your message is:", ciphertext)

print("Decrypting the message with private key:")

t0 = time.time()
decrypted_text = decrypt(ciphertext, d, n)
t1 = time.time()
print(t1-t0)

print("Your original message is:", decrypted_text)

print("Thank you!")






           

