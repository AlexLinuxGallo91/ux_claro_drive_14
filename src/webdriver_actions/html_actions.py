from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.utils_temporizador import Temporizador
from src.webdriver_actions import webdriver_actions_constantes
import time


class HtmlActions:

    @staticmethod
    def webdriver_wait_element_to_be_clickable(web_driver, time=5, id=None, xpath=None, link_text=None,
                                               partial_link_text=None, name=None, tag_name=None, class_name=None,
                                               css_selector=None):

        msg_exception = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        try:
            selector_por_buscar, elemento_html_por_localizar = HtmlActions.verificar_elemento_y_selector_por_localizar(
                id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

            return WebDriverWait(web_driver, time).until(
                EC.element_to_be_clickable((selector_por_buscar, elemento_html_por_localizar)))

        except TimeoutException as e:
            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_TIMEOUT_EXCEPTION.format(time, msg_exception, e.msg)
            raise e

    @staticmethod
    def webdriver_wait_presence_of_element_located(
            web_driver, time=5, id=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None,
            class_name=None, css_selector=None):

        msg_exception = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        try:

            selector_por_buscar, elemento_html_por_localizar = HtmlActions.verificar_elemento_y_selector_por_localizar(
                id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

            return WebDriverWait(web_driver, time).until(
                EC.presence_of_element_located((selector_por_buscar, elemento_html_por_localizar)))

        except TimeoutException as e:
            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_TIMEOUT_EXCEPTION.format(time, msg_exception, e.msg)
            raise e

    @staticmethod
    def webdriver_wait_invisibility_of_element_located(
            web_driver, time=5, id=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None,
            class_name=None, css_selector=None):

        msg_exception = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        try:
            selector_por_buscar, elemento_html_por_localizar = HtmlActions.verificar_elemento_y_selector_por_localizar(
                id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

            return WebDriverWait(web_driver, time).until(
                EC.invisibility_of_element_located((selector_por_buscar, elemento_html_por_localizar)))

        except TimeoutException as e:
            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_TIMEOUT_EXCEPTION.format(time, msg_exception, e.msg)
            raise e

    @staticmethod
    def verificar_elemento_html_hasta_no_existir_en_el_dom_html(
            web_driver: WebDriver, time=5, id=None, xpath=None, link_text=None, partial_link_text=None, name=None,
            tag_name=None, class_name=None, css_selector=None):

        msg_selector_html_a_localizar = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        tiempo_inicial = Temporizador.obtener_tiempo_timer()

        while True:
            try:
                if id is not None:
                    web_driver.find_element_by_id(id)
                elif xpath is not None:
                    web_driver.find_element_by_xpath(xpath)
                elif link_text is not None:
                    web_driver.find_element_by_link_text(link_text)
                elif partial_link_text is not None:
                    web_driver.find_element_by_partial_link_text(partial_link_text)
                elif name is not None:
                    web_driver.find_element_by_name(name)
                elif tag_name is not None:
                    web_driver.find_element_by_tag_name(tag_name)
                elif class_name is not None:
                    web_driver.find_element_by_class_name(class_name)
                elif css_selector is not None:
                    web_driver.find_element_by_css_selector(css_selector)

                segundos_transcurridos = Temporizador.obtener_tiempo_timer() - tiempo_inicial

                if segundos_transcurridos > time:
                    e = TimeoutException()
                    e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_UNTIL_NOT_TIMEOUT_EXCEPTION.format(
                        time, msg_selector_html_a_localizar, e.msg)

                    raise e
                else:
                    pass

            except NoSuchElementException:
                break

    @staticmethod
    def webdriver_wait_until_not_invisibility_of_element_located(
            web_driver, time=5, id=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None,
            class_name=None, css_selector=None):

        msg_exception = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        try:
            selector_por_buscar, elemento_html_por_localizar = HtmlActions.verificar_elemento_y_selector_por_localizar(
                id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

            return WebDriverWait(web_driver, time).until_not(
                EC.invisibility_of_element_located((selector_por_buscar, elemento_html_por_localizar)))

        except TimeoutException as e:

            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_UNTIL_NOT_TIMEOUT_EXCEPTION.format(
                time, msg_exception, e.msg)

            raise e

    @staticmethod
    def webdriver_wait_until_not_presence_of_element_located(
            web_driver, time=5, id=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None,
            class_name=None, css_selector=None):

        msg_exception = HtmlActions.generar_identificador_excepcion(
            id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

        try:
            selector_por_buscar, elemento_html_por_localizar = HtmlActions.verificar_elemento_y_selector_por_localizar(
                id, xpath, link_text, partial_link_text, name, tag_name, class_name, css_selector)

            return WebDriverWait(web_driver, time).until_not(
                EC.presence_of_element_located((selector_por_buscar, elemento_html_por_localizar)))

        except TimeoutException as e:

            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_UNTIL_NOT_TIMEOUT_EXCEPTION.format(
                time, msg_exception, e.msg)

            raise e

    @staticmethod
    def verificar_elemento_y_selector_por_localizar(
            id=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None, class_name=None,
            css_selector=None):

        if id is not None:
            selector_por_buscar = By.ID
            elemento_html_por_localizar = id
        elif xpath is not None:
            selector_por_buscar = By.XPATH
            elemento_html_por_localizar = xpath
        elif link_text is not None:
            selector_por_buscar = By.LINK_TEXT
            elemento_html_por_localizar = link_text
        elif partial_link_text is not None:
            selector_por_buscar = By.PARTIAL_LINK_TEXT
            elemento_html_por_localizar = partial_link_text
        elif name is not None:
            selector_por_buscar = By.NAME
            elemento_html_por_localizar = name
        elif tag_name is not None:
            selector_por_buscar = By.CLASS_NAME
            elemento_html_por_localizar = tag_name
        elif class_name is not None:
            selector_por_buscar = By.CLASS_NAME
            elemento_html_por_localizar = class_name
        elif css_selector is not None:
            selector_por_buscar = By.CSS_SELECTOR
            elemento_html_por_localizar = css_selector
        else:
            raise NoSuchElementException(msg='Sucedio un error NoSuchElementException. No se establecio el '
                                             'identificador o clase css del elemento HTML por buscar')

        return selector_por_buscar, elemento_html_por_localizar

    @staticmethod
    def enviar_data_keys(elemento_html, data_key: str, id=None, class_name=None, xpath=None, name=None):

        identifier_message = HtmlActions.generar_identificador_excepcion(
            id=id, class_name=class_name, xpath=xpath, name=name)

        try:
            elemento_html.send_keys(data_key)

        except ElementNotInteractableException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_ElEMENT_NOT_INTERACTABLE_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except NoSuchElementException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_NO_SUCH_ELEMENT_EXCEPTION.format(identifier_message, e.msg)
            raise e

        except TimeoutException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_TIME_OUT_EXCEPTION.format(identifier_message, e.msg)
            raise e

        except ElementClickInterceptedException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_ELEMENT_CLICK_INTERCEPTED_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except StaleElementReferenceException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_STALE_ELEMENT_REFERENCE_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except WebDriverException as e:
            e.msg = webdriver_actions_constantes.SEND_KEY_WEBDRIVER_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

    @staticmethod
    def click_html_element(html_element, id=None, class_name=None, xpath=None, name=None):

        identifier_message = HtmlActions.generar_identificador_excepcion(
            id=id, class_name=class_name, xpath=xpath, name=name)

        try:

            html_element.click()

        except ElementNotInteractableException as e:
            e.msg = webdriver_actions_constantes.CLICK_ElEMENT_NOT_INTERACTABLE_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except NoSuchElementException as e:
            e.msg = webdriver_actions_constantes.CLICK_NO_SUCH_ELEMENT_EXCEPTION.format(identifier_message, e.msg)
            raise e

        except TimeoutException as e:
            e.msg = webdriver_actions_constantes.CLICK_TIME_OUT_EXCEPTION.format(identifier_message, e.msg)
            raise e

        except ElementClickInterceptedException as e:
            e.msg = webdriver_actions_constantes.CLICK_ELEMENT_CLICK_INTERCEPTED_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except StaleElementReferenceException as e:
            e.msg = webdriver_actions_constantes.CLICK_STALE_ELEMENT_REFERENCE_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

        except WebDriverException as e:
            e.msg = webdriver_actions_constantes.CLICK_WEBDRIVER_EXCEPTION.format(
                identifier_message, e.msg)
            raise e

    @staticmethod
    def click_en_elemento_html_con_intentos(
            elemento_html, numero_de_intentos: int = 1, id=None, class_name=None, xpath=None, name=None):

        contador_intentos = 0

        while contador_intentos < numero_de_intentos:

            contador_intentos = contador_intentos + 1

            try:
                HtmlActions.click_html_element(elemento_html, id, class_name, xpath, name)
                break

            except ElementNotInteractableException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

            except NoSuchElementException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

            except TimeoutException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

            except ElementClickInterceptedException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

            except StaleElementReferenceException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

            except WebDriverException as e:
                if contador_intentos == numero_de_intentos:
                    raise e
                else:
                    time.sleep(1)

    @staticmethod
    def generar_identificador_excepcion(id=None, xpath=None, link_text=None, partial_link_text=None,
                                        name=None, tag_name=None, class_name=None, css_selector=None):

        identifier_message = ''

        if id is not None:
            identifier_message = 'elemento con el id {}'.format(id)
        elif xpath is not None:
            identifier_message = 'elemento con el xpath {}'.format(xpath)
        elif link_text is not None:
            identifier_message = 'elemento con el link text {}'.format(link_text)
        elif partial_link_text is not None:
            identifier_message = 'elemento con el partial link text {}'.format(partial_link_text)
        elif name is not None:
            identifier_message = 'elemento con el name {}'.format(name)
        elif tag_name is not None:
            identifier_message = 'elemento con el tag name {}'.format(tag_name)
        elif class_name is not None:
            identifier_message = 'elemento con el class name {}'.format(class_name)
        elif css_selector is not None:
            identifier_message = 'elemento con el selector css {}'.format(css_selector)

        return identifier_message

    @staticmethod
    def verificar_display_flex_modal_mensaje_de_exito(web_driver: WebDriver):
        try:
            modal_de_exito = web_driver.find_element_by_id('notification')
            display = modal_de_exito.value_of_css_property('display')

            while display == 'flex':
                modal_de_exito = web_driver.find_element_by_id('notification')
                display = modal_de_exito.value_of_css_property('display')

        except NoSuchElementException:
            pass

    @staticmethod
    def verificar_error_de_credenciales(web_driver: WebDriver):
        css_class_div_error = 'Notifier Error ng-star-inserted'

        try:
            HtmlActions.webdriver_wait_presence_of_element_located(web_driver, 6, class_name=css_class_div_error)
            se_presenta_error_de_credenciales = True
        except TimeoutException:
            se_presenta_error_de_credenciales = False

        return se_presenta_error_de_credenciales






