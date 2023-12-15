def palavras_geradas_anagrama(nome, qtds):
    def anagrama(nome, qtds):
        def permutar(palavra):
            if len(palavra) == 1:
                return [palavra]

            permutacoes = []
            for x in range(len(palavra)):
                l = palavra[x]
                xs = palavra[:x] + palavra[x+1:]
                for p in permutar(xs):
                    permutacoes.extend([l + p])

            return permutacoes

        anagrama_set = set(permutar(nome))  # Usar um conjunto para evitar duplicatas
        anagrama_list = list(anagrama_set)  # Converter de volta para uma lista

        if qtds >= len(anagrama_list):
            return anagrama_list

        return anagrama_list[:qtds]  # Limitar a quantidade de anagramas
    
    return {
        'nome': nome,
        'qtds_de_anagramas': qtds,
        'anagramas': anagrama(nome, qtds)
    }