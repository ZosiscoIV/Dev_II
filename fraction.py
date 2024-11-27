import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
        POST : crée une fraction selon le numérateur et le dénominateur spécifiés en paramètres.
        RAISE : ValueError lorsque num ou den ne sont pas des entiers ou que den est égal à 0
        """
        if isinstance(num,int) and isinstance(den,int) and den != 0 :
            if den < 0:
                self._num = -num
                self._den = -den
            else:
                self._num = num
                self._den = den
        else:
            if den == 0:
                raise ZeroDivisionError("Le denominateur ne peut pas valoir zéro")
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
        return f"{self.numerator}/{self.denominator}"


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
        POST : renvoie un str donnant le resultat en "unite + fraction" ou juste "unite" si le résultat est un entier
        """
        nbr = abs(self.numerator) // self.denominator
        if abs(self.numerator) % self.denominator == 1:
            fr = (abs(self.numerator) - (nbr * self.denominator))
            if self.numerator < 0:
                return f"{-nbr} - {fr}/{self.denominator}"
            else:
                return f"{nbr} + {fr}/{self.denominator}"
        if self.numerator < 0:
            return f"{-nbr}"
        return f"{nbr}"

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :
         POST : retourne une nouvelle fraction équivalente au resultat de la somme de la fraction courante et de la fraction other
         RAISE : TypeError si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        n = self.numerator * other.denominator + self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE :
         POST : retourne une nouvelle fraction équivalente au resultat de la différence de la fraction courante et de la fraction other
         RAISE : TypeError si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        n = self.numerator * other.denominator - self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE :
         POST : retourne une nouvelle fraction équivalente au resultat de la multiplication de la fraction courante et de la fraction other
         RAISE : TypeError si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE :
         POST : retourne une nouvelle fraction équivalente au resultat de la division de la fraction courante et de la fraction other
         RAISE : TypeError si other n'est pas une fraction
         RAISE : ZeroDivisionError si other à un den égal à 0
         """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        if other.numerator == 0:
            raise ZeroDivisionError("impossible de diviser par 0")
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Fraction(n, d)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

         PRE :
         POST : retourne une nouvelle fraction équivalente au resultat de l'exponentielle dont la base est la fraction courante et l'exposant est l'entier other
         RAISE : TypeError si other n'est pas un entier
         """
        if not isinstance(other,int):
            raise TypeError("other doit être de type Fraction")

        if other < 0:
            n = self.denominator ** abs(other)
            d = self.numerator ** abs(other)

        else:
            n = self.numerator ** other
            d = self.denominator ** other

        return Fraction(n, d)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE :
        POST : retourne True si la fraction courante est égale à la fraction other, sinon False
        RAISE : TypeError si other n'est pas une fraction
        """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
        POST : retourne la valeur de la fraction courante en décimal
        """
        return float(self.numerator/self.denominator)


    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    def __lt__(self, other):
        """Overloading the < operator for fractions.

        PRE :
        POST : retourne True si la fraction courante est plus petite que la fonction other, sinon False
        RAISE : TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être de type fraction")
        return self.numerator * other.denominator < self.denominator * other.numerator


    def __gt__(self, other):
        """Overloading the > operator for fractions.

        PRE :
        POST : retourne True si la fonction courante est plus grande que la fonction other, sinon False
        RAISE : TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être de type fraction")
        return self.numerator * other.denominator > self.denominator * other.numerator

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE :
        POST : retourne True si la valeur de la fraction courante est 0, False sinon
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (e.g., 8/4, 3, 2/2, ...)

        PRE :
        POST : retourne True si la fraction courante représente un entier, False sinon
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :
        POST : retourne True si la valeur absolue de la fraction courante est inférieure à 1, False sinon
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :
        POST : retourne True si le numérateur est 1, False sinon
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of their difference is a unit fraction.

        PRE :
        POST : retourne True si la fraction courante et la fraction other sont adjacentes, False sinon
        RAISE : TypeError si other n'est pas une fraction
        """
        if not isinstance(other,Fraction):
            raise TypeError("other doit être de type Fraction")
        diff = self - other
        diff2 = Fraction(abs(diff.numerator), diff.denominator)
        return diff2.is_unit()


# if __name__ == "__main__":
#
#     f1 = Fraction(2, 8)
#     f2 = Fraction(1, 8)
#     print(f1.is_adjacent_to(f2))
