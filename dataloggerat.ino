#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>


#define BAUDRATE 74880                   // Habilita o BAUDRATE em 74880
#define F_CPU 16000000UL                  // Define a frequência da CPU
#define UBRR F_CPU/BAUDRATE/16UL - 1      // Calula o valor de reg UBRR 


int Digital_input() // Função que permite ler uma entrada digital
{
  int Digital_val;
  DDRD&=!(1<<2); // Habilita PD2 como uma entrada
  Digital_val = (PIND & (1<<2))>>2; // Configura HIGH (1) e LOW (0) 
  if(Digital_val==1){Digital_val='A';}
  else{Digital_val='Z';}
  return Digital_val;
}
byte ADCsingleREAD() Função que habilita e configura o ADC
{
    byte value;
    
    ADMUX = (1<<REFS0) | (1<<MUX0) | (1<<MUX2); // Configura a V de Referência e o input analógico (A5)
    ADMUX  &= ~(0 << ADLAR);   // clear for 10 bit resolution 
    ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);    // 128 prescale for 8Mhz
    ADCSRA |= (1 << ADEN);    // Habilita o ADC
    ADCSRA |= (1 << ADSC);    // Permite inicialização da conversão
    while(ADCSRA & (1 << ADSC));      // A partir daqui, espera-se a finalização do ADC
    uint8_t lowADC = ADCL;                  // salva a info de lowADC       
    uint16_t x = ADCH<<8 | lowADC;          // highADC + lowADC 
    value = uint8_t(x>>2);                  // Com o deslocamento de bits utilizamos os 8 bits MSB
    return value;
}

    
void USART_init(void) 
{
  UBRR0H = (UBRR>>8);      // config 
  UBRR0L = (UBRR);         // UBRR
  UCSR0B = (1<<RXEN0)|(1<<TXEN0);         // Habilita TX e RX
  UCSR0C = ((1<<UCSZ00)|(1<<UCSZ01));     // 8 bits
  UCSR0A&=~(1<<U2X0);                     // asynchronous normal mode
}

void USART_send(unsigned char data)
{
  while(!(UCSR0A & (1<<UDRE0)));          // espera o buffer para enviar os dados
  UDR0 = data;                            // envia o valor para o buffer
}

int main(void)
{
   USART_init();
   while (1)
    {  
       USART_send(ADCsingleREAD()); //Envia a leitura do ADC para o terminal
       USART_send(Digital_input()); //Envia a leitura digital para o terminal
       _delay_ms(400);
       
          
    }
}
