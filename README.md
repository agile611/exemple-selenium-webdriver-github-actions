[![Agile611](https://www.agile611.com/wp-content/uploads/2020/09/cropped-logo-header.png)](http://www.agile611.com/)

# Agile611 — Selenium WebDriver Tests - Yahoo.com

Automatització de tests amb Selenium WebDriver en Python, executats automàticament mitjançant GitHub Actions.

## 📋 Descripció

Aquest projecte conté una suite de tests d'automatització web que:
- Verifica que la pàgina principal de Yahoo.com es carrega correctament
- Valida la funcionalitat de cerca de Yahoo
- S'executa automàticament en cada push a la branca `main`
- Es prova en entorn Linux amb Python 3.11

## 🛠️ Requisits Previs

- **Python 3.11** o superior
- **Chrome/Chromium** instal·lat al sistema
- **pip** (gestor de paquets de Python)

## 📦 Instal·lació

### 1. Clonar el repositori

```bash
git clone https://github.com/yourusername/exemple-selenium-webdriver-github-actions.git
cd exemple-selenium-webdriver-github-actions
```

### 2. Crear un entorn virtual (opcional però recomanat)

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
# o
venv\Scripts\activate  # En Windows
```

### 3. Instal·lar dependències

```bash
pip install -r requirements.txt
```

## 📁 Estructura del Projecte

```
.
├── README.md                          # Aquest fitxer
├── .gitignore                         # Configuració de Git
├── requirements.txt                   # Dependències de Python
├── yahootest.py                       # Test bàsic de Yahoo
├── test_yahoo_search.py               # Test de cerca de Yahoo
└── .github/
    └── workflows/
        └── selenium-test.yml          # Configuració de GitHub Actions
```

## ✅ Tests Disponibles

### 1. `yahootest.py` - Test Bàsic de Yahoo
Verifica que:
- La pàgina de Yahoo.com es carrega correctament
- El títol de la pàgina conté "Yahoo"

```bash
python yahootest.py
```

### 2. `test_yahoo_search.py` - Test de Cerca
Verifica que:
- Es pot accedir a la pàgina de Yahoo.com
- S'accepta el botó de consentiment
- Es pot fer una cerca ("pizza hawaiana")
- S'obren resultats en una nova finestra
- Els resultats de cerca es mostren correctament

```bash
python test_yahoo_search.py
```

## 🚀 Executar els Tests Localment

### Executar tots els tests

```bash
pytest yahootest.py test_yahoo_search.py -v
```

### Executar un test específic

```bash
pytest yahootest.py -v
pytest test_yahoo_search.py -v
```

### Executar amb més detalls

```bash
pytest yahootest.py test_yahoo_search.py -v --tb=short
```

## 🔄 GitHub Actions

Els tests s'executen automàticament quan:
- Es fa push a la branca `main`
- S'obre un pull request a la branca `main`
- Diàriament a les 00:00 UTC (per a monitoratge continu)

### Configuració

El workflow de GitHub Actions es defineix a [`.github/workflows/selenium-test.yml`](.github/workflows/selenium-test.yml) i:
- **Sistema operatiu**: Ubuntu Linux (latest)
- **Python**: 3.11
- **Navegador**: Chrome (instal·lat automàticament)

### Veure els resultats

1. Anar a la pestanya **"Actions"** del repositori
2. Seleccionar el workflow **"Selenium WebDriver Tests"**
3. Veure els detalls de l'execució

## 📚 Tecnologies Utilitzades

- **[Selenium WebDriver](https://www.selenium.dev/)** - Automatització de navegadors
- **[Python 3.11](https://www.python.org/)** - Llenguatge de programació
- **[pytest](https://pytest.org/)** - Framework de testing
- **[webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)** - Gestió automàtica de ChromeDriver
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD

## 🔧 Requisits del projecte (`requirements.txt`)

```
selenium>=4.0.0           # Framework d'automatització web
webdriver-manager>=3.8.0  # Gestor automàtic de drivers
pytest>=7.0.0             # Framework de testing
```

## ⚠️ Notas Importants

1. **Headless Mode**: En GitHub Actions, els tests s'executen en mode headless (sense interfície gràfica)
2. **Waits**: Els tests utilitzen WebDriverWait per a garantir que els elements estiguin disponibles
3. **Manejo d'excepcions**: Els tests inclouen manejo robust d'excepcions per a evitar falls inesperats

## 🐛 Resolució de Problemes

### "Chrome not found" en local
```bash
# macOS
brew install chromium

# Ubuntu/Debian
sudo apt-get install chromium-browser

# Windows
choco install chromium
```

### Els tests no troben els elements
- Verificar que Yahoo.com no ha canviat la seva estructura HTML
- Incrementar el timeout en `WebDriverWait`
- Comprovar la connexió a Internet

### Els tests funcionen localment però no a GitHub Actions
- Verificar que el fitxer `requirements.txt` té totes les dependències
- Revisar els logs del workflow a GitHub

---

## 📄 Licencia

Publicado por [Agile611](http://www.agile611.com/) bajo licencia
**Creative Commons Attribution-NonCommercial 4.0 International**.

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

README escrito por [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).

**Contacto:**
- 🌐 [agile611.com](http://www.agile611.com/)
- 📍 Carrer Laureà Miró 309, 08950 Esplugues de Llobregat (Barcelona)