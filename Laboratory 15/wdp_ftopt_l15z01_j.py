# Wstęp do programowania
# Zaliczenie całościowe
# 30.01.2020 grupa P11-17j
# imię:
# nazwisko:
# indeks:

# Zadanie 1 (15 pkt.)
# Napisz program, pobierający od użytkownika 3 liczby
# rzeczywiste będące długościami boków trójkąta.
# Następnie sprawdź, czy pobrane boki są liczbami dodatnimi.
# Jeżeli podane długości są nieprawidłowe to zakończ program.
# W kolejnym kroku sprawdź, czy podane boki spełniają nierówność
# trójkąta
#   a + b > c, b + c > a, c + a > b
# Jeżeli powyższe zależności nie są spełnione,
# to wydrukuj komunikat o błędzie w przeciwnym razie,
# oblicz pole trójkąta zgodnie ze wzorem Herona:
#       ________________
# P = \/s(s-a)(s-b)(s-c), s = (a+b+c)/2
# Dodatkowo sprawdź, czy trójkąt jest trójkątem równoramiennym
# lub równobocznym. Wypisz odpowiednie komunikaty.

# Przykładowe efekty działania programu:
# =======================================
# Podaj długośc pierwszego boku trójkąta: -2
# Podaj długośc drugiego boku trójkąta: -3
# Podaj długośc trzeciego boku trójkąta: -4
# Przynajmniej jedna z podanych długości nie jest dodatnia. Koniec programu.
# =======================================
# Podaj długośc pierwszego boku trójkąta: 2
# Podaj długośc drugiego boku trójkąta: 2
# Podaj długośc trzeciego boku trójkąta: 2
# Pole trójkąta wynosi: 1.7320508075688772
# Trójkat jest równoboczny
# Trójkat jest równoramienny
# =======================================
# Podaj długośc pierwszego boku trójkąta: 3
# Podaj długośc drugiego boku trójkąta: 4
# Podaj długośc trzeciego boku trójkąta: 5
# Pole trójkąta wynosi: 6.0
# =======================================

