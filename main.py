# import <
from os import path
from json import loads
from github import Github
from discord import Intents
from discord.ext import commands
from lxRbckl import jsonLoad, jsonDump

# >


# global <
gPath = path.realpath(__file__).split('/')
gDirectory = '/'.join(gPath[:(len(gPath) - 1)])
github = Github('')
actaMea = commands.Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


def setData(pRepository: str, pFile: str, pData: dict) -> None:
    '''  '''

    # get repository <
    # get file <
    # update file <
    repository = github.get_repo(pRepository)
    content = repository.get_contents(pFile)
    repository.update_file(

        sha = content.sha,
        message = 'update',
        path = content.path,
        content = str(pData)

    )

    # >


def getData(pRepository: str, pFile: str) -> dict:
    '''  '''

    # get data <
    # try if structured return decoded <
    # except then unstructured return decoded <
    content = github.get_repo(pRepository).get_contents(pFile)
    try: return loads(content.decoded_content.decode())
    except: return content.decoded_content.decode()

    # >


@actaMea.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases']['set'])
async def setCommand(pServer: str, pService: str = None):
    ''' a server or service '''

    # <
    # <
    pass

    # >


@actaMea.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases']['get'])
async def getCommand(pServer: str):
    ''' a server or default all '''

    # <
    # <
    pass

    # >


@actaMea.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases']['update'])
async def updateCommand(pServer: str):
    ''' a server '''

    # <
    # <
    pass

    # >


@actaMea.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases']['delete'])
async def deleteCommand(pServer: str, pService: str = None):
    ''' a server or service '''

    # <
    # <
    pass

    # >


# main <
if (__name__ == '__main__'):

    x = getData(pRepository = 'lxRbckl/Project-Acta-Mea-3', pFile = 'data.json')

    print(x)
    input(': ')

    setData(pRepository = 'lxRbckl/Project-Acta-Mea-3', pFile = 'data.json', pData = x)

# >
