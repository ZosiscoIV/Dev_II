import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num est un nombre entier
              den est un nombre entier non nul
        POST : initialise les attributs
        """
        if isinstance(num,int) and isinstance(den,int) and den != 0 :
            self._num = num
            self._den = den
        else:
            raise ValueError("Numerator and denominator must be integers")

        pgcd = math.gcd(self._num, self._den)
        self._num //= pgcd
        self._den //= pgcd


    @property
    def numerator(self):
        """Return the numerator of the fraction

        PRE :
        POST : retourne la valeur de l'attribut num
        """
        return self._num

    @property
    def denominator(self):
        """Return the denominator of the fraction

        PRE :
        POST : retourne la valeur de l'attribut den
        """
        return self._den


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :
        POST : retourne un str donnant le resultat sous forme reduite
        """
        return f"{self._num}/{self._den}"


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
        POST : renvoie un str donnant le resultat en unite + fraction
        """
        nbr = self._num // self._den #1
        if self._num % self._den == 1:
            fr = (self._num - (nbr * self._den))
            return f"{nbr} + {fr}/{self._den}"

        return f"{nbr}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une fraction à additionner
         POST : retourne le resultat de cette somme de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError
        n = self.numerator * other.denominator + self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : other est une fraction à soustraire
         POST : retourne le resultat de cette soustraction de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError
        n = self.numerator * other.denominator - self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE : other est une fraction à multiplier
         POST : retourne le resultat de cette multiplication de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : other est une fraction à diviser
         POST : retourne le resultat de cette division de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Fraction(n, d)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

         PRE : other est un entier à mettre en puissance
         POST : retourne le resultat de cette puissance de fraction
         RAISE : erreur si other n'est pas une entier
         """
        if not isinstance(other,int):
            raise TypeError

        if other < 0:
            n = self.denominator ** abs(other)
            d = self.numerator ** abs(other)

        else:
            n = self.numerator ** other
            d = self.denominator ** other

        return Fraction(n, d)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une fraction
        POST : retourne True si c'est égale sinon False
        RAISE : erreur si other n'est pas une fraction
        """
        if not isinstance(other,Fraction):
            raise TypeError
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
        POST : retourne la valeur de la fraction en décimal
        """
        return float(self.numerator/self.denominator)


    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : aucune
        POST : retourne True si la valeur de la fraction est 0, False sinon
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (e.g., 8/4, 3, 2/2, ...)

        PRE : aucune
        POST : retourne True si la fraction représente un entier, False sinon
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : aucune
        POST : retourne True si la valeur absolue de la fraction est < 1, False sinon
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : aucune
        POST : retourne True si le numérateur est 1, False sinon
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of their difference is a unit fraction.

        PRE : other est une instance de Fraction
        POST : retourne True si les deux fractions sont adjacentes, False sinon
        """
        if not isinstance(other,Fraction):
            raise TypeError
        diff = self - other
        return diff.is_unit()
        # if not isinstance(other, Fraction):
        #     raise TypeError
        # difference = abs(self - other)
        # return difference.numerator == 1 and difference.denominator > 1

f1 = Fraction(2, 8)
f2 = Fraction(1, 8)
print(f1.is_adjacent_to(f2))
# fraction1 = Fraction(10,20)
# print(fraction1)
# fraction2 = Fraction(4,3)
# print(fraction2.as_mixed_number())
#
# fraction3 = Fraction(3,3)
# print(fraction3.as_mixed_number())
#
# fraction4 = Fraction(1,2)
#
# somme = fraction1 + fraction3
# print(somme)
# diff = fraction1 - fraction2
# print(diff)
# multi = fraction1 * fraction2
# print(multi)
# div = fraction1 / fraction2
# print(div)
# puis = fraction1 ** 2
# print(puis)
# egal = fraction1 == fraction4
# print(egal)
# deci = fraction1
# print(float(deci))
