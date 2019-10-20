livre, alvo, corredor, onibus = "OO", "++", "|", []

def solution(n, onibus):
    ans, onibus_ = "NO", onibus.copy()
    for i in range(0,n):
        if livre in onibus_[i]: ans = "YES"

        lado_esq, lado_dir = onibus_[i].split(corredor)
        if lado_esq == livre:
            onibus_[i] = alvo + corredor + lado_dir
            break
        elif lado_dir == livre:
            onibus_[i] = lado_esq + corredor + alvo
            break

    return ans, onibus_


if __name__ == "__main__":
    n = int(input())
    for _ in range(0,n):
        onibus.append(input())

    ans, onibus_ = solution(n, onibus)
    print(ans)
    if ans == "YES":
        print('\n'.join(onibus_))