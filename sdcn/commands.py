'''
Created on Feb 2, 2015

@author: taewankung
'''
import threading
import subprocess
import cmd

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
    
class PDFMergging(Command):
    def build(self):
        cmd = ['convert']
        cmd.extend(self.kwargs['source'])
        cmd.append(self.kwargs['target'])
        return cmd
class ConvertMusicCommands(Command):
    def build(self):
        cmd = ['mpg123','-w']
        cmd.append(self.kwargs['target'])
        cmd.extend(self.kwargs['source'])
        return cmd
class ConvertMusicFile(Command):
        def build(self):
             return ['mpg123', '-w', self.kwargs['source'], self.kwargs['target']]
class CompressFileZip(Command):
    def build(self):
        cmd = ['zip']
        cmd.append(self.kwargs['target'])
        cmd.extend(self.kwargs['source'])
        return cmd
class ConvertVideoFile(Command):
    def build(self):
        return ['ffmpeg', '-i', self.kwargs['source'], self.kwargs['target']]

class Resize(Command):
    def build(self):
        return ['convert', self.kwargs['source'],'-resize',self.kwargs['percent'],self.kwargs['target']]
    
class Rotate(Command):
    def build(self):
        return ['convert', self.kwargs['source'], '-rotate',self.kwargs['degree'], self.kwargs['target']]
    
class NewFolders(Command):
    def build(self):
            return ['mkdir' , self.kwargs['target']]
    
class DocToText(Command):
    def buid(self):
        pass

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