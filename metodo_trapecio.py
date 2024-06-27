import numpy as np
import sympy as sp

# Aproxima la integral de f(x) desde a hasta b usando el método del trapecio para n puntos.
def metodo_trapecio(f, a, b, n):
    # Paso 1: Calcular el tamaño del subintervalo
    h = (b - a) / n
    
    if n == 1:
        # Calcular el error
        x = sp.symbols('x')
        f_simbolica = f(x)  # La función simbólica
        f_segunda_derivada = sp.diff(f_simbolica, x, 2)
        
        # Evaluar la segunda derivada en varios puntos para encontrar el máximo en valor absoluto
        num_puntos = 1000
        valores_x = np.linspace(a, b, num_puntos)
        max_f_segunda_derivada = max(abs(float(f_segunda_derivada.subs(x, val))) for val in valores_x)
        
        error = -(h**3 * max_f_segunda_derivada) / 12
        
        # Usar la fórmula del trapecio simple
        integral_aproximada = (h / 2) * (f(a) + f(b))
    else:
        # Calcular el error
        x = sp.symbols('x')
        f_simbolica = f(x)  # La función simbólica
        f_segunda_derivada = sp.diff(f_simbolica, x, 2)
        
        # Encontrar el máximo de la segunda derivada en el intervalo [a, b]
        num_puntos = 1000
        valores_x = np.linspace(a, b, num_puntos)
        max_f_segunda_derivada = max(abs(float(f_segunda_derivada.subs(x, val))) for val in valores_x)
        
        error = -((b - a)**3 * max_f_segunda_derivada) / (12 * n**2)
        
        # Usar la fórmula del trapecio para n subintervalos
        integral_aproximada = (h / 2) * (f(a) + 2 * sum(f(a + i * h) for i in range(1, n)) + f(b))
    
    # Paso 2: Calcular la integral exacta usando SymPy
    integral_exacta = sp.integrate(f_simbolica, (x, a, b))
    
    # Paso 3: Retornar la aproximación de la integral, el error de aproximación y la integral exacta
    return integral_aproximada, error, integral_exacta.evalf()

# Función personalizada para evaluar expresiones matemáticas
def evalua_expresion(expr, valor_x):
    try:
        resultado = eval(expr, {'x': valor_x, 'np': np, 'sp': sp, 'log': np.log, 
                                'sqrt': np.sqrt, 'exp': np.exp, 'sin': np.sin, 'cos': np.cos,
                                'tan': np.tan, 'asin': np.arcsin, 'acos': np.arccos,
                                'atan': np.arctan, 'sinh': np.sinh, 'cosh': np.cosh,
                                'tanh': np.tanh, 'abs': np.abs, 'log10': np.log10,
                                'log2': np.log2, 'pow': np.power, 'div': np.divide})
    except (SyntaxError, TypeError, NameError):
        resultado = eval(expr, {'x': valor_x, 'np': np, 'sp': sp, 'log': sp.log,
                                'sqrt': sp.sqrt, 'exp': sp.exp, 'sin': sp.sin, 'cos': sp.cos,
                                'tan': sp.tan, 'asin': sp.asin, 'acos': sp.acos,
                                'atan': sp.atan, 'sinh': sp.sinh, 'cosh': sp.cosh,
                                'tanh': sp.tanh, 'abs': sp.Abs, 'log10': sp.log,
                                'log2': lambda x: sp.log(x, 2), 'pow': lambda x, y: x**y,
                                'div': lambda x, y: x / y})
    return resultado