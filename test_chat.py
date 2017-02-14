from chatterbot import ChatBot
import sys
sys.setrecursionlimit=float('inf')
import data
from chatterbot.training.trainers import ListTrainer
bot = ChatBot('new',
        storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
        database='database'
        )
