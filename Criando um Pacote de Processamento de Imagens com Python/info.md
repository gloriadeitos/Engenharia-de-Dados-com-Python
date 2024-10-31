#### Glória Maria Deitos Gomes da Silva <br> 31.Outubro.2024

## Image Processor - Pacote de Processamento de Imagens

Bem-vindo ao **Image Processor**! Este pacote oferece ferramentas básicas para redimensionamento e aplicação de filtros em imagens. Ideal para desenvolvedores que buscam manipulação rápida e eficiente de imagens em Python.

**[Código do Projeto: Criando um Pacote de Processamento de Imagens com Python](https://github.com/gloriadeitos/NTT_DATA-Engenharia_de_Dados_com_Python/blob/main/Criando%20um%20Pacote%20de%20Processamento%20de%20Imagens%20com%20Python/codigo.md)**

## Índice

1. [Instalação](#instalação)
2. [Configuração do GitHub Packages](#configuração-do-github-packages)
3. [Como Usar](#como-usar)
4. [Funcionalidades](#funcionalidades)
5. [Contribuindo](#contribuindo)

---

## Instalação
Para instalar o pacote diretamente do GitHub Packages, use o comando abaixo. Substitua `<seu-usuario>` pelo seu nome de usuário no GitHub e `<seu-PAT>` pelo seu Personal Access Token.

```bash
pip install --index-url https://<seu-usuario>:<seu-PAT>@github.com/<seu-usuario>/image_processor
```
**Nota:** O token de acesso pessoal (PAT) é necessário para acessar pacotes privados. Consulte as instruções de configuração abaixo para gerar e configurar o seu.

## Configuração do GitHub Packages
Para autenticar-se ao GitHub Packages, siga as etapas abaixo:

1. Gere um **Personal Access Token (PAT)** no GitHub com permissões `write:packages` e `repo`. [Clique aqui para criar um token.](https://github.com/settings/tokens)
2. Configure o arquivo `.pypirc` na sua máquina para autenticação, adicionando o seguinte conteúdo (substitua `seu-usuario` e `seu-PAT` pelo seu nome de usuário e token):

```ini
[distutils]
index-servers =
    github

[github]
repository: https://upload.pypi.org/legacy/
username: seu-usuario
password: seu-PAT
```

Com essas configurações, você estará pronto para enviar atualizações do pacote para o GitHub Packages e fazer instalações com autenticação automática.

## Como Usar
Após a instalação, importe o pacote `image_processor` para usar suas funções principais. Aqui está um exemplo básico de uso:

```python
from image_processor import resize_image, apply_filter

# Exemplo de redimensionamento de imagem
resized_image = resize_image('caminho/para/imagem.jpg', (100, 100))

# Exemplo de aplicação de filtro
filtered_image = apply_filter('caminho/para/imagem.jpg', 'sepia')
```

## Funcionalidades
- **Redimensionamento de Imagem**: Ajuste as dimensões de uma imagem facilmente.
- **Aplicação de Filtros**: Aplique filtros populares como preto e branco, sepia, negativo, entre outros.

## Contribuindo
Contribuições são bem-vindas! Para contribuir com o desenvolvimento do pacote:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua modificação (`git checkout -b minha-modificacao`).
3. Envie um Pull Request descrevendo sua alteração.

Para mais detalhes, acesse a página oficial do projeto.
