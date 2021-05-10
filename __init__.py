from mycroft import MycroftSkill, intent_file_handler


class Gebaeude(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gebaeude.intent')
    def handle_gebaeude(self, message):
        self.speak_dialog('gebaeude')


def create_skill():
    return Gebaeude()

