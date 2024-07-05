# Generated from Dust.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DustParser import DustParser
else:
    from DustParser import DustParser
from symbol_table import SymbolTable
from tools import check_is_defined,is_valid_class
from error_handler import ErrorHandler
from valid_class import CLASSES

# This class defines a complete listener for a parse tree produced by DustParser.
class DustListener(ParseTreeListener):
    def __init__(self, ):
        # self._depth = 0
        self.scopes = list()
        pass

    # Enter a parse tree produced by DustParser#program.
    def enterProgram(self, ctx:DustParser.ProgramContext):
        # print('program start{')
        # self._depth +=1
        newScope = SymbolTable("program", ctx.start.line, None)
        self.scopes.append(newScope)
        SymbolTable.root = newScope

    # Exit a parse tree produced by DustParser#program.
    def exitProgram(self, ctx:DustParser.ProgramContext):
        # self._depth -=1
        # print('}')
        # self.scopes.pop()
        print('+'+55*'-'+'exitProgram'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass

    # Enter a parse tree produced by DustParser#importclass.
    def enterImportclass(self, ctx:DustParser.ImportclassContext):
        # print(' '*self._depth*4,'import class:',ctx.CLASSNAME())
        if not is_valid_class(ctx.CLASSNAME().getText()):
            ErrorHandler.import_error(ctx.CLASSNAME().getText(),ctx.start.line,ctx.start.column)

    # Exit a parse tree produced by DustParser#importclass.
    def exitImportclass(self, ctx:DustParser.ImportclassContext):
        print('+'+55*'-'+'exitImportclass'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass

    # Enter a parse tree produced by DustParser#classDef.
    def enterClassDef(self, ctx:DustParser.ClassDefContext):
        # print(' '*self._depth*4,'class:',ctx.CLASSNAME(0),end='')
        # if len(ctx.CLASSNAME())>1:
        #     print('/ class parent: ',end='')
        #     for par in ctx.CLASSNAME()[1:]:
        #         print(par,end=' ')
        # print('{')
        # self._depth +=1
        parents = []
        if ctx.CLASSNAME(1) is not None:
            for i in range(1, len(ctx.CLASSNAME())):
                parents.append(ctx.CLASSNAME(i).getText())
        else:
            parents.append("object")
        parents = ",".join(parents)
        identifier = ctx.CLASSNAME(0).getText()
        key = f"class_{identifier}"
        if not SymbolTable.root.insert(key, f"class (name: {identifier}) (parent: {parents})"):
            ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column)
        newScope = SymbolTable(identifier, ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        self.scopes[-1].children.append(newScope)
        self.scopes.append(newScope)

    # Exit a parse tree produced by DustParser#classDef.
    def exitClassDef(self, ctx:DustParser.ClassDefContext):
        # self._depth -=1
        # print(' '*self._depth*4,'}')
        print('+'+55*'-'+'exitClassDef'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass


    # Enter a parse tree produced by DustParser#class_body.
    def enterClass_body(self, ctx:DustParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by DustParser#class_body.
    def exitClass_body(self, ctx:DustParser.Class_bodyContext):
        print('+'+55*'-'+'exitClass_body'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#varDec.
    def enterVarDec(self, ctx:DustParser.VarDecContext):
        # _type = str(ctx.TYPE())
        # classname = str(ctx.CLASSNAME())
        # id = str(ctx.ID())
        # parent = str(type(ctx.parentCtx))

        # if "Parameter" in parent:
        #     if str(ctx.CLASSNAME()) == "None":
        #         classname = _type
        #     print(f"{classname} {id}", end=", ")
        #     return

        # if _type != "None":
        #     print(" "*self._depth*4,f"field: {id}/ type= {_type}")
        #     return
        # print(" "*self._depth*4,f"field: {id}/ type= {classname}")
        fieldType = ""
        identifier = ctx.ID().getText()
        if ctx.CLASSNAME() is None:
            dataType = f"{ctx.TYPE().getText()}, isDefined: True"
        else:
            dataType = f"{ctx.CLASSNAME().getText()}, isDefined: {check_is_defined(ctx.CLASSNAME().getText())}"        
        if ctx.parentCtx.getRuleIndex() == 3:
            fieldType = "ClassField"
        elif ctx.parentCtx.getRuleIndex() == 9:
            fieldType = "MethodVar"
        elif ctx.parentCtx.getRuleIndex() == 10:
            fieldType = "LocalVar"
        else:
            return

        key = f"Field_{identifier}"
        if not SymbolTable.root.insert(key, f"{fieldType} (name: {identifier}) (type: {dataType})"):
            ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column)
        

    # Exit a parse tree produced by DustParser#varDec.
    def exitVarDec(self, ctx:DustParser.VarDecContext):
        print('+'+55*'-'+'exitVarDec'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#arrayDec.
    def enterArrayDec(self, ctx:DustParser.ArrayDecContext):
        # _type = str(ctx.TYPE())
        # classname = str(ctx.CLASSNAME())
        # id = str(ctx.ID())
        # parent = str(type(ctx.parentCtx))

        # if "Parameter" in parent:
        #     if str(ctx.CLASSNAME()) == "None":
        #         classname = _type
        #     print(f"{classname} {id}", end=", ")
        #     return

        # if _type != "None":
        #     print(" "*self._depth*4,f"field: {id}/ type= {_type}")
        #     return
        # print(" "*self._depth*4,f"field: {id}/ type= {classname}")
        identifier = ctx.ID().getText()
        arr_len = ctx.INTEGER().getText()
        if ctx.parentCtx.getRuleIndex() == 3:  # RULE_classbody
            if ctx.CLASSNAME() is None:
                dataType = ctx.TYPE().getText() + ", isDefined: True"
            else:
                dataType = f"{ctx.CLASSNAME().getText()}[], isDefined: {check_is_defined(ctx.CLASSNAME().getText())}"
                
            key = "Field_" + identifier
            if not SymbolTable.root.insert(key, f"ClassField (name: {ctx.ID().getText()}) (type: {dataType}) (len: {arr_len})"):
                ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column)
        

    # Exit a parse tree produced by DustParser#arrayDec.
    def exitArrayDec(self, ctx:DustParser.ArrayDecContext):
        print('+'+55*'-'+'exitArrayDec'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#methodDec.
    def enterMethodDec(self, ctx:DustParser.MethodDecContext):
        # method_name = ctx.ID()
        # type = ctx.getChild(1)
        # print(' '*self._depth*4,'class method:',method_name,'/ return type:',type,'{')
        # self._depth +=1
        newScope = SymbolTable(ctx.ID().getText(), ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        returnType = ""
        identifier = ctx.ID().getText()
       
        if ctx.TYPE() is not None:
            returnType = ctx.TYPE().getText()
        elif ctx.CLASSNAME() is not None:
            returnType = ctx.CLASSNAME().getText()
        parameters_list = []
        if ctx.parameter() != []:
            index = 0
            for parameters in ctx.parameter():  # .typedarg():
                for parameter in parameters.varDec():
                    index += 1
                    if parameter.CLASSNAME() is not None:
                        parameters_list.append(f"[name: {parameter.ID().getText()}, type: {parameter.CLASSNAME().getText()}, len: {index}]")
                    else:
                        parameters_list.append(f"[name: {parameter.ID().getText()}, type: {parameter.TYPE().getText()}, len: {index}]")
        key = "Method_" + identifier
        if not SymbolTable.root.insert(key, f"method (name: {identifier}) (return type: [{returnType}]) (parameter list: [{', '.join(parameters_list)}])"):
            ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column)
        self.scopes.append(newScope)


    # Exit a parse tree produced by DustParser#methodDec.
    def exitMethodDec(self, ctx:DustParser.MethodDecContext):
        # self._depth -=1
        # print(' '*self._depth*4,'}')
        print('+'+55*'-'+'exitMethodDec'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass


    # Enter a parse tree produced by DustParser#constructor.
    def enterConstructor(self, ctx:DustParser.ConstructorContext):
        # print(' '*self._depth*4,'class constructor:',ctx.CLASSNAME(),'{')
        # self._depth +=1
        if ctx.CLASSNAME().getText() != SymbolTable.root.key_name:
            ErrorHandler.constructor_name_error(SymbolTable.root.key_name,ctx.CLASSNAME().getText(),ctx.start.line,ctx.start.column)
        newScope = SymbolTable(ctx.CLASSNAME().getText(), ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        identifier = ctx.CLASSNAME().getText()
        parameterList = []
        if ctx.parameter():
            index = 0
            #parameterList.append("[parameter list: ")
            for entry in ctx.parameter(0).varDec():
                index += 1
                if entry.CLASSNAME():   
                    dataType = entry.CLASSNAME().getText()
                    fullDataType = f"type: {dataType}, isDefined: {check_is_defined(dataType)}"
                else:
                    dataType = fullDataType = f"{entry.TYPE()}, isDefined: True"
                if not SymbolTable.root.insert(f"Field_{entry.ID()}", f"ParamField  (name: {entry.ID()}) ({fullDataType})"):
                    ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column)
                parameterList.append(f"[name: {entry.ID()}, type: {dataType}, len: {index}],")
            parameterList[-1] = parameterList[-1][:-1]
        key = f"Constructor_{identifier}"
        if not SymbolTable.root.insert(key, f"Constructor (name: {ctx.CLASSNAME()}) (return type: []) (parameter list: {parameterList})"):
                    ErrorHandler.duplicate_error(identifier,ctx.start.line,ctx.start.column) 
        self.scopes[-1].children.append(newScope)
        self.scopes.append(newScope)


    # Exit a parse tree produced by DustParser#constructor.
    def exitConstructor(self, ctx:DustParser.ConstructorContext):
        # self._depth -=1
        # print(' '*self._depth*4,'}')
        print('+'+55*'-'+'exitConstructor'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass


    # Enter a parse tree produced by DustParser#parameter.
    def enterParameter(self, ctx:DustParser.ParameterContext):
        # print(self._depth*4*' ','parameter list: [',end='')
        # self._depth +=1
        pass

    # Exit a parse tree produced by DustParser#parameter.
    def exitParameter(self, ctx:DustParser.ParameterContext):
        # self._depth -=1
        # print(']')
        print('+'+55*'-'+'exitParameter'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#statement.
    def enterStatement(self, ctx:DustParser.StatementContext):
        pass

    # Exit a parse tree produced by DustParser#statement.
    def exitStatement(self, ctx:DustParser.StatementContext):
        print('+'+55*'-'+'exitStatement'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#return_statment.
    def enterReturn_statment(self, ctx:DustParser.Return_statmentContext):
        pass

    # Exit a parse tree produced by DustParser#return_statment.
    def exitReturn_statment(self, ctx:DustParser.Return_statmentContext):
        print('+'+55*'-'+'exitReturn_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#condition_list.
    def enterCondition_list(self, ctx:DustParser.Condition_listContext):
        pass

    # Exit a parse tree produced by DustParser#condition_list.
    def exitCondition_list(self, ctx:DustParser.Condition_listContext):
        print('+'+55*'-'+'exitCondition_list'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#condition.
    def enterCondition(self, ctx:DustParser.ConditionContext):
        pass

    # Exit a parse tree produced by DustParser#condition.
    def exitCondition(self, ctx:DustParser.ConditionContext):
        print('+'+55*'-'+'exitCondition'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#if_statment.
    def enterIf_statment(self, ctx:DustParser.If_statmentContext):
        # print(' '*self._depth*4,"nested statement {")
        # self._depth +=1
        newScope = SymbolTable("if", ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        self.scopes[-1].children.append(newScope)
        self.scopes.append(newScope)

    # Exit a parse tree produced by DustParser#if_statment.
    def exitIf_statment(self, ctx:DustParser.If_statmentContext):
        # self._depth -=1
        # print(' '*self._depth*4,"}")
        print('+'+55*'-'+'exitIf_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass

    # Enter a parse tree produced by DustParser#while_statment.
    def enterWhile_statment(self, ctx:DustParser.While_statmentContext):
        # print(' '*self._depth*4,"nested statement {")
        # self._depth +=1
        newScope = SymbolTable("while", ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        self.scopes[-1].children.append(newScope)
        self.scopes.append(newScope)

    # Exit a parse tree produced by DustParser#while_statment.
    def exitWhile_statment(self, ctx:DustParser.While_statmentContext):
        # self._depth -=1
        # print(' '*self._depth*4,"}")
        print('+'+55*'-'+'exitWhile_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass

    # Enter a parse tree produced by DustParser#if_else_statment.
    def enterIf_else_statment(self, ctx:DustParser.If_else_statmentContext):
        # print(' '*self._depth*4,"nested statement {")
        # self._depth +=1
        newScope = SymbolTable("if-else", ctx.start.line, self.scopes[-1])
        SymbolTable.root = newScope
        self.scopes[-1].children.append(newScope)
        self.scopes.append(newScope)

    # Exit a parse tree produced by DustParser#if_else_statment.
    def exitIf_else_statment(self, ctx:DustParser.If_else_statmentContext):
        # self._depth -=1
        # print(' '*self._depth*4,"}")
        print('+'+55*'-'+'exitIf_else_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        scope = self.scopes.pop()
        SymbolTable.root = scope.parent
        pass

    # Enter a parse tree produced by DustParser#print_statment.
    def enterPrint_statment(self, ctx:DustParser.Print_statmentContext):
        pass

    # Exit a parse tree produced by DustParser#print_statment.
    def exitPrint_statment(self, ctx:DustParser.Print_statmentContext):
        print('+'+55*'-'+'exitPrint_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#for_statment.
    def enterFor_statment(self, ctx:DustParser.For_statmentContext):
        pass

    # Exit a parse tree produced by DustParser#for_statment.
    def exitFor_statment(self, ctx:DustParser.For_statmentContext):
        print('+'+55*'-'+'exitFor_statment'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#method_call.
    def enterMethod_call(self, ctx:DustParser.Method_callContext):
        pass

    # Exit a parse tree produced by DustParser#method_call.
    def exitMethod_call(self, ctx:DustParser.Method_callContext):
        print('+'+55*'-'+'exitMethod_call'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#assignment.
    def enterAssignment(self, ctx:DustParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DustParser#assignment.
    def exitAssignment(self, ctx:DustParser.AssignmentContext):
        print('+'+55*'-'+'exitAssignment'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#exp.
    def enterExp(self, ctx:DustParser.ExpContext):
        pass

    # Exit a parse tree produced by DustParser#exp.
    def exitExp(self, ctx:DustParser.ExpContext):
        print('+'+55*'-'+'exitExp'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#prefixexp.
    def enterPrefixexp(self, ctx:DustParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by DustParser#prefixexp.
    def exitPrefixexp(self, ctx:DustParser.PrefixexpContext):
        print('+'+55*'-'+'exitPrefixexp'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#args.
    def enterArgs(self, ctx:DustParser.ArgsContext):
        pass

    # Exit a parse tree produced by DustParser#args.
    def exitArgs(self, ctx:DustParser.ArgsContext):
        print('+'+55*'-'+'exitArgs'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#explist.
    def enterExplist(self, ctx:DustParser.ExplistContext):
        pass

    # Exit a parse tree produced by DustParser#explist.
    def exitExplist(self, ctx:DustParser.ExplistContext):
        print('+'+55*'-'+'exitExplist'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#arithmetic_operator.
    def enterArithmetic_operator(self, ctx:DustParser.Arithmetic_operatorContext):
        pass

    # Exit a parse tree produced by DustParser#arithmetic_operator.
    def exitArithmetic_operator(self, ctx:DustParser.Arithmetic_operatorContext):
        print('+'+55*'-'+'exitArithmetic_operator'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#relational_operators.
    def enterRelational_operators(self, ctx:DustParser.Relational_operatorsContext):
        pass

    # Exit a parse tree produced by DustParser#relational_operators.
    def exitRelational_operators(self, ctx:DustParser.Relational_operatorsContext):
        print('+'+55*'-'+'exitRelational_operators'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass


    # Enter a parse tree produced by DustParser#assignment_operators.
    def enterAssignment_operators(self, ctx:DustParser.Assignment_operatorsContext):
        pass

    # Exit a parse tree produced by DustParser#assignment_operators.
    def exitAssignment_operators(self, ctx:DustParser.Assignment_operatorsContext):
        print('+'+55*'-'+'exitAssignment_operators'+55*'-'+'+')
        SymbolTable.root.print_table()
        pass
    
   
    



del DustParser