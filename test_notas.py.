from sistema_notas import calcular_media, verificar_status

def test_calcular_media_com_notas():
    assert calcular_media([8.0, 7.0, 9.0]) == 8.0

def test_calcular_media_vazia():
    assert calcular_media([]) == 0.0

def test_aluno_aprovado():
    assert verificar_status(7.5) == "Aprovado"

def test_aluno_reprovado():
    assert verificar_status(6.9) == "Reprovado"
