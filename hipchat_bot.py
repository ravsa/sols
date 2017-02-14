from chatterbot import ChatBot
#from chatterbot.training.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('rvs',
                  input_adapter="chatterbot.adapters.input.TerminalAdapter",
                  output_adapter="chatterbot.adapters.output.TerminalAdapter",
                  logic_adapters=[
                      "chatterbot.adapters.logic.MathematicalEvaluation",
                      "chatterbot.adapters.logic.TimeLogicAdapter",
                      "chatterbot.adapters.logic.ClosestMatchAdapter",
                  ],
                  database="database.dbme"
                  )

# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.english")
print chatbot.get_response("did you eat all the neighbour candy")
while True:
    try:
        bot_response = chatbot.get_response(None)
    except:
        break
