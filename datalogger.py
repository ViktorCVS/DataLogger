import matplotlib.pyplot as plt #Biblioteca para a geração de gráficos
from drawnow import *           #Biblioteca para fazer os gráficos em tempo real
import serial                   #Biblioteca para pegar os dados da porta serial

arduino = serial.Serial("COM3",74880)  #Função que atribui à variável 'arduino' o conteúdo da porta serial selecionada

analog = []    #Vetor que armazenará as grandezas analógicas
digital = []   #Vetor que armazenará as grandezas digitais
aux = 0        #Variável auxiliar que irá fazer a separação dos dados entre analógicos ou digitais
cnt = 0        #Variável auxiliar para selecionar a janela de tempo em que os dados serão exibidos

plt.ion()      #Indicando para a biblioteca Matplotlib que os gráficos serão gerados em tempo real    

def figura():

    '''Função criada para gerar os gráficos'''

    plt.title("Mensuração de grandezas analógicas e digitais") #Título do gráfico
    
    plt.ylim(0,5.5)                             #Limites do gráfico analógico
    plt.grid(True)                              #Habilitando grade no gráfico
    plt.ylabel("Tensão Analógica 0-5V")         #Legenda no eixo y à esquerda
    plt.xlabel("Segundos transcorridos")        #Legenda no eixo x
    plt.plot(analog,"ro-",label="Analógica")    #Gerando o gráfico do vetor analógico
    plt.legend(loc='upper left')                #Definindo a legenda para a sessão superior esquerda
    
    plt2=plt.twinx()                            #Habilitando um novo eixo simultâneo
    plt.ylim(0,1.5)                             #Estabelendo os limites do gráfico digital
    plt.ylabel("Tensão Digital ")               #Legenda do eixo y à direita
    plt2.plot(digital,'b^-',label="Digital")    #Gerando o gráfico do vetor digital
    plt.legend(loc='upper right')               #Definindo a legenda para a sessão superior direita
    


while True:

    '''Laço que irá pegar os dados da porta serial e exibí-los como gráfico,
       sem condição de parada'''
    
    while (arduino.inWaiting()==0):

        '''Laço que irá fazer nada enquanto não houver dados na porta serial'''
        
        pass

    if(aux%2==0):

        '''Condicional que checa se a variável é par (referente à grande analógica)
           ou ímpar (referente à grandeza digital'''
        
        aux2 = int.from_bytes(arduino.read(),'big')  #Pegando os dados da porta serial ao mesmo tempo que converte de bytes para inteiro
        aux3 = 5*aux2/255                            #Regra de 3 para passar o valor de 0-255 à 0-5V
        analog.append(aux3)                          #Passando o valor convertido para o vetor analógico
        
    else:
        aux1 = int.from_bytes(arduino.read(),'big')  #Pegando os dados da porta serial ao mesmo tempo que converte de bytes para inteiro

        if(aux1 == 90 ):

            '''Condicional que converte as letras 'A' e 'Z' fornecidas no
               arduino para '0' ou '1', digital'''
            
            aux1 = 0  #Passando para 0 se seu valor inicial for 90
            
        else:
            
            aux1 = 1  #Passando para 1 se não
            
        digital.append(aux1) #Passando o valor convertido para o vetor digital


    drawnow(figura)    #Chamando a função que irá desenhar o gráfico em tempo real
    plt.pause(.000001) #Pequena pausa na geração do gráfico
    
    cnt += 1           #Incrementando a variável responsável pela janela de exibição
    if(cnt>60):

        '''Condicional que checa o valor de cnt para determinar quando os primeiros dados
           serão apagados'''
        
        if(aux%2==0):

            '''Condicional que checa se a variável é par (referente à grande analógica)
               ou ímpar (referente à grandeza digital'''
            
            analog.pop(0)  #Deletando o primeiro dado do vetor analógico
            
        else:
            
            digital.pop(0) #Deletando o primeiro dado do vetor digital
            
    aux+=1 #Incrementando aux para um novo ciclo de exibição



