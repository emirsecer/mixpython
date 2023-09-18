import tkinter as tk

def check_password():
    if password_entry.get() == "şifre1":
        success_window = tk.Toplevel(root)
        success_window.title("Giriş Başarılı")
        success_label = tk.Label(success_window, text="Giriş Başarılı!")
        success_label.pack(padx=50, pady=20)
    else:
        error_label.config(text="Yanlış Şifre!")

root = tk.Tk()
root.title("Giriş Ekranı")

# Hoşgeldiniz metni
welcome_label = tk.Label(root, text="Hoşgeldiniz", font=("Helvetica", 18))
welcome_label.pack(pady=20)

# Şifre etiketi
password_label = tk.Label(root, text="Şifrenizi giriniz:")
password_label.pack(pady=10)

# Şifre giriş kutusu
password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
password_entry.pack(pady=10)

# Giriş butonu
login_button = tk.Button(root, text="Giriş", font=("Helvetica", 14), command=check_password)
login_button.pack(pady=10)

# Yanlış şifre etiketi
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=5)

root.mainloop()
