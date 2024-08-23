import tkinter as tk
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(('Текстовый файл', '*.txt'), ('Все файлы', '*.*')))
    if filename:
        text['text'] = f"Файл: {filename}"


# Создание основного окна
window = tk.Tk()
window.title('Проводник')
window.geometry('400x200')
window.configure(bg='black')
window.resizable(False, False)

# Текстовый виджет для отображения выбранного файла
text = tk.Label(window, text='Файл:', height=5, width=50, background='silver', foreground='blue', anchor='w', padx=10)
text.grid(column=0, row=0, padx=10, pady=10)

# Кнопка для вызова диалога выбора файла
button_select = tk.Button(window, width=20, height=3, text='Выберите файл', background='silver', foreground='blue',
                          command=file_select)
button_select.grid(column=0, row=1, pady=10)

# Запуск главного цикла приложения
window.mainloop()
