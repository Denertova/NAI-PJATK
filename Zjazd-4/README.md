# Machine Learning Classification Project

## Autor
**Klaudia Denert - s29276**  

---

## Opis problemu
Projekt obejmuje klasyfikację danych przy użyciu dwóch algorytmów:

1. **Decision Tree Classifier** – dla zbioru danych **Abalone** (binarna klasyfikacja: `rings >= 10 → Class 1`, `rings < 10 → Class 0`).  
2. **Support Vector Machine (SVM)** – dla zbioru danych **Car Evaluation** (wieloklasowa klasyfikacja: `unacc`, `acc`, `good`, `vgood`).  

W projekcie zaprezentowano:  
- metryki jakości klasyfikacji: accuracy, precision, recall, F1-score, confusion matrix,  
- wizualizację danych i granic decyzyjnych klasyfikatora,  
- użycie różnych funkcji jądra (`linear`, `rbf`, `poly`) dla SVM i wpływ parametrów na wyniki klasyfikacji.  

---

## Dane

### 1. Abalone
- Źródło: [UCI Machine Learning Repository – Abalone](https://archive.ics.uci.edu/ml/datasets/Abalone)  
- Liczba próbek: 4177  
- Cechy: `Sex, Length, Diameter, Height, Whole weight, Shucked weight, Viscera weight, Shell weight`  
- Przekształcenie: `Sex` zakodowany jako liczby (M=0, F=1, I=2), etykieta binarna `y = (rings >= 10)`  

### 2. Car Evaluation
- Źródło: [UCI Machine Learning Repository – Car Evaluation](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)  
- Liczba próbek: 1728  
- Cechy: `buying, maint, doors, persons, lug_boot, safety` (kategoryczne, zakodowane one-hot)  
- Klasy: `unacc`, `acc`, `good`, `vgood`  

---

## Wymagania
- scikit-learn
- pandas
- numpy
- matplotlib
- joblib
 
 ```bash
  pip install numpy pandas matplotlib scikit-learn joblib
  ```

## Instrukcja użycia
Uruchomienie klasyfikatora Abalone

```bash
python3 abalone.py
```

Uruchomienie klasyfikatora Car Evaluation

```bash
python3 car.py
```

Dla obu zbiorów danych raportowane są:

- Accuracy

- Precision / Recall / F1-score dla każdej klasy

- Confusion matrix

Dla SVM w Car Evaluation dodatkowo analizowany jest wpływ wyboru kernela (linear, rbf, poly) i parametrów (C, gamma, degree) na wyniki klasyfikacji.

## Wizualizacja danych

Abalone: scatter plot pierwszych dwóch cech (Length, Diameter) z podziałem na klasy.

Car Evaluation: PCA 2D po zakodowaniu cech one-hot, kolorowanie punktów według klas.

## Dokumentacja kodu

Funkcja visualize_classifier w utilities.py generuje wizualizację granic decyzyjnych dla danych 2D.
