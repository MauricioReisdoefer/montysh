from montysh import PsyFileReader, Interpreter, BaseCommand

# comando echo: imprime os argumentos
def echo(*args):
    return " ".join(args)

echo_cmd = BaseCommand("echo", echo)

# comando sla: apenas um exemplo divertido
def sla(*args):
    return "Slaaaaa! 😎 " + " ".join(args)

sla_cmd = BaseCommand("sla", sla)

# comando add: soma números passados como argumentos
def add(*args):
    try:
        numbers = [int(a) for a in args]
    except ValueError:
        raise ValueError("Todos os argumentos de 'add' devem ser números")
    return sum(numbers)

add_cmd = BaseCommand("add", add)

# cria o interpretador
interpreter = Interpreter()

# registra alguns comandos
interpreter.register(echo_cmd)
interpreter.register(sla_cmd)
interpreter.register(add_cmd)

# cria o leitor de arquivos
reader = PsyFileReader(interpreter)

# executa um arquivo .psy
reader.run_file("script.psy")
