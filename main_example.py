from deflangs import rorun

@rorun.lua
class meuscript():
    def __init__(self, n):
        if n == 0:
            self.script = """
            local function bem_vindo(param)
                return "bem vindo ao lua wrapper! " .. param .. "!"
            end
            """
        elif n == 1:
            self.script = """
            local function sum(a, b)
                return a + b
            end
            """


result = meuscript(0).bem_vindo('Ronald')
print(result)
result = meuscript(1).sum(2, 2)
print('O resultado é: ', result)

# output
# bem vindo ao lua wrapper! Ronald!
# O resultado é: 4
