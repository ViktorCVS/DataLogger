# DataLogger
O atual projeto busca documentar a construção de um DataLogger com o microcontrolador Arduino ATmega328p, programado em C puro e seus dados tratado e exibidos em Python. Vou dividí-lo em 4 etapas

- [x] Montar o circuito
- [x] Programar o Arduino
- [x] Conseguir os dados pela porta serial com Python
- [x] Gerar o gráfico em tempo real

E esses são os materiais necessários:

- [x] Arduino UNO ATmega328p com o cabo serial
- [x] Potenciômetro
- [x] Botão
- [x] Protoboard (opcional)
- [x] Jumpers/fios 

Bibliotecas necessárias para o Arduino (todas nativas):

- [x] avr/io.h
- [x] stdint.h
- [x] util/delay.h

Bibliotecas necessárias para o Python (instalação com o 'pip install'):

- [x] pyserial
- [x] matplotlib
- [x] drawnow

## Montagem do circuito

### Potenciômetro

![f3](https://user-images.githubusercontent.com/69547580/117088058-c11a7b00-ad27-11eb-969b-8581669becb5.jpg)

Usamos o potenciômetro curva B de 1k ohm

### Botão

![f2](https://user-images.githubusercontent.com/69547580/117088056-c081e480-ad27-11eb-89c4-2526ab32bfcc.jpg)

Botão simples de dois terminais

### Resistor

![f1](https://user-images.githubusercontent.com/69547580/117088055-c081e480-ad27-11eb-9b19-e9afde85020e.jpg)

Aqui usamos um resistor de precisão de 2k ohm

### Esquemático

### Circuito montado

## Resultados

Aqui apresentarei os resultados de cada código

### Resultados do Arduino

![codear](https://user-images.githubusercontent.com/69547580/117087069-d510ad80-ad24-11eb-937f-999ec203627e.jpg)

Perceba que os dados, apesar de não serem legíveis ainda, estão aparecendo na porta serial e variam conforme mexemos no circuito. O tratamento será feito posteriormente.

### Resultados do Python 'entradas.py'

![codepf](https://user-images.githubusercontent.com/69547580/117087070-d5a94400-ad24-11eb-95ea-d43676599c0f.jpg)

Aqui conseguimos pegar os dados de saída da porta serial (enviados pelo arduino) com um código em Python.

### Resultados do Python 'datalogger.py'

![gsm](https://user-images.githubusercontent.com/69547580/117087071-d5a94400-ad24-11eb-9a87-272ef64bd1be.jpg)

Por fim, nosso resultado em gráfico com o tratamento dos dados da porta de comunicação feito em Python.





