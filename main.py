# import <
from os import path
from json import loads
from github import Github
from discord import Intents
from discord.ext import commands
from lxRbckl import jsonLoad, jsonDump

# >


# global <
gFile = ''
gRepository = ''
gPath = path.realpath(__file__).split('/')
gDirectory = '/'.join(gPath[:(len(gPath) - 1)])
githubToken = ''
actaMea = commands.Bot(command_prefix = '', intents = Intents.all())
discordToken = ''

# >


def setData(pData: dict, pGithub = Github(githubToken)) -> None:
    '''  '''

    # get content from file in repository <
    # update file <
    repository = pGithub.get_repo(gRepository)
    content = repository.get_contents(gFile)
    repository.update_file(

        sha = content.sha,
        message = 'update',
        path = content.path,
        content = str(pData).replace('\'', '\"')

    )

    # >


def getData(pGithub = Github(githubToken)) -> dict:
    '''  '''

    # get data <
    # try if structured return decoded <
    # except then unstructured return decoded <
    content = pGithub.get_repo(gRepository).get_contents(gFile)
    try: return loads(content.decoded_content.decode())
    except: return dict(content.decoded_content.decode())

    # >


async def setFunction(ctx, pServer: str, pService: str, pData: dict):
    '''  '''

    # if server <
    # elif service <
    if ((pServer not in pData.keys()) and (not pService)):

        # add new element <
        # set data and delete message <
        pData[pServer] = []
        setData(pData = pData)
        await ctx.message.delete()

        # >

    elif ((pServer in pData.keys()) and (pService)):

        # add service to server <
        # set data and delete message <
        pData[pServer].append(pService)
        setData(pData = pData)
        await ctx.message.delete()

        # >

    # >


async def getFunction(ctx, pServer: str, pService: str, pData: dict):
    '''  '''

    # if server <
    # elif default <
    if (pServer in pData.keys()):

        # send output and delete message <
        await ctx.channel.send('\n'.join(f'`{i}`' for i in pData[pServer]), delete_after = 60)
        await ctx.message.delete()

        # >

    elif (not pServer):

        # send output and delete message <
        await ctx.channel.send('\n'.join(f'`{i}`' for i in pData.keys()), delete_after = 60)
        await ctx.message.delete()

        # >

    # >


async def updateFunction(ctx, pServerTo: str, pServerFrom: str, pData: dict):
    '''  '''

    # if ((new server destination) and (existing server origination)) <
    if ((pServerTo not in pData.keys()) and (pServerFrom in pData.keys())):

        # add new server <
        # delete old server <
        pData[pServerTo] = pData[pServerFrom]
        del pData[pServerFrom]

        # >

        # set data <
        # delete message <
        setData(pData = pData)
        await ctx.message.delete()

        # >

    # >


async def deleteFunction(ctx, pServer: str, pService: str, pData: dict):
    '''  '''

    # if server then delete server <
    # elif service then delete service <
    if ((pServer in pData.keys()) and (not pService)):

        # delete server <
        # set data and delete message <
        del pData[pServer]
        setData(pData = pData)
        await ctx.message.delete()

        # >

    elif ((pServer in pData.keys()) and (pService)):

        # delete service from server <
        # set data and delete message <
        pData[pServer].remove(pService)
        setData(pData = pData)
        await ctx.message.delete()

        # >

    # >


@actaMea.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases'])
async def commandFunction(ctx, pServer: str = None, pService: str = None):
    '''  '''

    dictVariable = {

        'set' : setFunction,
        'get' : getFunction,
        'update' : updateFunction,
        'delete' : deleteFunction

    }
    await dictVariable[ctx.invoked_with.lower()](

        ctx,
        pServer,
        pService,
        getData()

    )


# main <
if (__name__ == '__main__'): actaMea.run(discordToken)

# >
