# Gerar todos os graficos, dados e tabelas do excel baseados nos dados da db.
from .lib.est import Est

est = Est()
est.set_database("test.json", "json")
