# NC = Nível Territorial (Código)   example "1"
# NN = Nível Territorial            example "Brasil"
# MC = Unidade de Medida (Código)   example "2"
# MN = Unidade de Medida            example "%"
# D1C = Brasil (Código)             example "1"
# D1N = Brasil                      example "Brasil"
# D2C = Variável (Código)           example "Brasil"
# D2N = Variável                    example "4099"
# D3N = Trimestre Móvel (Código)    example "Taxa de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade"
# D3C = Trimestre Móvel (Código)    example "201203
# V = Valor                         example "8.0"

from enum import Enum


class HEADER(Enum):
    NIVEL_TERRITORIAL = "NN"
    NIVEL_TERRITORIAL_COD = "NC"
    UNIDADE_MEDIDA = "MN"
    UNIDADE_MEDIDA_COD = "MC"
    BRASIL = "D1N"
    BRASIL_COD = "D1C"
    VARIAVEL = "D2N"
    VARIAVEL_COD = "D2C"
    TRIMESTRE_MOVEL = "D3N"
    TRIMESTRE_MOVEL_COD = "D3C"
    VALOR = "V"
