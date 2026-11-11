import tkinter as tk
import random
coins = 10
day = 1
max_days = 5
souvenirs = []

Name=input("Как вас зовут")

window=tk.Tk()
window.title("Остров удачи")
window.geometry("1600x800")
title_label = tk.Label(
    window,
    text="🏝 ОСТРОВ УДАЧИ",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


little_label=tk.Label(
    window,
    text="МЫ ПРОГРАММИСТЫ",
    font=("Arial", 65,"bold")

)
little_label.pack(pady=100)

name_label=tk.Label(
    window,
    text=Name,
    font=("Arial", 30,"bold")

)
name_label.pack(pady=30)

# def save_name():
# global player_name

# player_name = name_entry.get().strip()

# if player_name == "":
# name_label.config(
# text="Введите имя игрока!"
# )
# return

# name_label.config(
# text=f"Привет, {player_name}! 👋"
# )


day_label = tk.Label(
    window,
    text=f"День: {day} / {max_days}",
    font=("Arial", 14)
)
day_label.pack()


coins_label = tk.Label(
    window,
    text=f"Монеты: {coins} 🪙",
    font=("Arial", 14)
)
coins_label.pack(pady=5)


event_label = tk.Label(
    window,
    text="Куда отправимся сегодня?",
    font=("Arial", 13),
    wraplength=500,
    justify="center"
)
event_label.pack(pady=20)

def go_beach():
    global coins
    found = random.randint(1, 8)
    coins += found
    event_label.config(
        text=f"🏖 На пляже ты нашёл {found} монет!"
    )
    crystall = random.randint(1, 10)
    if crystall == 6:
        souvenirs.append("редкий кристалл")
        event_label.config(
            text="🛍 Ты нашел редкий кристалл!"
    )
    next_day()
    update_screen()


def go_garden():
    global coins
    luck = random.randint(1, 6)
    if luck >= 4:
        coins += 10
        event_label.config(
            text=f"🌳 Кубик: {luck}. Удача! +10 монет."
        )
    else:
        event_label.config(
            text=f"🌳 Кубик: {luck}. Сегодня без подарка."
        )
    next_day()
    update_screen()

def go_shop():
    global coins
    if "открытка" in souvenirs:
        event_label.config(
            text="🛍 У тебя уже есть открытка."
        )
    elif coins >= 5:
        coins -= 5
        souvenirs.append("открытка")
        event_label.config(
            text="🛍 Ты купил открытку за 5 монет!"
        )
    else:
        event_label.config(
            text="🛍 Монет не хватает."
        )
    next_day()
    update_screen()


def go_shop_rakyshka():
    global coins
    if "ракушка" in souvenirs:
        event_label.config(
            text="🛍 У тебя уже есть ракушка."
        )
    elif coins >= 8:
        coins -= 8
        souvenirs.append("ракушка")
        event_label.config(
            text="🛍 Ты купил ракушка за 8 монет!"
        )
    else:
        event_label.config(
            text="🛍 Монет не хватает."
        )

    next_day()
    update_screen()

beach_button = tk.Button(
    window,
    text="🏖 Пляж",
    bg="black",
    fg="red",
    command=go_beach,
    width=18
)
beach_button.pack(pady=4)

garden_button = tk.Button(
    window,
    text="🌳 Волшебный сад",
    bg="black",
    fg="green",
    command=go_garden,
    width=18
)
garden_button.pack(pady=4)

shop_button = tk.Button(
    window,
    text="🛍 Лавка",
    bg="black",
    fg="blue",
    command=go_shop,
    width=18
)
shop_button.pack(pady=4)

go_shop_rakyshka_button= tk.Button(
    window,
    text="🛍 Морепродукты",
    bg="black",
    fg="yellow",
    command=go_shop_rakyshka,
    width=18
)
go_shop_rakyshka_button.pack(pady=4)

def play_again():
    global coins
    coins=10
    global day 
    day=1
    global max_days
    max_days=10
    global souvenirs 
    souvenirs=[]
    update_screen()

play_again_button = tk.Button(
    window,
    text="Начать сначала",
    bg="black",
    fg="pink",
    command=play_again,
    width=30
)
play_again_button.pack(pady=4)

def next_day():
    global day
    day += 1

inventory_label = tk.Label(
    window,
    text="Сувениры: пока пусто",
    font=("Arial", 12)
)

inventory_label.pack(pady=15)

def update_screen():

    day_label.config(
        text=f"День: {day} / {max_days}"
    )

    coins_label.config(
        text=f"Монеты: {coins} 🪙"
    )

    if len(souvenirs) == 0:
        inventory_label.config(
            text="Сувениры: пока пусто"
        )
    else:
        inventory_label.config(
            text="Сувениры: " + ", ".join(souvenirs)
        )

def daily_event():
    global coins

    event = random.randint(1, 5)

    if event == 1:
        coins += 3
        return " 🎁 Сюрприз: +3 монеты!"

    return ""

def check_game_over():

    if day > max_days:

        beach_button.config(state="disabled")
        garden_button.config(state="disabled")
        shop_button.config(state="disabled")

        if coins >= 30:
            event_label.config(
                text="🌟 Путешествие закончено! Очень удачный результат!"
            )
        else:
            event_label.config(
                text="🏝 Путешествие закончено! Спасибо за игру."
            )

















window.mainloop()





































































































































































































