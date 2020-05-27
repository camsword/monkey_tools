#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年7月9日

@author: liangjie02
"""

import os
from configparser import ConfigParser
from utils.log import logger


class Config(ConfigParser):
    """
    从config.ini文件中获取相应的配置信息，继承自ConfigParser
    """

    def __init__(self,
            config_path):
        """
        :param config_path:配置文件路径
        """
        super(Config, self).__init__()
        if not os.path.exists(config_path):
            os._exit(-1)

        self.config_path = config_path
        self.read(self.config_path,
                encoding="utf-8")

        def get_section_values(self,
                section):
            """
        获取某一个section所有的值
        :param section:配置文件中section
        :return:返回section中所有的值
        """
        return self.items(section).values()

    def add_option(self,
            section,
            option,
            value):
        """
        向某个section中添加一个option
        :param section:
        :param option:
        :param value:
        :return:
        """
        if not self.has_section(section):
            self.add_section(section)
        self.set(section, option, value)
        with open(self.config_path, 'w') as config_file:
            self.write(config_file)


if __name__ == "__main__":
    config_path = "/Users/liangjie02/work/code/icode/baidu/sh-qa/AIID/config.ini"
    config_obj = Config(config_path)
    logger.info(config_obj.get("email", "host"))
