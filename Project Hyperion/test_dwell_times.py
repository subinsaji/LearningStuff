
import numpy as np


def non_integer_dwell_time(dwell_time_ms: float) -> float:
        dwell_time_floor_rounded = np.floor(dwell_time_ms)
        dwell_time_is_close = np.isclose(
            dwell_time_ms, dwell_time_floor_rounded, rtol=1e-3
        )
        if not dwell_time_is_close:
            raise ValueError(
                f"Dwell time of {dwell_time_ms}ms is not an integer value"
            )
        return print(dwell_time_floor_rounded, dwell_time_is_close, type(dwell_time_ms))
    
non_integer_dwell_time(150)    
