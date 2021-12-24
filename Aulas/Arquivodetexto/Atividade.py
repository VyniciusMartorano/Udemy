import json
d1 = {
    'pessoa1':{
        'nome':'vitor','idade':18
    },'pessoa2':{
        'nome':'josue','idade':26
    }
}
d1_json = json.dumps(d1, indent=True)
with open('dados.txt','w+') as arq:
    arq.write(d1_json)
    arq.close()