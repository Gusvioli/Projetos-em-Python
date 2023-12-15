from anagrama import calcularanagrama
from palavras_geradas_anagrama import palavras_geradas_anagrama


qtds = calcularanagrama('Shakespeare')
ver = palavras_geradas_anagrama('Shakespeare', qtds)

print(ver)
