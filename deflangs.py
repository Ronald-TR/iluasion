import subprocess

class rorun():
    def lua(func):
        def argsfunction(*args, **kwargs):
            def exec_script(func_name, values, script):
                kwargs = ['"' + i + '"' if type(i) == str else str(i) for i in values]
                script += '\n print(' + func_name + '(' + ','.join(kwargs) + '))'
                
                return subprocess.run('lua -e \'' + script + '\'',
                    shell=True,
                    check=True,
                    stdout=subprocess.PIPE).stdout.decode('utf-8')

            def replace_args_in_script(self, name, arguments): # aqui ira o script
                signature = 'local function ' + name
                ascript = self.script
                index = ascript.find(signature) + len(signature)
                params = ascript[index+1:ascript.find(')')]
                arrparams = params.split(',')

                for i in range(0, arrparams.__len__()):
                    params = params.replace(arrparams[i], arguments[i])

                aux = ascript[:index+1] + params + ascript[ascript.find(')'):]

                return aux
            def getattribute(self, name):
                def wrapper(*arg, **kwarg):
                    if name != 'script': # depois alterar para qualquer atributo da classe
                        return exec_script(name, list(arg), self.script)
                    else:
                        return getattr(self, name)
                return wrapper
            setattr(func, '__getattr__', getattribute)
            return func(*args, **kwargs)
        return argsfunction
