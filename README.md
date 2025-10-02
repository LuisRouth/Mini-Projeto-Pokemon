# Pokémon Image Scraper

Um script simples em Python que baixa a imagem principal de cada Pokémon do site [PokemonDB](https://pokemondb.net).

## O que este script faz?

- **Navega automaticamente** por todas as páginas de Pokémon do site, começando pelo Bulbasaur.
- **Extrai o nome** e o link da imagem de cada Pokémon.
- **Cria uma pasta** chamada `pokemon_images` no mesmo diretório.
- **Salva cada imagem** com o nome do respectivo Pokémon em formato `.jpg`.

## Pré-requisitos

- Python 3.6 ou mais recente.

## Como Executar

Siga os 3 passos abaixo no seu terminal.

#### Passo 1: Prepare o Ambiente

Recomenda-se usar um ambiente virtual para que as bibliotecas deste projeto não interfiram com outros projetos em seu sistema.

```sh
# Navegue até a pasta onde estão seus arquivos

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

#### Passo 2: Instale as Dependências

Este projeto precisa de algumas bibliotecas externas. O arquivo `requirements.txt` lista todas elas. Para instalar, execute:

```sh
pip install -r requirements.txt
```

#### Passo 3: Rode o Script

Com tudo instalado, execute o script principal no terminal ou execute o arquivo:

```sh
python download_pokemon.py
```

O script começará a exibir no terminal os nomes dos Pokémon à medida que baixa as imagens. Ao final, a pasta `pokemon_images` estará cheia de imagens.

---

### Aviso Importante sobre Web Scraping

Este script depende da estrutura do site `pokemondb.net`. Se o site sofrer alterações no seu código HTML, o scraper pode quebrar e precisará de manutenção para funcionar novamente.

## Bônus: Aplicação Pokémon Team Builder

Este projeto também inclui uma aplicação principal na pasta `TeamBuilder`. Nela, é possível gerar uma equipe inicial única e treiná-la para evoluir. Para executar, siga as instruções de instalação e ambiente virtual, e então rode `python main_app.py` dentro da pasta do projeto.