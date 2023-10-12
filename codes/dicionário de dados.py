
participantes = [
    {
        "nome": "rafael",
        "faixa": "Azul",
        "idade": 18,
        "escola": "karate kid"
    },
    {
        "nome": "gabriel",
        "faixa": "azul",
        "idade": 19,
        "escola": "cobraKai"
    }
]
if(participantes[0]["escola"] != participantes[1]["escola"]):


    if (diferençaIdade >= -1) and (diferençaIdade<=1):

        if(participantes[0]["faixa"] == participantes[1]["faixa"]):

            print(participantes[0]["nome"]+" x "+participantes[1]["nome"])
        else:
            print("participantes não correspondem")
    else:
        print("participantes são de idades muito diferentes")
else:
    print("participantes são da mesma escola")
            

