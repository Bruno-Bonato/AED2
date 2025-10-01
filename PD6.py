import time

n = 4

inicio_algoritmo = time.perf_counter()

inicio_base = time.perf_counter() #Caso Base - Tempo de execução constante O(1)
if n == 0 or n == 1:
    resultado = 1
fim_base = time.perf_counter()

inicio_loop = time.perf_counter() #Loop para degraus maiores que 1 - Tempo de execução O(n)
antes_anterior = 1
anterior = 1
for i in range(2, n + 1):
    atual = anterior + antes_anterior
    antes_anterior = anterior
    anterior = atual
fim_loop = time.perf_counter()

inicio_retorno = time.perf_counter() #Quantidade de formas de subir - Tempo de execução constante O(1)
resultado = anterior
fim_retorno = time.perf_counter()

fim_algoritmo = time.perf_counter()

print(f"Resultado: {resultado} formas de subir a escada")
print(f"Tempo caso base: {fim_base - inicio_base:.8f} s")
print(f"Tempo de loop: {fim_loop - inicio_loop:.8f} s")
print(f"Tempo retorno: {fim_retorno - inicio_retorno:.8f} s")
print(f"Tempo total do algoritmo: {fim_algoritmo - inicio_algoritmo:.8f} s")

