Modules et tests
================

But du TD :  Séparer le code dans différents fichiers et permettre de lancer les
tests automatiquemet.
Écrire nos premiers tests afin de s'assurer au fil du temps du bon
fonctionnement de nos programmes.

1 / Créer un fichier bibliotheque.py  et déplacer les fonction et classes définies
précédemment.

2 / Modifier le fichier main pour importer les fonctions et classes.

Exemple : from bibliotheque import moyenne

3 / à la fin du fichier  bibliotheque utiliser le mot clef `assert` qui arrête
l'exécution d'un programme si la condition n'est pas vérifiée.
Par exemple: `assert True` de fera rien.
`assert False, message` va arrêter le programme et afficher message.


créer une liste : l_1 = [1,1,1]

Vérifier que `moyenne([1,1,1])` vaut 1 et que `écart_type([1,1,1])` vaut zéro.


4/ Créer un fichier test sur le modèle suivant:

```python
from unittest import TestCase
from bibliotheque import fonction2
class MoyenneTestCase(TestCase):

  def test_exemple(self): #Votre test a vous.
    assert fonction2() == 2

  def test_moyenne_111(self):
    assert moyenne([1,1,1]) == 1

```

Modifier le fichier `.replit` pour obtenir le contenu suivant:

```
language = "python3"
run = "python -m unittest discover"
```

5/ Utiliser des méthodes adéquates

Avec les TestCase on peut utiliser des fonction spécifiques,
remplacer `assert op1 == op2, message`  par `self.AssertEqual(op, op2, message)`
message est facultatif.

Les différentes fonctions disponibles pour les test:

- assertAlmostEqual
- assertDictContainsSubset
- assertDictEqual
- assertEqual
- assertEquals
- assertFalse
- assertGreater
- assertGreaterEqual
- assertIn
- assertIs
- assertIsInstance
- assertIsNone
- assertIsNot
- assertIsNotNone
- assertItemsEqual
- assertLess
- assertLessEqual
- assertListEqual
- assertNotAlmostEqual
- assertNotAlmostEquals
- assertNotEqual
- assertNotEquals
- assertNotIn
- assertNotIsInstance
- assertNotRegexpMatches
- assertRaises
- assertSequenceEqual
- assertSetEqual
- assertTrue
- assertTupleEqual

Ecrire un classe pour

Créer un dossier td3 et créer trois fichiers dedans :

- tests.py
- bibliotheque.py (sans accent)
- \_\_init\_\_.py




Dans le fichier main ajouter la ligne 'from td3.bibliotheque import moyenne'
déplacer aussi les classes créées pendant le td2.


