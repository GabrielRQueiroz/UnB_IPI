# UnB_IPI
Repositório de Introdução ao Processamento de Imagens

## Sobre

Este repositório contém materiais e projetos para a disciplina de Introdução ao Processamento de Imagens da Universidade de Brasília (UnB).

## Configuração do Ambiente

### Pré-requisitos

- Python 3.9 ou superior (recomendado: 3.9.5)
- pip (gerenciador de pacotes Python)
- Opcional: pyenv ou asdf para gerenciamento de versões Python

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/GabrielRQueiroz/UnB_IPI.git
cd UnB_IPI
```

2. (Opcional) Se você usa pyenv, a versão correta do Python será automaticamente selecionada através do arquivo `.python-version`:
```bash
pyenv install 3.9.5  # se ainda não instalado
```

3. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: venv\Scripts\activate
```

4. Instale as dependências:
```bash
# Para uso básico
pip install -r requirements.txt

# Para desenvolvimento (inclui ferramentas de teste e formatação)
pip install -r requirements-dev.txt

# Ou usando pyproject.toml
pip install -e .
pip install -e ".[dev]"  # com dependências de desenvolvimento
```

## Estrutura do Projeto

```
UnB_IPI/
├── .python-version       # Versão do Python para pyenv/asdf
├── pyproject.toml        # Configuração do projeto e dependências
├── requirements.txt      # Dependências principais
├── requirements-dev.txt  # Dependências de desenvolvimento
├── src/                 # Código fonte do pacote
│   └── unb_ipi/         # Módulo principal
├── tests/               # Testes unitários
├── notebooks/           # Jupyter notebooks
├── examples/            # Scripts de exemplo
├── README.md           # Este arquivo
└── LICENSE             # Licença MIT
```

## Dependências Principais

- **NumPy**: Computação numérica e arrays multidimensionais
- **OpenCV**: Biblioteca de visão computacional
- **Matplotlib**: Visualização de dados e imagens
- **Pillow**: Processamento de imagens
- **SciPy**: Algoritmos científicos e matemáticos

## Ferramentas de Desenvolvimento

- **pytest**: Framework de testes
- **black**: Formatador de código
- **flake8**: Linter Python
- **mypy**: Verificação de tipos estáticos
- **Jupyter**: Notebooks interativos

## Uso

### Executar testes
```bash
pytest
```

### Formatação de código
```bash
black .
```

### Verificação de estilo
```bash
flake8 .
```

## Contribuindo

Este é um repositório educacional. Contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
