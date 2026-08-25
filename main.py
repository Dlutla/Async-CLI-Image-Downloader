import asyncio
import aiohttp
import aiofiles
import os
from pathlib import Path
from urllib.parse import urlparse
from prettytable import PrettyTable

async def download_image(session, url, save_path, results, index):
    try:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
            filename = f"image_{index}.jpg"
        full_path = save_path / filename

        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                async with aiofiles.open(full_path, 'wb') as f:
                    await f.write(await response.read())
                results.append((url, "Успех"))
                print(f"[OK] {url} -> {full_path}")
            else:
                results.append((url, f"Ошибка HTTP {response.status}"))
                print(f"[FAIL] {url} -> HTTP {response.status}")
    except asyncio.TimeoutError:
        results.append((url, "Ошибка: таймаут"))
        print(f"[FAIL] {url} -> таймаут")
    except Exception as e:
        results.append((url, f"Ошибка: {str(e)}"))
        print(f"[FAIL] {url} -> {str(e)}")

async def main():
    while True:
        save_dir = input("Введите путь для сохранения изображений: ").strip()
        if not save_dir:
            print("Путь не может быть пустым. Попробуйте снова.")
            continue
        path = Path(save_dir).expanduser().resolve()
        try:
            path.mkdir(parents=True, exist_ok=True)
            test_file = path / ".write_test"
            test_file.touch()
            test_file.unlink()
            break
        except Exception as e:
            print(f"Некорректный путь или нет доступа: {e}")
            continue

    urls = []
    print("\nВведите ссылки на изображения (пустая строка для завершения):")
    while True:
        url = input().strip()
        if not url:
            break
        urls.append(url)

    if not urls:
        print("Нет ссылок для загрузки.")
        return

    results = []
    connector = aiohttp.TCPConnector(ssl=False)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [download_image(session, url, path, results, idx) for idx, url in enumerate(urls)]
        await asyncio.gather(*tasks)

    print("\nСводка об успешных и неуспешных загрузках")
    table = PrettyTable()
    table.field_names = ["Ссылка", "Статус"]
    table.align["Ссылка"] = "l"
    table.align["Статус"] = "l"
    for url, status in results:
        table.add_row([url, status])
    print(table)

if __name__ == "__main__":
    asyncio.run(main())