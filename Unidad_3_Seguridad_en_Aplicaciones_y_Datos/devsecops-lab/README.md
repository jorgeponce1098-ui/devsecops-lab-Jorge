# Lab DevSecOps — Semana 9
## Arquitectura de Sistemas de Seguridad | CUGDL — UDG

### Instrucciones
1. Hacer **fork** de este repositorio
2. Navegar a `Unidad_3_Seguridad_en_Aplicaciones_y_Datos/devsecops-lab/`
3. Leer `app/app.py` e identificar las vulnerabilidades antes de ejecutar el pipeline
4. Completar `.github/workflows/security.yml` con el pipeline de seguridad
5. Activar Dependabot en Settings → Security
6. Analizar los resultados del pipeline

### Estructura del laboratorio
- `app/app.py` — Aplicación Flask con vulnerabilidades intencionales para el lab
- `app/requirements.txt` — Dependencias con CVEs conocidos
- `tests/test_app.py` — Tests básicos
- `.github/workflows/security.yml` — Pipeline de seguridad (completar en el lab)

### ⚠ Advertencia
Este código contiene vulnerabilidades INTENCIONALES con fines educativos.
NO usar en producción. NO ejecutar en redes no controladas.
