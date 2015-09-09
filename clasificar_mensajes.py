#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esto es algo muy feo que me veo obligado a hacer para que no haya errores al tratar de imprimir en la
# pantalla el símbolo del Euro, en su lugar aparecerá <euro>...
from __future__ import print_function
def print(*args, **kwargs):
    text = args[0]
    text = text.replace(u'€', '<euro>')
    __builtins__.print(text)


import os
import sys
import json
from io import open


def clasificar_mensaje(texto):
    # Tarea 1) Identificar si es un mensaje de venta de billetes
    is_venta = False
    # TODO: Identificar si es un mensaje de venta de billetes


    # Tarea 2) (Para nota): Identificar origen, destino y precio (sólo cuando sea venta)
    origin = None
    destiny = None
    price = None
    if is_venta:
        # TODO: Identificar origen, destino y precio (sólo cuando sea venta)
        pass

    # La función devuelve todos los valores calculados
    return is_venta, origin, destiny, price


# Esta función imprime los resultados de manera "bonita"
def print_results(message, is_venta, origin, destiny, price):
    print(u"\n\t\tDATO\t\tETIQUETA\tCALCULADO\tOK?")
    print(u"  \t\t====\t\t========\t=========\t===")
    data_is_venta = message.get("is_venta", None)
    data_origin = message.get("origen", None)
    data_destiny = message.get("destino", None)
    data_price = message.get("precio", None)

    def print_line(dato, etiqueta, calculado):
        if etiqueta:
            print(u"\t\t%-8s\t%-8s\t%-8s\t%s" % (dato, etiqueta, calculado, 'ok' if etiqueta==calculado else 'no'))
        else:
            print(u"\t\t%-8s\t%-8s\t%-8s\t%s" % (dato, '--', calculado or '--', 'ok'))
        return etiqueta==calculado

    ok = print_line('is_venta', data_is_venta, is_venta)
    print_line('ciudad de origen', data_origin, origin)
    print_line('ciudad de destino', data_destiny, destiny)
    print_line('precio del billete', data_price, price)
    print(u"\n")
    return ok


# El ordenador empieza a ejecutar el programa por aquí
if __name__ == '__main__':
    print(u"\n")
    print(u"============================")
    print(u"= CLASIFICADOR DE MENSAJES =")
    print(u"============================")

    # Compruebo que se le ha pasado un argumento al programa
    if len(sys.argv) != 2:
        print(u"Usage: 'python %s filename.txt'" % sys.argv[0])
        sys.exit()

    # Compruebo que el archivo cuyo nombre se ha pasado como argumento es accesible
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(u"File '%s' not accesible" % filename)
        sys.exit()

    # Voy a leer los mensajes del archivo de texto y almacenarlos en la variable "messages"
    print(u"\nProcessing file: '%s'" % filename)
    try:
        data = json.load(open(filename, encoding='utf-8'))
    except ValueError as e:
        print(u"\n[ERROR!] loading %r" % filename)
        print(u'\tLos archivos JSON tienen un formato muy muy rígido (por eso son tan buenos para que un ordenador los lea). Existen validadores online donde puedes copiar el contenido del archivo y te ayudarán a corregirlo, i.e.: http://jsonformatter.curiousconcept.com/')
        sys.exit()
    messages = data["messages"]
    total = len(messages)
    print(u"\t- %d messages found" % total)

    # Y ahora voy a trabajar en cada mensaje por separado, de uno en uno
    print(u"\nWorking on messages:")
    i = 1
    for message in messages:
        text = message["texto"]
        origin = message.get("origen", None)
        destiny = message.get("destino", None)
        price = message.get("precio", None)
        print(u'\t- Message %d/%d: "%s"' % (i, total, text.replace(u'€', '<euro>')))
        is_venta, origin, destiny, price = clasificar_mensaje(text)

        print_results(message, is_venta, origin, destiny, price)
        i += 1

