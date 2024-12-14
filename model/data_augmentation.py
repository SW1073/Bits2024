import os
import google.generativeai as genai

genai.configure(api_key="THIS IS A SECRET BOI")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("""Donades aquestes dades:
"27/11/2024";11;1;1;0;0;0;0;1;0;0;8;1;0;1;"Institut Sant Feliu Sant Feliu FIP1 Classe42"
"28/11/2024";17;0;0;1;0;2;1;0;1;0;13;3;1;0;"Institut Sant Feliu Sant Feliu FIP1 Classe42"
"29/11/2024";13;1;1;0;1;0;0;1;0;1;10;2;0;1;"Institut Sant Feliu Sant Feliu FIP1 Classe42"
"30/11/2024";19;0;0;0;0;1;0;0;1;0;15;5;1;0;"Institut Sant Feliu Sant Feliu FIP1 Classe42"
"01/12/2024";14;2;1;1;0;2;0;1;0;1;11;2;0;1;"Institut Castelló Castelló FIP1 Classe43"
"02/12/2024";18;1;0;0;1;0;1;0;1;0;14;4;1;0;"Institut Castelló Castelló FIP1 Classe43"
"03/12/2024";11;0;1;0;0;1;0;1;0;0;8;1;0;1;"Institut Castelló Castelló FIP1 Classe43"
"04/12/2024";16;2;0;1;1;0;1;0;0;1;12;3;1;0;"Institut Castelló Castelló FIP1 Classe43"
"05/12/2024";12;1;1;0;0;2;0;1;0;0;9;2;0;1;"Institut Castelló Castelló FIP1 Classe43"
"06/12/2024";17;0;0;1;0;1;1;0;1;0;13;4;1;0;"Institut Torroella Torroella FIP1 Classe44"
"07/12/2024";13;2;1;0;1;0;0;1;0;1;10;1;0;1;"Institut Torroella Torroella FIP1 Classe44"
"08/12/2024";19;1;0;1;0;1;0;0;0;0;15;3;1;0;"Institut Torroella Torroella FIP1 Classe44"
"09/12/2024";10;0;1;0;0;2;1;1;0;0;7;2;0;1;"Institut Torroella Torroella FIP1 Classe44"
"10/12/2024";15;1;0;0;1;0;0;0;1;1;11;5;1;0;"Institut Torroella Torroella FIP1 Classe44"

Pots generar noves dades a partir d'aquestes?
En noves línies, afegeix diferents instituts que et semblin interessants. Continua amb Classe45, Classe46, etc.
Els valors de les columnes per la meitat poden ser aleatoris, però intenta que tinguin sentit.
Genera 50 línies. No diguis res més, simplement afegeix les línies amb les dades que generis.

""")

print(response.text)