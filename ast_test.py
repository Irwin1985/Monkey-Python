import unittest
from lexer import Token, TokenType
from ast import Program, LetStatement, Identifier


class AstTest(unittest.TestCase):
    def test_string(self):
        program = Program([
            LetStatement(
                Token(TokenType.LET, "let"),
                Identifier(Token(TokenType.IDENT, "myVar"), "myVar"),
                Identifier(Token(TokenType.IDENT, "anotherVar"), "anotherVar")
            )])

        self.assertEqual(program.string(), "let myVar = anotherVar;")
