import numpy as np
import pandas as pd

def fftSmoother(inputData, threshold):
    """
    Apply FFT-based smoothing to the input data.

    Parameters:
    - inputData: list, numpy array, or pandas series
        The input data to be smoothed.
    - threshold: float
        The threshold for filtering out high-frequency components in the FFT.
        Should be in the range (0, 1).

    Returns:
    - inputData_reconstructed: numpy array
        The smoothed/reconstructed input data.
    """
    if not isinstance(inputData, (list, np.ndarray, pd.Series)):
        raise TypeError("Input data must be a list, numpy array, or pandas series.")
    if not 0 < threshold < 1:
        raise ValueError("Threshold should be in the range (0, 1).")
    
    fft_result = np.fft.fft(inputData)
    frequencies = np.fft.fftfreq(fft_result)
    fft_result_filtered = fft_result.copy()
    fft_result_filtered[np.abs(frequencies) > threshold] = 0
    inputData_reconstructed = np.real(np.fft.ifft(fft_result_filtered))
    return inputData_reconstructed

