import config, logging, os, json, importlib, telebot, random, time, threading, telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

#Solicitar TOKEN comentar según corresponda.
#TOKEN = os.getenv("TOKEN")
TOKEN = config.TOKEN
MI_CHAT_ID = config.MI_CHAT_ID

# Instanciamos el Bot de Telegram
bot = telebot.TeleBot(TOKEN)

""" Esto pasará a estar en una base de datos independiente y autónoma que el programa consultará """

# Definiciones 

respuestas = {
    "verdad": [
        "La verdadera democracia es aquella donde el gobierno hace lo que el pueblo quiere y defiende un solo interés: el del pueblo.",
        "El peronismo es esencialmente popular. Todo círculo político es antipopular y, por lo tanto, no peronista.",
        "El peronista trabaja para el Movimiento. El que, en su nombre, sirve a un círculo o a un caudillo, lo es solo de nombre.",
        "No existe para el peronismo más que una sola clase de personas: los que trabajan.",
        "En la nueva Argentina de Perón, el trabajo es un derecho que crea la dignidad del Hombre y es un deber, porque es justo que cada uno produzca por lo menos lo que consume.",
        "Para un peronista no puede haber nada mejor que otro peronista.",
        "Ningún peronista debe sentirse más de lo que es ni menos de lo que debe ser. Cuando un peronista comienza a sentirse más de lo que es, empieza a convertirse en oligarca.",
        "En la acción política, la escala de valores de todo peronista es la siguiente: primero la patria, después el Movimiento y luego los hombres.",
        "La política no es para nosotros un fin, sino solo el medio para el bien de la Patria, que es la felicidad de sus hijos y la grandeza nacional.",
        "Los dos brazos del peronismo son la justicia social y la ayuda social. Con ellos, damos al pueblo un abrazo de justicia y amor.",
        "El peronismo anhela la unidad nacional y no la lucha. Desea héroes, pero no mártires.",
        "En la nueva Argentina, los únicos privilegiados son los niños.",
        "Un gobierno sin doctrina es un cuerpo sin alma. Por eso, el peronismo tiene una doctrina política, económica y social: el justicialismo.",
        "El justicialismo es una nueva filosofía de la vida, simple, práctica, popular, profundamente cristiana y profundamente humanista.",
        "Como doctrina política, el justicialismo realiza el equilibrio del derecho del individuo con el de la comunidad.",
        "Como doctrina económica, el justicialismo realiza la economía social, poniendo el capital al servicio de la economía y ésta al servicio del bienestar social.",
        "Como doctrina social, el justicialismo realiza la justicia social, que da a cada persona su derecho en función social.",
        "Queremos una Argentina socialmente justa, económicamente libre y políticamente soberana.",
        "Constituimos un gobierno centralizado, un Estado organizado y un pueblo libre.",
        "En esta tierra, lo mejor que tenemos es el pueblo."
    ],
    "saludo": [
        "¡Hola! ¿Cómo estás?",
        "¡Buen día!",
        "¡Qué tal todo!",
        "¡Hola! Me alegra verte de nuevo.",
        "¡Hola! ¿En qué puedo ayudarte?"
    ],
    "despedida": [
        "¡Hasta pronto!",
        "¡Adiós! Que tengas un buen día.",
        "¡Chau! Cuídate mucho.",
        "¡Hasta la próxima!",
        "¡Nos vemos!"
    ]
}

# Responder al comando /start
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    """ Da la bienvenida al usuario del Bot """
    bot.reply_to(message, "¡Hola! ¿En qué te puedo servir?")

# Responder a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text", "photo"])
def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        respuesta = None
        for etiqueta, respuestas_etiqueta in respuestas.items():
            if etiqueta in message.text.lower():
                respuesta = random.choice(respuestas_etiqueta)
                break

        if respuesta:
            bot.send_message(message.chat.id, respuesta)
        else:
            x = bot.send_message(message.chat.id, "<b>No entendí lo que dijiste. ¿Podrías reformularlo?</b>", parse_mode="html")
            time.sleep(2)
            bot.edit_message_text(text="<u>Y siempre es mejor participar de cualquier Unidad Básica para hablar con los compañeros</u>", chat_id=message.chat.id, message_id=x.message_id, parse_mode="html")
            time.sleep(3)
            bot.edit_message_text('<a href="https://t.me/UB_Comunidad_Organiza">UB Comunidad Organizada</a>', message.chat.id, x.message_id, parse_mode="html")
            time.sleep(5)
            bot.delete_message(message.chat.id, x.message_id)
            bot.delete_message(message.chat.id, message.message_id)

def recibir_mensajes():
    """Bucle infinito que comprueba si hay nuevos mensajes en el bot"""
    bot.infinity_polling()


# MAIN #########################################################
if __name__ == '__main__':
    # configuramos los comandos disponibles del bot
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da la bienvenida"),
        telebot.types.BotCommand("/ayuda", "Da lo mismo que start"),
        ])
    print('iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot ya iniciado')
    bot.send_message(chat_id=MI_CHAT_ID, text='Ya estamos en linea!')

updater = Updater(TOKEN)
updater.start_polling()

# Detener el bot con Updater.stop()
updater.stop()


# Updater.idle() # Permite finalizar el bot con Ctrl + C

""" # Viejo lanzador.

# Ejecutar el bot
bot.polling()

"""