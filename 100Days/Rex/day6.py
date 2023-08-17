import asyncio



#Asynchronous Proccessing...

async def fun1():
    r=0
    while r<500000001:
        r+=1
    return r-1

async def fun2():
    r=0
    while r<500000001:
        r+=1
    return r-1

async def fun3():
    r=0
    while r<500000001:
        r+=1
    return r-1

async def main():
    a1 = await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
    )

    print(a1)


asyncio.run(main())