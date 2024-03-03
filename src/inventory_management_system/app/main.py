import uvicorn

from fastapi import FastAPI
from inventory_management_system.app.routers.main_router import api_router
from inventory_management_system.app.settings.config import Config, load_config

config: Config = load_config()

app = FastAPI(
    title=f"{config.app_config.app_name} API",
    openapi_url="/openapi.json",
)

app.include_router(api_router)

if __name__ == "__main__":
    port = int(config.app_config.app_port)

    if config.app_config.debug:
        uvicorn.run(
            "inventory_management_system.app.main:app",
            host="0.0.0.0",
            port=port,
            reload=True,
        )
    else:
        uvicorn.run(app, host="0.0.0.0", port=port)
