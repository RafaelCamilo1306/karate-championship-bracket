
participantes = [
    {
        "nome": "rafael",
        "faixa": "Azul",
        "idade": 18,
        "escola": "karate kid"
    },
    {
        "nome": "gabriel",
        "faixa": "Azul",
        "idade": 19,
        "escola": "cobraKai"
    }
]

def verificaChave(participante, chaveamento):
    for nomes in chaveamento:
        if participantNome.lower() in nomes.lower():
            return True
    return False

chaveamento = [""]
participantNome=participantes[0]["nome"]

if verificaChave(participantNome,chaveamento):
    print("participante ja chaveado")
else:
    if(participantes[0]["escola"] != participantes[1]["escola"]):

        diferençaIdade=participantes[0]["idade"]-participantes[1]["idade"]

        if (diferençaIdade >= -1) and (diferençaIdade<=1):

            if(participantes[0]["faixa"] == participantes[1]["faixa"]):

                chaveamento=[participantes[0]["nome"], participantes[1]["nome"]]
                print(chaveamento)
            else:
                print("participantes não correspondem")
        else:
            print("participantes são de idades muito diferentes")
    else:
        print("participantes são da mesma escola")
                        

