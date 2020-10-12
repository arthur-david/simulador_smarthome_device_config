import yaml
from unidecode import unidecode

def load_devices():
    with open('devices_config.yaml') as f:
        return yaml.load(f, Loader = yaml.FullLoader)

devices = load_devices()

list_devices = devices["devices"]

def string_format(palavras):

    if type(palavras) is list:

        for i in range(len(palavras)):

            palavra = palavras[i].strip()
            palavra = unidecode(u"{}".format(palavra))
            palavra = palavra.lower()
            palavra = palavra.replace(" ", "_")

            palavras[i] = palavra

    else:

        palavras = palavras.strip()
        palavras = unidecode(u"{}".format(palavras))
        palavras = palavras.lower()
        palavras = palavras.replace(" ", "_")

    return palavras


def list_device_names():
    device_names = list()

    for device in list_devices:

        name_formated = string_format(device["device"]["name"])
        
        device_names.append(name_formated)

    print(device_names)

def list_device_sensors():
    device_sensors = dict()

    for device in list_devices:
        name_formated = string_format(device["device"]["name"])
        sensors_formated = string_format(device["device"]["sensors"])


        expression_for_update = {name_formated: sensors_formated}
        device_sensors.update(expression_for_update)

    print(device_sensors)


def list_device_internal_state():
    device_internal_state = dict()

    for device in list_devices:

        internal_state_list = list()
        
        try:
            for internal_state in device["device"]["internal-state"]:
                x = list(internal_state)
                internal_state_list.extend(x)

            name_formated = string_format(device["device"]["name"])
            internal_state_formated = string_format(internal_state_list)

            expression_for_update = {name_formated: internal_state_formated}
            device_internal_state.update(expression_for_update)
        except:
            continue

    print(device_internal_state)


def list_device_actuators():
    device_actuators = dict()

    for device in list_devices:
        actuators_list = list()
        
        try:
            for actuator in device["device"]["actuators"]:
                x = list(actuator)
                actuators_list.extend(x)

            name_formated = string_format(device["device"]["name"])
            actuators_formated = string_format(actuators_list)

            expression_for_update = {name_formated: actuators_formated}
            device_actuators.update(expression_for_update)

        except:
            continue

    print(device_actuators)


def list_environment_devices():
    environment_devices = dict()

    environment_list = list()

    for device in list_devices:

        if device["device"]["environment"] not in environment_list:
            devices_in_environment = list()

            for i in range(len(list_devices)):
                expression_for_if = list_devices[i]["device"]["environment"] == device["device"]["environment"]

                if expression_for_if:
                    devices_in_environment.append(list_devices[i]["device"]["name"])
                
                continue

            environment_list.append(device["device"]["environment"])

            environment_formated = string_format(device["device"]["environment"])
            devices_formated = string_format(devices_in_environment)

            expression_for_update = {environment_formated: devices_formated}
            environment_devices.update(expression_for_update)
        
        continue

    print(environment_devices)

while True:
    print("""


      ______________________________________
    /                                       \\
    | Devices config - Simulador SmartHome   |
    |                                        |
    | Escolha uma das seguintes funcoes      |
    |                                        |
    | 1 - Mostrar nome dos dispositivos.     |
    | 2 - Mostrar lista de sensores dos      |
    |     dispositivos.                      |
    | 3 - Mostrar lista de estados internos  |
    |     dos dispositivos.                  |
    | 4 - Mostrar lista de atuadores dos     |
    |     dispositivos.                      |
    | 5 - Mostrar lista de ambientes e seus  |
    |     dispositivos.                      |
    | 0 - Sair.                              |
     \\______________________________________/

    """)

    choice = input("Escolha: ")
    print("")

    if choice == 1:
        list_device_names()
    
    elif choice == 2:
        list_device_sensors()
    
    elif choice == 3:
        list_device_internal_state()
    
    elif choice == 4:
        list_device_actuators()

    elif choice == 5:
        list_environment_devices()

    elif choice == 0:
        break
    
    else:
        print("Opcao invalida! Tente novamente.")
        continue
