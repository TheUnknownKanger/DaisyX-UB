
import asyncio
import glob
import ntpath
import shlex
from typing import Tuple

def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
