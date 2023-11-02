def sumar(*args):
    try:
        resultado = sum(args)
        return resultado
    except Exception as e:
        return f"Error: {e}"

def restar(num1, num2):
    try:
        resultado = num1 - num2
        return resultado
    except Exception as e:
        return f"Error: {e}"

def multiplicar(*args):
    try:
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    except Exception as e:
        return f"Error: {e}"

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero"
    except Exception as e:
        return f"Error: {e}"

def operacion(num1, oper, num2):
    try:
        if oper == "+":
            return num1 + num2
        elif oper == "-":
            return num1 - num2
        elif oper == "*":
            return num1 * num2
        elif oper == "/":
            if num2 == 0:
                return "Error: División por cero"
            return num1 / num2
        else:
            return "Operador no válido"
    except Exception as e:
        return f"Error: {e}"
