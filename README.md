# LogHawk

![LogHawk](assets/LogHawkBanner.jpeg)

LogHawk é um aplicativo de terminal para análise de logs, desenvolvido em Python. O projeto tem como objetivo proporcionar uma interface interativa e eficiente para profissionais de TI e cibersegurança analisarem logs de maneira rápida e organizada.

## Índice

- [Características](#características)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Características

- **Interface Interativa**: Navegue pelas funcionalidades através de um menu interativo no terminal.
- **Análise Avançada**: Filtragem e análise de logs com diversas opções personalizáveis.
- **Exportação de Resultados**: Exporte os logs filtrados em formatos diversos.
- **Customização**: Modularidade que permite adicionar novas funcionalidades com facilidade.

## Instalação

Para instalar e configurar o LogHawk, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/username/loghawk.git
   cd loghawk
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o setup inicial:
   ```bash
   bash scripts/setup_env.sh
   ```

## Uso

Após a instalação, você pode iniciar o LogHawk através do terminal:

```bash
python -m loghawk.main
```

### Comandos Básicos

- `--analyze`: Inicia o processo de análise de logs.
- `--export`: Exporta os resultados para um arquivo específico.
- `--help`: Exibe ajuda sobre os comandos disponíveis.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Para contribuir:

1. Fork o repositório.
2. Crie um branch com a nova funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para o branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.