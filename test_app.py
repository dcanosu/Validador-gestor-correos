from sprint1 import registrar, lista_estudiantes, lista_docentes

def test_registro_estudiante(monkeypatch):
    # Simula la entrada de un correo de estudiante
    monkeypatch.setattr('builtins.input', lambda _: 'juan@estudiante.utv.edu.co')
    lista_estudiantes.clear()
    lista_docentes.clear()
    
    registrar()

    # Verifica que el correo fue agregado correctamente
    assert lista_estudiantes == ['juan@estudiante.utv.edu.co']
    assert lista_docentes == []

def test_registro_docente(monkeypatch):
    # Simula la entrada de un correo de docente
    monkeypatch.setattr('builtins.input', lambda _: 'profesor@utv.edu.co')
    lista_estudiantes.clear()
    lista_docentes.clear()

    registrar()

    # Verifica que el correo fue agregado correctamente
    assert lista_docentes == ['profesor@utv.edu.co']
    assert lista_estudiantes == []

def test_registro_invalido(monkeypatch):
    # Simula un correo con dominio inválido
    monkeypatch.setattr('builtins.input', lambda _: 'otro@gmail.com')
    lista_estudiantes.clear()
    lista_docentes.clear()

    registrar()

    # Verifica que no se agregó a ninguna lista
    assert lista_estudiantes == []
    assert lista_docentes == []
