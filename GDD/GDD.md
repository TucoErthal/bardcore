
# 1 - Nome do Projeto: BARDCORE

Este projeto está sendo desenvolvido por: Arthur Macabu Erthal, Luan Lopes da Silva, Lucas Coutinho Cunha

---
# 2 - Highconcept

Um twin stick shooter onde o jogador luta contra inimigos usando um alaúde elétrico. Atire e se mova no ritmo da música e use o poder do METAL para dominar os reinos! 

---
# 3 - Gameplay e Enredo

## Aparência do personagem

Um bardo coberto por um capuz, deixando sua aparência coberta na maior parte, mostrando somente seus olhos brilhando pelo capuz. Ele utiliza um chapéu com pena, considerado o símbolo de um bardo no universo do jogo. Ele segura um alaúde mágico que utiliza como arma principal para combater os inimigos desse universo e precisa coletar cordas para restaurar a harmonia dos reinos através do seu alaúde.

![[littlebard.png]]
Arte conceito do bardo, com somente uma corda em seu alaúde.

## Controles do jogador

O jogador se move com as teclas do teclado e mira com o mouse. Ao apertar o botão do mouse esquerdo no ritmo da música, um disparo básico é disparado. Ao apetar o botão direito, as teclas de movimento se tornam teclas de combo e o jogador precisa apertar a sequência correta para empoderar os próximos disparos do jogador com um efeito especial. O jogador pode dar dash (no ritmo da música), o que o move uma certa distância mais rápido e o torna temporariamente invulnerável, para desviar os ataques inimigos.
Ao longo do jogo, o jogador desbloqueia novos combos e notas ao pegar cordas para o seu alaúde, para empoderar os disparos do jogador com novos efeitos. Se um tipo de disparo já estiver equipado e um novo combo for feito, os efeitos dos dois tipos de disparo se combinam formando um com os dois efeitos levemente reduzidos. Disparos equipados têm um número de usos limitado.
O jogador terá uma quantidade pequena de "hit points", ou quantos impactos que o jogador poderá levar antes de ser derrotado. Ele poderá recuperar seus hit points no meio do jogo, e se perder todos os hit points, perderá a fase e terá que começar do início.


## Detalhes dos inimigos

### Inimigos comuns

Terão dois tipos de inimigos comuns, atacando somente com disparos simples (também com temática musical) e sendo derrotados após uma pequena quantidade de disparos.

Um deles terá a forma de um gato humanoide que ataca com arranhões de perto. 
O outro terá a forma de um serval humanoide, atacando de longe com miados mágicos.

### Inimigo elite

Um tipo de inimigo que aparece com frequência menor, porém leva mais dano para ser derrotado e só pode ser derrotado quando acertado a um ritmo específico. Serão ursos pardos vestidos com roupas associadas a um estereótipo de cantor russo e serão chamados de "Urso bardo".

### Boss

No final do mapa, o jogador encontrará o "boss", que é um cahorro cyborgue chamado de "Subwoofer", onde o fluxo de batalha será muito mais focado em desviar os ataques do boss. Após derrotar o boss, o jogador vencerá o jogo e resturará a última corda do seu alaúde.

## Detalhes do mapa
O mapa consistirá de salas de um castelo organizados como uma dungeon, onde o jogador precisará explorá-lo lutando contra diversos inimigos para achar a sala do trono, onde o boss se encontra. O jogador deve encontrar todas as cordas de seu alaúde e tocar uma melodia para desbloquear a porta ao boss, que se encontra no topo do castelo. Ao entrar na sala do trono o jogador lutará contra o Subwoofer.


---
# 4 - Interface de usuário

## Interface

Na tela do jogador, como mostrado abaixo, o medidor de sua vida, o indicador de quantos disparos especiais o jogador tem e o indicador de quantas cordas o seu alaúde tem são mostradas numa barra escura no topo da tela, seguindo o estilo de UIs de jogos antigos. A câmera seguirá o jogador e irá se deslocar levemente na direção do mouse, permitindo que o jogador utilize-o como uma forma de olhar em volta. No mouse, terá uma mira indicando a direção que os projéteis irão a, com um temporizador para que o jogador consiga sincronizar seus inputs ao ritmo da música.

![[ScreenGDD 1.png]]

Abaixo, é um gif mostrando como o ritmo será mostrado ao jogador.

![[GDDtest.gif]]

Abaixo é mostrado, de forma simples, como funcionará o sistema de combos do jogo. O jogador poderá tocar melodias diferentes para empoderar seus disparos usando as teclas direcionais após abrir o menú do alaúde com o botão direito do mouse. Para cada corda que o jogador conseguir para seu alaúde, poderá desbloquear novos combos. O jogador poderá conseguir até 4 cordas para usar em combos, pois a quinta corda sinalizará o final do jogo.

![[GDDnotes.gif]]

Quando um inimigo de elite é instanciado, um padrão rítmico (que chamaremos de compasso) aleatório* é associado a ele. Esse padrão é formado por notas e pausas que correspondem, cada uma, a uma batida da música. O primeiro ataque que o jogador fizer contra o inimigo inicia a detecção do padrão. A cada batida, a instrução apropriada deve ser respeitada pelo jogador (atirar ou esperar). Se o padrão for quebrado, ele é reiniciado. Quando a sequência é completada, o inimigo perde uma vida (representada pelo círculo vermelho acima da barra de compasso). O inimigo é derrotado quando não restar nenhuma vida.

* O padrão é formado por 8 notas/pausas, e sempre começa com uma nota (para que a detecção de padrão não seja iniciada em resposta a um eventual silêncio acidental do jogador.

![[rhythmtest.gif]]

## Input

W, A, S, D - teclas direcionais, serão usadas para movimentar o jogador ou tocar combos de notas no menú do alaúde.

Botão esquerdo do mouse - dispara uma nota musical onde o mouse estiver apontando.

Botão direito do mouse - abre o menú do alaúde, onde o jogador pode tocar um combo de notas.

Barra de espaço / Shift - o jogador dá um dash, permitindo desviar de ataques inimigos.

ESC - fecha o jogo.

---
# 5 - Audio e música

O jogo terá música original feita baseado no design do jogo e do universo dele. Os efeitos sonoros serão do domínio público.

Terão 4 músicas: O tema de introdução do jogo, tema do tutorial, tema de batalha, tema para o boss.

---
# 6 - Arte Conceito e referências


A inspiração para os gráficos do jogo é o jogo Shovel Knight, como a resolução da arte e o UI do jogo.

![[shovel-knight-screen_20-1.png]]

Abaixo, os jogos Crypt of the Necrodancer e Bullets Per Minute são as principais fontes de inspiração para as mecânicas de ritmo do jogo, incluindo ideias como o indicador de ritmo na tela do jogador.

![[maxresdefault.jpg]]
![[ss_39c531e1831491b2140a3bdf36cf70ee342a1e6d.1920x1080.jpg]]


O jogo Enter the Gungeon é outra referência para a dinâmica de ação do gameplay, com o sistema de combate rápido onde a mira do jogador move a câmera.

![[PREVIEW_SCREENSHOT1_109467.webp]]


Por fim, o jogo Everhood foi o pontapé inicial da ideia desse jogo, usando música como um meio de combate.

![[ss_f809bba93b1dc91ff39a091ed78d02102303623a.1920x1080.jpg]]


---
# 7 - Ideias adicionais e observações

Muitas mecânicas no jogo ainda serão ajustadas de acordo com a gameplay, com o intuito de criar uma experiência melhor e mais balanceada. Parâmetros como a vida do jogador, quantos disparos especiais ele recebe, quais tipos de disparos especiais serão disponíveis, o comportamento de inimigos, o layout do mapa, entre outros fatores podem sofrer diversas mudanças até o final do seu desenvolvimento. As artes mostradas neste documento de desenvolvimento não são finais e sofrerão refinamento até que se torne um produto satisfatório.

Entre algumas das ideias que temos para o jogo, estão:
### Algumas ideias para tipos de disparo
- Distante --> Um disparo que vai mais longe do que o normal.
- Explosivo --> "Explode" e dá dano em área ao impacto.
- Múltiplo --> Atira mais de um disparo de uma vez em um cone.


### Ideias para coletáveis
- Item de cura --> Recupera parte da vida.