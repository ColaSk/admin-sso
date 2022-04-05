from passlib.context import CryptContext


def hash(secret, scheme=None, category=None, **kwds):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(
        secret, scheme, category, **kwds
    )


def verify(secret, hash, scheme=None, category=None, **kwds):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
        secret, hash, scheme, category, **kwds
    )
