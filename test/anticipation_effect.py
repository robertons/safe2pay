import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    antecipacao = safe2pay.Anticipation()
    antecipacao.SessionGuid = "efcbd735-xxxx-4e5b-xxxx-ed9f5acf5594"

    effectiveness1 = safe2pay.Effectiveness()
    effectiveness1.ReleaseDate = '2023-07-10'
    antecipacao.EffectivenessList.add(effectiveness1)
    
    effectiveness2 = safe2pay.Effectiveness()
    effectiveness2.ReleaseDate = '2023-07-12'
    antecipacao.EffectivenessList.add(effectiveness2)
    
    effectiveness3 = safe2pay.Effectiveness()
    effectiveness3.ReleaseDate = '2023-07-13'
    antecipacao.EffectivenessList.add(effectiveness3)
    
    effectiveness4 = safe2pay.Effectiveness()
    effectiveness4.ReleaseDate = '2023-07-14'
    antecipacao.EffectivenessList.add(effectiveness4)

    retorno = antecipacao.EffectSimulate()
    print(f'Retorno EffectSimulate: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)