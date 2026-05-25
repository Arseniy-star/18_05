import tkinter as tk


class Pet:
    def __init__(self, name: str):
        self.__name = name
        self.__hunger = 30
        self.__happiness = 70
        self.__energy = 50
        self.__is_alive = True

    @property
    def name(self) -> str:
        return self.__name

    @property
    def hunger(self) -> int:
        return self.__hunger

    @property
    def happiness(self) -> int:
        return self.__happiness

    @property
    def energy(self) -> int:
        return self.__energy

    @property
    def is_alive(self) -> bool:
        return self.__is_alive

    def feed(self, amount: int = 20) -> None:
        if not self.__is_alive:
            return

        self.__hunger = self.__clamp(self.__hunger - amount)
        self.__energy = self.__clamp(self.__energy + 5)
        self.__validate_life()

    def play(self, duration: int = 15) -> None:
        if not self.__is_alive:
            return

        self.__happiness = self.__clamp(self.__happiness + duration)
        self.__energy = self.__clamp(self.__energy - duration // 2)
        self.__hunger = self.__clamp(self.__hunger + 5)
        self.__validate_life()

    def status(self) -> str:
        if not self.__is_alive:
            return "Питомец ушёл... RIP"
        if self.__happiness > 70 and self.__hunger < 30:
            return "Счастлив и сыт"
        if self.__hunger > 70:
            return "Очень голоден"
        if self.__energy < 20:
            return "Ужасно устал"
        return "Всё в порядке"

    def levels_text(self) -> str:
        return (
            f"Голод: {self.__hunger} | "
            f"Счастье: {self.__happiness} | "
            f"Энергия: {self.__energy}"
        )

    def __clamp(self, value: int) -> int:
        return max(0, min(100, value))

    def __validate_life(self) -> None:
        if self.__hunger == 100 or self.__energy == 0:
            self.__is_alive = False


class TamagotchiApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Тамагочи")
        self.root.resizable(False, False)
        self.default_bg = self.root.cget("bg")

        self.pet = Pet("Пушистик")

        self.name_label = tk.Label(
            root,
            text=f"Питомец: {self.pet.name}",
            font=("Arial", 18, "bold"),
            pady=10,
        )
        self.name_label.pack()

        self.levels_label = tk.Label(root, font=("Arial", 12), pady=6)
        self.levels_label.pack()

        self.status_label = tk.Label(root, font=("Arial", 13), pady=6)
        self.status_label.pack()

        buttons_frame = tk.Frame(root)
        buttons_frame.pack(padx=16, pady=14)

        self.feed_button = tk.Button(
            buttons_frame,
            text="Покормить",
            width=12,
            command=self.feed_pet,
        )
        self.feed_button.grid(row=0, column=0, padx=5)

        self.play_button = tk.Button(
            buttons_frame,
            text="Поиграть",
            width=12,
            command=self.play_pet,
        )
        self.play_button.grid(row=0, column=1, padx=5)

        self.exit_button = tk.Button(
            buttons_frame,
            text="Выход",
            width=12,
            command=root.destroy,
        )
        self.exit_button.grid(row=0, column=2, padx=5)

        self.update_ui()

    def feed_pet(self) -> None:
        self.pet.feed()
        self.update_ui()

    def play_pet(self) -> None:
        self.pet.play()
        self.update_ui()

    def update_ui(self) -> None:
        self.name_label.config(text=f"Питомец: {self.pet.name}")
        self.levels_label.config(text=self.pet.levels_text())
        self.status_label.config(text=self.pet.status())

        if not self.pet.is_alive:
            self.feed_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.DISABLED)
            self.root.config(bg="lightgray")
            self.status_label.config(fg="red")
        else:
            self.feed_button.config(state=tk.NORMAL)
            self.play_button.config(state=tk.NORMAL)
            self.root.config(bg=self.default_bg)
            self.status_label.config(fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = TamagotchiApp(root)
    root.mainloop()