from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *
from mycroft.util.log import LOG

from datetime import date

# TODO: Fallback Skill einrichten

class MarienkapelleSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    def initialize(self):
        # Word entity ist Platzhalter für beliebiges Wort
        self.register_entity_file("word.entity")
        # self.parser = WiktionaryParser()


    ### normale Frage-Antwort-Intents ###

    @intent_file_handler('marienkapelle.building.style.intent')
    def handle_marienkapelle_style(self, message):
        self.speak_dialog('marienkapelle.building.style')

    @intent_file_handler('marienkapelle.how.old.intent')
    def handle_marienkapelle_how_old(self, message):
        self.speak_dialog('marienkapelle.built.year')

    @intent_file_handler('marienkapelle.reconstruction.intent')
    def handle_marienkapelle_rebuilt(self, message):
        self.speak_dialog('marienkapelle.rebuilt.in')

    @intent_file_handler('marienkapelle.tell.facts.intent')
    def handle_marienkapelle_facts(self, message):
        self.speak_dialog('marienkapelle.facts')

    @intent_file_handler('marienkapelle.what.is.intent')
    def handle_marienkapelle_what_is(self, message):
        self.speak_dialog('marienkapelle.this.is')

    @intent_file_handler('marienkapelle.when.market.open.intent')
    def handle_marienkapelle_market_open(self, message):
        self.speak_dialog('marienkapelle.market.time.is')

    @intent_file_handler('marienkapelle.which.religion.intent')
    def handle_marienkapelle_which_religion(self, message):
        self.speak_dialog('marienkapelle.is.religion')







    # @intent_file_handler('fallback.wiktionary.definition.intent')
    # def handle_wiktionary_definition(self, message):
        # #Get word to define from utterance
        # word = message.data.get('word')
        # #Lookup the word using Wiktionary
        # get_word_info = self.parser.fetch(word)

        # #Speak definition for requested word back to user
        # try:
            # # Get first definition from wiktionary response
            # response = get_word_info[0]['definitions'][0]['text'][1]
            # # Log the definition
            # LOG.info(response)
            # self.speak_dialog('fallback.wiktionary', {'word': word, 'definition': response})
        # except:
            # self.speak_dialog('error.wiktionary')


    def stop(self):
        pass


def create_skill():
    return MarienkapelleSkill()

