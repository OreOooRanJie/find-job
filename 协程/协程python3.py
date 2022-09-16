import asyncio

async def foo(name):
   await asyncio.sleep(1)      # 这是一个不会阻塞的sleep，是一个协程
   print(f"name = {name}")


async def main():
   # 协程本身就是一个可等待对象
   await foo("lczmx")  # 执行协程
   print("done")

if __name__ == '__main__':
   # 使用asyncio.run运行
   asyncio.run(main())