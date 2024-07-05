from symbol_table import SymbolTable
from valid_class import CLASSES

def check_is_defined(_class):
    if SymbolTable.root.lookup_table("import_" + _class) is None and SymbolTable.root.lookup_table("class_" + _class) is None:
        return False 
    return True

def is_valid_class(_class):
    return _class in CLASSES