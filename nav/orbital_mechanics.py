"""Basic orbital mechanics helpers (Keplerian elements)."""
import math

MU_EARTH = 3.986004418e14  # m^3/s^2
RE = 6_371_000  # mean Earth radius, metres

def semi_major_axis(r_perigee: float, r_apogee: float) -> float:
    """Return semi-major axis in metres given perigee and apogee radii."""
    if r_perigee <= 0 or r_apogee <= 0:
        raise ValueError("Radii must be positive")
    return (r_perigee + r_apogee) / 2.0

def orbital_period(a: float) -> float:
    """Orbital period in seconds for a given semi-major axis (m)."""
    return 2 * math.pi * math.sqrt(a**3 / MU_EARTH)

def vis_viva(r: float, a: float) -> float:
    """Velocity at radius r on an orbit with semi-major axis a."""
    return math.sqrt(MU_EARTH * (2 / r - 1 / a))

def altitude(r: float) -> float:
    """Convert geocentric radius to altitude above mean sea level."""
    return r - RE
