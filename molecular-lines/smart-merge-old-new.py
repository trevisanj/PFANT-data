# """
# I created this script to replace molecules in molecules.dat from
# mghc2cnr_cn3ch13chtiog3tio.dat,
# because the data in the latter seems to be more complete than in the former,
# in a number of senses:
#   - wavelengths more precise
#   - most molecules have more lines
#
# However, the script is not taking action yet, just reporting some findings.
#
# TODO To be continued...
# """
#
# from pyfant import *
# from collections import OrderedDict
#
# def list_file(f):
#     n = len(f.titm)
#     print "\n"+"*"*n
#     print f.titm
#     print "*" * n
#     for i, m in enumerate(f.molecules):
#         print "%2d %6d %s" % (i, m.num_lines, m.titulo)
#
# def match_files(fsrc, fdest):
#     """Creates a dictionary to indicate which molecular lines from fsrc should be copied into which from fdest"""
#     nn = [m.num_lines for m in fdest.molecules]
#
#     ret = OrderedDict()
#     for i, m in enumerate(fsrc.molecules):
#         n = m.num_lines
#         for j, n_dest in enumerate(nn):
#             if n == n_dest:
#                 ret[i] = j
#     return ret
#
#
# fb = FileMolecules()
# fb.load("mghc2cnr_cn3ch13chtiog3tio.dat")
#
# fg = FileMolecules()
# fg.load("molecules.dat")
#
# list_file(fb)
# list_file(fg)
#
# map = match_files(fb, fg)
#
# print map