from color import Color
CRED = '\033[91m'
CEND = '\033[0m'
def printerr(msg):
    print(Color.FAIL)
    print(msg)
    print(Color.END)

class ErrorHandler:
    def duplicate_error(var_name,line,column):
        printerr(f"duplicate error:[{line}:{column}] {var_name}")

    def import_error(class_name,line,column):
        printerr(f"import class error:[{line}:{column}] {class_name}")
    
    def method_call_error(method_name,line,column):
        #idk
        printerr(f"method call error:[{line}:{column}] {method_name}")
        pass

    def constructor_name_error(class_name,constructor_name,line,column):
        printerr(f"constructor name error:[{line}:{column}] class name \"{class_name}\" but constructor name \"{constructor_name}\"")
        pass

    def index_out_of_range_error(var_name,index,len,line,column):
        # ta shab ishalla
        printerr(f"index out of range error:[{line}:{column}] {index} out of range {var_name}[{len-1}]")
        pass
    
    def undefined_variable_error(var_name,line,column):
        #done but don't use lookup method in symbole table
        printerr(f"undefined variable error:[{line}:{column}] undefined variable with name {var_name}")
        pass 




