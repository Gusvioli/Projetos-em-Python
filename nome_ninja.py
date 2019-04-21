nome_ninja = {"a":"KA","b":"ZU","c":"MI","d":"TE","e":"KU","f":"LU","g":"JI","h":"RI","i":"KI","j":"ZUS"
              ,"k":"ME","l":"TA","m":"RIN","n":"TO","o":"MO","p":"NO","q":"KE","r":"SHI","s":"ARI"
              ,"t":"CHI","u":"DO","v":"RU","w":"MEI","x":"NA","y":"FU","z":"ZI"}

while True:
    tex = ""
    input_ent = input("Seu nome:\n").lower()
    for x in input_ent:
        tex = tex + nome_ninja[x]
    print(tex)
