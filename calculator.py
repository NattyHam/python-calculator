class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0       
        for i in range(abs(b)):
            result = self.add(result, abs(a))
        if (a<0 and b>=0) or (a>=0 and b<0):
            return -result 
        else: return result

    def divide(self, a, b):
        if b==0 :
            return "Error"
        result = 0
        abs_a = abs(a)
        abs_b = abs(b)
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if (a < 0) != (b < 0):
            return -result
        else: return result
    
    def modulo(self, a, b):
        if b==0:
            return "Error"
        if a==b:
            return 0
        while a > b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))