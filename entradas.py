import serial #Biblioteca necessária para ler a porta serial

arduino_dados = serial.Serial("COM3",74880) #Função que lê os dados da porta serial

while(True):

    '''Loop infinito que lê e printa os dados
    da porta serial'''
    
    print(arduino_dados.read()) #Printando os dados lidos da porta serial
