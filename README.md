@ -1,21 +1,22 @@

# 1 - Nome do Projeto: BARDCORE

Este projeto está sendo desenvolvido por: Arthur Macabu Erthal, Luan Lopes da Silva, Lucas Coutinho Cunha

---
# 2 - Highconcept

BARDCORE é um twin-stick shooter em que o jogador age no ritmo da música. Derrote inimigos e supere contratempos para fugir da tirania da NAÇÃO DO MAL! 

---
# 3 - Gameplay e Enredo

## Aparência do personagem

O protagonista é um bardo misterioso que veste um chapéu por cima do capuz, revelando somente os olhos. Ele porta um alaúde mágico e batalha contra inimigos com o poder da música.

![bard](https://github.com/TucoErthal/bardcore/assets/67657590/55b45a38-dee3-40b6-8cac-a886eda0ffa8)

Arte conceito do Bardo, o protagonista.

## Interface
![Screenshot_7.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/Screenshot_7.png)
A interface gráfica contará com um medidor de vida e uma barra de ritmo, indicando quando o jogador deve agir, localizados em uma barra na parte superior da tela, como em vários jogos arcade e de NES. A câmera seguirá o jogador, tendendo levemente para direção do cursor, permitindo que o jogador controle o campo de visão com o mouse. O cursor terá o formato de uma mira, indicando a direção para a qual os projéteis irão.

## Inimigos

O jogador irá navegar entre diversas salas, estas podendo ser bloqueadas até que todos os inimigos da sala são derrotados. 

Entre os inimigos, há aqueles que lançam projéteis na direção do jogador, 
![mage.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/mage.png)  ![Skelly 1.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/Skelly%201.png)
ou os que tentam atacar o jogador por contato. 

![bell.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/bell.png)![ghost 1.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/ghost%201.png)

Após uma certa quantidade de tiros acertarem um inimigo, este irá sumir do mapa. Se os inimigos derrotarem o jogador, todos os inimigos que uma vez foram derrotados irão reaparecer, porém portas que estavam trancadas irão permanecer destrancadas.

Inimigos tem uma chance de, ao serem derrotados, deixarem um coração coletável para trás. Quando o jogador coleta o coração, uma pequena quantidade de vida é restaurada.

![[miniheart.png]]
Após coletar duas cordas mágicas, 

![string.png](https://github.com/TucoErthal/bardcore/blob/main/assets/GDD%20Images/string.png)

cada uma localizada no final de uma sequência de salas, o jogador irá desbloquear a porta central, levando à sala onde o Boss o aguarda. Este inimigo é mais poderoso que os outros, tendo 3 fases de ataque. Com vida máxima, ele atira diretamente ao jogador, e na medida que sua vida é reduzida, os ataques ficam mais intensos. Seu segundo ataque é lançar 3 tiros de uma vez, e o terceiro é lançar tiros em todas as direções. Além disso, enquanto ele atira ao jogador, tentará esmagá-lo com pulos.

Derrotado o boss, o jogador poderá prosseguir para a última sala do jogo, onde vencerá.

## Armadilhas

Existem 3 tipos de armadilhas

### Spike 
Armadilhas que ficam no chão e são ativadas quando o jogador passa por cima

![[Screenshot_3.png]]
### Flamethrower
Armadilhas que ficam presas na parede e atiram bolas de fogo no ritmo da musica

![[Screenshot_8.png]]
### Conveyor
Armadilhas que empurram o jogador na direção das setas, tambem funcionam como uma barreira
![[Screenshot_2.png]]
## Input

W, A, S, D - teclas direcionais, serão usadas para movimentar o jogador ou tocar combos de notas com o alaúde.

Botão esquerdo do mouse - dispara uma nota musical onde o mouse estiver apontando.

Barra de espaço - O Bardo realiza um avanço horizontal, desviando de ataques inimigos.

---
# 5 - Audio e música
A trilha sonora do jogo consistirá de composições originais, com inspiração nas trilhas de jogos da era NES / SNES. Usaremos efeitos sonoros de domínio público ou geradas proceduralmente. As músicas utilizadas são:
* Tema de introdução do jogo, que se toca no trailer
* Tema principal

---
# 6 - Arte Conceito e referências

Everhood serviu como ponto de partida para o projeto. A forma como o jogo integra elementos de música e ritmo com o combate, assim como a estética e a atmosfera do jogo, serviram de inspiração.
![ss_f809bba93b1dc91ff39a091ed78d02102303623a 1920x1080](https://github.com/TucoErthal/bardcore/assets/67657590/12ecf433-9808-4b4a-ba40-11def55afae5)

Shovel Knight serviu como inspiração estética. Adotaremos como referência a resolução de 400x225 que o jogo utiliza, e o teremos como inspiração para o design da interface gráfica.
![shovel-knight-screen_20-1](https://github.com/TucoErthal/bardcore/assets/67657590/e81d7229-9e17-48e2-aae7-6366901daf83)


Os jogos Crypt of the Necrodancer e BPM: Bullets Per Minute são as principais fontes de inspiração em termos de gameplay. Dentre os elementos desse jogo, incorporaremos o indicador de ritmo no cursor do jogador
![crypt](https://github.com/TucoErthal/bardcore/assets/67657590/4ed32941-43f1-488b-a415-585ec6eebda2)
![ss_39c531e1831491b2140a3bdf36cf70ee342a1e6d 1920x1080](https://github.com/TucoErthal/bardcore/assets/67657590/a83d6915-6fa7-4efb-808e-da1afab88034)


O jogo Enter the Gungeon motivou a inclusão de elementos de ação que conferirão maior dinamismo ao jogo, como a perspectiva e a movimentação da câmera e do cursor.
![enter-the-gungeon-switch-switch-spel-nintendo-eshop-europe-wallpaper-4](https://github.com/TucoErthal/bardcore/assets/67657590/8197b617-b836-45bf-89a6-3c5b3a26aa0d)
