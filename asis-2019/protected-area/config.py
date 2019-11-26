import os

class Config:
    """Set Flask configuration vars from .env file."""

    # general config
    FLAG       = os.environ.get('FLAG')
    SECRET     = "s3cr3t"
    ADMIN_PASS = "b5ec168843f71c6f6c30808c78b9f55d"

    