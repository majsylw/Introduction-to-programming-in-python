## Laboratorium 1 - 12.10.2020r.

# Pierwsze kroki
## Instalacja środowiska
Zanim zaczniemy kodować musimy zainstalować na naszym komputerze odpowiednie programy:
- interpreter języka Python (wraz z potrzebnymi bibliotekami - opcjonalnie) 
- zintegrowane środowisko programistyczne (ang. integrated development environment, IDE, <br>w naszym przypadku będzie to IDLE).

Interpreter wraz ze środowiskiem można pobrać z oficjalnej strony https://www.python.org/. Warto zwrócić uwagę na to, że istnieją dwie wersje języka Python: 2 i 3. Pomiędzy nimi są zasadnicze różnice, znacznie większe niż tylko numerek przy nazwie. Aktualnie rozwijaną wersją jest wersja 3.x i to właśnie jej dotyczy ten poradnik. Od stycznia 2020 wersja 2.x przestanie być wspierana, a tym samym uaktualniana.

Aby pobrać interpreter przechodzimy w zakładkę "Downloads" i wybieramy "Download Python 3.x" (obecnie najbardziej aktualną wersją jest wersja 3.8.0).
![](https://github.com/majsylw/Introduction-to-programming-in-python/blob/master/screens/screenshot.png)
Jeśli szukasz innych wersji, wystarczy zjechać w dół strony i wybrać odpowiednią.
![](https://github.com/majsylw/Introduction-to-programming-in-python/blob/master/screens/releases.png)

Następnie przechodzimy przez proces instalacji.

## Uruchomienie powłoki Pythona (python shell)
Korzystając ze zintegrowanego środowiska programistycznego IDLE możemy pracować w trybie interaktywnym oraz skryptowym.
Działając w trybie interaktywnym mamy do czynienia z powłoką Pythona (python shell).
![](https://github.com/majsylw/Introduction-to-programming-in-python/blob/master/screens/shell.png)
Tryb interaktywny jest użyteczny podczas testowania kodu, ale wpisywane polecenia nie będą zapisane jako program. Aby zapisać nasz kod musimy utworzyć skrypt, czyli plik z rozszerzeniem *.py. W tym celu z menu głównego wybieramy "File", a następnie "New file" (lub kilkamy kombinację Ctrl+N).

Wpiszmy następujący kod w nowo utworzony plik:
```python
def main():
    print("Witaj świecie!")
main()
```
i zapiszmy go (albo wybierając kolejno File -> Save lub kombinację klawiszową Ctrl+S) jako ```witaj_swiecie.py```.
![](https://github.com/majsylw/Introduction-to-programming-in-python/blob/master/screens/script.png)

Za chwilę omówimy składowe powyższego skryptu, ale na początek sprawdźmy jaki jest efekt jego działania. W tym celu naciśij klawisz F5 lub wybierz z menu Run -> Run Module. W interpreterze powinien pojawić się napis ```"Witaj świecie!"```.
![](https://github.com/majsylw/Introduction-to-programming-in-python/blob/master/screens/witaj.png)

Skoro nasza ciekawość została zaspokojona i wiemy już, że nasz program działa. Czas zrozumieć poszczególne składowe kodu. Nasz program to skrypt napisany w języku Python. Tutaj musimy zwrócić szczególną uwagę na dwie rzeczy:
- po pierwsze napisany przez nas kod jest interpretowany przy każdym uruchomieniu, co oznacza tyle, że aby uruchomić program na urządzeniu potrzebujemy aby było ono wyposażone w interpreter dla języka python (możemy sobie wyobrazić go jako taki program tłumaczący linijka po linijce kod na język bardziej zrozumiały dla komputera),
- po drugie, nasz skrypt wykonuje się cały od góry do dołu - aby uniknąć bałaganu tworzymy funkcję main() (korzystając z instrukcji ```def main()```, którą w ostatniej linijce programu wywołujemy (mówimy, że jej treść ma zostać wykonana) poprzez polecenie ```main()```.

Utworzenie funkcji main() jest naszym własnym wyborem, konwencją, której będziemy się trzymać podczas tych zajęć. Więcej o funkcjach dowiemy się na przyszłych zajęciach. Teraz jeszcze skoncentrujemy się na wnętrzu funkcji main, czyli na linijce ```print("Witaj świecie!")```. print() to funkcja wypisująca podany komunikat (w naszym przypadku “Witaj świecie!”) na tzw. standardowe wyjście. Zazwyczaj oznacza to po prostu konsolę, w której kazaliśmy wykonać nasz program - w naszym przypadku jest to powłoka IDLE.

Na koniec zwróćmy jeszcze uwagę na jeszcze jeden ważny szczegół: tzw. wcięcia. Liczba spacji poprzedzająca kod we wnętrzu funkcji, np. main musi być taka sama. Co więcej, liczba wcięć, czyli spacji, ew. znaków tabulacji, powinna być taka sama w całym programie. My będziemy korzystać z 4-spacjowego wcięcia lub pojedynczej tabulacji. Kod wcina się w każdej konstrukcji językowej: funkcji, instrukcji warunkowej, pętli itp. Wcięcia “kumulują się” wraz z zagnieżdżaniem takich konstrukcji. Oznacza to, że w instrukcji warunkowej w funkcji napiszemy kod poprzedzony 8 spacjami. Jeśli masz doświadczenia z innymi językami programowania, to zapewne w nich funkcję wydzielania fragmentu kodu pełniły klamerki. To znak rozpocznawczy języka Python: nie ma klamerek, jest za to wymuszenie spójnej liczby wcięć, co ma zapewnić większą czytelność kodu.

Jeśli czytelniku dotrwałeś do tego momentu: Gratulacje, udało Ci się stworzyć swój pierwszy program w języku python :-)

Ten i dalsze tutoriale znajdziesz na [wiki](https://github.com/majsylw/Introduction-to-programming-in-python/wiki).