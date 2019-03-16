# *- coding:utf-8 -*-

"""
 module for annual reports data clean.
 including:
    年报-企业基本信息
    年报-企业资产状况信息
    年报-对外投资信息
    年报-的对外提供保证担保信息
    年报-社保信息
    年报-网站或网点信息
    年报-股东股权转让
    年报-股东（发起人）及出资信息

 Empty values are mostly replaced by -1.
"""

import data_clean_utils as dcu
import primary_analysis as panaly
from file_directions import clean_data_temp_file_url


def duplicate_handle_basic_info():
    """
    handle duplicate data
    :return:
    """
    dcu.merge_rows(u'年报-企业基本信息.xlsx', [u'企业编号', u'年报年份'])


# TODO handle all the duplicate data in all tables listed in '年报类'


def primary_analysis_after_duplicate_handled():
    """
    primary analysis after duplicate data handled
    :return:
    """
    panaly.list_category_columns_values([u'年报-企业基本信息'], u'年报类_basic_info', file_url=clean_data_temp_file_url)


"""
    Dirty value handle for table 年报-企业基本信息.
    First we'll drop rows that empty value is too many.
    ['企业经营状态','从业人数','是否有网站或网点','企业是否有投资信息或购买其他公司股权',
        '有限责任公司本年度是否发生股东股权转','是否提供对外担保']
    Once there are more than 3 empties in these 6 columns we will drop that row.
    Then we check nulls column by column and decide how to process with it.
    Next we should numeric all the value for future process.
    After these are done, it's time to work out features we can use in this table which belongs
        to exploratory data analysis. 

    -----------------------------
    注册资本
    ------
    Based on the primary analysis data, we can drop column 注册资本 which empty percentage is 88%
    -----------------------------
    企业经营状态
    ------
    Empty percentage is 1.5%(219 out of 15056).
    8 status this value has, they are ['停业','其他','存续','开业','开业/正常经营','歇业','正常开业','清算'].
    We just add another status for the empty value:'Unknown'.
    And based on the counts for every status, we simplify these status to ['正常经营','非正常经营','Unknown']
    ['开业','开业/正常经营','正常开业'] belongs to '正常经营' and ['停业','其他','存续','歇业','清算'] belongs to '非正常经营'.
    So we can map these total 9 status to three: {'正常经营':0,'非正常经营':1,'Unknown':-1}.
    -----------------------------
    从业人数
    ------
    Empty percentage is 1.5%(218 out of 15056), and some value end with '人' while some are pure number.
    But also there are lots of value valued '企业选择不公示'(11623) and a few valued '人' without number.
    For empty value, we replace with -1 indicating there's no value(be careful here, we don't trigger them as -1 people,
        -1 here works as a status). Those end with '人', we simply drop '人'. Those valued '企业选择不公示',
        we replace it as number 0 which also works as a status, there's 8 '0人's in the original value but
        shouldn't matter.
    -----------------------------
    是否有网站或网点
    ------
    Empty percentage is 1.5%(218 out of 15056).
    There are 4 status here:['否','无','是','有'], and ['否','无'] should belong to 'No', ['是','有'] belong to 'Yes'.
    Empty value will be replaced with
    -----------------------------
    企业是否有投资信息或购买其他公司股权
    ------

    -----------------------------
    有限责任公司本年度是否发生股东股权转
    ------

    -----------------------------
    是否提供对外担保
    ------

    -----------------------------
    发布日期
    ------

    -----------------------------
    年报年份


    -----------------------------
    :return:
"""


def empty_value_handle_basic_info():
    """
    empty_value handle for table 年报-企业基本信息.
    :return:
    """



def numeric_handle_basic_info():
    """
    numeric data for table 年报-企业基本信息.
    :return:
    """