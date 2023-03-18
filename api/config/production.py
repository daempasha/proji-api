"""Production configuration"""

from .base import Base


class Production(Base):
    """Production configuration class"""

    PROD_CONFIG = True
