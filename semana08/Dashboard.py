#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard.py - Versión 100% compatible con PyCharm + UEA
Autor: Jhon Michael Panta Buste
Objetivo: Funcionar incluso si Dashboard.py está en cualquier subcarpeta.
Solución: Usa os.getcwd() en lugar de __file__ para detectar la raíz.
"""

import os
from pathlib import Path


def verificar_terminal():
    import shutil
    if os.name == 'nt':
        return "cmd"
    elif shutil.which("konsole"):
        return "konsole"
    elif shutil.which("xterm"):
        return "xterm"
    else:
        return None


def mostrar_codigo(ruta_script: Path) -> bool:
    try:
        with open(ruta_script, 'r', encoding='utf-8') as f:
            print(f"\n{'='*60}")
            print(f"📄 SCRIPT: {ruta_script.name}")
            print(f"📍 Ruta absoluta: {ruta_script.resolve()}")
            print('='*60)
            print(f.read())
        return True
    except Exception as e:
        print(f"❌ Error al leer '{ruta_script}': {e}")
        return False


def ejecutar_codigo(ruta_script: Path):
    terminal = verificar_terminal()
    try:
        if os.name == 'nt':
            os.system(f'start cmd /k python "{ruta_script}"')
        elif terminal == "konsole":
            os.system(f'konsole --hold -e python3 "{ruta_script}" &')
        elif terminal == "xterm":
            os.system(f'xterm -hold -e python3 "{ruta_script}" &')
        else:
            import subprocess
            subprocess.Popen(['python3', str(ruta_script)])
    except Exception as e:
        print(f"⚠️ Ejecución fallida: {e}")


def listar_carpetas_con_py(ruta_base: Path) -> list[str]:
    """Lista carpetas en ruta_base que contienen al menos un .py (cualquier nivel)."""
    carpetas = []
    for item in ruta_base.iterdir():
        if item.is_dir():
            if any(item.rglob("*.py")):
                carpetas.append(item.name)
    return sorted(carpetas)


def menu_principal(ruta_base: Path):
    carpetas = listar_carpetas_con_py(ruta_base)
    if not carpetas:
        print("❌ No se encontraron carpetas con archivos .py en:")
        print(f"   {ruta_base}")
        print("\n💡 Verifica:")
        print("   1. Que los archivos terminen en '.py' (no solo 'nombre')")
        print("   2. Que no estén ocultos (empiecen con '.')")
        print("   3. Que el Working Directory en PyCharm sea correcto")
        return

    while True:
        print("\n" + "📁".center(50, "="))
        print("DASHBOARD UNIVERSAL – POO (UEA)")
        print("=" * 50)
        for i, c in enumerate(carpetas, 1):
            print(f"{i} - {c}")
        print("0 - Salir")

        opt = input("\n👉 Elige: ").strip()
        if opt == '0':
            print("👋 ¡Hasta luego!")
            break
        try:
            idx = int(opt) - 1
            if 0 <= idx < len(carpetas):
                menu_scripts(ruta_base / carpetas[idx])
            else:
                print("❌ Fuera de rango.")
        except ValueError:
            print("❌ Ingresa un número.")


def menu_scripts(ruta_carpeta: Path):
    scripts = sorted([f.relative_to(ruta_carpeta).as_posix() for f in ruta_carpeta.rglob("*.py")])
    if not scripts:
        print(f"ℹ️  No hay .py en '{ruta_carpeta.name}'")
        input("⏎ Enter para regresar...")
        return

    while True:
        print(f"\n🐍 Scripts en '{ruta_carpeta.name}':")
        for i, s in enumerate(scripts, 1):
            print(f"{i} - {s}")
        print("0 - ← Regresar")

        opt = input("Elige script: ").strip()
        if opt == '0':
            break
        try:
            idx = int(opt) - 1
            if 0 <= idx < len(scripts):
                full_path = ruta_carpeta / scripts[idx]
                if mostrar_codigo(full_path):
                    if input("\n¿Ejecutar? (1=Sí, 0=No): ").strip() == '1':
                        ejecutar_codigo(full_path)
                input("\n⏎ Enter para continuar...")
            else:
                print("❌ Número inválido.")
        except ValueError:
            print("❌ Ingresa un número.")


# === PUNTO DE ENTRADA — USAR os.getcwd() EN VEZ DE __file__ ===
if __name__ == "__main__":
    RUTA_BASE = Path(os.getcwd()).resolve()
    print(f"✅ Working directory (según sistema): {RUTA_BASE}")
    menu_principal(RUTA_BASE)