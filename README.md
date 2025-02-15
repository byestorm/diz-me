# 📖 Diz-Me

O **Diz-Me** é uma ferramenta de CLI que permite procurar definições de palavras na Infopédia diretamente através do terminal.

---

## 🛠 Tech Stack

- **Botasaurus** → Para realizar calls ao site da Infopédia
- **LXML** → Para fazer parsing do HTML e extrair os dados
- **Argparse** → Para receber os argumentos no terminal

---

## 🛠 Uso

### 📌 Exibir ajuda

```python diz-me.py ajuda```

Output:

```========================================================================================================================
Dicionário CLI Diz-Me
========================================================================================================================
python diz-me.py ajuda -> devolve esta lista de comandos
python diz-me.py porfavor <palavra1> <palavra2> ... -> devolve os conjuntos de dados associados às palavras na Infopédia
========================================================================================================================```

### 🔍 Procurar a definição de palavras

```python diz-me.py porfavor gato peixe```

Output:

```========================================================================================================================
Palavra: gato
Tipo: nome masculino
Definições:
- 1.  pequeno mamífero carnívoro, domesticado, da família dos Felídeos, digitígrado e de garras retráteis, de que existem diversas raças, apresenta geralmente corpo esguio, com cerca de 50 centímetros de comprimento, patas curtas, cauda longa e pelagem macia, sendo tradicionalmente utilizado para caçar ou afugentar ratos
- 2.  designação comum, extensiva a diferentes espécies de outros pequenos mamíferos carnívoros da família dos Felídeos
(...)
========================================================================================================================


========================================================================================================================
Palavra: peixe
Tipo: nome masculino
Definições:
- 1.  designação comum aos animais vertebrados, aquáticos, com respiração branquial, esqueleto ósseo ou cartilaginoso, geralmente com o corpo coberto de escamas e membros em forma de barbatanas
- 2.  pessoa que goza de certos privilégios por ser protegida por outra, mais influente
========================================================================================================================```



