import sys, asyncio
from playwright.async_api import async_playwright
async def main(items):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for html,w,h,out in items:
            pg = await b.new_page(viewport={'width':w,'height':h}, device_scale_factor=1)
            import os
            await pg.goto('file://'+os.path.abspath(html)); await pg.wait_for_timeout(400)
            await pg.screenshot(path=out, full_page=False)
            print(out)
        await b.close()
args=sys.argv[1:]
asyncio.run(main([(args[i],int(args[i+1]),int(args[i+2]),args[i+3]) for i in range(0,len(args),4)]))
