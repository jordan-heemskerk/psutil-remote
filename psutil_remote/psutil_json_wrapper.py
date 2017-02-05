import psutil
import json


class PsutilJsonWrapper(object):

    def dumps(self):
        encoded = {}
        encoded['users'] = psutil.users()
        encoded['meminfo'] = psutil.virtual_memory()
        encoded['cpuinfo'] = psutil.cpu_times_percent()
        encoded['processes'] = [proc.as_dict(['name'])
                                for proc in psutil.process_iter()]

        return json.dumps(encoded)
