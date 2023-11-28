import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create an energy meter
        self.energy_meter = pyjoules.EnergyMeter()

        # Entry to display the input and result
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place the buttons on the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        # Start measuring energy consumption
        self.energy_meter.start()

        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        elif button == 'C':
            self.entry.delete(0, tk.END)

        else:
            self.entry.insert(tk.END, button)

        # Stop measuring energy consumption and print the result
        energy_consumed = self.energy_meter.stop()
        print(f"Energy consumed: {energy_consumed} Joules")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
