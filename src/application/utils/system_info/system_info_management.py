import platform 
import dotenv
from pathlib import Path


class SystemInfo:


    @staticmethod
    def managing_dot_env_file() -> dict:

        about_dot_env = {}
        # Get the current directory
        about_dot_env["home"] = Path(__file__).parent.parent.parent.parent.parent

        # Use a single .env file at the project root
        env_file = about_dot_env["home"] / '.env'
        about_dot_env["path"] = env_file
        print(f".env file path: {about_dot_env['path']}")

        # If a directory exists at .env (legacy), move inner file out and remove dir
        if env_file.exists() and env_file.is_dir():
            inner = env_file / '.env'
            if inner.exists():
                target = about_dot_env["home"] / '.env'
                # copy contents from inner file to target file path
                try:
                    with inner.open('rb') as src, target.open('wb') as dst:
                        dst.write(src.read())
                    print(f"Copied inner .env file to {target}")
                except Exception:
                    print(f"Failed to copy inner .env file to {target}")
            # remove remaining files and the directory
            for child in env_file.iterdir():
                try:
                    if child.is_file():
                        child.unlink()
                    else:
                        # attempt to remove directories
                        for sub in child.iterdir():
                            if sub.is_file():
                                sub.unlink()
                        child.rmdir()
                except Exception:
                    pass
            try:
                env_file.rmdir()
            except Exception:
                pass

        # If a file exists at .env, remove it to refresh timestamp
        if about_dot_env["path"].exists() and about_dot_env["path"].is_file():
            print(f".env file already exists at: {about_dot_env['path']}. The file will be deleted and re-created to update the timestamp.")
            about_dot_env["path"].unlink()

        about_dot_env["path"].touch()  # Create the .env file if it doesn't exist


        

        return about_dot_env

    @staticmethod
    def initializing_dot_env_variables():

        dot_env_file_info = SystemInfo.managing_dot_env_file()

        # Load the .env file
        print(f"Loading .env file from: {dot_env_file_info['path']}")
        dotenv.load_dotenv(dot_env_file_info["path"])

        # Set some environment variables for demonstration
        dotenv.set_key(str(dot_env_file_info["path"]), "PROJECT_ROOT_DIRECTORY", f"{str(dot_env_file_info['home'])}")
        # Get the current system information
        system_info = platform.uname()
        dotenv.set_key(str(dot_env_file_info["path"]), "SYSTEM_INFORMATION", f"{system_info.system}")
        dotenv.set_key(str(dot_env_file_info["path"]), "NODE_INFORMATION", f"{system_info.node}")
