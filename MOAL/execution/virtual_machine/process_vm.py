# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from MOAL.helpers.display import print_success
from MOAL.data_structures.graphs.graphs import DirectedGraph

DEBUG = True if __name__ == '__main__' else False


class ProcessVirtualMachine(DirectedGraph):

    def __init__(self, graph_data, **kwargs):
        """onjava.com/pub/a/onjava/2007/05/07/the-process-virtual-machine.html

        This implementation represents the PVM concept and orchestration
        manager as an abstraction over the directed graph. Invocations
        are embedded in the graph and can be called by associating their
        function and action together. This makes the creation of highly
        complicated PVM/State machines very easy and intuitive, and de-coupled
        from many layers of class objects."""
        normalized = {}
        self.invocations = {}
        self.execution = None
        for src, data in graph_data.iteritems():
            invocation, edges = data
            self.invocations[src] = invocation
            edges = edges if edges is not None else []
            normalized[src] = {'edges': edges, 'val': src}
        super(ProcessVirtualMachine, self).__init__(normalized, **kwargs)

    def proceed(self, execution):
        print('-- Executing task with {}'.format(execution))
        self.execution = execution
        self._invoke()

    def _invoke(self):
        # Run the matching job
        self.invocations[self.execution]()


# Various task functions

def submit_claim():
    print_success('Submit claim task running!', prefix='+ PVM:')


def pay_claim():
    print_success('Pay claim task running!', prefix='+ PVM:')


def reject_claim():
    print_success('Reject claim task running!', prefix='+ PVM:')


def accept_claim():
    print_success('Accept claim task running!', prefix='+ PVM:')


def close_claim():
    print_success('Close claim task running!', prefix='+ PVM:')


def need_more_input():
    print_success('Need more input task running!', prefix='+ PVM:')


def archive_claim():
    print_success('Archive claim task running!', prefix='+ PVM:')


def evaluate_claim():
    print_success('Evaluate claim task running!', prefix='+ PVM:')


if DEBUG:
    with Section('Process Virtual Machine'):
        # Edges:
        #   - do submit
        #   - more
        #   - reject
        #   - accept
        #   - return more
        #   - do pay
        #   - do archive
        # Nodes:
        #   - submit claim
        #   - evaluate
        #   - more input
        #   - pay
        #   - archive
        #   - closed
        data = {
            'Submit Claim': (submit_claim, []),
            'Evaluate': (evaluate_claim, ['Submit Claim', 'More Input']),
            'More Input': (evaluate_claim, ['Evaluate']),
            'Closed': (close_claim, ['Rejected?', 'Archive']),
            'Archive': (pay_claim, ['Pay']),
            'Pay': (pay_claim, ['Accepted?']),
            'Accepted?': (accept_claim, ['Evaluate']),
            'Rejected?': (reject_claim, ['Evaluate'])
        }
        submit_claim = ProcessVirtualMachine(data)
        print(submit_claim)
        submit_claim.render_graph('pvmachine-viz.png', directed=True)

        workflow_1 = [
            'Submit Claim', 'More Input', 'Accepted?',
            'Pay', 'Archive', 'Closed']
        workflow_2 = [
            'Submit Claim', 'Evaluate', 'Accepted?', 'Pay', 'Archive', 'Closed']
        workflow_3 = ['Submit Claim', 'Evaluate', 'Rejected?', 'Closed']

        for workflow in [workflow_1, workflow_2, workflow_3]:
            divider('~+', newline=False)
            print('=== New workflow...')
            for task in workflow:
                submit_claim.proceed(task)
