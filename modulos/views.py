from odorwatch.models import Cliente, UnidadFiscalizable

# Enviar datos a Cliente 
def add_cliente(nombre_cliente):
    """Añade un nuevo cliente a la base de datos."""
    # Importación diferida
    from .main import log_activity

    log_activity("1- Añadiendo Cliente a BD")
    try:
        if not nombre_cliente:
            return "El nombre del cliente es requerido."

        # Crea o obtiene el cliente en la base de datos
        cliente, created = Cliente.objects.get_or_create(nombre=nombre_cliente)

        if created:
            log_activity("2- El usuario ha sido recibido")
            return f"Cliente '{nombre_cliente}' añadido a la base de datos."
        else:
            return f"Cliente '{nombre_cliente}' ya existe en la base de datos."

    except Exception as e:
        return f"Error al añadir el cliente: {str(e)}"

# Enviar datos a Unidad Fiscalizable
def add_unidad(nombre_unidad, ubicacion_unidad, url_unidad, nombre_cliente):
    """Añade una nueva unidad fiscalizable a la base de datos."""
    # Importación diferida
    from .main import log_activity

    log_activity("1- Añadiendo Unidad Fiscalizable a BD")
    try:
        if not nombre_unidad or not nombre_cliente or not ubicacion_unidad or not url_unidad:
            return "Los datos son requeridos."

        # Obtiene el cliente de la base de datos
        cliente = Cliente.objects.get(nombre=nombre_cliente)

        # Crea o obtiene la unidad fiscalizable en la base de datos
        ufiscal, created = UnidadFiscalizable.objects.get_or_create(
            nombre=nombre_unidad,
            ubicacion=ubicacion_unidad,
            url=url_unidad,
            cliente=cliente
        )

        if created:
            log_activity("2- La unidad fiscalizable ha sido añadida")
            return f"Unidad Fiscalizable '{nombre_unidad}' añadida a la base de datos."
        else:
            return f"Unidad Fiscalizable '{nombre_unidad}' ya existe en la base de datos."

    except Cliente.DoesNotExist:
        return f"Error: Cliente '{nombre_cliente}' no encontrado."
    except Exception as e:
        return f"Error al añadir la unidad fiscalizable: {str(e)}"
