@ -1,21 +1,22 @@

# 1 - Nome do Projeto: BARDCORE

Este projeto está sendo desenvolvido por: Arthur Macabu Erthal, Luan Lopes da Silva, Lucas Coutinho Cunha

---
# 2 - Highconcept

BARDCORE é um twin-stick shooter em que o jogador age no ritmo da música. Derrote inimigos e supere contratempos para restaurar e harmonia entre os reinos! 

---
# 3 - Gameplay e Enredo

## Aparência do personagem

O protagonista é um menestrel misterioso que veste um chapéu por cima do capuz, revelando somente os olhos. Ele porta um alaúde mágico que tem uma única corda, e batalha contra inimigos com o poder da música.

![bard](https://github.com/TucoErthal/bardcore/assets/67657590/55b45a38-dee3-40b6-8cac-a886eda0ffa8)

Arte conceito do Bardo, o protagonista.

## Controles do jogador
@ -52,72 +53,74 @@
## Interface

![ScreenGDD 1](https://github.com/TucoErthal/bardcore/assets/67657590/4e5e78cb-29e9-4884-a0d7-3156af5b775d)

A interface gráfica contará com um medidor de vida e um indicador para o número de disparos especiais restantes, entre outras métricas, localizados em uma barra na parte superior da tela, como em vários jogos arcade e de NES. A câmera seguirá o jogador, tendendo levemente para direção do cursor, permitindo que o jogador controle o campo de visão com o mouse. O cursor terá o formato de uma mira, indicando a direção para a qual os projéteis irão, e contará com um temporizador que assiste o jogador a sincronizar seus inputs com o ritmo da música.
![crosshair](https://github.com/TucoErthal/bardcore/assets/67657590/4fec7972-a142-4b22-8a94-332dc12cdf1d)


![combo](https://github.com/TucoErthal/bardcore/assets/67657590/b95346f0-677f-40d5-9f7d-9ce97d347edc)

Enquanto o botão direito do mouse se mantiver pressionado, o personagem não poderá se mover, e as teclas direcionais serão convertidas em notas. O jogador poderá tocar melodias diferentes (combos) para empoderar seus próximos disparos. Novas notas são desbloqueadas à medida que o Bardo recupera as cordas do seu alaúde. Além da corda com a qual o Bardo inicia sua jornada, o jogador pode obter 3 cordas que incrementam o sistema de combos. A obtenção da quinta corda representa o final da aventura.

![pattern](https://github.com/TucoErthal/bardcore/assets/67657590/9eff9c1f-10a7-44e0-a866-192611daad14)

Quando um inimigo de elite é instanciado, um padrão rítmico (que chamaremos de compasso) aleatório* é associado a ele. Esse padrão é formado por notas e pausas que correspondem, cada uma, a uma batida da música. O primeiro ataque que o jogador fizer contra o inimigo inicia a detecção do padrão. A cada batida, a instrução apropriada deve ser respeitada pelo jogador (atirar ou esperar). Se o padrão for quebrado, ele é reiniciado. Quando a sequência é completada, o inimigo perde uma vida (representada pelo círculo vermelho acima da barra de compasso). O inimigo é derrotado quando não restar nenhuma vida.

* O padrão é formado por 8 notas/pausas, e sempre começa com uma nota (para que a detecção de padrão não seja iniciada em resposta a um eventual silêncio acidental do jogador.


## Input

W, A, S, D - teclas direcionais, serão usadas para movimentar o jogador ou tocar combos de notas com o alaúde.

Botão esquerdo do mouse - dispara uma nota musical onde o mouse estiver apontando.

Botão direito do mouse - Usado em combinação com as teclas direcionais para tocar combos de notas.

Barra de espaço / Shift - O Bardo realiza um avanço horizontal, desviando de ataques inimigos.

ESC - fecha o jogo.

---
# 5 - Audio e música
A trilha sonora do jogo consistirá em 4+ composições originais adequadas aos cenários mencionados, com inspiração nas trilhas de jogos da era NES / SNES. Usaremos efeitos sonoros de domínio público. As músicas planejadas são:
* Tema de introdução do jogo (Abertura, tela de início)
* Música da zona de tutorial
* Tema de combate principal
* Trilha de combate contra o boss.

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



---
# 7 - Ideias adicionais e observações

Muitas mecânicas ainda estão sendo avaliadas e estão sujeitas a mudanças no curso do desensolvimento do jogo. Parâmetros como a vida do jogador, quantos disparos especiais ele recebe, assim como o comportamento dos inimigos, serão ajustados de acordo com playtesting, com o intuito de criar uma experiência justa e divertida. As artes exibidas neste documento de desenvolvimento não são finais e serão refinadas e reiteradas até que os resultados sejam satisfatórios.

Entre algumas das ideias que temos para o jogo, estão:
### Algumas ideias para tipos de disparo
- Distante --> Um disparo que vai mais longe do que o normal.
- Explosivo --> "Explode" e dá dano em área ao impacto.
- Múltiplo --> Atira mais de um disparo de uma vez em um cone.


### Ideias para coletáveis
- Item de cura --> Recupera parte da vida.
