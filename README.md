# bug-in-the-demo-file-of-scipy.fft
The official demo code of scipy.fft has a small bug

## Quick demo
The file fft_test1.py used a piece of demo code for implementing FFT using scipy.fft, from the [official document](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html#d-discrete-fourier-transforms).
    But this demo has a small bug: the f-axis (of FT) missed the median point of the symmetrical FT spectrum,
    so that it will not excatly sync to corresponding frequncy, thus yielding a very tiny frequency shift (e.g., ~1/fs Hz) as shown in the plot below.
    The corrected demo code is also included in:
```
fft_test1.py
```

<p align="center">
    <img width="200%" src="fft_demo.png" style="max-width:200%;"></a>
</p>
