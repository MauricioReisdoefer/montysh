import sys
from montysh.core.interpreter import Interpreter
from montysh.core.psyfilereader import PsyFileReader

def main():
    interpreter = Interpreter()
    reader = PsyFileReader(interpreter)

    print("MontySH - Python Shell (write CTRL+C to leave)")
    while True:
        try:
            line = input("montysh> ").strip()
            if not line:
                continue
            if line.lower() in ("exit", "quit"):
                print("Leaving MontySH...")
                break
            if line.endswith(".psy"):
                try:
                    reader.run_file(line)
                except FileNotFoundError:
                    print(f"File not found: {line}")
                continue
            result = interpreter.run_line(line)
            if result is not None:
                print(result)

        except KeyboardInterrupt:
            print("\n(CTRL+C) - Use 'exit' to leave")
        except Exception as e:
            print(f"Erro: {e}")
            
if __name__ == "__main__":
    main()