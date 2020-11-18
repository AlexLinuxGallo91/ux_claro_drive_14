from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


class ValidacionesHtml:

    @staticmethod
    def verificar_ventana_archivo_duplicado(webdriver_test_ux: WebDriver):

        try:
            WebDriverWait(webdriver_test_ux, 20).until(
                EC.presence_of_element_located((By.ID, 'oc-dialog-fileexists-content')))

            check_sustituir_archivos = WebDriverWait(webdriver_test_ux, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//label[@for="checkbox-allnewfiles"][text()="Archivos Nuevos"]')))

            check_sustituir_archivos.click()

            btn_continuar = WebDriverWait(webdriver_test_ux, 20).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="continue"][text()="Continuar"]')))

            btn_continuar.click()

        except ElementNotInteractableException:
            pass
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    @staticmethod
    def minimizar_ventana_estatus_descarga(webdriver_test_ux: WebDriver):

        try:
            btn_minimizar = WebDriverWait(webdriver_test_ux, 6).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'up-minimize')))

            btn_minimizar.click()

        except ElementNotInteractableException:
            pass
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    @staticmethod
    def remover_ventana_notificacion(webdriver_test_ux: WebDriver):

        try:
            btn_cancelar_notificacion = WebDriverWait(webdriver_test_ux, 6).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@class="close-btn"][@alt="Descartar"]')))

            btn_cancelar_notificacion.click()

        except ElementNotInteractableException:
            pass
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass
