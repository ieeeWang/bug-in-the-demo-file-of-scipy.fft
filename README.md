# bug-in-the-demo-file-of-scipy.fft
This demo code of scipy.fft has a small bug

## Quick demo
The following code include A demo of scipy.fft, from:
    https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html#d-discrete-fourier-transforms
    But, This demo of scipy has a small bug: f-axis miss the median point of the symmetrical spectrum,
    so that it will has a very tiny shift of frequency (e.g., <0.001 Hz).
    The correct demo is shown here.
```
fft_test1.py
```

<p align="center">
    <img width="200%" src="fft_demo.png" style="max-width:200%;"></a>
</p>
