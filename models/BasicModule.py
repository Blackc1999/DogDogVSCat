# -*- coding:gb2312 -*-
# -*- coding:UTF-8 -*-
# @Time     :2020 09 2020/9/3 11:09
# @Author   :ǧ��

import torch as t
import time

'''���׷�װModule,�ṩ�ӿ�'''


class BasicModule(t.nn.Module):
    def __init__(self):
        super(BasicModule, self).__init__()
        self.model_name = str(type(self))

    def load(self, path):
        '''
        ����ָ��·��ģ��
        :param path: path
        :return: None
        '''
        self.load_state_dict(t.load(path))

    def save(self, name=None):
        '''
        ����ģ�ͣ�ʹ��'ģ������+ʱ��'��Ϊ�ļ���
        :return: name

        '''
        if name is None:
            prefix = 'checkpoints/' + self.model_name + '_'
            name = time.strftime(prefix + '%m%d_%H:%M:%S.pth')
        t.save(self.state_dict(), name)
        return name
