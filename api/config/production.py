"""Production configuration"""

from .base import Base


class Production(Base):
    """Production configuration class"""

    FRONTEND_HOST = "https://proji.daempasha.com"
