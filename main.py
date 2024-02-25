from apps import app_no2, app_titanic
from apps.utils_module.utils import column

apps= [app_no2, app_titanic]

# Menu
menu = []
for i in range(0, len(apps)):
    app = apps[i]
    menu.append(f"[{i + 1}] - {str.upper(app.get_name())}")

column(menu)


app_choice = int(input("Escolha: "))

if (app_choice >= 1) or (app_choice <= len(apps)):
    apps[app_choice - 1].main()
else:
    print("Opacao Invalida")
    exit(-1)
