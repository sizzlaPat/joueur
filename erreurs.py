class Erreur(Exception):
    """ class de base pour les autres erreurs"""
pass

class ErreurMinAge(Erreur):
    """survient quand la valeur entre est petite"""
pass

class ErreurMaxAge(Erreur):
    """survient quand la valeur entre est grande"""
pass

class ErreurSexe(Erreur):
    """survient quand la valeur entre est grande"""
pass


