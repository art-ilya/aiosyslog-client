import asyncio as aio
import socket
from datetime import datetime


async def get_fqdn(name: str = "") -> str:
    return await aio.to_thread(socket.getfqdn, name)


def datetime2rfc3339(dt: datetime, sep: str = " ") -> str:
    offset = dt.utcoffset()
    if offset is None or offset.seconds == 0:
        dt_str = dt.strftime(f"%Y-%m-%d{sep}%H:%M:%S.%f")[:-3]
        return f"{dt_str}Z"
    return dt.isoformat(sep=sep, timespec="milliseconds")
