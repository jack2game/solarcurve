import vapoursynth as vs
from vapoursynth import core
import math

t = 5
k = 5.5
m = (k * math.pi - 128 / t)
A = -1 / 4194304 * m
B = 3 / 32768 * m
C = 1 / t

def solar(clip):
    if clip.format is None:
        raise vs.Error("Tweak: only clips with constant format are accepted.")

    if clip.format.color_family == vs.RGB:
        raise vs.Error("Tweak: RGB clips are not accepted.")
    
    output = core.resize.Spline36(clip=clip, format=vs.RGB24, matrix_in_s="709")
    output = core.std.Lut(clip=output, planes=[0], function=solar24r)
    output = core.std.Lut(clip=output, planes=[1], function=solar24g)
    output = core.std.Lut(clip=output, planes=[2], function=solar24b)
    return core.resize.Spline36(clip=output, format=clip.format, matrix_s="709")

def solar48(clip):
    if clip.format is None:
        raise vs.Error("Tweak: only clips with constant format are accepted.")

    if clip.format.color_family == vs.RGB:
        raise vs.Error("Tweak: RGB clips are not accepted.")
    
    output = core.resize.Spline36(clip=clip, format=vs.RGB48, matrix_in_s="709")
    output = core.std.Lut(clip=output, planes=[0], function=solar48r)
    output = core.std.Lut(clip=output, planes=[1], function=solar48g)
    output = core.std.Lut(clip=output, planes=[2], function=solar48b)
    return core.resize.Spline36(clip=output, format=clip.format, matrix_s="709")

def solar24r(x):
   return round(127.9999 * math.sin(A * (x) ** 3 + B * (x) ** 2 + C * (x) - math.pi / 2) + 127.5)
def solar24g(x):
   return round(127.9999 * math.sin(A * (x-5) ** 3 + B * (x-5) ** 2 + C * (x-5) - math.pi / 2) + 127.5)
def solar24b(x):
   return round(127.9999 * math.sin(A * (x+5) ** 3 + B * (x+5) ** 2 + C * (x+5) - math.pi / 2) + 127.5)
def solar48r(x):
   return round((127.9999 * math.sin(A * (x/65535*255) ** 3 + B * ((x/65535*255)) ** 2 + C * ((x/65535*255)) - math.pi / 2) + 127.5)**2)
def solar48g(x):
   return round((127.9999 * math.sin(A * ((x/65535*255)-5) ** 3 + B * ((x/65535*255)-5) ** 2 + C * ((x/65535*255)-5) - math.pi / 2) + 127.5)**2)
def solar48b(x):
   return round((127.9999 * math.sin(A * ((x/65535*255)+5) ** 3 + B * ((x/65535*255)+5) ** 2 + C * ((x/65535*255)+5) - math.pi / 2) + 127.5)**2)