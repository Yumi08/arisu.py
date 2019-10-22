async def msg_delete(message):
    await message.channel.send('A message has been deleted.')

async def blk_msg_delete(messages):
    await message.channel.send('Multiple messages have been deleted.')

async def msg_edit(before, after):
    await before.channel.send('A message has been edited.')
