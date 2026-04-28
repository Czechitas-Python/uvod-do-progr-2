import shutil
import os

EXPORT_DIR = "export-da"

# (source_path, flat_filename) — flat filename uses section prefix to avoid collisions
FILES = [
    # json
    ("uvod-do-programovani-2/json/format-json.md", "json-format-json.md"),
    ("uvod-do-programovani-2/json/json-api.md", "json-json-api.md"),
    # slicing-metody-moduly
    ("uvod-do-programovani-2/slicing-metody-moduly/slicing.md", "slicing-metody-moduly-slicing.md"),
    ("uvod-do-programovani-2/slicing-metody-moduly/metody.md", "slicing-metody-moduly-metody.md"),
    ("uvod-do-programovani-2/slicing-metody-moduly/moduly.md", "slicing-metody-moduly-moduly.md"),
    ("uvod-do-programovani-2/slicing-metody-moduly/vicerozmerne-struktury.md", "slicing-metody-moduly-vicerozmerne-struktury.md"),
    # slovniky
    ("uvod-do-programovani-2/slovniky/slovniky.md", "slovniky-slovniky.md"),
    ("uvod-do-programovani-2/slovniky/slovniky-a-cykly.md", "slovniky-slovniky-a-cykly.md"),
    ("uvod-do-programovani-2/slovniky/slovniky-a-cykly-2.md", "slovniky-slovniky-a-cykly-2.md"),
    ("uvod-do-programovani-2/slovniky/mnoziny.md", "slovniky-mnoziny.md"),
    ("uvod-do-programovani-2/slovniky/dvourozmerne-tabulky.md", "slovniky-dvourozmerne-tabulky.md"),
    # soubory
    ("uvod-do-programovani-2/soubory/cteni-souboru.md", "soubory-cteni-souboru.md"),
    ("uvod-do-programovani-2/soubory/zapis-souboru.md", "soubory-zapis-souboru.md"),
    # uvod
    ("uvod-do-programovani-2/uvod/uvod.md", "uvod-uvod.md"),
    ("uvod-do-programovani-2/uvod/sekvence.md", "uvod-sekvence.md"),
    ("uvod-do-programovani-2/uvod/podminky.md", "uvod-podminky.md"),
    ("uvod-do-programovani-2/uvod/cykly.md", "uvod-cykly.md"),
    ("uvod-do-programovani-2/uvod/priklady.md", "uvod-priklady.md"),
    # bonusy/python-sql
    ("bonusy/python-sql/python-sql.md", "python-sql-python-sql.md"),
    ("bonusy/python-sql/cyklus_sql.md", "python-sql-cyklus_sql.md"),
    ("bonusy/python-sql/krokovani.md", "python-sql-krokovani.md"),
    # vyjimky (only the specific file requested)
    ("uvod-do-programovani-2/vyjimky/chyby-v-programu.md", "vyjimky-chyby-v-programu.md"),
]


def main():
    if os.path.exists(EXPORT_DIR):
        shutil.rmtree(EXPORT_DIR)

    os.makedirs(EXPORT_DIR)

    for src, dest_name in FILES:
        dest = os.path.join(EXPORT_DIR, dest_name)
        shutil.copy2(src, dest)
        print(f"Copied: {src} -> {dest_name}")

    print(f"\nDone. {len(FILES)} files copied to {EXPORT_DIR}/")


if __name__ == "__main__":
    main()
