# Solar Curve

* VapourSynth implementation of solar curve in RGB48 colorspace, as in [Easy Compare](https://greasyfork.org/en/scripts/397200-easy-compare)
* Filter function same as in Easy Compare `y = 127.9999 * sin( A * (x+5) ^ 3 + B * (x+5) ^ 2 + C * (x+5) - π / 2) + 127.5`
* Function [plot from Google](https://www.google.com/search?q=y%3D127.999*sin(0.00000198394*x%5E3%2B0.00076183231*x%5E2%2B0.2*x-3.14159%2F2)%2B127.5&pws=0&gl=us&gws_rd=cr)
* Don't use this filter too much if you are a sensible encoder. **TRUST YOUR OWN EYES!!**

Usage:

```python
import solar
output = solar.solar48(clip)
```
