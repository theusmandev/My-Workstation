import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, LabelFrame, Entry, Button, Label
import time
import random
import os
import smtplib
import tempfile
from threading import Thread

class MenuItem:
    """Represents a menu item with name, price, and associated entry widget."""
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.entry = None

    def get_total(self):
        """Calculate total price for this item based on quantity."""
        try:
            return int(self.entry.get()) * self.price
        except ValueError:
            messagebox.showerror("Error", f"Please enter a digit for {self.name}")
            return 0

class BillManager:
    """Handles bill generation, saving, and searching."""
    def __init__(self):
        self.bill_number = random.randint(500, 1000)
        self.date = time.strftime('%d/%m/%Y')
        self.bills_dir = 'bills'
        if not os.path.exists(self.bills_dir):
            os.mkdir(self.bills_dir)

    def save_bill(self, content, textarea):
        """Save bill to a file."""
        result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
        if result:
            try:
                with open(f'{self.bills_dir}/{self.bill_number}.txt', 'w', encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo('Success', f'Bill number {self.bill_number} saved successfully')
                self.bill_number = random.randint(500, 1000)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save bill: {e}")

    def search_bill(self, bill_number, textarea):
        """Search for a bill by number and display it."""
        if not os.path.exists(self.bills_dir):
            messagebox.showerror('Error', 'Bills directory not found.')
            return
        for filename in os.listdir(self.bills_dir):
            if filename.split('.')[0] == bill_number:
                try:
                    with open(os.path.join(self.bills_dir, filename), 'r', encoding='utf-8') as file:
                        textarea.delete(1.0, tk.END)
                        textarea.insert(tk.END, file.read())
                    return
                except Exception as e:
                    messagebox.showerror('Error', f'Error reading bill: {e}')
        messagebox.showerror('Error', 'Invalid bill number.')

    def print_bill(self, content):
        """Print the bill content."""
        if content.strip() == '':
            messagebox.showerror("Error", "Bill is empty.")
        else:
            content = content.replace('━', '━━')
            file = tempfile.mktemp('.txt')
            with open(file, 'w', encoding="utf-8") as f:
                f.write(content)
            os.startfile(file, 'print')

class EmailSender:
    """Handles sending bills via email."""
    def send_email(self, sender_email, password, receiver_email, message, parent):
        """Send email with bill content."""
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, message)
            smtp.quit()
            messagebox.showinfo('Success', 'Bill sent successfully', parent=parent)
        except Exception as e:
            messagebox.showerror('Error', f'Something went wrong: {e}', parent=parent)

class Calculator:
    """Calculator functionality integrated into the app."""
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("375x630+800+0")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.window.config(bd=1)
        self.total_expression = ""
        self.current_expression = ""
        self.create_ui()

    def create_ui(self):
        """Set up calculator UI."""
        display_frame = tk.Frame(self.window, height=221, bg="white", bd=1)
        display_frame.pack(expand=True, fill="both")
        total_label = tk.Label(display_frame, text=self.total_expression, anchor=tk.E, bg="white",
                               fg="black", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill='both')
        self.label = tk.Label(display_frame, text=self.current_expression, anchor=tk.E, bg="white",
                              fg="black", padx=24, font=("Arial", 40, "bold"))
        self.label.pack(expand=True, fill='both')

        buttons_frame = tk.Frame(self.window, bd=3)
        buttons_frame.pack(expand=True, fill="both")
        buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            buttons_frame.rowconfigure(x, weight=1)
            buttons_frame.columnconfigure(x, weight=1)

        digits = {7: (1, 1), 8: (1, 2), 9: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3),
                  1: (3, 1), 2: (3, 2), 3: (3, 3), 0: (4, 2), '.': (4, 1)}
        operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        for digit, grid in digits.items():
            tk.Button(buttons_frame, text=str(digit), bg="chocolate", fg="black", font=("Arial", 24, "bold"),
                      borderwidth=0, bd=3, command=lambda x=digit: self.add_to_expression(x)).grid(row=grid[0], column=grid[1], sticky=tk.NSEW)

        for i, (op, symbol) in enumerate(operations.items()):
            tk.Button(buttons_frame, text=symbol, bg="chocolate3", fg="black", font=("Arial", 20),
                      borderwidth=0, bd=3, command=lambda x=op: self.append_operator(x)).grid(row=i, column=4, sticky=tk.NSEW)

        tk.Button(buttons_frame, text="C", bg="chocolate3", fg="black", font=("Arial", 20),
                  borderwidth=0, bd=3, command=self.clear).grid(row=0, column=1, sticky=tk.NSEW)
        tk.Button(buttons_frame, text="=", bg="white", fg="black", font=("Arial", 20),
                  borderwidth=0, bd=3, command=self.evaluate).grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
        tk.Button(buttons_frame, text="x\u00b2", bg="chocolate3", fg="black", font=("Arial", 20),
                  borderwidth=0, bd=3, command=self.square).grid(row=0, column=2, sticky=tk.NSEW)
        tk.Button(buttons_frame, text="\u221ax", bg="chocolate3", fg="black", font=("Arial", 20),
                  borderwidth=0, bd=3, command=self.sqrt).grid(row=0, column=3, sticky=tk.NSEW)

        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.label.config(text=self.current_expression[:11])

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.label.config(text="")
        self.window.children['!frame'].children['!label'].config(text="")

    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.label.config(text=self.current_expression[:11])
        except:
            self.current_expression = "Error"
            self.label.config(text=self.current_expression)

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.label.config(text=self.current_expression[:11])
        except:
            self.current_expression = "Error"
            self.label.config(text=self.current_expression)

    def evaluate(self):
        try:
            self.total_expression += self.current_expression
            self.update_total_label()
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except:
            self.current_expression = "Error"
        self.label.config(text=self.current_expression[:11])

    def update_total_label(self):
        expression = self.total_expression
        for op, symbol in {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}.items():
            expression = expression.replace(op, f' {symbol} ')
        self.window.children['!frame'].children['!label'].config(text=expression)

class JKBannuPulaoApp:
    """Main application class for J&K Bannu Pulao Billing System."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("J&K Bannu Pulao")
        self.root.geometry('1270x685')
        self.bill_manager = BillManager()
        self.email_sender = EmailSender()
        self.is_dark_mode = False
        self.menu_items = {
            'pulao': [
                MenuItem("Aik Pao Pulao", 180),
                MenuItem("Aadha Kilo Pulao", 360),
                MenuItem("Aik Kilo Pulao", 720)
            ],
            'kabab': [MenuItem("Chapli Kabab", 130)],
            'raita_salad': [
                MenuItem("Raita", 40),
                MenuItem("Salad", 40)
            ],
            'drinks': [
                MenuItem("Regular Drink", 60),
                MenuItem("Half Litre Drink", 100),
                MenuItem("Litre Drink", 150),
                MenuItem("1.5 Litre Drink", 200)
            ],
            'mineral': [
                MenuItem("500ml Mineral", 60),
                MenuItem("1000ml Mineral", 100)
            ]
        }
        self.totals = {
            'pulao': 0,
            'kabab': 0,
            'raita_salad': 0,
            'drinks': 0,
            'mineral': 0
        }
        self.total = 0
        self.create_ui()

    def create_ui(self):
        """Set up the main application UI."""
        # Heading
        self.heading_label = Label(self.root, text='J&K Bannu Pulao', font=('times new roman', 25, 'bold'),
                                  bg='chocolate3', fg='white', relief=tk.GROOVE, bd=10)
        self.heading_label.pack(fill=tk.X)

        # Customer Details
        customer_frame = LabelFrame(self.root, text='Customer Details', font=('times new roman', 12, "bold"),
                                   fg="gold", bd=6, relief=tk.GROOVE, bg='chocolate3')
        customer_frame.pack(fill=tk.X)
        self.name_entry = Entry(customer_frame, font=('arial', 15), bd=7, width=18)
        Label(customer_frame, text='Customer Name', font=('times new roman', 12, "bold"), bg="chocolate3", fg='white').grid(row=0, column=0, padx=20)
        self.name_entry.grid(row=0, column=1, padx=8)
        self.phone_entry = Entry(customer_frame, font=('arial', 15), bd=7, width=18)
        Label(customer_frame, text='Phone Number', font=('times new roman', 12, "bold"), bg="chocolate3", fg='white').grid(row=0, column=2, padx=20, pady=2)
        self.phone_entry.grid(row=0, column=3, padx=8)
        self.bill_number_entry = Entry(customer_frame, font=('arial', 15), bd=7, width=18)
        Label(customer_frame, text='Bill Number', font=('times new roman', 12, "bold"), bg="chocolate3", fg='white').grid(row=0, column=4, padx=20, pady=2)
        self.bill_number_entry.grid(row=0, column=5, padx=8)
        Button(customer_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, cursor='hand2',
               command=lambda: self.bill_manager.search_bill(self.bill_number_entry.get(), self.textarea)).grid(row=0, column=6, padx=25, pady=6)

        # Product Frames
        product_frame = tk.Frame(self.root)
        product_frame.pack()
        self.create_menu_frame(product_frame, 'pulao', 'Pulao', 0, 0)
        self.create_menu_frame(product_frame, 'drinks', 'Cold Drinks', 0, 1)
        kabab_frame = LabelFrame(self.menu_items['pulao'][0].entry.master, text='Kabab', font=('times new roman', 15, "bold"),
                                 fg="gold", bd=5, relief=tk.GROOVE, bg='chocolate3')
        kabab_frame.grid(row=3, column=0)
        self.create_menu_items(kabab_frame, 'kabab', 0)
        raita_salad_frame = LabelFrame(self.menu_items['pulao'][0].entry.master, text='Raita&Salad', font=('times new roman', 15, "bold"),
                                      fg="gold", bd=5, relief=tk.GROOVE, bg='chocolate3')
        raita_salad_frame.grid(row=4, column=0)
        self.create_menu_items(raita_salad_frame, 'raita_salad', 0)
        mineral_frame = LabelFrame(self.menu_items['drinks'][0].entry.master, text='Mineral Water', font=('times new roman', 15, "bold"),
                                  fg="gold", bd=5, relief=tk.GROOVE, bg='chocolate3')
        mineral_frame.grid(row=4, column=0, pady=15)
        self.create_menu_items(mineral_frame, 'mineral', 0)

        # Bill Area
        bill_frame = tk.Frame(product_frame, bd=8, relief=tk.GROOVE)
        bill_frame.grid(row=0, column=2, padx=5)
        Label(bill_frame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=tk.GROOVE).pack()
        scrollbar = Scrollbar(bill_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textarea = Text(bill_frame, height=22, width=50, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textarea.yview)
        self.textarea.pack()

        # Total Prices
        bill_menu_frame = LabelFrame(self.root, text='Total Prices', font=('times new roman', 15, "bold"),
                                     fg="gold", bd=8, relief=tk.GROOVE, bg='chocolate3')
        bill_menu_frame.pack(fill=tk.X)
        self.total_entries = {}
        for i, (category, label) in enumerate([('pulao', 'Pulao'), ('kabab', 'Kabab'), ('raita_salad', 'Raita&\nSalad'), ('drinks', 'Cold Drinks'), ('mineral', 'Mineral Water')]):
            Label(bill_menu_frame, text=label, font=('times new roman', 15, "bold"), bg="chocolate3", fg='white').grid(row=0, column=i*2, pady=4, padx=10, sticky='w')
            entry = Entry(bill_menu_frame, font=('times new roman', 12, "bold"), width=9, bd=5)
            entry.grid(row=0, column=i*2+1)
            self.total_entries[category] = entry

        # Buttons
        button_frame = tk.Frame(bill_menu_frame, bd=5, relief=tk.GROOVE)
        button_frame.grid(row=0, column=8, padx=10, pady=5)
        buttons = [
            ('Total', self.calculate_total),
            ('Bill', self.generate_bill),
            ('Print', lambda: self.bill_manager.print_bill(self.textarea.get(1.0, tk.END))),
            ('Send', self.open_email_window),
            ('Clear', self.clear),
            ('Dark Mode', self.toggle_dark_mode),
            ('Calculator', lambda: Calculator())
        ]
        for i, (text, command) in enumerate(buttons):
            Button(button_frame, text=text, font=('arial', 10, 'bold'), bg='chocolate3', fg='white', bd=5, width=8 if text == 'Dark Mode' else 5,
                   cursor='hand2', command=command).grid(row=0, column=9+i, padx=4)

    def create_menu_frame(self, parent, category, title, row, col):
        """Create a frame for a menu category."""
        frame = LabelFrame(parent, text=title, font=('times new roman', 15, "bold"), fg="gold", bd=5, relief=tk.GROOVE, bg='chocolate3')
        frame.grid(row=row, column=col)
        self.create_menu_items(frame, category, 0)

    def create_menu_items(self, frame, category, start_row):
        """Create menu items for a category."""
        for i, item in enumerate(self.menu_items[category]):
            Label(frame, text=f"    {item.name}", font=('times new roman', 15, "bold"), bg="chocolate3", fg='white').grid(row=start_row+i, column=0, pady=10, padx=5, sticky='w')
            item.entry = Entry(frame, font=('times new roman', 15, "bold"), width=10, bd=5)
            item.entry.grid(row=start_row+i, column=1, pady=10, padx=8)
            item.entry.insert(0, 0)

    def calculate_total(self):
        """Calculate and display total prices for each category."""
        self.total = 0
        for category in self.menu_items:
            self.totals[category] = sum(item.get_total() for item in self.menu_items[category])
            self.total_entries[category].delete(0, tk.END)
            self.total_entries[category].insert(0, f"{self.totals[category]} RS")
            self.total += self.totals[category]

    def generate_bill(self):
        """Generate and display the bill."""
        if all(item.entry.get() == '0' for category in self.menu_items for item in self.menu_items[category]):
            messagebox.showinfo('Info', 'Please select items and then hit the Total button')
        elif not self.total_entries['pulao'].get():
            messagebox.showerror('Error', 'Please hit the Total button')
        elif not self.name_entry.get() or not self.phone_entry.get():
            messagebox.showinfo('Info', 'Please provide customer details')
        else:
            self.textarea.delete(1.0, tk.END)
            lines = [
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                f"\n\t      ❖ 𝙅&𝙆 𝘽𝙖𝙣𝙣𝙪 𝙋𝙪𝙡𝙖𝙤 ❖   \t\t{self.bill_manager.date}",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                f"\n Bill Number:\t{self.bill_manager.bill_number}",
                f"\n Customer Name:\t{self.name_entry.get()}",
                f"\n Phone Number:\t{self.phone_entry.get()}",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "    𝙄𝙩𝙚𝙢𝙨\t\t\t𝙌𝙮𝙩\t\t𝙋𝙧𝙞𝙘𝙚",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            ]
            for category, title in [('pulao', '𝙋𝙪𝙡𝙖𝙤'), ('kabab', '𝘾𝙝𝙖𝙥𝙡𝙞 𝙆𝙖𝙗𝙖𝙗'), ('raita_salad', ''), ('drinks', '𝘾𝙤𝙡𝙙 𝘿𝙧𝙞𝙣𝙠𝙨'), ('mineral', '𝙈𝙞𝙣𝙚𝙧𝙖𝙡 𝙒𝙖𝙩𝙚𝙧')]:
                if title:
                    lines.append(f"    {title}\n")
                for item in self.menu_items[category]:
                    qty = item.entry.get()
                    if qty != '0':
                        lines.append(f"   {item.name}\t\t\t{qty}\t\t{item.get_total()}RS")
                if title:
                    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append(f"    𝙏𝙤𝙩𝙖𝙡\t\t\t{self.total} RS")
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            lines.append("  Software by Muhammad Usman | Tel:) 03277179560")
            self.textarea.insert(tk.END, '\n'.join(lines))
            self.bill_manager.save_bill(self.textarea.get(1.0, tk.END), self.textarea)

    def open_email_window(self):
        """Open a window to send the bill via email."""
        if self.textarea.get(1.0, tk.END).strip() == '':
            messagebox.showerror("Error", "Bill is empty.")
        else:
            email_window = Toplevel()
            email_window.title('Send Email')
            email_window.config(bg='chocolate3')
            email_window.resizable(0, 0)
            sender_frame = LabelFrame(email_window, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='chocolate3', fg='white')
            sender_frame.grid(row=0, column=0, padx=40, pady=20)
            Label(sender_frame, text="Sender's Email", font=('arial', 14, 'bold'), bg='chocolate3', fg='white').grid(row=0, column=0, padx=10, pady=8)
            sender_entry = Entry(sender_frame, font=('arial', 14, 'bold'), bd=2, width=23)
            sender_entry.grid(row=0, column=1, padx=10, pady=8)
            Label(sender_frame, text="Password", font=('arial', 14, 'bold'), bg='chocolate3', fg='white').grid(row=1, column=0, padx=10, pady=8)
            password_entry = Entry(sender_frame, font=('arial', 14, 'bold'), bd=2, width=23, show='*')
            password_entry.grid(row=1, column=1, padx=10, pady=8)
            receiver_frame = LabelFrame(email_window, text='RECEIVER', font=('arial', 16, 'bold'), bd=6, bg='chocolate3', fg='white')
            receiver_frame.grid(row=1, column=0, padx=40, pady=20)
            Label(receiver_frame, text="Email Address", font=('arial', 14, 'bold'), bg='chocolate3', fg='white').grid(row=0, column=0, padx=10, pady=8)
            receiver_entry = Entry(receiver_frame, font=('arial', 14, 'bold'), bd=2, width=23)
            receiver_entry.grid(row=0, column=1, padx=10, pady=8)
            Label(receiver_frame, text="Message", font=('arial', 14, 'bold'), bg='chocolate3', fg='white').grid(row=1, column=0, padx=10, pady=8)
            email_textarea = Text(receiver_frame, font=('arial', 14, 'bold'), bd=2, relief=tk.SUNKEN, width=42, height=9)
            email_textarea.grid(row=2, column=0, columnspan=2)
            email_textarea.insert(tk.END, self.textarea.get(1.0, tk.END).replace('━', '').replace('\t\t\t', '\t\t').replace('Software by Muhammad Usman | Tel:) 03277179560', ''))
            Button(email_window, text='SEND', font=('arial', 14, 'bold'), width=9, cursor='hand2',
                   command=lambda: self.email_sender.send_email(sender_entry.get(), password_entry.get(), receiver_entry.get(), email_textarea.get(1.0, tk.END), email_window)).grid(row=2, column=0, pady=20)

    def toggle_dark_mode(self):
        """Toggle between dark and light modes for all widgets."""
        self.is_dark_mode = not self.is_dark_mode
        bg_color = "#212121" if self.is_dark_mode else "white"
        fg_color = "white" if self.is_dark_mode else "black"
        frame_bg = "black" if self.is_dark_mode else "chocolate3"
        button_bg = "red4" if self.is_dark_mode else "chocolate3"
        button_fg = "white" if self.is_dark_mode else "white"
        entry_bg = "#333333" if self.is_dark_mode else "white"
        text_bg = "#333333" if self.is_dark_mode else "white"

        def update_widget(widget):
            """Recursively update widget colors based on type."""
            try:
                if isinstance(widget, (tk.Frame, tk.LabelFrame)):
                    widget.configure(bg=frame_bg, fg=fg_color)
                elif isinstance(widget, tk.Label):
                    widget.configure(bg=frame_bg, fg=fg_color)
                elif isinstance(widget, tk.Button):
                    widget.configure(bg=button_bg if widget.cget('text') == 'Dark Mode' else frame_bg, fg=button_fg)
                elif isinstance(widget, tk.Entry):
                    widget.configure(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
                elif isinstance(widget, tk.Text):
                    widget.configure(bg=text_bg, fg=fg_color, insertbackground=fg_color)
                elif isinstance(widget, tk.Scrollbar):
                    widget.configure(bg=frame_bg, troughcolor=frame_bg)
            except tk.TclError:
                pass  # Ignore widgets that don't support bg/fg
            for child in widget.winfo_children():
                update_widget(child)

        # Update root and all its children
        self.root.configure(bg=bg_color)
        update_widget(self.root)

    def clear(self):
        """Clear all input fields and reset the bill area."""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.bill_number_entry.delete(0, tk.END)
        self.textarea.delete(1.0, tk.END)
        for category in self.menu_items:
            for item in self.menu_items[category]:
                item.entry.delete(0, tk.END)
                item.entry.insert(0, 0)
            self.total_entries[category].delete(0, tk.END)
        self.total = 0

    def run(self):
        """Start the application."""
        self.root.mainloop()

if __name__ == "__main__":
    app = JKBannuPulaoApp()
    app.run()