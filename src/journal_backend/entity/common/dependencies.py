from typing import TYPE_CHECKING, AsyncGenerator, TypeAlias

from redis.asyncio import Connection, ConnectionPool, Redis

from journal_backend.entity.common.email_sender import EmailSender

if TYPE_CHECKING:
    ConnectionPoolT: TypeAlias = ConnectionPool[Connection]  # type:ignore
else:
    ConnectionPoolT = ConnectionPool


def get_email_sender() -> EmailSender:
    yield EmailSender()


async def get_redis_conn(
    pool: ConnectionPoolT  # type:ignore
) -> AsyncGenerator[Connection, None]:  # type:ignore
    conn = Redis.from_pool(pool)  # type:ignore
    yield conn  # type:ignore
