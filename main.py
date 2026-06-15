from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

options = Options()
options.add_experimental_option(
    "debuggerAddress",
    "127.0.0.1:9222"
)

driver = webdriver.Chrome(options=options)

#import excel
# print("Memproses:excel")
df = pd.read_excel("sample.xlsx")
data = df.iloc[3:]

for index, row in data.iloc[218:].iterrows():

    icd = str(row["No.Daftar Terperinci"]).strip()

    if "." not in icd:
        print(icd, "Skip")
        continue
    # print("Memproses:", icd)

    # Klik +
    for link in driver.find_elements(By.TAG_NAME, "a"):
        if link.text.strip() == "+":
            link.click()
            break

    time.sleep(1)

    # Cari A01
    search = driver.find_element(By.NAME, "caripenyakit")
    search.clear()
    search.send_keys(icd)

    # Klik Cari
    for btn in driver.find_elements(By.TAG_NAME, "button"):
        if btn.text.strip() == "Cari":
            btn.click()
            break

    time.sleep(1)

    # Klik Tambah pertama
    tambah_ditemukan = False

    for btn in driver.find_elements(By.TAG_NAME, "button"):
        if btn.text.strip() == "Tambah":
            btn.click()
            tambah_ditemukan = True
            break

    if not tambah_ditemukan:
        print(icd,"ICD tidak ditemukan")
        continue

    time.sleep(3)

    # Pilih tahun
    Select(driver.find_element(By.ID, "tahun")).select_by_visible_text("2026")

    # Pilih bulan
    Select(driver.find_element(By.ID, "bulan")).select_by_visible_text("Februari")

    # # Isi satu field
    # row = data.iloc[17:]  # A01.0

    field_names = [
        # "jmlhPasHidupMatiUmurGen01JamL",
        # "jmlhPasHidupMatiUmurGen01JamP",
        "jmlhPasHidupMatiUmurGen123JamL",
        "jmlhPasHidupMatiUmurGen123JamP",
        "jmlhPasHidupMatiUmurGen17hrL",
        "jmlhPasHidupMatiUmurGen17hrP",
        "jmlhPasHidupMatiUmurGen828hrL",
        "jmlhPasHidupMatiUmurGen828hrP",
        "jmlhPasHidupMatiUmurGen29hr3blnL",
        "jmlhPasHidupMatiUmurGen29hr3blnP",
        "jmlhPasHidupMatiUmurGen36blnL",
        "jmlhPasHidupMatiUmurGen36blnP",
        "jmlhPasHidupMatiUmurGen611blnL",
        "jmlhPasHidupMatiUmurGen611blnP",
        "jmlhPasHidupMatiUmurGen14thL",
        "jmlhPasHidupMatiUmurGen14thP",
        "jmlhPasHidupMatiUmurGen59thL",
        "jmlhPasHidupMatiUmurGen59thP",
        "jmlhPasHidupMatiUmurGen1014thL",
        "jmlhPasHidupMatiUmurGen1014thP",
        "jmlhPasHidupMatiUmurGen1519thL",
        "jmlhPasHidupMatiUmurGen1519thP",
        "jmlhPasHidupMatiUmurGen2024thL",
        "jmlhPasHidupMatiUmurGen2024thP",
        "jmlhPasHidupMatiUmurGen2529thL",
        "jmlhPasHidupMatiUmurGen2529thP",
        "jmlhPasHidupMatiUmurGen3034thL",
        "jmlhPasHidupMatiUmurGen3034thP",
        "jmlhPasHidupMatiUmurGen3539thL",
        "jmlhPasHidupMatiUmurGen3539thP",
        "jmlhPasHidupMatiUmurGen4044thL",
        "jmlhPasHidupMatiUmurGen4044thP",
        "jmlhPasHidupMatiUmurGen4549thL",
        "jmlhPasHidupMatiUmurGen4549thP",
        "jmlhPasHidupMatiUmurGen5054thL",
        "jmlhPasHidupMatiUmurGen5054thP",
        "jmlhPasHidupMatiUmurGen5559thL",
        "jmlhPasHidupMatiUmurGen5559thP",
        "jmlhPasHidupMatiUmurGen6064thL",
        "jmlhPasHidupMatiUmurGen6064thP",
        "jmlhPasHidupMatiUmurGen6569thL",
        "jmlhPasHidupMatiUmurGen6569thP",
        "jmlhPasHidupMatiUmurGen7074thL",
        "jmlhPasHidupMatiUmurGen7074thP",
        "jmlhPasHidupMatiUmurGen7579thL",
        "jmlhPasHidupMatiUmurGen7579thP",
        "jmlhPasHidupMatiUmurGen8084thL",
        "jmlhPasHidupMatiUmurGen8084thP",
        "jmlhPasHidupMatiUmurGenLebih85thL",
        "jmlhPasHidupMatiUmurGenLebih85thP"
    ]

    wanita = False

    for i, field_name in enumerate(field_names):

        nilai = row.iloc[i + 5]

        if pd.isna(nilai):
            continue

        if float(nilai) == 0:
            continue

        field_l = driver.find_element(
            By.NAME,
            "jmlhPasHidupMatiUmurGen123JamL"
        )

        wanita = not field_l.is_enabled()


        field = driver.find_element(By.NAME, field_name)

        if not field.is_enabled():
            continue

        field.clear()
        field.send_keys(str(int(nilai)))

        # print(field_name, "=", nilai)


    # Pasien keluar mati
    mati_l = row.iloc[56]
    mati_p = row.iloc[57]

    if pd.isna(mati_l):
        mati_l = 0

    if pd.isna(mati_p):
        mati_p = 0

    # Laki-laki
    if float(mati_l) > 0:

        field = driver.find_element(
            By.NAME,
            "jmlhPasKeluarMatiGenL"
        )

        if field.is_enabled():

            field.clear()
            field.send_keys(str(int(mati_l)))

        # else:

        #     print(
        #         f"{icd} | Mati L disabled"
        #     )

    # Perempuan
    if float(mati_p) > 0:

        field = driver.find_element(
            By.NAME,
            "jmlhPasKeluarMatiGenP"
        )

        if field.is_enabled():

            field.clear()
            field.send_keys(str(int(mati_p)))

        # else:

        #     print(
        #         f"{icd} | Mati P disabled"
        #     )
    

    # Klik Simpan
    for btn in driver.find_elements(By.TAG_NAME, "button"):
        if btn.text.strip() == "Simpan":

            driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                btn
            )

            time.sleep(1)

            btn.click()

            # print("Data disimpan")
            break

    time.sleep(3)
    
    if wanita:
        print(icd, "Perempuan")
    else:
        print(icd, "Berhasil")