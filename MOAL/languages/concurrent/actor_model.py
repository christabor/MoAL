"""Random excerpts of Act V of Romeo and Juliet.

Source:
http://www.william-shakespeare.info/act5-script-text-romeo-and-juliet.htm
"""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import pykka
from random import choice
import time
from MOAL.helpers.display import Section


class Montague(pykka.ThreadingActor):
    """Actor on the stage."""

    def on_receive(self, message):
        """Receiver."""
        phrases = [
            ("Alas, my liege, my wife is dead to-night; "
             " Grief of my son's exile hath stopp'd her breath:"
             " What further woe conspires against mine age?"),
            ("O thou untaught! what manners is in this?"
             " To press before thy father to a grave?"),
            ("But I can give thee more:"
             " For I will raise her statue in pure gold;"
             " That while Verona by that name is known,"
             " There shall no figure at such rate be set"
             " As that of true and faithful Juliet."),
        ]
        print('[montague]: {0}\n----------------'.format(choice(phrases)))


class Capulet(pykka.ThreadingActor):
    """Actor on the stage."""

    def on_receive(self, message):
        """Receiver."""
        phrases = [
            ("As rich shall Romeo's by his lady's lie;"
             " Poor sacrifices of our enmity!"),
            ("O brother Montague, give me thy hand:"
             " This is my daughter's jointure, for no more"
             " Can I demand."),
            ("What should it be, that they so shriek abroad?"),
            (" O heavens! O wife, look how our daughter bleeds!"
             " This dagger hath mista'en--for, lo, his house"
             " Is empty on the back of Montague,--"
             " And it mis-sheathed in my daughter's bosom!"),
        ]
        print('[capulet]: {0}\n----------------'.format(choice(phrases)))


if DEBUG:
    with Section('Actor model - via Pykka'):
        actors = [choice([Montague, Capulet]).start() for _ in range(10)]
        futures = []
        for actor in actors:
            future = actor.ask({
                'msg': 'Willst thine actor speaketh unto thee program?'
            }, block=False)
            time.sleep(0.5)
            futures.append(future)
        for fut in futures:
            fut.get()
