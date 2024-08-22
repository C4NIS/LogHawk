# LogHawk

LogHawk é uma poderosa ferramenta de análise de logs em terminal, desenvolvida em Python, que facilita a importação, filtragem, visualização e exportação de logs. Ideal para profissionais de TI e segurança, o LogHawk oferece uma interface intuitiva e modular, suportando diversos formatos de logs e permitindo fácil customização e extensão.

## Funcionalidades

- **Importação de Logs:** Suporte para diferentes formatos de logs, incluindo JSON, CSV, syslog, e mais.
- **Filtragem e Busca Avançada:** Pesquisa por palavras-chave, datas, níveis de severidade, e expressões regulares.
- **Visualização Organizada:** Exibição clara e formatada dos logs diretamente no terminal.
- **Exportação de Resultados:** Exportação dos logs filtrados para formatos como CSV ou JSON.
- **Modularidade:** Estrutura modular que permite a fácil adição de novas funcionalidades.

## Instalação

Para começar a usar o LogHawk, siga as instruções abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado em seu sistema. Para verificar a versão do Python, execute:

```bash
python3 --version
```

### Clone o Repositório

Clone o repositório LogHawk para seu ambiente local:

```bash
git clone https://github.com/seu-usuario/loghawk.git
cd loghawk
```

### Instale as Dependências

Instale as dependências necessárias utilizando `pip`:

```bash
pip install -r requirements.txt
```

### Executando o LogHawk

Para iniciar o LogHawk, execute o seguinte comando:

```bash
python3 loghawk.py
```

## Uso

Aqui estão alguns exemplos básicos de uso:

### Importação de Logs

```bash
loghawk import --file /caminho/para/o/log.json
```

### Filtragem de Logs

```bash
loghawk filter --keyword "ERROR"
```

### Visualização de Logs

```bash
loghawk view --tail 100
```

### Exportação de Logs

```bash
loghawk export --format csv --output /caminho/para/salvar.csv
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

### Para Desenvolvedores

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona minha feature'`).
4. Faça o push para a branch (`git push origin minha-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato:

- **LinkedIn:** https://www.linkedin.com/in/933d13b9/
- **GitHub:** [C4NIS](https://github.com/C4NIS)
