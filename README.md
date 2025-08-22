# 📅 Napi Feladatkezelő (To-Do Handler)

Egy pici, könnyen használható **Python Tkinter** alapú alkalmazás, ami segít nyomon követni a napi teendőidet. Feladatokat adhatsz hozzá, pipálhatod őket, és a program elmenti őket egy **`tasks_log.txt`** fájlba a Dokumentumok mappádban.

---

## 🚀 Funkciók

* Új feladat hozzáadása
* Feladatok állapotának jelölése (✔ kész, ✘ nincs kész)
* Feladatok mentése naplófájlba az aktuális dátummal és idővel
* Egyszerű, letisztult Tkinter GUI

---

## 💻 Telepítés és futtatás - Ha a kódot használnád

1. Győződj meg róla, hogy **Python 3** telepítve van.
2. Mentsd el a kódot egy `todo.py` fájlba.
3. Nyisd meg a terminált (vagy CMD), és navigálj a fájl helyére.
4. Futtasd:

```bash
python todo.py
```

5. A GUI felület felugrik, és kezdődhet a teendők felvétele! ✨

---

## 📝 Használat - Ha a kódot használnád

1. Írd be a feladatot az input mezőbe.
2. Kattints a **➕ Feladat hozzáadása** gombra.
3. Pipáld ki a kész feladatokat a listából.
4. Kattints a **💾 Mentés** gombra, hogy elmentse a státuszokat a **`Documents/tasks_log.txt`** fájlba.
5. A státusz a GUI-ban is megjelenik, hogy hol lett elmentve a fájl. ✅

---

## 💻 Telepítés és futtatás - Ha az exe fájlt használnád

1. Töltsd le az `todo.exe` fájlt.
2. Dupla kattintással indítsd el.
3. A GUI felület felugrik, és kezdődhet a teendők felvétele! ✨

*(Nincs szükség Python telepítésre, az exe mindent tartalmaz.)*

---

## 📝 Használat - Ha az exe fájlt használnád

1. Írd be a feladatot az input mezőbe.
2. Kattints a **➕ Feladat hozzáadása** gombra.
3. Pipáld ki a kész feladatokat a listából.
4. Kattints a **💾 Mentés** gombra, hogy elmentse a státuszokat a **`Documents/tasks_log.txt`** fájlba.
5. A státusz a GUI-ban is megjelenik, hogy hol lett elmentve a fájl. ✅


## 🖼 Hogyan néz ki az alkalmazás?

```
📅 2025. August 22. (Friday)

[______________________________]  <- Ide írod a feladatot
[➕ Feladat hozzáadása]        <- Gomb új feladathoz

[ ] Feladat 1                  <- Checkbutton lista
[ ] Feladat 2
[✔] Kész Feladat

[💾 Mentés]                     <- Mentés gomb
✅ A fájl elmentve ide: C:/Users/Kincső/Documents/tasks_log.txt
```

**Jelmagyarázat:**

* `[ ]` → feladat nincs kész
* `[✔]` → feladat kész
* Az input mezőbe írod a feladatot, majd a **➕ Feladat hozzáadása** gombbal bekerül a listába.
* A **💾 Mentés** gomb rögzíti a státuszokat a `tasks_log.txt` fájlba.


## ⚡ Extra tippek

* A naplófájl minden mentésnél hozzáfűződik, így mindig megmarad a múltbéli napló.
* A dátum és az idő automatikusan bekerül a mentett listába.
* Könnyen testreszabhatod a betűtípust vagy az ikonokat (📅, ➕, 💾) a Tkinter gomboknál.