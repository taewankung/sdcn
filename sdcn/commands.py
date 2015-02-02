'''
Created on Feb 2, 2015

@author: taewankung
'''
import threading
import subprocess

class Command:
    command_pattern = ''
    
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def build(self):
        return self.command_pattern


class FindCommand(Command):
    #command_pattern = 'find %s -name %s'
        
    def build(self):
        return ['find', self.kwargs['path'], '-name', self.kwargs['pattern']]
    
class ConvertFileCommand(Command):
    #command_pattern = 'pandoc -s %s -o %s'
    
    def build(self):
        #return ['pandoc', '-s', self.kwargs['source'], '-o', self.kwargs['target']]
        return ['convert', self.kwargs['source'], self.kwargs['target']]
class ChangImageTypeCommand(Command):
    
    def build(self):
        return ['convert', self.kwargs['source'], self.kwargs['target']]
    
    
class CommandRunner(threading.Thread):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.output = []
        
    def run(self):
        print("command:", self.command)

        output = subprocess.check_output(self.command)
        print("outputs:", output)
        self.output = output.decode('utf-8').split('\n')
        self.output.remove('')
