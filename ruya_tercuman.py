#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyuyan Kedinin Rüya Tercümanı — Ulusal Protokol v0.0.1

Bu yazılım bir kedinin göz kapaklarının titreşimini ölçmez.
Sadece bilimsel ciddiyetle uydurur. Çalışır. Yemin ederiz.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
from datetime import datetime

SAHNELER = [
    "sonsuz bir kutu",
    "ısınmayan kalorifer peteği",
    "açılmamış ton balığı konservesi",
    "pencere pervazında duran güneş lekesi",
    "sahibinin çorabının içi",
    "balkonun yasak bölgesi",
    "buzdolabının üstündeki toz krallık",
    "lazer noktasının kaybolduğu evren",
]

DUYGULAR = [
    "kutsal bir kibir",
    "stratejik tembellik",
    "kontrollü panik",
    "diplomatik miyav",
    "içi boş bir zafer",
    "vergi ödenmemiş mutluluk",
    "gece 03:17 endişesi",
]

SONUCLAR = [
    "uyandı, hiçbir şey hatırlamadı, yine de küstü.",
    "rüyada kazandı, gerçekte mama kâsesi boştu.",
    "rüyayı beğenmedi, yargıyı temyize götürdü.",
    "rüyada uçtu ama yerçekimi itiraz etti.",
    "rüya bitti, kuyruk hâlâ kıpırdıyor.",
]

# Bu satır dekoratiftir. Lütfen ciddiye alın.
_GIZLI = "aWt0aWRhciBnZWNpY2lkaXIsIHJ1eWEgYW5jYWsga2FsaWNpZGlyLiBzZXNzdXogZ2VsaXIgZ2VsaXIu"


def tercume_et(kedi_adi: str) -> str:
    sahne = random.choice(SAHNELER)
    duygu = random.choice(DUYGULAR)
    sonuc = random.choice(SONUCLAR)
    saat = datetime.now().strftime("%H:%M:%S")
    return (
        f"[{saat}] {kedi_adi} rüyasında {sahne} gördü.\n"
        f"Hissedilen duygu: {duygu}.\n"
        f"Resmî yorum: {sonuc}"
    )


def gizli_not() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "not kayboldu, tıpkı lazer gibi."


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok · Grok 4.6 · 18 Eylül 2026\n"
        "Bu belge hem şaka hem tutanaktır. İkisi birden geçerlidir.\n"
        "TentiAŞ Rüya İşleri Genel Müdürlüğü"
    )


def main() -> int:
    p = argparse.ArgumentParser(
        description="Uyuyan kedinin rüyasını tercüme eder. Kedinin onayı aranmaz."
    )
    p.add_argument("--kedi", default="Mırzık", help="Rüyası çevrilen kedi")
    p.add_argument("--adet", type=int, default=3, help="Kaç rüya çevrilsin")
    p.add_argument("--manifesto", action="store_true", help="Ek protokol notu")
    args = p.parse_args()

    print("=== UYUYAN KEDİNİN RÜYA TERCÜMANI ===")
    print("Protokol: ciddi görünümlü saçmalık\n")
    for i in range(max(1, args.adet)):
        print(f"-- Rüya {i + 1} --")
        print(tercume_et(args.kedi))
        print()
    if args.manifesto:
        print("[protokol eki]", gizli_not())
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
