# Testeando librearia locale
import locale
locale.setlocale(locale.LC_ALL, '')

numero_test = 5000

print(f"${numero_test:n}")