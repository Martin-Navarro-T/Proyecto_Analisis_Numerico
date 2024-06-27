"""
Recuerda antes de ejecutar el codigo haber seguido los pasos que se muestran en el archivo README.md

"""
from metodo_trapecio import metodo_trapecio, evalua_expresion
from colorama import Fore, Style
import shutil 

name = input(f"\n{Style.BRIGHT}{Fore.CYAN}-> Ingrese su nombre:{Style.RESET_ALL} ").title()

def instrucciones_funcion():
    titulo = f"{Style.BRIGHT}{Fore.MAGENTA}INSTRUCCIONES DE USO{Style.RESET_ALL}"
    terminal_width = shutil.get_terminal_size().columns
    print(f"\n{'-' * terminal_width}")
    print(f"{titulo.center(terminal_width)}")
    print("-" * terminal_width)
    print(f"{name} para ingresar la función a integrar, puedes usar las siguientes operaciones y funciones:")
    print("- Operaciones básicas: +, -, *, /")
    print("- Potencia: Usa 'pow(base, exponente)' o 'base ** exponente'")
    print("- Logaritmo natural: 'log(x)' para ln(x)")
    print("- Logaritmo base 10: 'log10(x)'")
    print("- Logaritmo base 2: 'log2(x)'")
    print("- Exponencial: 'exp(x)' para e^x")
    print("- Raíz cuadrada: 'sqrt(x)'")
    print("- Funciones trigonométricas: 'sin(x)', 'cos(x)', 'tan(x)'")
    print("- Funciones trigonométricas inversas: 'asin(x)', 'acos(x)', 'atan(x)'")
    print("- Funciones hiperbólicas: 'sinh(x)', 'cosh(x)', 'tanh(x)'")
    print("- Valor absoluto: 'abs(x)'")
    print("- Otras funciones matemáticas: Puedes usar funciones definidas en numpy o sympy como 'np.func()' o 'sp.func()'")
    print("-" * terminal_width)
    print("- Asegúrate de usar paréntesis para agrupar operaciones correctamente.")
    print("- Ejemplo válido: 'x * log(x)' para x * ln(x)")
    print("- Ejemplo válido: 'pow(x, 2) + sqrt(x)'")
    print("- Ejemplo válido: 'exp(-x) / (1 + x)'")
    print("- Ejemplo válido: '2*x + 3' para 2x + 3")
    print("-" * terminal_width)
    
# Función para mostrar el mensaje de bienvenida
def mensaje_bienvenida():
    terminal_width = shutil.get_terminal_size().columns  # Obtiene el ancho actual de la consola
    titulo1 = f"{Style.BRIGHT}{Fore.BLUE}Hola {name}! Bienvenido a la calculadora de integrales por el Método del Trapecio{Style.RESET_ALL}"
    titulo2 = f"{Style.BRIGHT}{Fore.BLUE}Esta calculadora fue creada por Martin Navarro para el Proyecto de Análisis Numérico{Style.RESET_ALL}"
    
    print("-" * terminal_width)
    print(titulo1.center(terminal_width))
    print(titulo2.center(terminal_width))
    print("-" * terminal_width)

def mostrar_menu():
    titulo = f"{Style.BRIGHT}{Fore.MAGENTA}MENÚ PRINCIPAL{Style.RESET_ALL}"
    terminal_width = shutil.get_terminal_size().columns
    print(f"\n{'-' * terminal_width}")
    print(f"{titulo.center(terminal_width)}")
    print("-" * terminal_width)
    print("1. Ver Instrucciones")
    print("2. Calcular Integral por el Método del Trapecio")
    print("3. Salir")
    print("-" * terminal_width)


mensaje_bienvenida()

# Bucle principal para ejecutar el código continuamente
while True:
    mostrar_menu()
    opcion = input(f"\n{Style.BRIGHT}{Fore.CYAN}-> {name} elige una opción (1/2/3):{Style.RESET_ALL} ")
    
    if opcion == '1':
        instrucciones_funcion()
    elif opcion == '2':
        while True:  # Bucle para calcular múltiples integrales
            try:
                func_str = input(f"\n{Style.BRIGHT}{Fore.CYAN}-> Introduce la función a integrar (o 'fin' para terminar):{Style.RESET_ALL} ").strip()
                
                if func_str.lower() == 'fin':
                    titulo = f"{Style.BRIGHT}{Fore.YELLOW}{name} has finalizado la ejecución de la calculadora de integrales{Style.RESET_ALL}"
                    terminal_width = shutil.get_terminal_size().columns
                    print(f"\n{'-' * terminal_width}")
                    print(f"{titulo.center(terminal_width)}")
                    print("-" * terminal_width)
                    break  # Salir del bucle interno
                
                if func_str == "":
                    print(f"\n{Style.BRIGHT}{Fore.RED}Error: {name} debes ingresar una función válida.{Style.RESET_ALL}")
                    continue  # Vuelve a pedir la función
                
                # Valida la función ingresada
                def f(x):
                    return evalua_expresion(func_str, x)
                
                a = float(input(f"\n{Style.BRIGHT}{Fore.CYAN}-> Introduce el límite inferior de integración (a):{Style.RESET_ALL} "))
                b = float(input(f"\n{Style.BRIGHT}{Fore.CYAN}-> Introduce el límite superior de integración (b):{Style.RESET_ALL} "))
                
                # Solicitar el número de subintervalos
                n = int(input(f"\n{Style.BRIGHT}{Fore.CYAN}-> Introduce el número de subintervalos (n):{Style.RESET_ALL} "))
                
                # Calcular la integral aproximada, el error y la integral exacta usando metodo_trapecio
                resultado, error, integral_exacta = metodo_trapecio(f, a, b, n)
                
                titulo = f"{Style.BRIGHT}{Fore.GREEN}RESULTADOS{Style.RESET_ALL}"
                terminal_width = shutil.get_terminal_size().columns
                print(f"\n{'-' * terminal_width}")
                print(f"{titulo.center(terminal_width)}")
                print("-" * terminal_width)
                print(f"{Style.BRIGHT}{Fore.GREEN}{name} los resultados a tus datos ingresados son:{Style.RESET_ALL}")
                print(f"{Style.BRIGHT}La aproximación de la integral es: {resultado}{Style.RESET_ALL}")
                print(f"{Style.BRIGHT}El error de aproximación es: {error}{Style.RESET_ALL}")
                print(f"{Style.BRIGHT}La aproximación de la integral + el error: {resultado + error}{Style.RESET_ALL}")
                print(f"{Style.BRIGHT}La integral exacta es: {integral_exacta}{Style.RESET_ALL}")
                print(f"{Style.BRIGHT}El error absoluto es: {integral_exacta - resultado}{Style.RESET_ALL}")
                print("-" * terminal_width)
                
                while True:
                    decision = input(f"\n{Style.BRIGHT}{Fore.CYAN}-> {name} ¿deseas calcular otra integral? (sí/no):{Style.RESET_ALL} ").strip().lower()
                    if decision == 'no':
                        # Salir del bucle interno
                        break
                    elif decision == 'sí' or decision == 'si':
                        break  # Volver a calcular otra integral
                    else:
                        print(f"\n{Style.BRIGHT}{Fore.RED}Respuesta no válida. Por favor {name} responde 'sí' o 'no'.{Style.RESET_ALL}")
                
                if decision == 'no':
                    # Salir del bucle externo y finalizar el programa
                    break
            
            except ValueError as e:
                terminal_width = shutil.get_terminal_size().columns
                print(f"\n{'-' * terminal_width}")
                print(f"{Style.BRIGHT}{Fore.RED}Error: {e}{Style.RESET_ALL}")
                print("-" * terminal_width)
                

            except Exception as e:
                terminal_width = shutil.get_terminal_size().columns
                print(f"\n{'-' * terminal_width}")
                print(f"{Style.BRIGHT}{Fore.RED}{name} ocurrió un error inesperado, error: {e}{Style.RESET_ALL}")
                print("-" * terminal_width)
            
    elif opcion == '3':
        titulo = f"{Style.BRIGHT}{Fore.YELLOW}¡Hasta luego {name}!{Style.RESET_ALL}"
        terminal_width = shutil.get_terminal_size().columns
        print(f"\n{'-' * terminal_width}")
        print(f"{titulo.center(terminal_width)}")
        print("-" * terminal_width)
        break
    else:
        print(f"\n{Style.BRIGHT}{Fore.RED}Opción inválida. Por favor {name} selecciona 1, 2 o 3.{Style.RESET_ALL}")