
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSAND COMP_DIFF COMP_EQ COMP_EQ_GR COMP_EQ_LE COMP_GR COMP_LE DIVIDE EQUAL LPAREN MINUS NAME NUMBER OR PLUS RPAREN SEMICOLON TIMESblock : block statement\n             | statementstatement : expression SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQUAL expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEstatement : NAME EQUAL expression SEMICOLONempty :statement : expression COMP_EQ expression\n                 | expression COMP_LE expression\n                 | expression COMP_GR expression\n                 | expression COMP_DIFF expression\n                 | expression COMP_EQ_GR expression\n                 | expression COMP_EQ_LE expression '
    
_lr_action_items = {'NAME':([0,1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,],[4,4,-2,23,23,-11,-1,-3,23,23,23,23,23,23,23,23,23,23,23,23,-9,-12,-15,-16,-17,-18,-19,-20,-4,-5,-6,-7,-8,-10,-13,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[5,5,-2,17,-12,5,5,-11,-1,-3,5,5,5,5,5,5,5,5,5,5,5,5,-9,-12,17,17,17,17,17,17,17,-4,-5,-6,-7,17,17,-10,-13,]),'LPAREN':([0,1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,],[6,6,-2,6,6,-11,-1,-3,6,6,6,6,6,6,6,6,6,6,6,6,-9,-12,-15,-16,-17,-18,-19,-20,-4,-5,-6,-7,-8,-10,-13,]),'NUMBER':([0,1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,],[7,7,-2,7,7,-11,-1,-3,7,7,7,7,7,7,7,7,7,7,7,7,-9,-12,-15,-16,-17,-18,-19,-20,-4,-5,-6,-7,-8,-10,-13,]),'$end':([1,2,7,8,9,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,],[0,-2,-11,-1,-3,-9,-12,-15,-16,-17,-18,-19,-20,-4,-5,-6,-7,-8,-10,-13,]),'SEMICOLON':([3,4,7,22,23,31,32,33,34,35,36,37,],[9,-12,-11,-9,-12,-4,-5,-6,-7,-8,38,-10,]),'COMP_EQ':([3,4,7,22,23,31,32,33,34,35,37,],[10,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'COMP_LE':([3,4,7,22,23,31,32,33,34,35,37,],[11,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'COMP_GR':([3,4,7,22,23,31,32,33,34,35,37,],[12,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'COMP_DIFF':([3,4,7,22,23,31,32,33,34,35,37,],[13,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'COMP_EQ_GR':([3,4,7,22,23,31,32,33,34,35,37,],[14,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'COMP_EQ_LE':([3,4,7,22,23,31,32,33,34,35,37,],[15,-12,-11,-9,-12,-4,-5,-6,-7,-8,-10,]),'PLUS':([3,4,7,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[16,-12,-11,-9,-12,16,16,16,16,16,16,16,-4,-5,-6,-7,16,16,-10,]),'TIMES':([3,4,7,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[18,-12,-11,-9,-12,18,18,18,18,18,18,18,18,18,-6,-7,18,18,-10,]),'DIVIDE':([3,4,7,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[19,-12,-11,-9,-12,19,19,19,19,19,19,19,19,19,-6,-7,19,19,-10,]),'EQUAL':([3,4,7,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[20,21,-11,-9,-12,20,20,20,20,20,20,20,-4,-5,-6,-7,20,20,-10,]),'RPAREN':([7,22,23,24,31,32,33,34,35,37,],[-11,-9,-12,37,-4,-5,-6,-7,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,],[1,]),'statement':([0,1,],[2,8,]),'expression':([0,1,5,6,10,11,12,13,14,15,16,17,18,19,20,21,],[3,3,22,24,25,26,27,28,29,30,31,32,33,34,35,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> block statement','block',2,'p_bloc','calc1.py',60),
  ('block -> statement','block',1,'p_bloc','calc1.py',61),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','calc1.py',74),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calc1.py',79),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calc1.py',80),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calc1.py',81),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calc1.py',82),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','calc1.py',83),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calc1.py',93),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calc1.py',97),
  ('expression -> NUMBER','expression',1,'p_expression_number','calc1.py',101),
  ('expression -> NAME','expression',1,'p_expression_name','calc1.py',105),
  ('statement -> NAME EQUAL expression SEMICOLON','statement',4,'p_expression_affect','calc1.py',109),
  ('empty -> <empty>','empty',0,'p_empty','calc1.py',115),
  ('statement -> expression COMP_EQ expression','statement',3,'p_expression_comp','calc1.py',119),
  ('statement -> expression COMP_LE expression','statement',3,'p_expression_comp','calc1.py',120),
  ('statement -> expression COMP_GR expression','statement',3,'p_expression_comp','calc1.py',121),
  ('statement -> expression COMP_DIFF expression','statement',3,'p_expression_comp','calc1.py',122),
  ('statement -> expression COMP_EQ_GR expression','statement',3,'p_expression_comp','calc1.py',123),
  ('statement -> expression COMP_EQ_LE expression','statement',3,'p_expression_comp','calc1.py',124),
]
