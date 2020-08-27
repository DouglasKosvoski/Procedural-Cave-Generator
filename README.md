
# Procedural Cave Generator

Gerador Procedural de Cavernas 2D (bidimensional), desenvolvido como projeto pessoal, utilizando o algoritmo [Marching Squares](https://en.wikipedia.org/wiki/Marching_squares) implementado com a linguagem de programação Python 3 e o framework gráfico PyGame, que utiliza uma matriz de duas dimensões em um espaço escalar, para gerar valores numéricos individuais e traçar um contorno entre eles gerando assim um aspecto que se assemelha a cavernas. Calculando primeiramente cada célula do vetor como um indivíduo independente e comparando o aos seus vizinhos na matriz para assim gerar um contorno condizente.


## Para utilizar o programa

### 1. Instalação de dependências

Baixa o repositório com o código-fonte
```
https://github.com/DouglasKosvoski/Procedural_Cave_Generator.git
```

Instala interpretador Python:

```
apt get install python3.8.5
```

Instala Framework gráfico PyGame:

```
 pip install -r requirements.txt
```

Se a instalação tiver ocorrido de forma esperada, o interpretador Python e o framework PyGame estarão instalados corretamentes no seu computador.

### 2. Rodando o programa

Entre no diretório onde o repositorio foi baixado:
```
cd Procedural_Cave_Generator
```

e dentro do repositório rode o arquivo "main.py"
```
python main.py
```
