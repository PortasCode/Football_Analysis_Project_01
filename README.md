# ⚽ Football Data Pipeline (Scout Alert)

## Cel Projektu
Stworzenie bezobsługowego potoku danych (ETL) w Google Cloud Platform (GCP), który codziennie integruje dane z zewnętrznego API piłkarskiego, strukturyzuje je za pomocą Pythona, zapisuje historię do bazy BigQuery, a wyniki analizy wysyła w formie powiadomienia na komunikator.

## Architektura
*   **Źródło danych:** API piłkarskie (np. API-Football, football-data.org)
*   **Język programowania:** Python 3 (biblioteki: `requests`, `pandas` / `json`)
*   **Chmura:** Google Cloud Platform (GCP)
*   **Przetwarzanie (Compute):** Cloud Functions
*   **Hurtownia danych (DWH):** Google BigQuery
*   **Harmonogramowanie:** Cloud Scheduler
*   **Powiadomienia:** Webhook (Telegram / Discord)

---

## Harmonogram Projektu

### Tydzień 1: Opanowanie danych na własnym podwórku (Extract & Transform)
- [ ] Założenie konta na platformie z API sportowym i uzyskanie klucza (API Key).
- [ ] Napisanie skryptu w Pythonie pobierającego surowe dane w formacie JSON (wczorajsze wyniki / dzisiejsze mecze).
- [ ] Wyodrębnienie z JSON-a interesujących danych (np. nazwy drużyn, wyniki, strzelcy).
- [ ] Wyświetlenie przefiltrowanych i sformatowanych danych w konsoli.

### Tydzień 2: Baza danych i pierwsza integracja (Load)
- [ ] Utworzenie darmowego projektu w GCP.
- [ ] Skonfigurowanie BigQuery i utworzenie docelowej tabeli (zaplanowanie schematu danych).
- [ ] Rozbudowa skryptu Python o autoryzację do GCP.
- [ ] Napisanie kodu wstawiającego przetworzone dane jako nowe rekordy do bazy danych BigQuery.

### Tydzień 3: Przeprowadzka do chmury (Deployment)
- [ ] Przystosowanie skryptu do działania jako Google Cloud Function.
- [ ] Ukrycie wrażliwych danych (Klucz API, poświadczenia) w zmiennych środowiskowych, aby nie trzymać ich bezpośrednio w kodzie.
- [ ] Ręczne uruchomienie funkcji w chmurze i weryfikacja w logach, czy poprawnie komunikuje się z API i z bazą.

### Tydzień 4: Automatyzacja i alerty (Orchestration & Alerting)
- [ ] Konfiguracja Cloud Scheduler, aby uruchamiał funkcję chmurową codziennie o wybranej porze (np. 7:00 rano).
- [ ] Dodanie na samym końcu skryptu w Pythonie requestu wysyłającego zebrane dane na webhook komunikatora (Discord/Telegram).
- [ ] Weryfikacja działania całego, bezobsługowego potoku przez 3 dni z rzędu.
