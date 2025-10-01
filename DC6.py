import time
inicio_algoritmo = time.perf_counter()
def elemento_majoritario(vet):
    def rec_majoritario(inicio, fim):
        if inicio == fim:
            return vet[inicio]  # O(1)
        mid = (inicio + fim) // 2  # O(1)
        esquerda = rec_majoritario(inicio, mid)  # T(n/2)
        direita = rec_majoritario(mid + 1, fim)  # T(n/2)
        if esquerda == direita:
            return esquerda  # O(1)
        cont_esquerda = 0     
        cont_direita = 0
        for i in range(inicio, fim + 1):  # O(n)
            if vet[i] == esquerda:
                cont_esquerda += 1
            if vet[i] == direita:
                cont_direita += 1
        if cont_esquerda > cont_direita:
            return esquerda  # O(1)
        else:
            return direita   # O(1)
    candidato = rec_majoritario(0, len(vet) - 1)  # O(n log n)
    contagem = vet.count(candidato)  # O(n)
    if contagem > len(vet) // 2:
        return candidato  # O(1)
    else:
        return "Não existe elemento majoritário"  # O(1)

vet = [2, 2, 1, 1, 2, 2, 2]
print(elemento_majoritario(vet))
fim_algoritmo = time.perf_counter()
print(f"Tempo de execução: {fim_algoritmo - inicio_algoritmo:.8f} segundos")
# O (n log n)
# T(n) = 2T(n/2) + O(n)
# a = 2, b = 2, f(n) = n
# log_b(a) = log_2(2) = 1
# f(n) é Θ(n^1) = n