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
df = pd.read_excel("sample RL5.xlsx")
data = df.iloc[3:]

for index, row in data.iterrows():

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
    Select(driver.find_element(By.ID, "bulan")).select_by_visible_text("Januari")

    # # Isi satu field
    # row = data.iloc[17:]  # A01.0

    field_names = [
    # "jumlah_L_dibawah_1_jam",
    # "jumlah_P_dibawah_1_jam",
    "jumlah_L_1_sampai_23_jam",
    "jumlah_P_1_sampai_23_jam",
    "jumlah_L_1_sampai_7_hari",
    "jumlah_P_1_sampai_7_hari",
    "jumlah_L_8_sampai_28_hari",
    "jumlah_P_8_sampai_28_hari",
    "jumlah_L_29_hari_sampai_dibawah_3_bulan",
    "jumlah_P_29_hari_sampai_dibawah_3_bulan",
    "jumlah_L_3_bulan_sampai_dibawah_6_bulan",
    "jumlah_P_3_bulan_sampai_dibawah_6_bulan",
    "jumlah_L_6_bulan_sampai_11_bulan",
    "jumlah_P_6_bulan_sampai_11_bulan",
    "jumlah_L_1_sampai_4_tahun",
    "jumlah_P_1_sampai_4_tahun",
    "jumlah_L_5_sampai_9_tahun",
    "jumlah_P_5_sampai_9_tahun",
    "jumlah_L_10_sampai_14_tahun",
    "jumlah_P_10_sampai_14_tahun",
    "jumlah_L_15_sampai_19_tahun",
    "jumlah_P_15_sampai_19_tahun",
    "jumlah_L_20_sampai_24_tahun",
    "jumlah_P_20_sampai_24_tahun",
    "jumlah_L_25_sampai_29_tahun",
    "jumlah_P_25_sampai_29_tahun",
    "jumlah_L_30_sampai_34_tahun",
    "jumlah_P_30_sampai_34_tahun",
    "jumlah_L_35_sampai_39_tahun",
    "jumlah_P_35_sampai_39_tahun",
    "jumlah_L_40_sampai_44_tahun",
    "jumlah_P_40_sampai_44_tahun",
    "jumlah_L_45_sampai_49_tahun",
    "jumlah_P_45_sampai_49_tahun",
    "jumlah_L_50_sampai_54_tahun",
    "jumlah_P_50_sampai_54_tahun",
    "jumlah_L_55_sampai_59_tahun",
    "jumlah_P_55_sampai_59_tahun",
    "jumlah_L_60_sampai_64_tahun",
    "jumlah_P_60_sampai_64_tahun",
    "jumlah_L_65_sampai_69_tahun",
    "jumlah_P_65_sampai_69_tahun",
    "jumlah_L_70_sampai_74_tahun",
    "jumlah_P_70_sampai_74_tahun",
    "jumlah_L_75_sampai_79_tahun",
    "jumlah_P_75_sampai_79_tahun",
    "jumlah_L_80_sampai_84_tahun",
    "jumlah_P_80_sampai_84_tahun",
    "jumlah_L_diatas_85_tahun",
    "jumlah_P_diatas_85_tahun",
    "jumlah_kunjungan_L",
    "jumlah_kunjungan_P"
]

    wanita = False

    field_l = driver.find_element(
        By.NAME,
        "jumlah_L_1_sampai_23_jam"
    )

    for i, field_name in enumerate(field_names):

        nilai = row.iloc[i + 5]

        if pd.isna(nilai):
            continue

        if float(nilai) == 0:
            continue

        field = driver.find_element(By.NAME, field_name)

        if not field.is_enabled():
            continue

        field.clear()
        field.send_keys(str(int(nilai)))

    # Pasien kunjungan
    kunjungan_l = row.iloc[53]
    kunjungan_p = row.iloc[54]

    if pd.isna(kunjungan_l):
        kunjungan_l = 0

    if pd.isna(kunjungan_p):
        kunjungan_p = 0

    # Laki-laki
    if float(kunjungan_l) > 0:

        field = driver.find_element(
            By.NAME,
            "jumlah_kunjungan_L"
        )

        if field.is_enabled():

            field.clear()
            field.send_keys(str(int(kunjungan_l)))

    # Perempuan
    if float(kunjungan_p) > 0:

        field = driver.find_element(
            By.NAME,
            "jumlah_kunjungan_P"
        )

        if field.is_enabled():

            field.clear()
            field.send_keys(str(int(kunjungan_p)))


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