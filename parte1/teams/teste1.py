#Dados o tamanho de um arquivo (Em bits), bem como a velocidade da conexão
#(Em bits por segundo), informe o tempo necessário para o download do arquivo.

#Atividade 2:

print('Programa que calcula o tempo necessário para download de um arquivo')


#VAR

tamanhoArquivo = int(input('Digite o tamanho do Arquivo: \n'))

velocidadeConexao = float(input('Coloca a velocidade (bits/s) \n'))


#exec.

tempoDownload = tamanhoArquivo / velocidadeConexao

print('Tempo de download é de: ', tempoDownload, '/s')