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

class MoyenneTestCase(TestCase):

  def test_exemple(self):
    assert 1 ==1

  def test_moyenne_111(self):
    assert moyenne([1,1,1]) == 1

```
Créer un dossier td3 et créer trois fichiers dedans :

- tests.py
- bibliotheque.py (sans accent)
- __init__.py


Déplacer les fonctions et classes crées dans bibliothèque.py


Dans le fichier main ajouter la ligne 'from td3.bibliotheque import moyenne'
déplacer aussi les classes créées pendant le td2.


