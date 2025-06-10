import math

def estimate_pi():
    estimativa = 0
    k = 0
    
    while True:
        termo = ((2 * math.sqrt(2)) / 9801) * (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
        estimativa += termo
        if termo < 1e-15: 
            break
        k += 1
        
    return 1 / estimativa

# Teste a função
pi_estimate = estimate_pi()
print(f"Aproximação de pi: {pi_estimate}")
print({math.pi})