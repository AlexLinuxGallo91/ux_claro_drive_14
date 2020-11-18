from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

import src.validaciones_json.constantes_json as contantes_json
from src.utils.utils_format import FormatUtils
from src.utils.utils_main import UtilsMain
from src.utils.utils_temporizador import Temporizador
from src.webdriver_actions.html_actions import HtmlActions
from src.webdriver_config import config_constantes
import time


class UtilsEvaluaciones:

    @staticmethod
    def finalizar_tiempos_en_step(json_eval, indice: int, tiempo_step_inicio, fecha_inicio):

        if tiempo_step_inicio is None:
            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

        tiempo_step_final = Temporizador.obtener_tiempo_timer() - tiempo_step_inicio
        fecha_fin = Temporizador.obtener_fecha_tiempo_actual()
        json_eval["steps"][indice]["time"] = FormatUtils.truncar_float_cadena(tiempo_step_final)
        json_eval["steps"][indice]["start"] = fecha_inicio
        json_eval["steps"][indice]["end"] = fecha_fin

        return json_eval

    @staticmethod
    def establecer_output_status_step(json_eval, indice: int, sub_indice: int, paso_exitoso: bool, mensaje_output: str):

        status_del_step = contantes_json.SUCCESS if paso_exitoso else contantes_json.FAILED

        json_eval["steps"][indice]["output"][sub_indice]["status"] = status_del_step
        json_eval["steps"][indice]["status"] = status_del_step
        json_eval["steps"][indice]["output"][sub_indice]["output"] = mensaje_output

        return json_eval

    @staticmethod
    def generar_json_inicio_de_sesion_incorrecta(json_eval, tiempo_step_inicio, fecha_inicio, indice: int,
                                                 msg_output: str):

        if tiempo_step_inicio is None:
            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

        json_eval["steps"][indice]["output"][0]["status"] = contantes_json.FAILED
        json_eval["steps"][indice]["status"] = contantes_json.FAILED
        json_eval["steps"][indice]["output"][0]["output"] = msg_output

        tiempo_step_final = Temporizador.obtener_tiempo_timer() - tiempo_step_inicio
        fecha_fin = Temporizador.obtener_fecha_tiempo_actual()

        json_eval["steps"][indice]["time"] = FormatUtils.truncar_float_cadena(tiempo_step_final)
        json_eval["steps"][indice]["start"] = fecha_inicio
        json_eval["steps"][indice]["end"] = fecha_fin

        return json_eval

    @staticmethod
    def se_ingreso_correctamente_a_la_sesion(json_eval):
        return True if json_eval["steps"][1]["status"] == contantes_json.SUCCESS else False

    @staticmethod
    def se_ingreso_correctamente_a_la_pagina_principal(json_eval):
        return True if json_eval["steps"][0]["status"] == contantes_json.SUCCESS else False

    @staticmethod
    def se_cargo_correctamente_el_fichero(json_eval):
        return True if json_eval["steps"][2]["status"] == contantes_json.SUCCESS else False

    @staticmethod
    def verificar_descarga_en_ejecucion(nombre_del_archivo, extension_del_archivo):
        tiempo_inicio = Temporizador.obtener_tiempo_timer()
        se_descargo_el_archivo_exitosamente = False
        archivo_a_localizar = '{}{}'.format(nombre_del_archivo, extension_del_archivo)

        while (Temporizador.obtener_tiempo_timer() - tiempo_inicio) < 180:
            lista_archivos = UtilsMain.obtener_lista_ficheros_en_directorio(config_constantes.PATH_CARPETA_DESCARGA)

            if archivo_a_localizar in lista_archivos:
                se_descargo_el_archivo_exitosamente = True
                break

        if not se_descargo_el_archivo_exitosamente:
            raise TimeoutException(msg='Han transcurrido 3 minutos sin finalizar la descarga del archivo {} desde '
                                       'el portal Claro Drive'.format(archivo_a_localizar))

    @staticmethod
    def establecer_vista_de_archivos_como_lista(webdriver: WebDriver):

        boton_vista = webdriver.find_element_by_xpath('//div[@class="icon view-toggle"]')
        tool_tip = boton_vista.find_element_by_class_name('amx-tooltip')
        tool_tip = tool_tip.get_attribute('innerHTML')
        tool_tip = tool_tip.strip()

        if tool_tip == 'Vista lista':
            HtmlActions.webdriver_wait_until_not_presence_of_element_located(
                webdriver, 15, xpath='//div[@class="row type-success"]')
            boton_vista.click()

    @staticmethod
    def esperar_aparicion_modal_de_exito(webdriver: WebDriver, tiempo_de_espera: int = 10):

        tiempo_de_inicio = Temporizador.obtener_tiempo_timer()
        tiempo_transcurrido = 0

        while tiempo_transcurrido < tiempo_de_espera:
            tiempo_transcurrido = Temporizador.obtener_tiempo_timer() - tiempo_de_inicio
            modal_de_exito = webdriver.find_elements_by_xpath('//div[@class="row type-success"]')

            if len(modal_de_exito) == 1:

                modal = modal_de_exito[0]

                if modal.is_displayed() and modal.is_enabled():
                    break

    @staticmethod
    def esperar_desaparicion_modal_exito(webdriver: WebDriver, tiempo_de_espera: int = 10):
        tiempo_de_inicio = Temporizador.obtener_tiempo_timer()
        tiempo_transcurrido = 0

        while tiempo_transcurrido < tiempo_de_espera:
            tiempo_transcurrido = Temporizador.obtener_tiempo_timer() - tiempo_de_inicio
            modal_de_exito = webdriver.find_elements_by_xpath('//div[@class="row type-success"]')

            if len(modal_de_exito) == 0:
                break

    @staticmethod
    def esperar_carga_total_de_archivo(webdriver: WebDriver, tiempo_de_espera: int = 720):
        tiempo_de_inicio = Temporizador.obtener_tiempo_timer()
        tiempo_transcurrido = 0
        se_cargo_correctamente_el_fichero = False
        mensaje_exception = 'Han transcurrido mas de 12 minutos, sin cargar correctamente el archivo dentro del ' \
                            'portal de Claro Drive'

        while tiempo_transcurrido < tiempo_de_espera:
            tiempo_transcurrido = Temporizador.obtener_tiempo_timer() - tiempo_de_inicio
            modal_de_exito = webdriver.find_elements_by_xpath('//div[@class="up-file-actions isDone"]')

            if len(modal_de_exito) == 1:
                se_cargo_correctamente_el_fichero = True
                break

            header = webdriver.find_elements_by_class_name('up-header')

            if len(header) > 0:
                mensaje_de_carga = header[0]
                mensaje_de_carga = mensaje_de_carga.find_elements_by_tag_name('span')

                if len(mensaje_de_carga) > 0:
                    mensaje_de_carga = mensaje_de_carga[0]

                    if 'Se ha cancelado la carga' in mensaje_de_carga.text:
                        se_cargo_correctamente_el_fichero = False
                        mensaje_exception = 'Ha sucedido un error durante la carga del archivo, se presenta el ' \
                                            'siguiente mensaje: {}'.format(mensaje_de_carga.text)
                        break

        if se_cargo_correctamente_el_fichero:
            UtilsEvaluaciones.esperar_desaparicion_modal_exito(webdriver)
        else:
            raise TimeoutException(msg=mensaje_exception)


