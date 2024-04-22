#dict without parameter
def fouziya():#function 
    return "this is my bank balance"
test_dict={"fname":fouziya,"age":19,"address":"ballari"}
print("the original dictionary:",str(test_dict))#dict and function return type string
res=test_dict['fname']()#calling function
print("the required call result:",str(res))