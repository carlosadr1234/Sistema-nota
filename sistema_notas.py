def calcular_media(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def verificar_status(media):
    if media >= 7.0:
        return "Aprovado"
    return "Reprovado"
