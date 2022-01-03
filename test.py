from dataclasses import dataclass

@dataclass
class Test:
    test_var1 : int = 1
    test_var2 : int = 2

# board_dim = Test()

print(Test.test_var2)

var = 1

var = ' '
if var == ' ':
    print(' TRUE')
    
var = '7\n'
print(int(var))
var = '\n'
print(int(var))