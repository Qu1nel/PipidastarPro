from pathlib import Path

import ujson  # pyright: ignore[reportMissingModuleSource]
import aiofiles


async def get_content_json_from_file(file_name: Path) -> list:
    json_files_path = Path(__file__).resolve().parent / Path("sources") / file_name
    if json_files_path.exists():
        async with aiofiles.open(json_files_path, mode="r", encoding="UTF-8") as file:
            return ujson.loads(await file.read())
    return []
