# PARA UTILIZAR O GEMINI PAR GERAR DESCRIÇÕES VAZIAS

import google.generativeai as genai

def get_car_descriptionAI(model, brand, year):

    GOOGLE_API_KEY= 'YOUR_API_KEY'
    genai.configure(api_key=GOOGLE_API_KEY)

    generation = {
        'candidate_count' : 1,
        'temperature' : 1,
    }
    security = {
        'HARASSMENT' : 'BLOCK_NONE',
        'HATE' : 'BLOCK_NONE',
        'SEXUAL' : 'BLOCK_NONE',
        'DANGEROUS' : 'BLOCK_NONE',
    }

    model_ai = genai.GenerativeModel(model_name= 'gemini-1.5-flash',
                                    generation_config = generation,
                                    safety_settings= security)

    prompt  =  f"""

                Crie uma descrição de venda para o carro {model} {brand} {year} em apenas 200 caracteres. Fale
                recursos técnicos específicos desse modelo. Se o carro não existir, não crie uma descrição. Apenas entregue: {model} {brand} {year} disponível.

                """
    response = model_ai.generate_content(prompt)

    return response.text
