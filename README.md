# Package Sorting Function

## Objective

This project contains an implementation of the `sort(width, height, length, mass)` function used to classify packages into stacks based on their size and mass. This exercise simulates sorting logic used in robotic automation systems.

---

## 📦 Classification Rules

### A package is **bulky** if:
- Its volume (`width * height * length`) is **≥ 1,000,000 cm³**, **OR**
- Any single dimension (width, height, or length) is **≥ 150 cm**

### A package is **heavy** if:
- Its mass is **≥ 20 kg**

---

## 🗂️ Stack Categories

| Bulky | Heavy | Result     |
|-------|--------|------------|
| No    | No     | STANDARD   |
| Yes   | No     | SPECIAL    |
| No    | Yes    | SPECIAL    |
| Yes   | Yes    | REJECTED   |

The function must return one of:

- `"STANDARD"`
- `"SPECIAL"`
- `"REJECTED"`

---

## 🧠 Implementation

Located in `sorter.py`:

```python
def sort(width, height, length, mass):
    """
    Determines the correct stack for a package based on its dimensions and mass.

    Args:
        width (int or float): Width in cm.
        height (int or float): Height in cm.
        length (int or float): Length in cm.
        mass (int or float): Mass in kg.

    Returns:
        str: One of "STANDARD", "SPECIAL", "REJECTED".
    """

    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
