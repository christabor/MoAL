# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


# http://www.codeproject.com
# /Articles/615139/An-Absolute-Beginners-Tutorial-on-Dependency-Inver

# From
# http://programmers.stackexchange.com/questions/274459
# /when-not-to-apply-dependency-inversion
#   "Part of the art of software development is having a good sense of what is
#   likely to change as time goes on, and what isn't. For the stuff that is
#   likely to change, use the interfaces and other SOLID concepts.
#   For the stuff that won't, use YAGNI and just pass concrete types,
#   forget the factory classes, forget all the runtime hooking up and
#   configuration, etc, and forget a lot of the SOLID abstractions.
#   In my experience, the YAGNI approach has proven to be correct
#   far more often than it is not."


class Messenger:
    """This class acts as a layer of indirection and inverts
    the dependency of the higher-level modules that use it,
    by provide a more abstract messaging mechanism.
    This makes any messenger that subclasses this class "pluggable"."""

    def message_action(self, message):
        return '[Message]: {}'.format(message)


class SMSMessenger(Messenger):

    def message_action(self, message):
        return '[SMS Message]: {}'.format(message)


class EMailMessenger(Messenger):

    def message_action(self, message):
        return '[Email Message]: {}'.format(message)


class LoggingMessenger(Messenger):

    def message_action(self, message):
        return '[Logging Message]: {}'.format(message)


class StillCoupledApplication:
    """This is the highest level class, and requires
    some kind of logging mechanism. It's easy to plug new loggers
    into this class because they all reside in front of a common class.
    The problem is, they still require knowledge of which logger to use."""

    logger = None

    def __init__(self, *args, **kwargs):
        # Map a concrete messenger type to the class, but everywhere else
        # in the class it doesn't know the difference between email, sms, etc...
        if self.logger is None:
            self.logger = Messenger()

    def log(self, message):
        self.logger.message_action(message)


class Application:
    """This class no longer requires any knowledge of the logger type,
    because it's passed in. So longer as the methods match, it will
    just work. This is called dependency injection."""

    logger = None

    def __init__(self, *args, **kwargs):
        if 'logger' not in kwargs:
            self.logger = Messenger()
        else:
            self.logger = kwargs.get('logger')()

    def log(self, message):
        msg = self.logger.message_action(message)
        print(msg)
        return msg


if DEBUG:
    with Section('SOLID - Dependency Inversion Principle'):
        # It seems that DIP is a concept, and the mechanism to achieve it
        # is actually Dependency Injection (e.g. Class/Method/Prop injection).
        app = Application()
        assert app.log('Foobar') == '[Message]: Foobar'

        app_email = Application(logger=EMailMessenger)
        assert app_email.log('Foobar') == '[Email Message]: Foobar'

        app_sms = Application(logger=SMSMessenger)
        assert app_sms.log('Foobar') == '[SMS Message]: Foobar'

        app_log = Application(logger=LoggingMessenger)
        assert app_log.log('Foobar') == '[Logging Message]: Foobar'
