<h1 align="center">
  Tibia Tool
</h1>

![tibiaBotReadme](https://github.com/afsdari0/ModuleTB/assets/100225519/fe3ec09a-5e8b-4d4d-af83-d0476ea5a574)
> Status: Concluído ✅

[Download](https://github.com/afsdari0/ModuleTB)

# Bot com várias funcionalidades automáticas para o jogo como:

+ Rotação de caça 
+ Cura com porção ou feitiço
+ Usar comida
+ Usar amuleto e anel 
+ Identificação de piso
+ Pegar itens dos inimigos 
  > Este ultimo precisa de um programa que faça um macro para Pegar itens ao redor do personagem! Com o macro já configurado coloque o botão de ativação na parte marcada no arquivo 📁[main.py](https://github.com/afsdari0/ModuleTB/blob/main/main.py) lembrando que só é aceito botoes do mouse sendo eles "middle, right ou left"
  > 
  > ![macrodef](https://github.com/afsdari0/ModuleTB/assets/100225519/78c361d8-ea13-495a-9a86-25623f35578b)

Pode ser usado por horas caçando totalmente de forma automática!

# Tecnologias utilizadas:

<table>
  <tr>
    <td>Python</td>
  </tr>
  <tr>
    <td>3.11.5</td>
  </tr>
</table>

Além disso, é preciso algumas bibliotecas:

+ Pyautogui
+ Pynput
+ Pillow
+ Opencv
+ Keyboard

Para fazer a instalação rode os seguintes comandos no terminal: 

![bibliotecaspy](https://github.com/afsdari0/ModuleTB/assets/100225519/7292bfaa-f708-4fac-9e04-e2a515f70edb)
> Lembrando que o Python já precisa está presente quando for instalar as bibliotecas! ⚠️

# Observação ⚠️

### O jogo não permite a captura de informações da tela, então você precisará simular uma "Live Stream"!

Segue o passo a passo de como passar por isso:

1) Baixe um software para gravação de vídeo como o [OBS](https://obsproject.com/pt-br/download).
2) Crie uma fonte para a "captura de jogo" e selecione a janela do tibia!
3) Clique com o direito do mouse na fonte de "captura de jogo" que você criou e selecione "Projetor em janela (fonte)" e maximize a janela.
    > Ótimo, agora você já está simulando a "Live Stream"
4) Agora acesse o arquivo 📁[window.py](https://github.com/afsdari0/ModuleTB/blob/main/window.py), executá-lo em um terminal mudara a opacidade da janela original do tibia!
    > As partes marcadas são a janela que será afetada e a opacidade que será configurada de 0 a 255, o correto seria 1 de opacidade para o tibia ficar transparente a cima da janela do OBS assim dando as informações que o bot precisa.
    >
    >![Opacidadepy](https://github.com/afsdari0/ModuleTB/assets/100225519/ebeed870-1980-48a8-a246-15b2cf0e3fc4)
5) Deixe a janela do OBS em toda a tela atrás da janela do tibia com opacidade 1!
    > Agora o bot poderá pegar informações do tibia por meio da janela do OBS que está logo atrás.

# Configuração

### A configuração é um tanto complexa, pois o bot funciona por meio de informações da tela!

No arquivo 📁[config.py](https://github.com/afsdari0/ModuleTB/blob/main/config.py) podemos fazer a configuração onde testaremos todos os locais da tela que precisam ser monitorados pelo bot. Quando pegar todas as coordenadas que precisa da tela coloque cada uma em seu lugar no arquivo 📁[main.py](https://github.com/afsdari0/ModuleTB/blob/main/main.py) 

![coordenadas](https://github.com/afsdari0/ModuleTB/assets/100225519/470d7da7-600d-46ee-8cdf-89e8db150b73)
> Recomendo que de uma olhada na documentação do [Pyautogui](https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions)!

# Marcação

### Será preciso fazer marcações no mapa para cada canto que você for usar o bot, só assim ele conseguirá percorrer sua rota!

![mapReadme](https://github.com/afsdari0/ModuleTB/assets/100225519/6b839d47-c8cd-4eae-894f-f3bb8ad95aaa)
  > Preste bem atenção que há quatro marcações em destaque, o personagem andará de uma a uma formando assim uma rotação do ambiente.

#### O personagem irá ate as marcações no mapa de acordo com suas ordens:

1) Marcação de pá:
     > ![iconfullpa](https://github.com/afsdari0/ModuleTB/assets/100225519/c5d182aa-c2ac-4970-a3a8-a38bfd1b6d86)
2) Marcação de X:
     > ![iconfullx](https://github.com/afsdari0/ModuleTB/assets/100225519/0d8eb38a-859d-49e1-9dff-3e277abd77c8)
3) Marcação de !:
     > ![iconfull!!!](https://github.com/afsdari0/ModuleTB/assets/100225519/8f1fb942-7363-4c26-82d9-5d16293ceb34)
4) Marcação de ?:
     > ![iconfull](https://github.com/afsdari0/ModuleTB/assets/100225519/6d372d9a-16b1-4b8f-a579-1c8bab2c4f04)

Todas as marcações devem aparecer no mini mapa a todo momento durante a execução do bot! ⚠️


# Funcionamento

### Após ter configurado e marcado tudo corretamente, precisara fazer esse procedimento para executar sem problemas: 

1) Fazer o procedimento do tópico "**Observação**"
   > Deixe o jogo com a opacidade = 1 acima da janela do OBS
2) Faça login na sua conta e se prepare para o local de caça!
3) Com todos os pontos marcados e aparentes no seu mini mapa execute o 📁[main.py](https://github.com/afsdari0/ModuleTB/blob/main/main.py) em um terminal.
   > O 📁[main.py](https://github.com/afsdari0/ModuleTB/blob/main/main.py) deve ser o já configurado para a sua máquina como fala no tópico "**Configuração**"!
4) Após aparecer o número "1" no terminal quer dizer que já está pronto para iniciar o bot.
   > ![terminalPrint1](https://github.com/afsdari0/ModuleTB/assets/100225519/b3fce182-c3ef-4ac9-8fe5-028e44da86cc)
5) Agora você pode teclar "**INSERT**" para iniciar o bot ou "**ESC**" para finalizar a execução.
   > Se o seu teclado não for completo, você pode usar o "**FN + INSERT**" para iniciar o bot. Caso inicie o bot, nao tecle INSERT novamente pois isso fará o ESC nao parar a execução e ter que interromper o terminal!! ⚠️

# Avisos ❗

+ Esse bot foi desenvolvido para fins de estudo práticos de Python!
+ Ainda pode conter bugs, futuras correções poderão ser feitas! ⚠️
+ Esse bot não pode ser identificado pelo tibia, mas jogadores podem te gravar usando e você poderá levar ban!
