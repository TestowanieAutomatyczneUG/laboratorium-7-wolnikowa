class Password:
    def isPasswordValid(self, password):
        r"""
        >>> p = Password()
        >>> p.isPasswordValid("")
        False
        >>> p.isPasswordValid("Has1*")
        False
        >>> p.isPasswordValid("haslo.123")
        False
        >>> p.isPasswordValid("Haslo.")
        False
        >>> p.isPasswordValid("Haslo123")
        False
        >>> p.isPasswordValid("haslo123")
        False
        >>> p.isPasswordValid("Haslo")
        False
        >>> p.isPasswordValid("haslo.")
        False
        >>> p.isPasswordValid("Haslo.123")
        True
        """

        numbersaray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        numbers = 0

        if type(password) is not str:
            raise Exception('Wrong input type.')
        if len(password) < 8:
            return False
        if password.lower() == password:
            return False
        if password.isalnum():
            return False
        for i in range(0, len(numbersaray)):
            if password.find(numbersaray[i]) != -1:
                numbers += 1
        if numbers == 0:
            return False
        return True


import unittest


class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = Password()

    def test_Password_Exceptions_None(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, None)

    def test_Password_Exceptions_Boolean(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, True)

    def test_Password_Exceptions_int(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, 2)

    def test_Password_Exceptions_float(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, 2.5)

    def test_Password_Exceptions_array(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, [1, 2, 3])

    def test_Password_Exceptions_object(self):
        self.assertRaises(Exception, self.temp.isPasswordValid, {})

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()