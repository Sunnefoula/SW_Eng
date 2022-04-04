class ThisIsCustomException(Exception):
    pass


sample_dict = {"a": 1}

print(sample_dict)
print(sample_dict["a"])
a=1
b=0
try:
    if b == 0:
        raise ThisIsCustomException
    c=a/b
    print(sample_dict["b"])
except KeyError:
    print("key Error")
except ThisIsCustomException:
    print("my exception")
except ZeroDivisionError:
    c = a/1
except Exception as e:
    print("oh, No!!", str(e))
finally:
    print("finally block")

#print("c=",c)
print("the End")
