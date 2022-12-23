from main_new import *
import os


os.system("cls")
player = make_hero(
    inventory=[
        {
            "type": "weapon",
            "name": "Обычный меч",
            "stat": "ATK",
            "mod": 2,
            "price": 5
        },
        {
            "type": "",
            "name": "Зелье лечения",
            "stat": "HP_curret",
            "mod": 5,
            "price": 5
        }
    ],
    name="Искатель",
    money=1000
)

while True:
    visit_hub(player)