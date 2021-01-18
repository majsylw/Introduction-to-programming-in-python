'''
Kółko i krzyżyk rozgrywane są na planszy 3 × 3. Pojedynczy wiersz planszy można reprezentować jako listę trzech elementów, 
reprezentujących pola wiersza, w której element ’X’ oznacza postawiony krzyżyk, ’O’ oznacza postawione kółko, a ’.’ oznacza puste pole. 
Całą planszę można reprezentować za pomocą trzech napisów, z której każdy reprezentuje kolejny wiersz planszy. 
Napisz program, który na podstawie podanych danych - stanu gry - zwraca komunikat kto wygrał. 

W swoim rozwiązaniu wyszczególnij:
- funkcję ttt_result(), która dla trzech argumentów (3 napisy) reprezentującej stan całej planszy od góry (pierwszy) 
do dołu (trzeci argument)  zwraca: 
    - 1, gdy wygrał gracz grający kółkiem; 
    - 2, gdy wygrał gracz grający krzyżykiem; 
    - lub 0, gdy gra nie jest rozstrzygnięta. 
- funkcję main(), w której wywołasz funkcję ttt_result()
  na przykładowych danych (nie musza być wprowadzane z klawiatury) 
   i w zależności od wyniku wypiszesz na ekran stosowny komunikat.

Przykładowo, wywołanie ttt_result(’XOO’,  ’.OX’, ’XO.’) powinno zwrócić 1.

Wskazówka: Aby dobrać się do poszczególnych składowych napisu użyj [], np.
napis = 'Anna'
print(napis[0]) # wypisze 'A'
print(napis[3]) # wypisze 'a'
'''
