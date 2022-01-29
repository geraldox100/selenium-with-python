from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="APP",
    env_switcher="APP",
    load_dotenv=True,
    environments=True,
)

ENV = settings.get('ENV', None)
REMOTE_BROWSER_URL = settings.get('REMOTE_BROWSER_URL', None)
DRIVER_DIR = settings.get('DRIVER_DIR', None)