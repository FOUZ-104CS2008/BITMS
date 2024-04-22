#with parameter
def fouziya(a,b):#function 
    print("my result bank balance=",a+b)
test_dict={"fname":fouziya,"age":19,"address":"ballari"}
print("the original dictionary:",str(test_dict))#dict and function return type string
test_dict["fname"](10,20)#calling function
