import PySimpleGUI as sg
from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, '')


sg.theme('DefaultNoMoreNagging')

class Tela:

    def __init__(self):

        # Layout
        layout = [
            [sg.OptionMenu(values=[
                "Taxa 1",
                "Taxa 2"],
                key='opcoes', size=(27, 0), pad=(15, 10))],
            [sg.Text('Digite o valor a ser calculado:', pad=(30, 0))],
            [sg.Input(key='valordigitado', size=(40, 0), pad=(0, 10))],
            [sg.Button('Calcular', pad=(80, 0), bind_return_key=True, size=(30,0))],
            [sg.Output(size=(30,20), key='output')]

        ]
        # Janela
        self.janela = sg.Window('Aplicadora de taxas',
                                size=(250, 460)).layout(layout)

    def iniciar(self):
        
        taxa01 = 1.15
        taxa02 = 1.30
        
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            opcoes = self.values['opcoes']
            valordigitado = self.values['valordigitado']

            self.janela['output'].Update('')
            
            if ',' in valordigitado:
                if '.' in valordigitado:
                    valordigitado = valordigitado.replace('.', '')
                valordigitado = valordigitado.replace(',', '.')

            try:
                valordigitado = Decimal(valordigitado)

            except:
                print('Digite um número válido.')
                continue
            
            #Cálculo
            try:
                if opcoes == 'Taxa 1':
                    valordigitado = valordigitado * Decimal(taxa01)
                
                elif opcoes == 'Taxa 2':
                    valordigitado = valordigitado * Decimal(taxa02)

            except:
                print('Digite um número válido.')
                continue
            

            print(f'R$ {locale.format_string("%.2f", valordigitado, grouping=True)}')


Tela().iniciar()