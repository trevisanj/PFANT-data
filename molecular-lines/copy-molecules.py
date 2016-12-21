# """
# Copies from file a to file b:
# - description
# - symbols
# - vl, v2l for all sets-of-lines
#
# Then saves file b, adds ".new"
# """
#
# import pyfant as pf
# import sys
#
# FNA = "molecules.dat"
# FNB = "moleculagrade-paula.dat"
#
#
# fa = pf.FileMolecules()
# fa.load(FNA)
#
# fb = pf.FileMolecules()
# fb.load(FNB)
#
#
# print(fa.num_lines, fb.num_lines)
#
# # assert fa.num_lines == fb.num_lines
#
# data = []
#
# if len(fa) != len(fb):
#     sys.exit("Numbers of molecules do not match: {} != {}".format(len(fa), len(fb)))
#
# for ma, mb in zip(fa, fb):
#     mb.description = ma.description
#     mb.symbols = ma.symbols
#
#     if len(ma) != len(mb):
#         print("Skipped copying (vl, v2l) because {} != {}".format(len(ma), len(mb)))
#     else:
#         for sola, solb in zip(ma, mb):
#             solb.vl = sola.vl
#             solb.v2l = sola.v2l
#
#
# fb.save_as(fb.filename+".new")