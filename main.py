# *- coding:utf-8 -*-

import sys

import data_clean_annual_report as dcar
import data_clean_soft_assets as dcsa
import exploratory_data_analysis_annual_report as edaar
import exploratory_data_analysis_soft_assets as edasa

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    dcar.work_()
    dcsa.work_()

    edaar.work_()
    edasa.work_()