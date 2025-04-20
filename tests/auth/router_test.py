from fastapi import HTTPException
import pytest
from jose import jwt

from api.auth.router import ALGORITHM, SECRET_KEY, get_user

@pytest.mark.asyncio
async def test_get_user_with_invalid_token():
    encode = {'roles': 'user'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    
    with pytest.raises(HTTPException) as ex:
        await get_user(token)
        
    assert ex.value.status_code == 401

