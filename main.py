from apps.app_no2 import AppNO2
from apps.utils_module.utils import *


apps = {
    1: AppNO2.main
}

column([
    f"[1] - {AppNO2.name}"
])

app_choice = int(input("Escolha: "))

apps.get(app_choice, lambda: print("Opcao Invalida"))
