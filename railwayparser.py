from pegparsing import BaseParser, memoise, memoise_left_recursive

from railwayparsergenerator import (
    Token, ThreadID, NumThreads, Lookup, Length, Uniop, Binop, ArrayLiteral,
    ArrayTensor, ArrayRange, Let
)

class RailwayParser(BaseParser):

    @memoise
    def rule_let_stmt(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('let')) is not None)
            and ((t1 := self.rule_name()) is not None)
            and ((t2 := self.expect('=')) is not None)
            and ((t3 := self.rule_expression()) is not None)
        ):
            return Let(t1, t3)
        self.reset(pos)

        return None

    @memoise_left_recursive
    def rule_expression(self):
        pos = self.mark()
        if (True
            and ((t0 := self.rule_expression()) is not None)
            and ((t1 := self.expect('+')) is not None)
            and ((t2 := self.rule_expr_()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expression()) is not None)
            and ((t1 := self.expect('-')) is not None)
            and ((t2 := self.rule_expr_()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expr_()) is not None)
        ):
            return t0
        self.reset(pos)

        return None

    @memoise_left_recursive
    def rule_expr_(self):
        pos = self.mark()
        if (True
            and ((t0 := self.rule_expr_()) is not None)
            and ((t1 := self.expect('*')) is not None)
            and ((t2 := self.rule_expr__()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expr_()) is not None)
            and ((t1 := self.expect('/')) is not None)
            and ((t2 := self.rule_expr__()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expr_()) is not None)
            and ((t1 := self.expect('//')) is not None)
            and ((t2 := self.rule_expr__()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expr_()) is not None)
            and ((t1 := self.expect('%')) is not None)
            and ((t2 := self.rule_expr__()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_expr__()) is not None)
        ):
            return t0
        self.reset(pos)

        return None

    @memoise_left_recursive
    def rule_expr__(self):
        pos = self.mark()
        if (True
            and ((t0 := self.rule_expr__()) is not None)
            and ((t1 := self.expect('**')) is not None)
            and ((t2 := self.rule_atom()) is not None)
        ):
            return Binop(t0, t1, t2)
        self.reset(pos)

        if (True
            and ((t0 := self.rule_atom()) is not None)
        ):
            return t0
        self.reset(pos)

        return None

    @memoise
    def rule_atom(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('(')) is not None)
            and ((t1 := self.rule_expression()) is not None)
            and ((t2 := self.expect(')')) is not None)
        ):
            return t1
        self.reset(pos)

        if (True
            and ((t0 := self.rule_array_literal()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.rule_array_tensor()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.rule_array_range()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.rule_lookup()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.expect('NUMBER')) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.rule_threadid()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.rule_numthreads()) is not None)
        ):
            return t0
        self.reset(pos)

        if (True
            and ((t0 := self.expect('-')) is not None)
            and ((t1 := self.rule_atom()) is not None)
        ):
            return Uniop(t0, t1)
        self.reset(pos)

        if (True
            and ((t0 := self.expect('!')) is not None)
            and ((t1 := self.rule_atom()) is not None)
        ):
            return Uniop(t0, t1)
        self.reset(pos)

        if (True
            and ((t0 := self.expect('#')) is not None)
            and ((t1 := self.rule_lookup()) is not None)
        ):
            return Length(t1)
        self.reset(pos)

        return None

    @memoise
    def rule_subrule_5(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect(',')) is not None)
            and ((t1 := self.rule_expression()) is not None)
        ):
            return t1
        self.reset(pos)

        return None

    def repeat_subrule_5(self):
        result = []
        while (item := self.rule_subrule_5()) is not None:
            result.append(item)
        return result

    @memoise
    def rule_array_literal(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('[')) is not None)
            and ((t1 := self.expect(']')) is not None)
        ):
            return ArrayLiteral([])
        self.reset(pos)

        if (True
            and ((t0 := self.expect('[')) is not None)
            and ((t1 := self.rule_expression()) is not None)
            and ((t2 := self.repeat_subrule_5()) is not None)
            and ((t3 := self.expect(']')) is not None)
        ):
            return ArrayLiteral([t1] + t2)
        self.reset(pos)

        return None

    @memoise
    def rule_subrule_8(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('by')) is not None)
            and ((t1 := self.rule_expression()) is not None)
        ):
            return t1
        self.reset(pos)

        return None

    @memoise
    def rule_array_range(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('[')) is not None)
            and ((t1 := self.rule_expression()) is not None)
            and ((t2 := self.expect('to')) is not None)
            and ((t3 := self.rule_expression()) is not None)
            and (((t4 := self.rule_subrule_8()) is not None) or True)
            and ((t5 := self.expect(']')) is not None)
        ):
            return ArrayRange(t1, t3, t4)
        self.reset(pos)

        return None

    @memoise
    def rule_array_tensor(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('[')) is not None)
            and ((t1 := self.rule_expression()) is not None)
            and ((t2 := self.expect('tensor')) is not None)
            and ((t3 := self.rule_expression()) is not None)
            and ((t4 := self.expect(']')) is not None)
        ):
            return ArrayTensor(t1, t3)
        self.reset(pos)

        return None

    @memoise
    def rule_subrule_11(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('[')) is not None)
            and ((t1 := self.rule_expression()) is not None)
            and ((t2 := self.expect(']')) is not None)
        ):
            return t1
        self.reset(pos)

        return None

    def repeat_subrule_11(self):
        result = []
        while (item := self.rule_subrule_11()) is not None:
            result.append(item)
        return result

    @memoise
    def rule_lookup(self):
        pos = self.mark()
        if (True
            and ((t0 := self.rule_name()) is not None)
            and ((t1 := self.repeat_subrule_11()) is not None)
        ):
            return Lookup(name=t0, index=tuple(t1))
        self.reset(pos)

        return None

    @memoise
    def rule_threadid(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('TID')) is not None)
        ):
            return ThreadID()
        self.reset(pos)

        return None

    @memoise
    def rule_numthreads(self):
        pos = self.mark()
        if (True
            and ((t0 := self.expect('#TID')) is not None)
        ):
            return NumThreads()
        self.reset(pos)

        return None

    @memoise
    def rule_name(self):
        pos = self.mark()
        if (True
            and (((t0 := self.expect('.')) is not None) or True)
            and ((t1 := self.expect('NAME')) is not None)
        ):
            return ('.' if t0 is not None else '') + t1.string
        self.reset(pos)

        return None