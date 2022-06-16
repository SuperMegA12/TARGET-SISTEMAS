SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

soma = SP + RJ + MG + ES + Outros

print(f'O valor total foi de {soma}R$')

SP_percentual = (SP / soma) * 100
RJ_percentual =  (RJ / soma) * 100
MG_percentual =  (MG / soma) * 100
ES_percentual =  (ES / soma) * 100
OUTROS_percentual =  (Outros / soma) * 100

print('E o percentual de cada estado foi:')

print(f' SP {SP_percentual:.1f}% \n RJ {RJ_percentual:.1f}% \n MG {MG_percentual:.1f}% \n ES {ES_percentual:.1f}% '
      f'\n OUTROS {OUTROS_percentual:.1f}%')

