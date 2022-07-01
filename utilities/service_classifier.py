import random


def service_classifier(service: str) -> dict:
    service_dict = {1: 'консультация', 2: 'лечение', 3: 'стационар', 4: 'диагностика', 5: 'лаборатория'}
    new_dict_key = random.choice(list(service_dict.keys()))
    return {new_dict_key: service_dict[new_dict_key]}
