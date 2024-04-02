import tkinter as tk
from datetime import datetime

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Секундомер")

        self.is_running = False
        self.start_time = None

        self.label = tk.Label(root, text="00:00:00.000", font=("Helvetica", 36))
        self.label.pack()

        self.start_button = tk.Button(root, text="Старт", command=self.start_stopwatch)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack()

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update_time()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_time(self):
        if self.is_running:
            elapsed_time = datetime.now() - self.start_time
            time_str = str(elapsed_time).split('.')[0]
            millisecs_str = str(elapsed_time.microseconds // 1000).zfill(3)
            time_str = f"{time_str}.{millisecs_str}"
            self.label.config(text=time_str)
            self.label.after(1, self.update_time)  # Обновление каждую миллисекунду

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

