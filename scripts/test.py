@Class
class test_uds():
    def __init__(self,test_case='read_errcode'):
        self.test_case=test_case
    def print_case(self):
        print(self.test_case)
        
def main():
    T = test_uds(test_case="UDS")
    T.print_case()
    print "%d--%d" % (13,14)
    return "%d--%d" % (13,14)

def fun(v1,v2):
    #tuple_init = (1,2,3,4)
    list_init = [1,2,3,56]
    for x in tuple_init:
        print x
    for y in list_init:
        print y
    return v1*v2
    
main()