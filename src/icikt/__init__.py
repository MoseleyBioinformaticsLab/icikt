__version__ = "1.2.0"

try:
        from . import _kendall_dis
except ImportError:
        from . import kendall_dis_doc as _kendall_dis
from .icikt import icikt
from .icikt import iciktArray


