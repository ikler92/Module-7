import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))


def show_info():
    messagebox.showinfo("Info", "Этот блокнот позволяет создавать, редактировать и сохранять текстовые файлы.\n"
                                "Вы можете использовать меню для открытия и сохранения файлов.\n"
                                "Кнопка 'Info' покажет это сообщение, а 'About' расскажет о программе.")


def show_about():
    messagebox.showinfo("About", "Автор: Иван Иванов\nВерсия: 1.0.0\n2024 год")


# Создание основного окна
window = tk.Tk()
window.title("Блокнот")
window.geometry("600x400")

# Текстовое поле для редактирования
text_area = tk.Text(window, wrap='word')
text_area.pack(expand=True, fill='both')

# Меню
menu = tk.Menu(window)
window.config(menu=menu)

# Меню "Файл"
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.quit)

# Меню "Справка"
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="Info", command=show_info)
help_menu.add_command(label="About", command=show_about)

# Запуск главного цикла приложения
window.mainloop()
