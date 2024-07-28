import google.generativeai as genai


def get_car_descriptionAI(model, brand, year):

    GOOGLE_API_KEY = 'YOUR_API_KEY'
    genai.configure(api_key=GOOGLE_API_KEY)

    model_ai = genai.GenerativeModel(model_name='gemini-1.5-flash')

    prompt = f"""

                Crie uma descrição de venda para o carro {model} {brand} {year} em apenas 200 caracteres. Fale
                recursos técnicos específicos desse modelo. Se o carro não existir, não crie uma descrição. Apenas entregue: {model} {brand} {year} disponível.

                """
    response = model_ai.generate_content(prompt)

    return response.text
