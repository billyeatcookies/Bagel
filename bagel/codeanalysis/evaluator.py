from .syntax.binary_expression_syntax import BinaryExpressionSyntax
from .syntax.expression_syntax import ExpressionSyntax
from .syntax.literal_expression_syntax import LiteralExpressionSyntax
from .syntax.parenthesized_expression_syntax import \
    ParenthesizedExpressionSyntax
from .syntax.syntaxkind import SyntaxKind
from .syntax.unary_expression_syntax import UnaryExpressionSyntax


class Evaluator:
    def __init__(self, root: ExpressionSyntax):
        self._root = root

    def evaluate(self) -> int:
        return self.evaluate_expression(self._root)

    def evaluate_expression(self, node: ExpressionSyntax) -> int:
        if isinstance(node, LiteralExpressionSyntax):
            return int(node.literal_token.value)

        if isinstance(node, UnaryExpressionSyntax):
            operand = self.evaluate_expression(node.operand)
            
            if node.operator_token.kind == SyntaxKind.PLUSTOKEN:
                return operand
            if node.operator_token.kind == SyntaxKind.MINUSTOKEN:
                return -operand
            
            raise Exception(f"Unexpected unary operator {node.operator_token.kind}")

        if isinstance(node, BinaryExpressionSyntax):
            left = self.evaluate_expression(node.left)
            right = self.evaluate_expression(node.right)

            if node.operator_token.kind == SyntaxKind.PLUSTOKEN:
                return left + right
            elif node.operator_token.kind == SyntaxKind.MINUSTOKEN:
                return left - right
            elif node.operator_token.kind == SyntaxKind.STARTOKEN:
                return left * right
            elif node.operator_token.kind == SyntaxKind.SLASHTOKEN:
                return left / right
            else:
                raise Exception(f"Unexpected binary operator {node.operator_token.kind}")

        if isinstance(node, ParenthesizedExpressionSyntax):
            return self.evaluate_expression(node.expression)

        raise Exception(f"Unexpected node {node.kind}")
