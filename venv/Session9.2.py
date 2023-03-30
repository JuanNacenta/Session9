# def my_simplest_function():
#    pass

# my_simplest_function()

def greet():
    print ("Hello dear, hope you're doind fine")

# for hace un loop range times
for i in range (10):
    print(f"{i+1} ", end="")
    greet()

x = greet()
print(x)
# It will give you none, because it is a fuction
# greet()
# greet()
# greet()