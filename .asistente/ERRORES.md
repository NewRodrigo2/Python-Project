# Errores conocidos

           ~~~~~~~~~^^^^^^^
  File "C:\Users\Rodrigo\Documents\GitHub\Python-Project\venv\Lib\site-packages\customtkinter\windows\widgets\ctk_button.py", line 564, in _on_release
    self._command()
    ~~~~~~~~~~~~~^^
  File "C:\Users\Rodrigo\Documents\GitHub\Python-Project\prueba\menu_gral.py", line 261, in <lambda>
    command=lambda: self.calcular_precio(self.ent_id.get(), self.ent_1.get()))
                    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: FrameManager.calcular_precio() takes 1 positional argument but 3 were given
