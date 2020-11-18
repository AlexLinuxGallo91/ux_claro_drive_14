from os import listdir, mkdir, umask
from os.path import isdir, isfile, join
from src.utils.utils_format import FormatUtils
from pathlib import Path
import shutil
import datetime
import random
import string


class UtilsMain:

    @staticmethod
    def verificar_path_es_directorio(path_por_analizar):
        return isdir(path_por_analizar)

    @staticmethod
    def obtener_lista_ficheros_en_directorio(path_directorio):
        return [archivo for archivo in listdir(path_directorio) if isfile(join(path_directorio, archivo))]

    @staticmethod
    def generar_cadena_alafanumerica_aleatoria(longitud_cadena):
        letras_y_numeros = string.ascii_letters + string.digits
        cadena = ''.join((random.choice(letras_y_numeros) for i in range(longitud_cadena)))
        return cadena

    @staticmethod
    def generar_carpeta_descarga_dinamica(path_imagen_prueba_claro_drive):
        path_descarga_hija = '{}_{}_{}'
        archivo_config_ini = FormatUtils.lector_archivo_ini()
        path_descarga_raiz = archivo_config_ini.get('Driver', 'folder_descargas')
        nombre_archivo_sin_extension = Path(path_imagen_prueba_claro_drive).stem
        datetime_fecha_actual = datetime.datetime.today()
        cadena_fecha_hora_actual = '{}_{}_{}_{}_{}_{}'.format(
            datetime_fecha_actual.day, datetime_fecha_actual.month, datetime_fecha_actual.year,
            datetime_fecha_actual.hour, datetime_fecha_actual.minute, datetime_fecha_actual.second)

        path_descarga_hija = path_descarga_hija.format(nombre_archivo_sin_extension, cadena_fecha_hora_actual,
                                                       UtilsMain.generar_cadena_alafanumerica_aleatoria(6))

        path_descarga_hija = join(path_descarga_raiz, path_descarga_hija)

        return path_descarga_hija

    @staticmethod
    def crear_directorio(path_directorio_por_crear):
        try:
            umask(0)
            mkdir(path_directorio_por_crear)
        except OSError as e:
            print('Sucedio un error al intentar crear el directorio {}: {}'.format(path_directorio_por_crear, e))

    @staticmethod
    def eliminar_directorio_con_contenido(path_directorio_por_borrar):
        shutil.rmtree(path=path_directorio_por_borrar, ignore_errors=True)




