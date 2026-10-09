entrada = input("Digite as páginas separadas por espaço: ")
paginas_usuario = [int(valor) for valor in entrada.split()]

quantidade_frames = int(input("Digite a quantidade de frames: "))

print("\nSequência:", paginas_usuario)
print("Frames:", quantidade_frames)

memoria = []
fila = []
faults_fifo = 0
hits_fifo = 0

print("\n--- FIFO ---")

for pagina in paginas_usuario:

    if pagina in memoria:
        hits_fifo += 1
        resultado = "HIT"

    else:
        faults_fifo += 1
        resultado = "PAGE FAULT"

        if len(memoria) < quantidade_frames:
            memoria.append(pagina)
            fila.append(pagina)

        else:
            antiga = fila.pop(0)
            memoria.remove(antiga)

            memoria.append(pagina)
            fila.append(pagina)

    print(pagina, "->", resultado, "| Memória:", memoria)


memoria = []
faults_lru = 0
hits_lru = 0

print("\n--- LRU ---")

for pagina in paginas_usuario:

    if pagina in memoria:
        hits_lru += 1

        memoria.remove(pagina)
        memoria.append(pagina)

        resultado = "HIT"

    else:
        faults_lru += 1
        resultado = "PAGE FAULT"

        if len(memoria) < quantidade_frames:
            memoria.append(pagina)

        else:
            memoria.pop(0)
            memoria.append(pagina)

    print(pagina, "->", resultado, "| Memória:", memoria)


total = len(paginas_usuario)

print("\n--- RESULTADOS ---")

print("\nFIFO")
print("Page Faults:", faults_fifo)
print("Hits:", hits_fifo)
print("Taxa de Page Faults:", f"{faults_fifo / total * 100:.2f}%")
print("Taxa de Hits:", f"{hits_fifo / total * 100:.2f}%")

print("\nLRU")
print("Page Faults:", faults_lru)
print("Hits:", hits_lru)
print("Taxa de Page Faults:", f"{faults_lru / total * 100:.2f}%")
print("Taxa de Hits:", f"{hits_lru / total * 100:.2f}%")



print("\n--- COMPARAÇÃO ---")

if faults_fifo < faults_lru:
    print("FIFO teve menos Page Faults que LRU.")

elif faults_fifo > faults_lru:
    print("LRU teve menos Page Faults que FIFO.")

else:
    print("FIFO e LRU tiveram o mesmo número de Page Faults.")