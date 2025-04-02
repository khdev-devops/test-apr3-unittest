# Enhetstestning med Python

Detta projekt innehåller sex olika övningar där du får träna på att förstå och skriva bättre enhetstester. Syftet är att bygga en förståelse för vad som gör tester bra, robusta och lättförståeliga.

## Vad du behöver

- [VS Code](https://code.visualstudio.com/docs/languages/python) (eller annan texteditor/IDE)
- [Python 3.13](https://www.python.org/downloads/) (eller senare stabil version) installerat
- **Ett terminalfönster** där du kan köra `pytest` (tex i VS Code).

## Installera beroenden

Kör följande kommando i projektets rotmapp:

```bash
pip install -r requirements.txt
```

Det installerar bland annat:
- [pytest](https://docs.pytest.org/) – testramverk
- [pytest-mock](https://pytest-mock.readthedocs.io/) – för att mocka beroenden
- [pyhamcrest](https://github.com/hamcrest/PyHamcrest/) – för läsbara och kraftfulla assertions
- [coverage](https://coverage.readthedocs.io/) – för att mäta testtäckning

## Köra alla tester

Från projektets rot, kör:

```bash
pytest
```

Det kör alla tester och visar vilka rader som saknar testtäckning.

## Köra ett enskilt test

Du kan köra en viss testfil med (exempel):

```bash
pytest tests/test_1_bad_naming.py
```

## Övningarna

Alla övningar ligger i mappen `tests/` och är döpta enligt:

- `test_1_bad_naming.py` – dålig namngivning
- `test_2_given_when_then.py` – saknar tydlig struktur
- `test_3_flaky.py` – test som fungerar ibland men inte alltid
- `test_4_needs_mock.py` – test som borde använda mock
- `test_5_missing_coverage.py` – skapa tester för att nå hög testtäckningen
- `test_6_boundary_analysis.py` – skriv tester med hjälp av gränsvärdesanalys

### Så här gör du
1. Läs igenom testfilen noggrant (och kika på kodfil som den testar).
2. Följ kommentarerna i filen – där står vad du ska ändra eller lägga till.
3. Kör testet själv för att se vad som händer.
4. Fixa problemet / förbättra testet.

Tips: Lägg till `-x` för att sluta vid första fel:

```bash
pytest -x tests/test_3_flaky.py
```

---

Lycka till!
