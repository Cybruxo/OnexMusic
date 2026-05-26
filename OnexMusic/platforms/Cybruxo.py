# * ● OnexMusic
# * ○ A high-performance engine for streaming music in Telegram voicechats.
# *
# * Copyright (C) 2026 Cybruxo
# *
# * This program is free software: you can redistribute it and/or modify it under the
# * terms of the GNU General Public License as published by the Free Software Foundation,
# * either version 3 of the License, or (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful, but WITHOUT ANY
# * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# * PARTICULAR PURPOSE. See the GNU General Public License for more details.
# *
# * Repository: https://github.com/Cybruxo/OnexMusic

import asyncio
import json
import sys
import traceback
from ytSearch import VideosSearch, CustomSearch


## Test file to check youtubesearchpython functionality

async def run_query(query: str):
	print(f"Query: {query}")

	try:
		videos_search = VideosSearch(query, limit=20)
		videos_data = await videos_search.next()
		print("VideosSearch response keys:", list(videos_data.keys()))
		print(
			json.dumps(
				{
					"result_count": len(videos_data.get("result", [])),
					"first_result": videos_data.get("result", [None])[0],
				},
				indent=2,
			)
		)
	except Exception as exc:
		print("VideosSearch raised:", repr(exc))
		traceback.print_exc()

	try:
		custom_search = CustomSearch(query=query, searchPreferences="EgIYAw==", limit=1)
		custom_data = await custom_search.next()
		print("CustomSearch response keys:", list(custom_data.keys()))
		print(json.dumps(custom_data, indent=2))
	except Exception as exc:
		print("CustomSearch raised:", repr(exc))
		traceback.print_exc()


async def main(argv):
	if not argv:
		print("Usage: python3 test.py <search-query-or-url>")
		return
	query = argv[0]
	await run_query(query)


if __name__ == "__main__":
	asyncio.run(main(sys.argv[1:]))
