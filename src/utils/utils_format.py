import configparser
import os
import json


class FormatUtils:

    @staticmethod
    def cadena_a_json_valido(cadena=''):
        try:
            json.loads(cadena)
            return True
        except ValueError as e:
            print('El texto "{}" no es un objeto JSON valido: {}, se omite experiencia de usuario Claro Drive'.format(
                cadena, e))
            return False

    @staticmethod
    def truncar_float_cadena(cifra_decimal):
        num = cifra_decimal

        if isinstance(cifra_decimal, str):
            try:
                num = float(cifra_decimal)
            except ValueError:
                num = 0

        num = round(num, 12)
        num = '{:.12f}'.format(num)
        return num

    @staticmethod
    def lector_archivo_ini():
        config = None

        try:
            config = configparser.ConfigParser()
            dir_module = os.path.dirname(__file__)
            dir_module = os.path.join(dir_module, '..', '..', 'config.ini')
            config.read(dir_module)
        except configparser.Error as e:
            print('sucedio un error al leer el archivo de configuracion: {}'.format(e))

        return config

    @staticmethod
    def verificar_keys_json(argumentos_json):
        list_keys = ['user', 'password', 'pathImage']

        for key in list_keys:
            if key not in argumentos_json:
                print('Favor de verificar el parametro json, la llave {} no esta presente dentro del json'.format(key))
                return False

        return True
