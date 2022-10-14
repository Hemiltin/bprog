# String
from re import I


a = "hello"
print (a)
print (type(a))

# interger
b = 12
print (b)
print (type(b))

# float
c = 10.5
print (c)
print (type(c))

# tuple
d = 20,5
print (d)
print (type(d))

# data complex
e = 1j
print (e)
print (type(e))

z = complex ('5-9j')
print (z)

# type data list
f = ["a","b","c"]
print (f)
print (type(f))

#contoh 
list_f = [1,2,3]
print (list_f[0])
#contoh tuple
tuple_f = 1,2,3
print (tuple_f[0])

#contoh set
set_f = {1,2,3}
print (set_f)

# type data set
g = {"a","b","c"}
print (g)
print (type(g))

#type data frozenset
h = frozenset({1,2,3})
print (type(h))

#type data boolean
i = True
j = False
print (i,j)
print (type(i))
print (type(j))

#variabel
a = "Hemiltin adilah"
def func():
    a = "datang"
    print ("selamat "+ a)
func()
print (a)

#definisi
def tambah():
    a = 10
    b= 15
    c= a+b
    print (c)

tambah()

#parameter
def data(nama,nim):
    print(f"nama saya {nama} dan nim {nim}")
data ("Hemiltin Adilah","20210801147")

#contoh
def total(sisi):
    return sisi*sisi


def segitiga(alas,tinggi):
    return 0.5*alas*tinggi