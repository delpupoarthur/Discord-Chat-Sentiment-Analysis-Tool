import google.generativeai as genai
from decouple import config

# Configuração da API Gemini
genai.configure(api_key=config('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def analyze_sentiment(text):
    """
    Realiza a análise de sentimento do texto usando a API Gemini.

    Args:
        text (str): O texto a ser analisado.

    Returns:
        dict: Um dicionário contendo a análise de sentimento no formato JSON.
    """

    prompt = (
        f"Por favor, realize uma análise profunda e DETALHADA do sentimento expresso em todo o texto entre chaves: "
        f"Seja cauteloso ao atribuir sentimentos tanto negativos como, quanto positivos. Certifique-se de que há evidências claras no texto para justificar esses sentimentos. Analise TODO o contexto antes de atribuir"
        f"{{ {text} }}, classificando-o dentro das seguintes categorias:\n\n"
        "* **Medo:** Sensação de perigo, ameaça ou apreensão.\n"
        "* **Tristeza:** Sentimento de pesar, melancolia ou infelicidade.\n"
        "* **Alegria:** Emoção de felicidade, contentamento ou prazer.\n"
        "* **Raiva:** Sentimento de irritação, indignação ou fúria.\n"
        "* **Nojo:** Aversão ou repulsa a algo considerado desagradável.\n"
        "* **Ansiedade:** Estado de apreensão, nervosismo ou preocupação.\n"
        "* **Tédio:** Sensação de desinteresse, falta de estímulo ou monotonia.\n"
        "* **Inveja:** Desejo de possuir algo que pertence a outra pessoa.\n"
        "* **Vergonha:** Sentimento de humilhação, constrangimento ou desonra.\n\n"
        "**Intensidade:**\n"
        "* Avalie a intensidade de cada sentimento identificado em uma escala de 0 (ausente) a 100 (extremamente intenso), considerando nuances e sutilezas.\n\n"
        "**Contribuições e Evidências:**\n"
        "* Indique TODAS as palavras, frases e expressões que contribuíram para cada sentimento identificado.\n"
        "* Explique detalhadamente como cada elemento do texto influencia a percepção do sentimento, incluindo o uso de figuras de linguagem, ironia ou sarcasmo.\n"
        "* Se houver ambiguidade ou múltiplas interpretações possíveis, apresente todas elas com suas respectivas justificativas.\n\n"
        "**Razões Possíveis:**\n"
        "* Explore as possíveis razões por trás de cada sentimento identificado, considerando o contexto do texto e o conhecimento de mundo.\n"
        "* Seja específico e detalhado nas suas sugestões, evitando generalizações.\n\n"
        "**Explicação do Modelo:**\n"
        "* Descreva em detalhes o processo de análise utilizado, incluindo os métodos, algoritmos e recursos linguísticos considerados.\n"
        "* Explique como cada aspecto do texto foi avaliado para chegar às conclusões sobre os sentimentos e suas intensidades.\n"
        "* Se houver incertezas ou limitações na análise, seja transparente e as mencione.\n\n"
        "Retorne todas essas informações no seguinte formato de um objeto JSON:\n\n"
        "{\n"
        "  \"sentimentos\": {\n"
        "    \"sentimento\": \"intensidade\"\n"
        "  },\n"
        "  \"contribuicoes\": {\n"
        "    \"palavra/frase\": \"sentimento associado (com explicação detalhada)\"\n"
        "  },\n"
        "  \"razoes_possiveis\": [\"string\"],\n"
        "  \"explicacao_modelo\": \"string\"\n"
        "}"
    )

    response = model.generate_content(prompt)
    return response.text

    response = model.generate_content(prompt)
    return response.text
