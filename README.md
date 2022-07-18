<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Logo <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<p align="center">
  <img align="center" width="40%" src="/imagens/banco-imobiliario.jpg"> 
</p>


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Título <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<h1 align="center"> <h1 align="center">Desafio BrasilPrev <br>
Jogo hipotético semelhante a Banco Imobiliário </h1>

<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Subtítulo <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<!--<p align="center"> Algoritmo Genético implementado para resolver o problema das n-rainhas. </p>-->


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Badges <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<!--<p align="center">    
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/cleidsonsouza/n-rainhas-2018">  
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/cleidsonsouza/n-rainhas-2018">      
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/cleidsonsouza/n-rainhas-2018">  
  <a href="https://github.com/cleidsonsouza/n-rainhas-2018/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/cleidsonsouza/n-rainhas-2018">
  </a>  
  <img alt="GitHub last commit" src="https://img.shields.io/github/issues/cleidsonsouza/n-rainhas-2018">  
  <a href="https://github.com/cleidsonsouza/n-rainhas-2018/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
  </a>  
   <!--<a href="https://github.com/tgmarinho/nlw1/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/tgmarinho/nlw1?style=social">
   </a> -->
</p>


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Descrição do Projeto <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<h2> :memo: Descrição do Projeto </h2>
    <p align="justify"> Este é um projeto que tem como objetivo resolver o desafio descrito a seguir. </p>    
    <h3> O Desafio </h3>    
    <p align="justify"> Considere o seguinte jogo hipotético muito semelhante a Banco Imobiliário, onde várias de suas mecânicas foram simplificadas. 
        Numa partida desse jogo, os jogadores se alteram em rodadas, numa ordem definida
        aleatoriamente no começo da partida. Os jogadores sempre começam uma partida com saldo de 300 para cada um. </p>        
    <p align="justify"> Nesse jogo, o tabuleiro é composto por 20 propriedades em sequência. Cada propriedade tem um custo de venda, um valor de aluguel, um 
        proprietário caso já estejam compradas, e seguem uma determinada ordem no tabuleiro. Não é possível construir hotéis e nenhuma outra melhoria 
        sobre as propriedades do tabuleiro, por simplicidade do problema. </p>       
    <p align="justify"> No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no
        tabuleiro o jogador vai andar. </p>        
        <ul>
           <li> Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a propriedade. 
                 Esse é a única forma pela qual uma propriedade pode ser comprada. </li>
           <li> Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da propriedade. </li>    
           <li> Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo </li>
        </ul>
    <p align="justify"> Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda. Ao comprar uma 
        propriedade, o jogador perde o dinheiro e ganha a posse da propriedade. </p>
    <p align="justify"> Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles vão tomar ao longo do jogo. 
        Mais detalhes sobre o comportamento serão explicados mais à frente. </p>
    <p align="justify"> Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto podem ser compradas por 
        qualquer outro jogador. </p> 
    <p align="justify"> Termina quando restar somente um jogador com saldo positivo, a qualquer momento da partida. Esse jogador é declarado o vencedor. 
    </p> 
    <p align="justify"> Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos 
        de possíveis jogadores. Os comportamentos definidos são </p>    
        <ul>
           <li> O jogador um é impulsivo; </li>
           <li> O jogador dois é exigente; </li>    
           <li> O jogador três é cauteloso; </li>
           <li> O jogador quatro é aleatório; </li>
        </ul>
    <p align="justify"> O jogador impulsivo compra qualquer propriedade sobre a qual ele parar. </p>
    <p align="justify"> O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50. </p>
    <p align="justify"> O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
        depois de realizada a compra. </p>
    <p align="justify"> O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%. </p>
    <p align="justify"> Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada com a vitória do jogador 
        com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
        partida. </p>    
<h4> Saída </h4>    
    <p align="justify"> Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes às execuções. Esperamos 
    encontrar nos dados as seguintes informações: </p>
        <ul>
           <li> Quantas partidas terminam por time out (1000 rodadas); </li>
           <li> Quantos turnos em média demora uma partida; </li>    
           <li> Qual a porcentagem de vitórias por comportamento dos jogadores; </li>
           <li> Qual o comportamento que mais vence. </li>
        </ul>
    
    
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Status <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<!--<h2> :information_source: Staus</h2>
   <p> Projeto concluído :heavy_check_mark:-->

<!-- Importante -->
  <!--<h3> Importante</h3>
      <p> Após a execução e exibição do resultado (tabuleiro com as rainhas nas devidas posições), há um pequeno "bug" que ainda precisa ser corrigido 
      :warning: </p>-->


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Layout <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
  <!-- <h2>Layout</h2> -->
  
  
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Funcionalidades <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --> 
  <!-- <h2>Funcionalidades</h2> --> <!-- <h3>Domontração</h3> --> <!-- Por meio de gifs ou imagens -->  

  
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Como executar o projeto <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->  
<h2> :dvd: Como executar o projeto </h2>

<!-- Pré-requisitos -->  
<!--<h3> Pré-requisitos</h3>
    <ul>
      <li> Módulo <strong> NumPy</strong>. </li>
      <li> Módulo <strong> Matplotlib</strong>. </li>  
      <li> Módulo <strong> Pytest</strong>. </li>  
     </ul> -->

<h3> Docker </h3>

```bash
# Clone este repositório
$ git clone https://github.com/cleidsonsouza/desafio-brasilprev.git

# Acesse a pasta do projeto
$ cd desafio-brasilprev

# Crie a imagem
$ docker build . -t brasilprev

# Execute o projeto
$ docker container run brasilprev
```

<h3> Ambiente Virtual </h3>

```bash
# Clone este repositório
$ git clone https://github.com/cleidsonsouza/desafio-brasilprev.git

# Acesse a pasta do projeto
$ cd desafio-brasilprev

# Atualize o pip
$ pip install --upgrade pip

# Instale as dependências
$ pip install -r requirements.txt

# Execute o projeto
$ python3 app.py
```


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Tecnologias <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->   
<h2> :hammer_and_wrench: Tecnologias</h2>
  <ul>
    <li> Python </li>
    <li> Docker </li>    
  </ul>
  
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Desenvolvimento <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->  
<h2> :computer: Desenvolvimento </h2>

<h3> Decisões de Projeto </h3>
  <ul>
    <li> Arquivo app.py </li>
      <ul>
        <li> A variável custo_max_venda corresponde ao valor máximo que uma propriedade pode custar. Ela foi definida com o valor de 350, pois é um valor 
          próximo ao inicial que cada jogador recebe para iniciar o jogo. Além disso, foram utilizados valores próximos a esse para realizar testes.</li>         <li> A variável percentual_aluguel foi definida com um valor superior ao praticádo na vida real. Enquanto na vida real esse valor que gira em 
          torno de 5% e 6%, foi utilizado o valor de 30% e próximos a esse para realizar testes, por se tratar de um jogo, </li>        
      </ul>
  </ul>


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Resultados <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->  
<h2> :bar_chart: Resultados </h2>

  <p align="justify"> Os resultados apresentados a seguir foram obtidos a partir da definição de 350 e 30% como valores de custo máximo de venda das 
    propriedades e percentual para calcular o aluguel, respectivamente. Caso sejam eses valores sejam alterados, os resultados sefrerão alteração. Um
    exemplo disso, acontece ao se alterar o valor de custo máximo de venda da propriedade (variável "custo_max_venda" - Arquivo app.py), que faz com 
    que haja um aumento significativo no número de partidas que terminam quando se atinge o número máximo de rodadas - 1000.  
  </p>
  
  <p align="center">
    <img align="justify" width="45%" src="/imagens/timeouts-simulacoes.png"> 
    <img align="justify" width="45%" src="/imagens/media-turnos.png">
    <img align="justify" width="45%" src="/imagens/media-vitorias-comportamento.png">
    <img align="justify" width="45%" src="/imagens/turnos-simulacao.png">       
  </p>
  <p align="center">    
    <img align="justify" width="40%" src="/imagens/saida.png">
  </p>


<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Como contribuir <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->  
<!-- <h2>Como contrinuir para o projeto</h2> -->  

<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Contribuidores <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<!-- <h3>Contribuidores</h3> -->
  
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Autor <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->  
<!-- <h2> :boy: Autor</h2> -->
    
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Licença <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->     
<h2> :unlock: Licença</h2>
<p> Este projeto está sob a <a href="https://github.com/cleidsonsouza/n-rainhas-2018/blob/master/LICENSE"> licença MIT</a>. </p>
  
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Versões do Readme <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< -->
<!-- <h2>Versões do Readme</h2> -->
