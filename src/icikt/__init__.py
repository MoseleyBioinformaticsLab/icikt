__version__ = "1.2.0"

try:
        from . import _kendall_dis
except ImportError:
        from . import kendall_dis as _kendall_dis
from .methods import icikt
from .methods import iciktArray


