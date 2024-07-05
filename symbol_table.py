from tabulate import tabulate
from error_handler import ErrorHandler
from color import Color

class SymbolTable:
    instances = []
    root = None

    def __init__(self, key_name, scope_num, parent=None):
        self.key_name = key_name
        self.scope_num = scope_num
        self.parent = parent
        self.children = []
        self.table = {}
        SymbolTable.instances.append(self)

    def insert(self, idef_name, values):
        print(f"inser id {idef_name} with value {values} in table {self.table}")
        if idef_name in self.table.keys():
            if values == self.table.get(idef_name):
                return False
            else:
                _parent = self.parent
                while _parent != None:
                    if idef_name in _parent.table.keys():
                        print('key finded')
                        if values == _parent.table.get(idef_name):
                            print('value finded')
                            return False
                    _parent = _parent.parent
        self.table[idef_name] = values
        return True

    def lookup_table(self, idef_name):
        this = self
        while this != None:
            if idef_name in this.table.keys():
                return this.table.get(idef_name)
            this = this.parent
        return None

    def print_symbols(self):
        head = ['',Color.HEADER+'keys'+Color.END,Color.HEADER+'value'+Color.END]
        data = []
        for item_num, (key, value) in enumerate(self.table.items(), start=1):
            key = Color.BLUE+ f"{key}" + Color.END
            value = Color.YELLOW + f"{value}" + Color.END
            data.append([item_num,key,value])

        return tabulate(data,headers=head,tablefmt="fancy_outline")

    def print_table(self):  # ToString
        output = "═" * 45 + f" {self.key_name}: {self.scope_num} " + "═" * 45 + '\n'
        output += self.print_symbols() if self.table else "\n"
        print(output)
        if self.parent is not None:
            output += self.parent.print_table()
        return output