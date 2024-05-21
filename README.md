# Discord-Chat-Sentiment-Analysis-Tool

Este bot do Discord utiliza a API Gemini da Google para realizar análises de sentimento detalhadas em mensagens de texto em canais do Discord. Com ele, você pode entender melhor as emoções e reações dos membros do seu servidor, identificar tendências e obter avaliações do humor dos membros desse servidor.

# Funcionalidades
## Coleta de Mensagens:
Coleta mensagens de canais específicos do Discord em um período de tempo definido.
Análise de Sentimento: Analisa o sentimento das mensagens, classificando-as em nove categorias principais:
- Medo
- Tristeza
- Alegria
- Raiva
- Nojo
- Ansiedade
- Tédio
- Inveja
- Vergonha
## Intensidade: 
Avalia a intensidade de cada sentimento em uma escala de 0 a 100.
#Contribuições: 
Identifica as palavras e frases que mais contribuíram para cada sentimento.
## Razões Possíveis: 
Sugere possíveis razões por trás dos sentimentos expressos.
## Explicação: 
Fornece uma explicação detalhada do processo de análise, incluindo os métodos e recursos linguísticos utilizados.
## Relatório Detalhado: 
Gera um relatório completo em formato JSON com todos os resultados da análise.
## Fácil Utilização: 
Interaja com o bot através de comandos simples no Discord.

# Como Usar 
1. Clone o Repositório:
```
git clone https://github.com/seu-usuario/Discord-Sentiment-Analyzer-Bot.git
```

2. Instale as Dependências:
```
pip install -r requirements.txt
```
3. Configure o Bot:
- Crie um arquivo .env na raiz do projeto e adicione seu token do Discord e a chave da API Gemini:
```
DISCORD_TOKEN=seu_token_do_discord
GEMINI_API_KEY=sua_chave_da_api_gemini
```
4. Execute o Bot:
```
python bot.py
```
5. Comandos:
- _scan <canal> days <numero_de_dias>: Coleta mensagens do canal especificado nos últimos X dias e gera um arquivo CSV.
- _analyse <canal> days <numero_de_dias>: Realiza a análise de sentimento das mensagens do canal especificado nos últimos X dias e envia o resultado por DM.
- _help: Exibe informações sobre os comandos disponíveis.

# Exemplo de Resultado
```
JSON
{
  "sentimentos": {
    "Alegria": 20,
    "Medo": 10,
    "Raiva": 10,
    "Ansiedade": 20,
    "Tédio": 10,
    "Nojo": 10
  },
  "contribuicoes": {
    "vamos revisar as entregas?": "Ansiedade (indicação de uma carga de trabalho iminente)",
    "quero comer açai hoje!": "Alegria (antecipação de um prazer)",
    "Manda o jira pra eu olhar!": "Raiva (impaciência ou frustração)",
    // ... (outras contribuições)
  },
  "razoes_possiveis": [
    "Carga de trabalho pesada ou prazos apertados (ansiedade)",
    "Comunicação deficiente ou falta de clareza (raiva)",
    // ... (outras razões)
  ],
  "explicacao_modelo": "A análise foi conduzida usando um algoritmo de processamento de linguagem natural (PNL) que identifica palavras-chave e expressões associadas a diferentes categorias de sentimentos. A intensidade dos sentimentos foi determinada com base na frequência e importância dessas palavras-chave. O contexto do texto, incluindo informações implícitas e figuras de linguagem, também foi levado em consideração. No entanto, é importante notar que a análise de sentimentos é uma tarefa complexa e pode haver nuances ou interpretações alternativas que não foram capturadas por este modelo."
}
```
# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias, adicionar recursos ou corrigir bugs.
