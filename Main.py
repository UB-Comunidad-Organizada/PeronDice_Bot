import os
import telebot # Para manejar la api de Telegram
import time # Para usar retrasos en las respuestas
import threading

#Solicitar TOKEN
TOKEN = os.getenv("TOKEN")

# Instanciamos el Bot de Telegram
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# definiciones

veinte_verdades = '''
# 1- La verdadera democracia es aquella donde el gobierno hace lo que el pueblo quiere y defiende un solo interés: el del pueblo.
# 2- El peronismo es esencialmente popular. Todo círculo político es antipopular y, por lo tanto, no peronista.
# 3- El peronista trabaja para el Movimiento. El que, en su nombre, sirve a un círculo o a un caudillo, lo es solo de nombre.
# 4- No existe para el peronismo más que una sola clase de personas: los que trabajan.
# 5- En la nueva Argentina de Perón, el trabajo es un derecho que crea la dignidad del Hombre y es un deber, porque es justo que cada uno produzca por lo menos lo que consume.
# 6- Para un peronista no puede haber nada mejor que otro peronista
# 7- Ningún peronista debe sentirse más de lo que es ni menos de lo que debe ser. Cuando un peronista comienza a sentirse más de lo que es, empieza a convertirse en oligarca.
# 8- En la acción política, la escala de valores de todo peronista es la siguiente: primero la patria, después el Movimiento y luego los hombres.
# 9- La política no es para nosotros un fin, sino solo el medio para el bien de la Patria, que es la felicidad de sus hijos y la grandeza nacional.
# 10- Los dos brazos del peronismo son la justicia social y la ayuda social. Con ellos, damos al pueblo un abrazo de justicia y amor.
# 11- El peronismo anhela la unidad nacional y no la lucha. Desea héroes, pero no mártires.
# 12- En la nueva Argentina, los únicos privilegiados son los niños.
# 13- Un gobierno sin doctrina es un cuerpo sin alma. Por eso, el peronismo tiene una doctrina política, económica y social: el justicialismo.
# 14- El justicialismo es una nueva filosofía de la vida, simple, práctica, popular, profundamente cristiana y profundamente humanista.
# 15- Como doctrina política, el justicialismo realiza el equilibrio del derecho del individuo con el de la comunidad.
# 16- Como doctrina económica, el justicialismo realiza la economía social, poniendo el capital al servicio de la economía y ésta al servicio del bienestar social.
# 17- Como doctrina social, el justicialismo realiza la justicia social, que da a cada persona su derecho en función social.
# 18- Queremos una Argentina socialmente justa, económicamente libre y políticamente soberana.
# 19- Constituimos un gobierno centralizado, un Estado organizado y un pueblo libre.
# 20- En esta tierra, lo mejor que tenemos es el pueblo.'''

# Responder al comando /Star
@bot.message_handler(commands =["start", "Start", "ayuda", "Ayuda", "help", "Help"])
def cmd_Start(message):
    """ Da la bienvenida al usuario del Bot """
    bot.reply_to(message, "Hola compañero! ¿En que te puedo servir?")
#    print(message.chat.id) # para imprimir el id del chat

# Responder a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text", "photo"])
def bot_menssajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        if (message.text.__contains__("20 verdades") or message.text.__contains__("veinte verdades")):
            bot.send_message(message.chat.id, veinte_verdades, parse_mode="html", disable_notification=True)
        else:
            x = bot.send_message(message.chat.id, "<b>HOLA</b>", parse_mode="html", disable_notification=True)
            time.sleep(2)
            bot.edit_message_text("<u>¡Lean a Perón!</u>", message.chat.id, x.message_id, parse_mode="html")
            time.sleep(1)
            bot.edit_message_text("<u>Mañana</u>", message.chat.id, x.message_id, parse_mode="html")
            time.sleep(1)
            bot.edit_message_text("<u>Tarde</u>", message.chat.id, x.message_id, parse_mode="html")
            time.sleep(1)
            bot.edit_message_text("<u>Noche</u>", message.chat.id, x.message_id, parse_mode="html")
            time.sleep(1)
            bot.edit_message_text("<u>Y siempre participen de una Unidad Básica</u>", message.chat.id, x.message_id, parse_mode="html")
            time.sleep(2)
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
    bot.send_message(MI_CHAT_ID, "¡Ya estamos en linea!")