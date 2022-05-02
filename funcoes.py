import datetime as dt
import math

def calc_periodo_locado(data_inicial, data_final):
    data_inicial = dt.datetime(2022, 2, 19, 18, 00, 00)
    data_final = dt.datetime(2022, 2, 20, 18, 00, 00)
    tempo_alugado = (data_final - data_inicial)
    return tempo_alugado

def tempo_em_hora():
    tempo_alugado = calc_periodo_locado
    tempo_alugado = tempo_alugado.seconds / 3600
    tempo_alugado_horas = math.ceil(tempo_alugado)
    return tempo_alugado_horas

def tempo_em_dias():
    tempo_alugado = calc_periodo_locado
    tempo_alugado_dias = tempo_alugado.days
    return tempo_alugado_dias

def tempo_em_semanas():
    tempo_alugado = calc_periodo_locado
    tempo_em_semanas = tempo_alugado.days / 7
    return tempo_em_semanas

