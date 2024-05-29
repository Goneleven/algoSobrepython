# ATIVIDADE 6
#|O cardápio da Lanchonete Bom Apetite é o seguinte:

"""                 Código do Lanche        Especificação           Preço
Unitário(R$)
                    100                 Cachorro quente         2,50
                    101                 Bauru simples           2,00
                    102                 Bauru c/ovo             3,50
                    103                 Hamburger               5,10
                    104                 Cheeseburger            3,30
                    105                 Refrigerante            2,00

Escrever um algoritmo que vá lendo o código do item pedido, a quantidade e vá calculando  o  valor  total  a  ser  pago  pelo  pedido.
OBSERVAÇÃO: Use  uma  flag  para continuar no programa.
"""

print("\n programa que calcula os pedidos de um restaurante\n")



flag = True
precoLanche = 0

while flag:
    codigoLanche = input("Digite o Código do Lanche: \n100 - Cachorro quente | R$2,50 \n101 - Bauru simples | R$2,00 \n102 - Bauru c/ovo | R$3,50 \n103 - Hamburger | R$5,10 \n104 - Cheeseburger | R$3,30 \n105 - Refrigerante | R$2,00\n 1 - Para pedir a Conta \n")

    

    if(codigoLanche == 1):
        flag = False
        
    else:
        if(codigoLanche == 100):
            precoLanche = precoLanche + 2.5
            
        else:
            if(codigoLanche == 101):
                precoLanche = precoLanche + 2.0
            
            else:
                if(codigoLanche == 102):
                    precoLanche = precoLanche + 3.5   
                    
                else:
                    if(codigoLanche == 103):
                        precoLanche = precoLanche + 5.10
                        
                    else:
                        if(codigoLanche == 104):
                            precoLanche = precoLanche + 3.30
                            
                        else:
                            if(codigoLanche == 105):
                                precoLanche = precoLanche + 2.0
                                
                            else:
                                print("Você colocou codigos Que não constam no sistema")
                                
    print(precoLanche)
        
        
print("A Conta deu ")