import src.validaciones_json.constantes_json as const
from src.utils.utils_format import FormatUtils

class GeneradorJsonBaseEvaluacion:

    @staticmethod
    def establecer_estructura_principal_json(correo, cuerpo_principal_json):
        raiz = {}
        raiz.update({'node': correo})
        raiz.update({'body': cuerpo_principal_json})

        return raiz

    @staticmethod
    def establecer_raiz_json():
        raiz = {}
        raiz.update({"start": ""})
        raiz.update({"end": ""})
        raiz.update({"status": ""})
        raiz.update({"time": 0})
        raiz.update({"steps": []})

        return raiz

    @staticmethod
    def generar_nodo_padre(order, name='', status='', output=None, start="", end=""):
        if output is None:
            output = []

        nodo_padre = {}
        nodo_padre.update({"order": order})
        nodo_padre.update({"name": name})
        nodo_padre.update({"status": status})
        nodo_padre.update({"output": output})
        nodo_padre.update({"start": start})
        nodo_padre.update({"end": end})
        nodo_padre.update({"time": 0})

        return nodo_padre

    @staticmethod
    def generar_nodo_hijo(order, name='', status='', output=""):
        nodo_hijo = {}
        nodo_hijo.update({"order": order})
        nodo_hijo.update({"name": name})
        nodo_hijo.update({"status": status})
        nodo_hijo.update({"output": output})

        return nodo_hijo

    @staticmethod
    def generar_nuevo_template_json():
        # genera el nodo raiz
        json_a_enviar = GeneradorJsonBaseEvaluacion.establecer_raiz_json()

        # establece las 3 evaluaciones principales
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(1))
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(2))
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(3))
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(4))
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(5))
        json_a_enviar["steps"].append(GeneradorJsonBaseEvaluacion.generar_nodo_padre(6))

        # establece cada uno los steps de cada evaluacion
        json_a_enviar["steps"][0]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]
        json_a_enviar["steps"][1]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]
        json_a_enviar["steps"][2]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]
        json_a_enviar["steps"][3]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]
        json_a_enviar["steps"][4]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]
        json_a_enviar["steps"][5]["output"] = [GeneradorJsonBaseEvaluacion.generar_nodo_hijo(1)]

        json_a_enviar["steps"][0]["name"] = const.STEP_NAME_INGRESO_PAGINA_PRINCIPAL_CLARO_DRIVE
        json_a_enviar["steps"][1]["name"] = const.STEP_NAME_INICIO_SESION_CLARO_DRIVE
        json_a_enviar["steps"][2]["name"] = const.STEP_NAME_CARGA_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][3]["name"] = const.STEP_NAME_DESCARGA_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][4]["name"] = const.STEP_NAME_BORRADO_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][5]["name"] = const.STEP_NAME_CIERRE_SESION_CLARO_DRIVE

        json_a_enviar["steps"][0]["output"][0]["name"] = const.STEP_OUTPUT_NAME_INGRESO_PAGINA_PRINCIPAL_CLARO_DRIVE
        json_a_enviar["steps"][1]["output"][0]["name"] = const.STEP_OUTPUT_NAME_INICIO_SESION_CLARO_DRIVE
        json_a_enviar["steps"][2]["output"][0]["name"] = const.STEP_OUTPUT_NAME_CARGA_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][3]["output"][0]["name"] = const.STEP_OUTPUT_NAME_DESCARGA_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][4]["output"][0]["name"] = const.STEP_OUTPUT_NAME_BORRADO_IMAGEN_CLARO_DRIVE
        json_a_enviar["steps"][5]["output"][0]["name"] = const.STEP_OUTPUT_NAME_CIERRE_SESION_CLARO_DRIVE

        return json_a_enviar

    @staticmethod
    def generar_json_error_ejecucion_en_script(json, tiempo_inicio, tiempo_fin, fecha_inicio, fecha_fin,
                                               msg_output_falla):
        time = tiempo_fin - tiempo_inicio

        json['start'] = fecha_inicio
        json['end'] = fecha_fin
        json['time'] = FormatUtils.truncar_float_cadena(time)
        json['status'] = const.FAILED

        for i, step in enumerate(json['steps']):
            json['steps'][i]['order'] = i+1
            json['steps'][i]['status'] = const.FAILED
            json['steps'][i]['start'] = fecha_inicio
            json['steps'][i]['end'] = fecha_fin
            json['steps'][i]['time'] = FormatUtils.truncar_float_cadena(time)

            json['steps'][i]['output'][0]['order'] = 1
            json['steps'][i]['output'][0]['status'] = const.FAILED
            json['steps'][i]['output'][0]['output'] = msg_output_falla

        return json




