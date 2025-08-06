from playwright.sync_api import sync_playwright

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://allegro.pl/login")
        print("➡️ Zaloguj się ręcznie w otwartej przeglądarce.")
        print("✅ Po zalogowaniu wróć do terminala i naciśnij ENTER.")

        input("🕐 Czekam... (naciśnij ENTER jak będziesz zalogowany)")
        context.storage_state(path="session.json")
        print("📦 Sesja została zapisana do pliku session.json")

        browser.close()

if __name__ == "__main__":
    save_session()
