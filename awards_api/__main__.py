import uvicorn

from awards_api.settings import settings


def main() -> None:
    uvicorn.run(
        "awards_api.application:get_app",
        host=settings.host,
        port=settings.port,
        workers=settings.workers_count,
        reload=settings.reload,
        factory=True,
        debug=settings.debug
    )


if __name__ == "__main__":
    main()
