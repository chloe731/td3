from unittest import TestCase

class MoyenneTestCase(TestCase):

  def test_exemple(self):
    assert 1 ==1 

  def test_moyenne_111(self):
    assert moyenne([1,1,1]) == 1




def moyenne(it):
  return sum(it)/len(it)