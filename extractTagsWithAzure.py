# Llamado a la aplicación de analisis de imágenes para extraer las etiquetas

# RETORNO de las etiquetas de la segmentación a partir de una confianza dada
def tagImage(image_url):
    from azure.cognitiveservices.vision.computervision import ComputerVisionClient
    from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
    from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
    from msrest.authentication import CognitiveServicesCredentials

    results = []

    subscription_key = ""
    endpoint = ""

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    tags_result_remote = computervision_client.tag_image(image_url)
    if (len(tags_result_remote.tags) == 0):
        results.append("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            if tag.confidence > 0.85:
                results.append(tag.name)
    return results