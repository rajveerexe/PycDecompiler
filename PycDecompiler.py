import os
import sys
import time
import shutil
import subprocess
import marshal
import base64
import zlib
import requests
from typing import Optional


class FileNotPyc(Exception):
    pass


class DecompilationError(Exception):
    pass


def remove_dir(path: str):
    try:
        shutil.rmtree(path)
    except Exception:
        pass


def get_python_executable():
    try:
        return __cpy_syspath__ + "\\python.exe"
    except NameError:
        return sys.executable


def get_current_python_version():
    """Get current Python version as X.Y format"""
    return ".".join(sys.version.split()[0].split(".")[:-1])


magic_map = {
    "3.6": b"3\r\r\n\x8bq\x98d\x0c\x00\x00\x00\xe3\x00\x00\x00",
    "3.7": b"B\r\r\n\x00\x00\x00\x00\x8bq\x98d\x0c\x00\x00\x00",
    "3.8": b"U\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.9": b"a\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.10": b"o\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.11": b"\xa7\r\r\n\x00\x00\x00\x004\x0eAi\n\x00\x00\x00",
    "3.12": b"\xcb\r\r\n\x00\x00\x00\x00{\x0eAi\n\x00\x00\x00",
    "3.13": b"\xf3\r\r\n\x00\x00\x00\x00\x90\x0eAi\n\x00\x00\x00",
    "3.14": b"+\x0e\r\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
    # magic number reference.
    # https://github.com/python/cpython/blob/main/Include/internal/pycore_magic_number.h
}


def get_pyc_magic(pyver: str) -> bytes:
    return magic_map.get(pyver, magic_map[get_current_python_version()])


def print_banner():
    text = f"{'=' * 55}\n    ____        __    _                         __\n   / __ \\__  __/ /   (_)___  ____ ___  ______ _/ /\n  / /_/ / / / / /   / / __ \\/ __ `/ / / / __ `/ /\n / ____/ /_/ / /___/ / / / / /_/ / /_/ / /_/ / /\n/_/    \\__, /_____/_/_/ /_/\\__, /\\__,_/\\__,_/_/\n      /____/              /____/\n{'=' * 55}\n{'P Y L I N G U A L'.center(55)}\n{'=' * 55}\n[ + ] Program:\n    -> Marshal/PYC Converter & Decompiler\n    \n[ * ] Features:\n    -> Convert Marshal to PYC (Python 3.6-3.13)\n    -> Decompile PYC to Python Source\n    \n[ </> ] Developer:\n    -> Github   : @rajveerexe\n    -> Telegram : @SoukPy\n{'=' * 55}"
    print(text)


def marshal_to_pyc(input_file: str, pyver: str = None) -> str:
    """Convert marshal file to PYC"""
    if pyver is None:
        pyver = get_current_python_version()
    print(f"\n[ * ] Converting Marshal to PYC (Python {pyver})...")
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        base_path = os.path.dirname(input_file)
        if base_path:
            base_path += os.sep
        filename = os.path.basename(input_file)
        name_only = ".".join(filename.split(".")[:-1])
        remove_dir("__pycache__")
        hook_code = '\nimport marshal, sys\n\ndef loads(data, *_):\n    open("temp_marshal.pyc", "wb").write(data)\n    sys.exit(0)\n'
        hook_payload = marshal.dumps(compile(hook_code, "<marshal_hook>", "exec"))
        encoded = base64.b64encode(zlib.compress(hook_payload))[::-1]
        with open("marshal_hook.py", "w") as f:
            f.write(
                f"import base64, zlib, marshal\nexec(marshal.loads(zlib.decompress(base64.b64decode({encoded}[::-1]))), globals())"
            )
        exec_code = (
            b"\nimport marshal_hook, sys\nsys.modules['marshal'] = marshal_hook\n"
            + data
        )
        exec_payload = marshal.dumps(compile(exec_code, "<exec>", "exec"))
        encoded_exec = base64.b64encode(zlib.compress(exec_payload))[::-1]
        with open("runner.py", "w") as f:
            f.write(
                f"import base64, zlib, marshal\nexec(marshal.loads(zlib.decompress(base64.b64decode({encoded_exec}[::-1]))), globals())"
            )
        subprocess.run(
            [get_python_executable(), "runner.py"],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        os.remove("marshal_hook.py")
        os.remove("runner.py")
        try:
            with open("temp_marshal.pyc", "rb") as f:
                marshal_data = f.read()
            os.remove("temp_marshal.pyc")
            pyc_path = f"{base_path}{name_only}.pyc"
            with open(pyc_path, "wb") as f:
                f.write(get_pyc_magic(pyver) + marshal_data)
            print(f"[ ✓ ] Saved: {pyc_path}")
            remove_dir("__pycache__")
            return pyc_path
        except FileNotFoundError:
            print("[ ! ] Not a valid marshal file")
            remove_dir("__pycache__")
            return None
    except Exception as e:
        print(f"[ ! ] Error: {e}")
        remove_dir("__pycache__")
        return None


def validate_pyc_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not file_path.endswith(".pyc"):
        raise FileNotPyc(f"File must have .pyc extension: {file_path}")


def upload_pyc_file(file_path: str) -> str:
    headers = {
        "accept": "*/*",
        "origin": "https://pylingual.io",
        "referer": "https://pylingual.io/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10) Chrome/139 Mobile",
    }
    with open(file_path, "rb") as f:
        files = {
            "file": ("script.pyc", f, "application/x-python-code"),
            "fileName": (None, "script.pyc"),
        }
        try:
            response = requests.post(
                "https://api.pylingual.io/upload",
                headers=headers,
                files=files,
                timeout=30,
            )
        except requests.RequestException as e:
            raise DecompilationError(f"Upload failed: {e}")
    if response.status_code == 502:
        raise DecompilationError("Service temporarily unavailable (502)")
    if response.status_code != 200:
        raise DecompilationError(
            f"Upload failed with status code: {response.status_code}"
        )
    try:
        resp_json = response.json()
    except ValueError:
        raise DecompilationError("Invalid JSON response from server")
    identifier = resp_json.get("identifier")
    if not identifier:
        raise DecompilationError("No identifier in response")
    return identifier


def wait_for_decompilation(identifier: str, timeout: int = 300) -> None:
    headers = {
        "accept": "application/json, text/plain, */*",
        "origin": "https://pylingual.io",
        "referer": "https://pylingual.io/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/139 Mobile Safari/537.36",
    }
    start_time = time.time()
    attempt = 0
    while True:
        if time.time() - start_time > timeout:
            raise DecompilationError("Decompilation timeout exceeded")
        attempt += 1
        elapsed = time.time() - start_time
        try:
            response = requests.get(
                "https://api.pylingual.io/get_progress",
                params={"identifier": identifier},
                headers=headers,
                timeout=10,
            )
            stage = response.json().get("stage")
            if stage == "done":
                print(
                    f"[ ✓ ] Decompilation complete (Attempts: {attempt}, Time: {elapsed:.2f}s)"
                )
                break
            elif stage == "error":
                raise DecompilationError("Decompilation failed on server")
            else:
                print(f"[ {attempt} ] Stage: {stage} | Elapsed: {elapsed:.1f}s")
                time.sleep(1.5)
        except requests.RequestException as e:
            raise DecompilationError(f"Progress check failed: {e}")


def retrieve_decompiled_code(identifier: str) -> str:
    headers = {
        "accept": "application/json, text/plain, */*",
        "origin": "https://pylingual.io",
        "referer": "https://pylingual.io/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/139 Mobile Safari/537.36",
    }
    try:
        response = requests.get(
            "https://api.pylingual.io/view_chimera",
            params={"identifier": identifier},
            headers=headers,
            timeout=30,
        )
        decoded_code = (
            response.json()
            .get("editor_content", {})
            .get("file_raw_python", {})
            .get("editor_content")
        )
        if not decoded_code:
            raise DecompilationError("No decompiled code in response")
        return decoded_code
    except requests.RequestException as e:
        raise DecompilationError(f"Failed to retrieve code: {e}")


def save_decompiled_code(original_file: str, code: str) -> str:
    base_name = os.path.basename(original_file)
    output_name = "decoded_" + base_name.replace(".pyc", ".py")
    output_path = os.path.join(os.path.dirname(original_file) or ".", output_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)
    return output_path


def decompile_pyc(file_path: str) -> None:
    """Decompile PYC file to Python source"""
    total_start_time = time.time()
    try:
        print(f"\n[ * ] Processing: {file_path}")
        validate_pyc_file(file_path)
        print("[ ✓ ] File validated")
        identifier = upload_pyc_file(file_path)
        print(f"[ ✓ ] Uploaded with identifier: {identifier}")
        wait_for_decompilation(identifier)
        code = retrieve_decompiled_code(identifier)
        output_path = save_decompiled_code(file_path, code)
        total_time = time.time() - total_start_time
        print(f"[ ✓ ] Decompiled code saved to: {output_path}")
        print(f"[ ✓ ] Total execution time: {total_time:.2f}s")
    except FileNotFoundError as e:
        print(f"[ ! ] File Error: {e}")
        raise
    except FileNotPyc as e:
        print(f"[ ! ] Format Error: {e}")
        raise
    except DecompilationError as e:
        print(f"[ ! ] Decompilation Error: {e}")
        raise
    except Exception as e:
        print(f"[ ! ] Unexpected Error: {e}")
        raise


def show_menu():
    """Display interactive menu"""
    print(f"\n{'=' * 55}")
    print("[ 1 ] Convert Marshal to PYC")
    print("[ 2 ] Decompile PYC to Python Source")
    print("[ 0 ] Exit")
    print(f"{'=' * 55}")


def select_python_version():
    """Let user select Python version"""
    print(f"\n{'=' * 55}")
    print("Available Python Versions:")
    versions = list(magic_map.keys())
    for i, ver in enumerate(versions, 1):
        print(f"[ {i} ] Python {ver}")
    print(f"[ 0 ] Current Version ({get_current_python_version()})")
    print(f"{'=' * 55}")
    while True:
        try:
            choice = input("[ ? ] Select version: ").strip()
            if choice == "0" or choice == "":
                return get_current_python_version()
            idx = int(choice) - 1
            if 0 <= idx < len(versions):
                return versions[idx]
            else:
                print("[ ! ] Invalid choice!")
        except ValueError:
            print("[ ! ] Enter a valid number!")


def interactive_mode():
    """Run in interactive menu mode"""
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    while True:
        show_menu()
        choice = input("[ ? ] Select option: ").strip()
        if choice == "0":
            print("\n[ ✓ ] Goodbye!")
            sys.exit(0)
        elif choice == "1":
            file_path = (
                input("\n[ ? ] Enter Marshal file path: ").strip().replace('"', "")
            )
            if not os.path.exists(file_path):
                print("[ ! ] File not found!")
                input("\nPress Enter to continue...")
                continue
            pyver = select_python_version()
            result = marshal_to_pyc(file_path, pyver)
            if result:
                print("[ ✓ ] Done!")
            input("\nPress Enter to continue...")
        elif choice == "2":
            file_path = input("\n[ ? ] Enter PYC file path: ").strip().replace('"', "")
            try:
                decompile_pyc(file_path)
                print("[ ✓ ] Done!")
            except Exception:
                pass
            input("\nPress Enter to continue...")
        else:
            print("[ ! ] Invalid option!")
            input("\nPress Enter to continue...")


def cli_mode(file_path: str, pyver: str = None):
    """Run in CLI mode with file detection"""
    if pyver is None:
        pyver = get_current_python_version()
    if not os.path.exists(file_path):
        print(f"[ ! ] File not found: {file_path}")
        sys.exit(1)
    if file_path.endswith(".pyc"):
        print("[ * ] Detected: PYC file")
        try:
            decompile_pyc(file_path)
            print("[ ✓ ] Done!")
        except Exception:
            sys.exit(1)
    elif file_path.endswith(".py"):
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            if b"marshal" in content:
                print("[ * ] Detected: Marshal file")
                pyc_file = marshal_to_pyc(file_path, pyver)
                if pyc_file:
                    print("\n[ * ] Now decompiling PYC...")
                    try:
                        decompile_pyc(pyc_file)
                        print("[ ✓ ] Done!")
                    except Exception:
                        sys.exit(1)
                else:
                    sys.exit(1)
            else:
                print("[ ! ] Not a marshal file")
                sys.exit(1)
        except Exception as e:
            print(f"[ ! ] Error: {e}")
            sys.exit(1)
    else:
        print("[ ! ] Unsupported file type (must be .pyc or .py)")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        pyver = sys.argv[2] if len(sys.argv) > 2 else None
        if pyver and pyver not in magic_map:
            print(f"[ ! ] Invalid Python version: {pyver}")
            print(f"[ * ] Available versions: {', '.join(magic_map.keys())}")
            sys.exit(1)
        cli_mode(file_path, pyver)
    else:
        interactive_mode()
