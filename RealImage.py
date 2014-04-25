import os, glob, math, time
from PIL import Image, ImageDraw

def read():
    i = Image.open("test-lock.png");

    pixels = i.load() #this is not a list, nor is it list()'able
    print i.size
    width, height = i.size
    
    all_pixels = []
    for y in range(height):
        for x in range(width):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)

    print all_pixels

def generate():
    img = Image.new('RGB', (36, 29), "white") 
    myImg = []
    theData = [(186, 186, 186), (186, 186, 186), (185, 185, 185), (184, 184, 184), (183, 183, 183), (181, 181, 181), (180, 180, 180), (179, 179, 179), (179, 179, 179), (176, 176, 176), (175, 175, 175), (172, 172, 172), (161, 161, 161), (109, 109, 109), (65, 65, 65), (33, 33, 33), (12, 12, 12), (2, 2, 2), (2, 2, 2), (11, 11, 11), (30, 30, 30), (57, 57, 57), (92, 92, 92), (130, 130, 130), (135, 135, 135), (133, 133, 133), (130, 130, 130), (127, 127, 127), (121, 121, 121), (121, 121, 121), (117, 117, 117), (116, 116, 116), (114, 114, 114), (113, 113, 113), (112, 112, 112), (110, 110, 110), (180, 180, 180), (179, 179, 179), (179, 179, 179), (177, 177, 177), (176, 176, 176), (174, 174, 174), (174, 174, 174), (172, 172, 172), (172, 172, 172), (169, 169, 169), (153, 153, 153), (63, 63, 63), (7, 7, 7), (0, 0, 0), (6, 6, 6), (52, 52, 52), (96, 96, 97), (124, 124, 126), (123, 124, 126), (94, 94, 96), (50, 50, 51), (4, 5, 5), (0, 0, 0), (5, 5, 5), (49, 49, 49), (117, 117, 117), (123, 123, 123), (121, 121, 121), (117, 117, 117), (114, 114, 114), (112, 112, 112), (110, 110, 110), (109, 109, 109), (107, 107, 107), (106, 106, 106), (104, 104, 104), (173, 173, 173), (172, 172, 172), (172, 172, 172), (171, 171, 171), (170, 170, 170), (168, 168, 168), (168, 168, 168), (165, 165, 165), (167, 167, 167), (122, 122, 122), (3, 3, 3), (1, 1, 1), (71, 71, 72), (166, 167, 168), (239, 239, 241), (250, 251, 254), (249, 250, 254), (248, 250, 254), (247, 249, 254), (246, 248, 253), (245, 247, 253), (231, 233, 239), (160, 162, 167), (67, 68, 70), (0, 0, 0), (2, 2, 2), (101, 101, 101), (119, 119, 119), (110, 110, 110), (108, 108, 108), (106, 106, 106), (105, 105, 105), (103, 103, 103), (102, 102, 102), (100, 100, 100), (99, 99, 99), (165, 165, 165), (166, 166, 166), (166, 166, 166), (165, 165, 165), (164, 164, 164), (163, 163, 163), (161, 161, 161), (167, 167, 167), (49, 49, 49), (0, 0, 0), (67, 68, 68), (204, 204, 205), (252, 252, 254), (251, 252, 254), (247, 249, 253), (241, 244, 252), (234, 239, 251), (228, 234, 251), (224, 231, 250), (225, 231, 250), (228, 234, 250), (236, 240, 252), (242, 244, 252), (240, 244, 253), (193, 196, 204), (62, 63, 66), (0, 0, 0), (41, 41, 41), (119, 119, 119), (104, 104, 104), (103, 103, 103), (101, 101, 101), (100, 100, 100), (98, 98, 98), (95, 95, 95), (94, 94, 94), (159, 159, 159), (160, 160, 160), (159, 159, 159), (160, 160, 160), (158, 158, 158), (156, 156, 156), (163, 163, 163), (23, 23, 23), (11, 11, 11), (155, 155, 156), (252, 252, 254), (251, 252, 254), (246, 248, 253), (238, 242, 252), (232, 237, 251), (229, 234, 251), (225, 231, 250), (220, 228, 250), (216, 225, 249), (212, 221, 248), (207, 218, 248), (203, 214, 247), (205, 216, 247), (221, 228, 250), (237, 241, 252), (235, 239, 250), (144, 147, 154), (9, 9, 10), (19, 19, 19), (113, 113, 113), (92, 92, 92), (88, 88, 88), (85, 85, 85), (84, 84, 84), (84, 84, 84), (84, 84, 84), (153, 153, 153), (152, 152, 152), (154, 154, 154), (152, 152, 152), (151, 151, 151), (159, 159, 159), (22, 22, 22), (23, 23, 23), (204, 204, 205), (252, 253, 254), (249, 250, 253), (241, 244, 252), (235, 240, 252), (232, 237, 251), (227, 233, 249), (139, 143, 155), (51, 53, 58), (30, 31, 34), (30, 32, 36), (62, 65, 74), (153, 162, 187), (197, 210, 246), (192, 206, 245), (187, 202, 245), (191, 205, 245), (221, 229, 250), (234, 238, 252), (188, 191, 203), (20, 21, 22), (17, 17, 17), (98, 98, 98), (80, 80, 80), (80, 80, 80), (80, 80, 80), (80, 80, 80), (81, 81, 81), (145, 145, 145), (145, 145, 145), (146, 146, 146), (146, 146, 146), (149, 149, 149), (47, 47, 47), (11, 11, 11), (204, 204, 205), (252, 252, 254), (246, 248, 253), (239, 242, 252), (235, 239, 252), (231, 236, 251), (226, 232, 249), (107, 110, 119), (30, 31, 34), (29, 30, 34), (28, 30, 34), (28, 29, 34), (27, 29, 34), (28, 30, 36), (130, 139, 166), (187, 202, 245), (182, 198, 244), (177, 194, 243), (172, 190, 243), (200, 212, 247), (231, 236, 251), (185, 190, 201), (9, 9, 10), (35, 35, 35), (84, 84, 84), (78, 78, 78), (78, 78, 78), (78, 78, 78), (79, 79, 79), (140, 140, 140), (139, 139, 139), (139, 139, 139), (139, 139, 139), (110, 110, 110), (0, 0, 0), (155, 155, 156), (252, 252, 254), (246, 248, 253), (238, 242, 252), (234, 239, 252), (231, 236, 251), (227, 233, 250), (129, 133, 144), (30, 31, 34), (29, 30, 34), (56, 58, 66), (133, 141, 162), (116, 123, 143), (37, 40, 47), (26, 28, 34), (28, 30, 37), (141, 154, 190), (176, 193, 243), (171, 189, 242), (166, 185, 241), (161, 181, 241), (193, 207, 246), (228, 234, 251), (138, 142, 152), (0, 0, 0), (81, 81, 81), (74, 74, 74), (74, 74, 74), (74, 74, 74), (75, 75, 75), (132, 132, 132), (133, 133, 133), (133, 133, 133), (123, 123, 123), (2, 2, 2), (66, 66, 67), (251, 251, 253), (248, 249, 253), (238, 241, 252), (234, 238, 251), (230, 236, 251), (226, 233, 250), (194, 200, 218), (34, 35, 38), (29, 30, 34), (61, 64, 73), (196, 207, 237), (200, 212, 247), (195, 208, 246), (163, 176, 211), (33, 36, 44), (24, 27, 33), (46, 50, 63), (167, 185, 238), (165, 185, 241), (160, 181, 241), (155, 177, 240), (150, 173, 239), (207, 218, 248), (224, 231, 249), (59, 61, 66), (1, 1, 1), (72, 72, 72), (72, 72, 72), (72, 72, 72), (72, 72, 72), (125, 125, 125), (127, 127, 127), (125, 125, 125), (48, 48, 48), (0, 0, 0), (203, 204, 205), (251, 251, 253), (239, 242, 252), (233, 238, 251), (230, 235, 251), (226, 232, 250), (222, 229, 250), (102, 106, 117), (29, 30, 34), (30, 31, 35), (168, 177, 204), (199, 211, 246), (194, 207, 246), (189, 204, 245), (184, 200, 244), (111, 121, 150), (23, 26, 33), (23, 25, 33), (112, 126, 165), (159, 180, 241), (154, 176, 240), (149, 172, 239), (144, 168, 238), (153, 175, 240), (223, 230, 250), (180, 185, 200), (0, 0, 0), (26, 26, 26), (69, 69, 69), (69, 69, 69), (69, 69, 69), (119, 119, 119), (118, 118, 118), (113, 113, 113), (5, 5, 5), (70, 70, 71), (251, 252, 254), (244, 247, 253), (233, 238, 251), (229, 235, 251), (225, 232, 250), (221, 228, 250), (208, 216, 239), (37, 39, 43), (28, 30, 34), (81, 86, 99), (198, 211, 246), (194, 207, 246), (189, 203, 245), (184, 199, 244), (179, 195, 243), (169, 186, 236), (36, 40, 52), (22, 25, 33), (55, 63, 85), (153, 175, 240), (148, 171, 239), (143, 167, 238), (138, 164, 237), (133, 160, 237), (186, 201, 244), (221, 229, 250), (61, 63, 69), (3, 3, 3), (63, 63, 63), (67, 67, 67), (67, 67, 67), (111, 111, 111), (112, 112, 112), (73, 73, 73), (0, 0, 0), (165, 166, 168), (250, 251, 254), (235, 239, 252), (228, 234, 251), (225, 231, 250), (220, 228, 249), (216, 225, 249), (156, 163, 182), (28, 30, 34), (27, 29, 34), (147, 156, 183), (193, 206, 246), (188, 203, 245), (183, 199, 244), (178, 195, 243), (173, 191, 243), (168, 187, 242), (86, 97, 127), (21, 24, 33), (22, 26, 35), (138, 160, 224), (142, 167, 238), (137, 163, 237), (132, 159, 237), (127, 155, 236), (139, 165, 238), (220, 227, 249), (144, 149, 164), (0, 0, 0), (41, 41, 41), (64, 64, 64), (64, 64, 64), (105, 105, 105), (107, 107, 107), (41, 41, 41), (5, 5, 5), (236, 237, 240), (245, 247, 253), (228, 234, 251), (224, 231, 250), (220, 227, 249), (215, 224, 249), (211, 221, 248), (109, 115, 131), (27, 29, 34), (35, 37, 44), (188, 201, 240), (187, 202, 245), (182, 198, 244), (177, 194, 243), (172, 190, 242), (167, 186, 242), (162, 182, 241), (126, 143, 193), (20, 23, 33), (20, 23, 33), (105, 123, 177), (136, 162, 237), (131, 159, 236), (126, 155, 236), (121, 151, 235), (117, 147, 234), (198, 210, 246), (206, 214, 236), (4, 4, 5), (25, 25, 25), (62, 62, 62), (62, 62, 62), (99, 99, 99), (98, 98, 98), (19, 19, 19), (50, 51, 51), (248, 250, 254), (237, 241, 252), (223, 230, 250), (219, 227, 249), (215, 224, 249), (210, 220, 248), (206, 216, 247), (74, 78, 90), (26, 28, 34), (70, 75, 90), (186, 201, 244), (181, 198, 244), (176, 194, 243), (171, 190, 242), (166, 186, 242), (161, 182, 241), (156, 178, 240), (148, 171, 235), (24, 28, 41), (19, 22, 33), (78, 94, 138), (130, 158, 236), (126, 154, 236), (121, 150, 235), (116, 147, 234), (111, 143, 234), (163, 184, 241), (216, 225, 249), (44, 45, 50), (12, 12, 12), (59, 59, 59), (59, 59, 59), (92, 92, 92), (93, 93, 93), (7, 7, 7), (94, 95, 96), (247, 249, 254), (229, 235, 251), (218, 226, 249), (214, 223, 248), (209, 219, 248), (205, 216, 247), (114, 121, 140), (112, 119, 140), (109, 117, 139), (106, 114, 139), (103, 112, 138), (100, 110, 138), (97, 108, 137), (94, 105, 137), (92, 103, 137), (89, 101, 136), (86, 99, 136), (83, 96, 136), (80, 94, 135), (77, 92, 135), (74, 90, 134), (91, 112, 172), (120, 150, 235), (115, 146, 234), (111, 142, 233), (106, 139, 233), (135, 161, 237), (215, 224, 249), (81, 84, 94), (4, 4, 4), (57, 57, 57), (57, 57, 57), (86, 86, 86), (85, 85, 85), (1, 1, 1), (122, 122, 125), (246, 248, 253), (221, 228, 250), (213, 222, 248), (209, 219, 248), (204, 215, 247), (200, 212, 246), (26, 28, 34), (26, 28, 33), (25, 27, 33), (24, 27, 33), (24, 26, 33), (23, 25, 33), (22, 25, 33), (21, 24, 33), (21, 24, 33), (20, 23, 33), (19, 23, 33), (19, 22, 33), (18, 22, 32), (17, 21, 32), (17, 21, 32), (54, 68, 108), (115, 145, 234), (110, 142, 233), (105, 138, 233), (101, 135, 232), (112, 143, 234), (214, 223, 249), (105, 109, 122), (0, 0, 0), (55, 55, 55), (55, 55, 55), (82, 82, 82), (82, 82, 82), (1, 1, 1), (121, 122, 125), (245, 247, 253), (216, 225, 249), (208, 218, 248), (203, 215, 247), (199, 211, 246), (194, 207, 246), (107, 115, 139), (104, 113, 139), (101, 110, 138), (98, 108, 138), (95, 106, 137), (92, 104, 137), (89, 102, 136), (87, 99, 136), (84, 97, 136), (81, 95, 135), (78, 93, 135), (75, 90, 135), (72, 88, 134), (69, 86, 133), (67, 84, 133), (82, 105, 171), (109, 141, 233), (105, 138, 233), (100, 134, 232), (96, 131, 231), (108, 140, 233), (213, 222, 249), (104, 109, 122), (0, 0, 0), (54, 54, 54), (54, 54, 54), (78, 78, 78), (77, 77, 77), (5, 5, 5), (93, 94, 96), (244, 246, 253), (217, 225, 249), (203, 214, 247), (198, 211, 246), (193, 207, 245), (188, 203, 245), (24, 26, 33), (23, 26, 33), (23, 25, 33), (22, 25, 33), (21, 24, 33), (20, 24, 33), (51, 60, 84), (142, 167, 238), (137, 163, 237), (32, 39, 58), (17, 21, 32), (16, 20, 32), (16, 20, 32), (15, 19, 32), (14, 19, 32), (47, 62, 107), (104, 137, 232), (100, 134, 232), (96, 131, 231), (92, 128, 231), (124, 152, 235), (212, 221, 248), (80, 83, 94), (4, 4, 4), (53, 53, 53), (53, 53, 53), (68, 68, 68), (56, 56, 56), (11, 11, 11), (49, 50, 51), (242, 245, 253), (222, 229, 250), (197, 210, 246), (193, 206, 245), (188, 202, 245), (183, 199, 244), (98, 108, 138), (95, 106, 137), (92, 104, 137), (89, 101, 136), (86, 99, 136), (84, 97, 136), (95, 113, 161), (136, 162, 237), (131, 158, 236), (79, 96, 147), (69, 86, 133), (67, 84, 133), (64, 82, 133), (61, 80, 132), (59, 78, 132), (72, 97, 169), (99, 133, 232), (95, 130, 231), (91, 127, 230), (87, 124, 230), (149, 172, 239), (211, 220, 248), (42, 44, 50), (10, 10, 10), (52, 52, 52), (52, 52, 52), (53, 53, 53), (52, 52, 52), (20, 20, 20), (4, 4, 5), (228, 231, 239), (231, 236, 251), (192, 206, 245), (187, 202, 245), (182, 198, 244), (177, 194, 243), (22, 25, 33), (22, 25, 33), (21, 24, 33), (20, 23, 33), (19, 23, 33), (19, 22, 33), (47, 56, 84), (130, 158, 236), (125, 154, 236), (29, 37, 57), (15, 20, 32), (15, 19, 32), (14, 19, 32), (14, 18, 32), (13, 18, 32), (42, 59, 106), (94, 130, 231), (90, 127, 230), (86, 124, 230), (83, 121, 229), (185, 200, 244), (198, 208, 235), (4, 4, 5), (19, 19, 19), (50, 50, 50), (50, 50, 50), (51, 51, 51), (51, 51, 51), (33, 33, 33), (0, 0, 0), (157, 159, 166), (238, 242, 252), (195, 208, 246), (181, 197, 244), (176, 193, 243), (171, 189, 242), (90, 102, 136), (87, 100, 136), (84, 98, 136), (81, 95, 135), (78, 93, 135), (76, 91, 135), (87, 106, 160), (125, 153, 235), (120, 150, 235), (71, 90, 145), (62, 80, 132), (59, 78, 132), (57, 76, 132), (55, 74, 131), (52, 73, 131), (64, 91, 168), (90, 126, 230), (86, 123, 230), (82, 120, 229), (101, 135, 232), (209, 219, 247), (137, 144, 163), (0, 0, 0), (32, 32, 32), (49, 49, 49), (49, 49, 49), (52, 52, 52), (51, 51, 51), (48, 48, 48), (2, 2, 2), (66, 67, 70), (237, 241, 252), (214, 223, 248), (175, 193, 243), (170, 189, 242), (165, 185, 241), (21, 24, 33), (20, 23, 33), (19, 23, 33), (19, 22, 33), (18, 22, 32), (17, 21, 32), (17, 21, 32), (16, 20, 32), (15, 20, 32), (15, 19, 32), (14, 19, 32), (13, 18, 32), (13, 18, 32), (12, 17, 32), (12, 17, 32), (39, 56, 106), (85, 123, 230), (82, 120, 229), (78, 117, 229), (158, 179, 240), (209, 219, 248), (58, 61, 69), (2, 2, 2), (47, 47, 47), (49, 49, 49), (49, 49, 49), (51, 51, 51), (51, 51, 51), (50, 50, 50), (19, 19, 19), (0, 0, 0), (190, 192, 202), (233, 238, 251), (180, 196, 244), (164, 184, 241), (159, 180, 241), (20, 23, 33), (19, 23, 33), (18, 22, 33), (18, 22, 32), (17, 21, 32), (16, 20, 32), (16, 20, 32), (15, 19, 32), (15, 19, 32), (14, 19, 32), (13, 18, 32), (13, 18, 32), (12, 17, 32), (12, 17, 32), (11, 16, 31), (37, 54, 105), (81, 120, 229), (78, 117, 229), (97, 132, 231), (206, 217, 247), (167, 176, 199), (0, 0, 0), (18, 18, 18), (48, 48, 48), (48, 48, 48), (48, 48, 48), (50, 50, 50), (50, 50, 50), (50, 50, 50), (52, 52, 52), (1, 1, 1), (61, 63, 66), (232, 236, 250), (215, 224, 249), (159, 180, 240), (153, 176, 240), (142, 167, 238), (137, 163, 237), (132, 159, 237), (127, 155, 236), (122, 152, 235), (118, 148, 234), (113, 144, 234), (108, 141, 233), (104, 137, 232), (100, 134, 232), (95, 130, 231), (91, 127, 230), (87, 124, 230), (84, 121, 229), (80, 119, 229), (77, 116, 228), (77, 117, 229), (76, 115, 228), (176, 193, 243), (207, 217, 246), (54, 57, 65), (1, 1, 1), (51, 51, 51), (48, 48, 48), (48, 48, 48), (48, 48, 48), (50, 50, 50), (50, 50, 50), (50, 50, 50), (49, 49, 49), (70, 70, 70), (0, 0, 0), (141, 144, 153), (230, 235, 251), (192, 206, 245), (147, 171, 239), (142, 167, 238), (137, 163, 237), (132, 159, 237), (127, 155, 236), (122, 152, 235), (118, 148, 234), (113, 144, 234), (108, 141, 233), (104, 137, 232), (100, 134, 232), (95, 130, 231), (91, 127, 230), (87, 124, 230), (84, 121, 229), (80, 119, 229), (77, 116, 228), (74, 114, 228), (142, 167, 238), (208, 218, 248), (126, 132, 150), (0, 0, 0), (69, 69, 69), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (56, 56, 56), (31, 31, 31), (9, 9, 10), (184, 189, 201), (227, 233, 250), (185, 200, 244), (137, 163, 237), (132, 159, 236), (126, 155, 236), (122, 151, 235), (117, 147, 234), (112, 144, 234), (108, 140, 233), (103, 137, 232), (99, 133, 232), (95, 130, 231), (91, 127, 230), (87, 124, 230), (83, 121, 229), (80, 118, 229), (76, 116, 228), (75, 114, 228), (142, 167, 238), (207, 217, 247), (167, 175, 199), (8, 8, 10), (31, 31, 31), (55, 55, 55), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (71, 71, 71), (14, 14, 14), (20, 20, 22), (182, 187, 201), (225, 231, 250), (201, 213, 246), (142, 167, 238), (121, 151, 235), (116, 147, 234), (112, 143, 234), (107, 140, 233), (103, 136, 232), (98, 133, 232), (94, 129, 231), (90, 126, 230), (86, 123, 230), (83, 121, 229), (79, 118, 229), (76, 115, 228), (95, 130, 231), (176, 193, 243), (208, 218, 248), (167, 175, 199), (18, 19, 22), (14, 14, 14), (71, 71, 71), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (49, 49, 49), (76, 76, 76), (14, 14, 14), (9, 9, 10), (136, 140, 152), (221, 228, 248), (219, 227, 249), (180, 196, 244), (129, 157, 236), (106, 139, 233), (102, 136, 232), (98, 132, 231), (94, 129, 231), (89, 126, 230), (86, 123, 230), (82, 120, 229), (79, 117, 229), (98, 133, 232), (156, 178, 240), (206, 217, 247), (206, 217, 246), (126, 132, 150), (8, 8, 10), (14, 14, 14), (75, 75, 75), (49, 49, 49), (49, 49, 49), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (51, 51, 51), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50), (49, 49, 49), (71, 71, 71), (31, 31, 31), (0, 0, 0), (58, 60, 66), (177, 183, 200), (218, 226, 249), (217, 225, 249), (193, 207, 245), (157, 179, 240), (128, 156, 236), (105, 138, 233), (101, 135, 232), (119, 149, 234), (146, 170, 238), (183, 199, 244), (209, 219, 247), (208, 218, 248), (167, 175, 199), (54, 57, 65), (0, 0, 0), (31, 31, 31), (71, 71, 71), (49, 49, 49), (49, 49, 49), (49, 49, 49), (49, 49, 49), (48, 48, 48), (48, 48, 48), (48, 48, 48)]
    for i in theData:
        myImg.append(i)
        img.putdata(myImg)
        img.save('test-generated.png')

start = time.clock()
read()
end = time.clock()

print "#\n#Generating 36x29 icon took " + str(end-start) + " seconds."
