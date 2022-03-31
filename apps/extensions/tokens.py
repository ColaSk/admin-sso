# -*- encoding: utf-8 -*-

from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from config import setting


def create_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建token

    Args:
        data (dict): token data 可以包含用户信息: name create_time id
        expires_delta (Optional[timedelta], optional): 两个时间的差值. Defaults to None.

    Returns:
        str: token string
    """
    now = datetime.now()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now +  timedelta(minutes=30)

    token_dict = {
        'exp': expire,
        'iat': now,
        'data': data.copy()
    }


    return jwt.encode(
        token_dict, 
        setting.jwt.secret_key, 
        algorithm=setting.jwt.algorithm)


def verify_token(token: str) -> dict:
    """验证token

    Args:
        token (str): tokens tring

    Raises:
        e: JWTError

    Returns:
        dict: token info
    """    
    try:
        return jwt.decode(
            token, 
            setting.jwt.secret_key, 
            algorithms=[setting.jwt.algorithm]) 
    except JWTError as e:
        raise e
