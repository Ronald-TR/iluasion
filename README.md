# iluasion
Run Lua methods dinamicaly and rescue their returns inside python!
## Go! Try it yourself!
* Clone the repo or download the sources
* import the module and the rorun class decorator
* Create a class with an attribute named **script** (mandatory)
* Call your Lua methods inside your Python Object like any native method!!!!
* And have fun learning and switching between both of them at same time!

#### Easy, quick, pratical and fun usage
```Python
@rorun.lua
class MeuScriptLua():
    def __init__(self):
        self.script = """
        local function bem_vindo(param)
            return "bem vindo ao lua wrapper! " .. param .. "!"
        end
        """
``````
And call:
```Python
result = MeuScriptLua().bem_vindo('Desenvolvedor')
```
The output be reference the behavior of your lua script!

output:
```bem vindo ao lua wrapper! Desenvolvedor!```

And some basic mathematic expression:

```Python
@rorun.lua
class MeuScriptLua():
    def __init__(self):
        self.script = """
        local function sum(a, b)
            return a + b
        end
        """
``````
And as the example above:
```Python
result = MeuScriptLua().sum(2, 2)
print('O resultado da soma é: ', result)
```
output:
```
O resultado da soma é: 4
```

enjoy

**beta**
