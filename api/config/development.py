"""Development configuration"""

from .base import Base


class Development(Base):
    """Development configuration class"""

    DEBUG = True
