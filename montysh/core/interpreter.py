from montysh.commands import BaseCommand

class Interpreter:
    def __init__(self):
        # Registred commands
        self.commands: dict[str, BaseCommand] = {}

    def register(self, command: BaseCommand):
        """Register a new command line in the Interpreter"""
        self.commands[command.name] = command

    def run_line(self, line: str):
        """Interpret a single line of code"""
        parts = line.strip().split()
        if not parts:
            return None
        
        name, *args = parts
        cmd = self.commands.get(name)

        if not cmd:
            raise ValueError(f"Comando não encontrado: {name}")

        return cmd(*args)

    def _register_builtins(self):
        # echo
        self.register(BaseCommand("echo", lambda *args: " ".join(args)))
        # time
        self.register(BaseCommand("time", lambda *args: _time.strftime("%Y-%m-%d %H:%M:%S", _time.localtime())))
        # exit
        self.register(BaseCommand("exit", lambda *args: (_ for _ in ()).throw(SystemExit("Saindo do Monty-SH..."))))
        # if
        self.register(BaseCommand("if", lambda condition, *args: bool(eval(condition))))
        # else
        self.register(BaseCommand("else", lambda *args: True))
        # here (pwd)
        self.register(BaseCommand("here", lambda *args: Path(".").resolve()))
        # touch
        def touch(*args):
            created = []
            for filename in args:
                Path(filename).touch(exist_ok=True)
                created.append(filename)
            return f"Arquivos criados: {', '.join(created)}"
        self.register(BaseCommand("touch", touch))
        # create (substitui cat)
        def create(filename, *contents):
            text = " ".join(contents)
            Path(filename).write_text(text)
            return f"Arquivo '{filename}' criado com conteúdo."
        self.register(BaseCommand("create", create))
        # rm
        def rm(*args):
            removed = []
            for filename in args:
                p = Path(filename)
                if p.exists():
                    p.unlink()
                    removed.append(filename)
            return f"Arquivos removidos: {', '.join(removed)}"
        self.register(BaseCommand("rm", rm))
        # input
        self.register(BaseCommand("input", lambda prompt="> ": input(prompt)))