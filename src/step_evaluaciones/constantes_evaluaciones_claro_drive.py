# argumentos json
JSON_ARG_USER = 'user'
JSON_ARG_PASSWORD = 'password'

# ingreso_pagina_principal_claro_drive

MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_EXITOSO = 'Se ingresa correctamente a la pagina principal de Claro Drive'
MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO = 'fue imposible ingresar principal de Claro Drive: {}'

# inicio_sesion_claro_drive
MSG_OUTPUT_INICIO_SESION_EXITOSO = 'Se ingresa correctamente al portal Claro Drive'
MSG_OUTPUT_INICIO_SESION_SIN_EXITO = 'fue imposible ingresar al portal Claro Drive: {}'
MSG_OUTPUT_INICIO_SESION_MSG_ERROR_INGRESO_PAGINA_PRINCIPAL = 'No fue posible iniciar sesion dentro del portal ' \
    'Claro Drive. No fue posible ingresar a la pagina principal de Claro Drive, favor de verificar la URL y ' \
    'conexion a la red.'

# carga_archivo_claro_drive
MSG_OUTPUT_CARGA_ARCHIVO_EXITOSO = 'Se realiza correctamente la carga del archivo'
MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO = 'No fue posible realizar la carga del archivo: {}'
MSG_OUTPUT_CARGA_ARCHIVO_MSG_ERROR_INICIO_SESION = 'No fue posible realizar la carga del archivo. No se ingreso a ' \
                                                   'la sesion de Claro Drive correctamente'

# descarga_archivo_claro_drive
MSG_OUTPUT_DESCARGA_ARCHIVO_EXITOSO = 'Se realiza la descarga del archivo correctamente'
MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO = 'No fue posible realizar la descarga del archivo correctamente: {}'
MSG_OUTPUT_DESCARGA_ARCHIVO_MSG_ERROR_INICIO_SESION = 'No fue posible realizar la descarga del archivo. No ' \
                                                      'se ingreso a la sesion de Claro Drive correctamente'
MSG_OUTPUT_DESCARGA_ARCHIVO_MSG_ERROR_CARGA_ARCHIVO = 'No fue posible realizar la descarga del archivo. No se ' \
                                                      'cargo correctamente el archivo dentro del portal Claro Drive.'

# borrar_archivo_claro_drive
MSG_OUTPUT_BORRADO_ARCHIVO_EXITOSO = 'Se realiza el borrado del archivo correctamente'
MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO = 'No fue posible realizar el borrado del archivo correctamente: {}'
MSG_OUTPUT_BORRADO_ARCHIVO_MSG_ERROR_INICIO_SESION = 'No fue posible realizar el borrado del archivo. No se ingreso ' \
                                                     'a la sesion de Claro Drive correctamente'
MSG_OUTPUT_BORRADO_ARCHIVO_MSG_ERROR_CARGA_ARCHIVO = 'No fue posible realizar la eliminacion del archivo. No se' \
                                                     ' cargo correctamente el archivo dentro del portal Claro Drive.'

# cerrar_sesion_claro_drive
MSG_OUTPUT_CIERRE_SESION_EXITOSO = 'Se cierra sesion correctamente'
MSG_OUTPUT_CIERRE_SESION_SIN_EXITO = 'No fue posible realizar el cierre de sesion: {}'
MSG_OUTPUT_CIERRE_SESION_MSG_ERROR_INICIO_SESION = 'No fue posible realizar el cierre de sesion. No se ingreso a la ' \
                                                   'sesion de Claro Drive correctamente'

# ELEMENTOS, ID, XPATH y CSS DE ALGUNOS ELEMENTOS HTML
# ingreso_pagina_principal_claro_drive

INGRESO_PAGINA_PRINCIPAL_ID_INPUT_LOGIN = 'login'

# inicio_sesion_claro_drive

INICIO_SESION_ID_INPUT_LOGIN = 'login'
INICIO_SESION_CLASS_NAME_INPUT_EMAIL = 'InputEmail'
INICIO_SESION_CLASS_NAME_INPUT_PASSWORD = 'InputPassword'
INICIO_SESION_XPATH_BTN_INICIAR_SESION = '//button[text()="INICIAR SESI\u00D3N"]'
INICIO_SESION_CLASS_NAME_BTN_CREATE_RESOURCE = 'button-create-resource'

# carga_archivo_claro_drive

CARGA_ARCHIVO_CLASS_NAME_BTN_CREATE_RESOURCE = 'button-create-resource'
CARGA_ARCHIVO_CLASS_NAME_FILE_NAME_READER = 'file-name-header'
CARGA_ARCHIVO_ID_INPUT_FILE_START = 'file_upload_start'
CARGA_ARCHIVO_CLASS_NAME_UP_CLOSE = 'up-close'

# descarga_archivo_claro_drive

DESCARGA_ARCHIVO_ID_SEARCH_BOX = 'searchbox'
DESCARGA_ARCHIVO_CLASS_NAME_RESULT = 'result'
DESCARGA_ARCHIVO_XPATH_ARCHIVO_POR_DESCARGAR = '//span[@class="name-without-extension"][text()="{} "]'
DESCARGA_ARCHIVO_CLASS_NAME_FILENAME = 'filename'
DESCARGA_ARCHIVO_CLASS_NAME_NAME_WITHOUT_EXT = 'name-without-extension'
DESCARGA_ARCHIVO_ATTR_INNER_TEXT = 'innerText'
DESCARGA_ARCHIVO_EXT = 'ext'
DESCARGA_ARCHIVO_CLASS_NAME_ACTION = 'action'

# borrar_archivo_claro_drive

BORRAR_ARCHIVO_XPATH_ARCHIVO_POR_DESCARGAR = '//span[@class="name-without-extension"][text()="{} "]'
BORRAR_ARCHIVO_CLASS_NAME_FILENAME = 'filename'
BORRAR_ARCHIVO_ATTR_INNER_TEXT = 'innerText'
BORRAR_ARCHIVO_CLASS_NAME_NAME_WITHOUT_EXT = 'name-without-extension'
BORRAR_ARCHIVO_EXT = 'ext'
BORRAR_ARCHIVO_CLASS_NAME_ACTION = 'action'

# cerrar_sesion_claro_drive

CERRAR_SESION_XPATH_LI_LOGOUT = '//li[@data-id="logout"]/a'
CERRAR_SESION_ATTR_HREF = 'href'
CERRAR_SESION_ID_LOGIN = 'login'
