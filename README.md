# Solar Curve

* VapourSynth implementation of solar curve in RGB24 & RGB48 colorspace, with idea from [Easy Compare](https://greasyfork.org/en/scripts/397200-easy-compare)
* Filter function: `y = 127.9999 * sin ( A * x ^ 3 + B * x ^ 2 + C * x - π / 2) + 127.5)^2`
* Function parameters from Easy Compare. [See its plot on Google](https://www.google.com/search?q=y%3D127.999*sin(0.00000198394*x%5E3%2B0.00076183231*x%5E2%2B0.2*x-3.14159%2F2)%2B127.5&pws=0&gl=us&gws_rd=cr)
* Takes YUV clip input and returns a YUV clip
* Don't use this filter too much if you are a sensible encoder. **TRUST YOUR OWN EYES!!**

**Usage**:

```python
import solar
output = solar.solar(clip)    # conversion in RGB24
```

or

```python
import solar
output = solar.solar48(clip)  # conversion in RGB48
```

**Result**: Before | After

<img src="https://github.com/jack2game/solarcurve/raw/main/solar_0.png" width="400"> <img src="https://github.com/jack2game/solarcurve/raw/main/solar_1.png" width="400">
